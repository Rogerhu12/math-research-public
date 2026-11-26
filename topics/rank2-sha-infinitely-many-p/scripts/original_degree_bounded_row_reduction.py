#!/usr/bin/env sage-python
"""Complete polynomial row HNF with an explicit degree bound.

R942 successor: no column-by-column Bezout transformation is used.  A
complete unshifted Popov basis is followed by recursive ONE-column shifts.
All operations are elementary unimodular operations on the entire input
row and, for a square input, its entire attached right block.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
import time
from sage.all import matrix, vector
from original_ys_divisor_ideal_tools import (
    canonical, digest, polynomial_digest, polynomial_matrix_digest,
    field_description, _hermite_remainder_rows)

SOURCE_DEPENDENCIES = (
    "original_degree_bounded_row_reduction.py",
    "original_ys_divisor_ideal_tools.py",
)


def _report(stage, **record):
    print("RANK2_DEGREE_BOUNDED_HERMITE_STAGE "+
          canonical(dict(stage=stage, **record)), flush=True)


def _degree(row):
    return max((int(f.degree()) for f in row), default=-1)


def complete_degree_bounded_row_hermite(rows, attached=None, progress=None,
                                        label="complete degree-bounded row module"):
    """Return the entire upper row HNF, attached transform, and certificate.

    For input degree D and module determinant degree delta, every LEFT
    entry during the algorithm has degree <= max(D, 2*delta+1).
    Neither the source module nor any attached coordinate is projected out.
    The attached block is not subjected to a false identical degree bound:
    for square M and attached B its proven bound is
      max(D,2*delta+1)+(n-1)*D-delta+degree(B).
    """
    R = rows.base_ring()
    m, n = int(rows.nrows()), int(rows.ncols())
    assert m >= n > 0
    report = progress or _report
    original = matrix(R, rows)
    current = [vector(R, row) for row in original.rows()]
    has_attached = attached is not None
    if has_attached:
        assert m == n and attached.base_ring() is R and attached.nrows() == m
        original_attached = matrix(R, attached)
        side = [vector(R, row) for row in original_attached.rows()]
        attached_input_degree = max((_degree(row) for row in side), default=-1)
    else:
        original_attached, side = None, None
        attached_input_degree = None
    input_degree = max(_degree(row) for row in current)
    assert input_degree >= 0
    counts = dict(swap=0, add=0, scale=0, bezout=0)
    stream = hashlib.sha256()
    phase_records = []
    max_left_degree = input_degree
    max_attached_degree = attached_input_degree
    started, last_report = time.monotonic(), time.monotonic()
    report("whole degree-bounded module start", label=label,
           original_rows=m, original_columns=n, input_degree=input_degree,
           attached_block=has_attached,
           attached_input_degree=attached_input_degree)

    def record(kind, indices, coefficients=()):
        counts[kind] += 1
        stream.update(canonical(dict(kind=kind, indices=list(indices),
            coefficients=[polynomial_digest(R(c)) for c in coefficients])).encode())
        stream.update(b"\n")

    def swap(i, j):
        if i != j:
            current[i], current[j] = current[j], current[i]
            if has_attached:
                side[i], side[j] = side[j], side[i]
            record("swap", (i, j))

    def add(i, j, coefficient):
        nonlocal max_left_degree, max_attached_degree, last_report
        coefficient = R(coefficient)
        assert i != j and coefficient
        current[i] = current[i]+coefficient*current[j]
        max_left_degree = max(max_left_degree, _degree(current[i]))
        if has_attached:
            side[i] = side[i]+coefficient*side[j]
            max_attached_degree = max(max_attached_degree, _degree(side[i]))
        record("add", (i, j), (coefficient,))
        now = time.monotonic()
        if now-last_report >= 30:
            report("whole degree-bounded row operations advanced", label=label,
                   operation_counts=dict(counts),
                   maximum_left_degree_seen=max_left_degree,
                   maximum_attached_degree_seen=max_attached_degree,
                   reduction_elapsed_seconds=now-started)
            last_report = now

    def scale(i, coefficient):
        coefficient = R(coefficient)
        assert coefficient and coefficient.degree() == 0
        if coefficient != 1:
            current[i] = coefficient*current[i]
            if has_attached:
                side[i] = coefficient*side[i]
            record("scale", (i,), (coefficient,))

    def leading(i, first, shifts):
        best = (-1, -1)
        for j in range(first, n):
            f = current[i][j]
            if f:
                best = max(best, (int(f.degree())+shifts[j-first], j))
        return best

    def popov(first, last, shifts, phase_label, expected_delta=None):
        """Entire shifted weak-Popov and column reduction by row additions."""
        assert len(shifts) == n-first and min(shifts) == 0
        indices = list(range(first, last))
        assert all(not current[i][j] for i in indices for j in range(first))
        before_degree = max(_degree(current[i][first:]) for i in indices)
        degree_cap = before_degree+max(shifts)
        old_add_count = counts["add"]
        leaders = {i:leading(i, first, shifts) for i in indices}
        initial_potential = sum(
            n*(d+1)+j+1 for d, j in leaders.values() if j >= 0)
        buckets = {j:set() for j in range(first, n)}
        for i in indices:
            if leaders[i][1] >= 0:
                buckets[leaders[i][1]].add(i)
        pending = [j for j in range(first, n) if len(buckets[j]) > 1]
        while pending:
            j = pending.pop()
            bucket = buckets[j]
            if len(bucket) < 2:
                continue
            # The smaller leader divides the leading degree of the other.
            source, target = sorted(bucket, key=lambda i:(leaders[i][0], i))[:2]
            bucket.remove(target)
            old_leader = leaders[target]
            q, unused_remainder = current[target][j].quo_rem(current[source][j])
            assert q
            add(target, source, -q)
            new_leader = leading(target, first, shifts)
            assert new_leader < old_leader
            assert _degree(current[target][first:]) <= degree_cap
            leaders[target] = new_leader
            if len(bucket) > 1:
                pending.append(j)
            if new_leader[1] >= 0:
                new_bucket = buckets[new_leader[1]]
                new_bucket.add(target)
                if len(new_bucket) > 1:
                    pending.append(new_leader[1])
        nonzero = [i for i in indices if leaders[i][1] >= 0]
        assert len(nonzero) == n-first, "The whole input does not have full column rank."
        assert sorted(leaders[i][1] for i in nonzero) == list(range(first, n))
        weak_add_count = counts["add"]-old_add_count
        assert weak_add_count <= initial_potential
        pivot_rows = {leaders[i][1]:i for i in nonzero}
        pivot_degrees = {j:int(current[i][j].degree()) for j, i in pivot_rows.items()}
        delta = sum(pivot_degrees.values())
        if expected_delta is not None:
            assert delta == expected_delta
        for j, i in pivot_rows.items():
            scale(i, R.base_ring().one()/current[i][j].leading_coefficient())
            assert current[i][j].leading_coefficient() == 1

        # Reduce the greatest reducible shifted monomial of EACH full row.
        # Reducer leaders are smaller than that row's own unchanged leader.
        for i in nonzero:
            own = leaders[i]
            while True:
                bad = []
                for j, reducer in pivot_rows.items():
                    if reducer != i and current[i][j] and (
                            current[i][j].degree() >= pivot_degrees[j]):
                        bad.append((int(current[i][j].degree())+shifts[j-first],
                                    j, reducer))
                if not bad:
                    break
                largest = max(bad)
                _, j, reducer = largest
                assert largest[:2] < own
                q, residual = current[i][j].quo_rem(current[reducer][j])
                assert q
                add(i, reducer, -q)
                assert current[i][j] == residual
                assert leading(i, first, shifts) == own
                assert _degree(current[i][first:]) <= degree_cap
                following_bad = [
                    (int(current[i][c].degree())+shifts[c-first], c)
                    for c, r in pivot_rows.items()
                    if r != i and current[i][c] and (
                        current[i][c].degree() >= pivot_degrees[c])]
                assert not following_bad or max(following_bad) < largest[:2]
        for j, i in pivot_rows.items():
            assert all(not current[r][j] or current[r][j].degree() < pivot_degrees[j]
                       for r in nonzero if r != i)
        # Every column is a pivot column.  Thus finished Popov entries have
        # degree <= their column pivot degree, hence <= delta.
        assert all(_degree(current[i][first:]) <= delta for i in nonzero)
        desired = sorted(nonzero, key=lambda i:leaders[i][1])+[
            i for i in indices if leaders[i][1] < 0]
        # Apply the exact permutation to BOTH entire blocks, preserving all rows.
        positions = list(indices)
        for offset, old_index in enumerate(desired):
            position = first+offset
            located = first+positions.index(old_index)
            swap(position, located)
            a, b = position-first, located-first
            positions[a], positions[b] = positions[b], positions[a]
        assert all(leading(i, first, shifts)[1] == i
                   for i in range(first, n))
        assert all(current[i].is_zero() for i in range(n, last))
        result = dict(
            phase=phase_label, first_column=first, active_rows=last-first,
            input_tail_degree=before_degree, largest_shift=max(shifts),
            left_entry_degree_bound=degree_cap,
            final_popov_degree=max(_degree(current[i][first:])
                                   for i in range(first, n)),
            determinant_degree=delta,
            weak_reductions=weak_add_count,
            all_row_additions=counts["add"]-old_add_count,
            weak_leader_potential_bound=initial_potential,
            every_weak_leader_strictly_descended=True,
            every_column_reduction_preserved_own_leader=True,
            all_column_degree_bounds_checked=True,
            full_attached_block_received_every_operation=has_attached)
        phase_records.append(result)
        report("complete bounded Popov phase certified", label=label, **result,
               reduction_elapsed_seconds=time.monotonic()-started)
        return delta

    delta = popov(0, m, [0]*n, "whole unshifted Popov")
    assert max_left_degree <= input_degree
    global_cap = max(input_degree, 2*delta+1)
    if has_attached:
        attached_cap = (global_cap+(n-1)*input_degree-delta+
                        attached_input_degree)
    else:
        attached_cap = None
    assert all(current[i].is_zero() for i in range(n, m))
    tail_delta = delta
    diagonal_degrees = []
    for first in range(n):
        # The remaining tail is unshifted Popov: the preceding stage shifted
        # only its removed first column, while all these columns had shift 0.
        assert all(leading(i, first, [0]*(n-first))[1] == i
                   for i in range(first, n))
        assert sum(int(current[i][i].degree()) for i in range(first, n)) == tail_delta
        g = R.zero()
        for i in range(first, n):
            g = g.gcd(current[i][first])
        assert g
        g = g.monic()
        gcd_degree = int(g.degree())
        safe_shift = tail_delta-gcd_degree+1
        assert safe_shift >= 1
        gap = min(safe_shift, max(1, max(
            _degree(current[i][first:]) for i in range(first, n))+1))
        while any(current[i][first] for i in range(first+1, n)):
            popov(first, n, [gap]+[0]*(n-first-1),
                  "single-column Hermite shift", expected_delta=tail_delta)
            assert max_left_degree <= global_cap
            if not any(current[i][first] for i in range(first+1, n)):
                break
            assert gap < safe_shift, "The proved one-column shift bound failed."
            gap = min(safe_shift, 2*gap)
        assert current[first][first] == g
        assert all(not current[i][j] for i in range(first+1, n)
                   for j in range(first+1))
        diagonal_degrees.append(gcd_degree)
        tail_delta -= gcd_degree
        report("whole first Hermite column extracted", label=label,
               completed_columns=first+1, total_columns=n,
               pivot_degree=gcd_degree, remaining_determinant_degree=tail_delta,
               maximum_left_degree_seen=max_left_degree,
               proved_global_left_degree_bound=global_cap,
               maximum_attached_degree_seen=max_attached_degree,
               proved_attached_degree_bound=attached_cap,
               reduction_elapsed_seconds=time.monotonic()-started)
    assert tail_delta == 0 and sum(diagonal_degrees) == delta

    # Lower rows are already HNF.  Reduction in increasing column order
    # does not increase max_j(deg(row_j)-degree(diagonal_j)).
    for i in range(n-1, -1, -1):
        excess = max(int(current[i][j].degree())-diagonal_degrees[j]
                     for j in range(i, n))
        for j in range(i+1, n):
            q, residual = current[i][j].quo_rem(current[j][j])
            if q:
                add(i, j, -q)
            assert current[i][j] == residual
            assert all(int(current[i][c].degree())-diagonal_degrees[c] <= excess
                       for c in range(i, n))
            assert _degree(current[i]) <= global_cap
    H = matrix(R, current[:n])
    assert H.is_hermite() and H.nrows() == H.ncols() == n
    assert all(row.is_zero() for row in current[n:])
    determinant = R.one()
    for i in range(n):
        assert H[i, i] and H[i, i].leading_coefficient() == 1
        determinant *= H[i, i]
    assert determinant.degree() == delta
    assert max_left_degree <= global_cap
    if has_attached:
        assert max_attached_degree <= attached_cap
    # The reverse inclusion is checked for EVERY original generating row.
    assert _hermite_remainder_rows(original, H).is_zero()
    transformed = matrix(R, side) if has_attached else None
    receipt = dict(
        method="complete unshifted Popov and recursive bounded single-column shifts",
        label=label, original_shape=[m, n], full_rank=n,
        original_rows_sha256=polynomial_matrix_digest(original),
        complete_hermite_basis_sha256=polynomial_matrix_digest(H),
        full_monic_determinant_sha256=polynomial_digest(determinant),
        determinant_degree=delta, original_entry_degree=input_degree,
        maximum_left_degree_seen=max_left_degree,
        proved_global_left_degree_bound=global_cap,
        maximum_attached_degree_seen=max_attached_degree,
        proved_attached_degree_bound=attached_cap,
        operation_counts=counts, full_operation_stream_sha256=stream.hexdigest(),
        phases=phase_records,
        only_elementary_unimodular_row_additions_swaps_and_field_scales=True,
        all_row_scales_are_nonzero_field_units=True,
        only_identically_zero_rows_removed=True,
        every_original_row_returned_by_exact_hermite_division=True,
        complete_row_module_preserved_at_every_operation=True,
        both_polynomial_row_module_inclusions_verified=True,
        accumulated_unimodular_matrix_constructed=False,
        attached_block=has_attached,
        original_attached_sha256=(polynomial_matrix_digest(original_attached)
                                 if has_attached else None),
        transformed_attached_sha256=(polynomial_matrix_digest(transformed)
                                    if has_attached else None),
        attached_block_receives_identical_complete_operations=has_attached,
        no_fraction_field_kernel_or_denominator_clearing_used=True,
        elapsed_seconds=time.monotonic()-started)
    return H, transformed, receipt
