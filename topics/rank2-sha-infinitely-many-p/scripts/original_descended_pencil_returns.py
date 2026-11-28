#!/usr/bin/env sage-python
"""Complete rectangular two-generator graph compression and both physical ideal returns."""
import os
if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise SystemExit("Run only in the named public research Actions.")
import hashlib
import numpy as np
from sage.all import matrix
from original_short_graph_field import PackedField
from original_short_graph_popov import PackedRow, divide_into_rows
from original_short_graph_outer import original_operator_product, projected_pair_after_proof
from original_ys_divisor_ideal_tools import canonical, digest, element_digest, polynomial_matrix_digest
from original_descended_pencil_sections import require


def compress_rectangular(Y, X, weights, omitted_pole_order, section_grade=12):
    """Weak Popov with honest zero rows. Retain the entire physical attached block."""
    R = Y.base_ring()
    height, n = map(int, Y.dimensions())
    require(height >= n > 0 and X.dimensions() == Y.dimensions() and X.base_ring() is R,
            "Malformed physical rectangular paired rows")
    arithmetic = PackedField(R.base_ring())
    source = [PackedRow(R, arithmetic, row) for row in Y.rows()]
    attached = [PackedRow(R, arithmetic, row) for row in X.rows()]
    positions = [row.leading() for row in source]
    maximum = max(d for d, j in positions)
    require(len(weights) == n and omitted_pole_order in (1, 3) and maximum <= section_grade+max(weights),
            "The original source exceeded its proven ordinary-degree bound")
    caps = maximum + max(weights) + omitted_pole_order - np.asarray(weights, dtype=np.int64)
    def within_attached(row, shift=0):
        degrees = row.degrees()
        return not np.any((degrees >= 0) & (degrees+shift > caps))
    require(all(within_attached(row) for row in attached), "An original image exceeded its true coordinate cap")
    buckets = [set() for _ in range(n)]
    dropped = []
    for i, (d, j) in enumerate(positions):
        if j >= 0:
            buckets[j].add(i)
        else:
            require(attached[i].leading()[1] < 0, "A zero projection retained a nonzero image")
            dropped.append(i)
    pending = [j for j, pool in enumerate(buckets) if len(pool) > 1]
    hasher = hashlib.sha256()
    count = 0
    while pending:
        j = pending.pop()
        pool = buckets[j]
        if len(pool) <= 1:
            continue
        i, k = sorted(pool, key=lambda index: (positions[index][0], index))[:2]
        old = positions[k]
        quo, rem = source[k].polynomial(j).quo_rem(source[i].polynomial(j))
        require(quo, "An elementary exact leading division yielded a zero quotient")
        require(int(quo.degree())+positions[i][0] <= maximum and within_attached(attached[i], int(quo.degree())),
                "An entire multiplied pivot row exceeds the proven physical cap")
        source[k].add_scaled(source[i], -quo)
        attached[k].add_scaled(attached[i], -quo)
        require(within_attached(attached[k]), "The updated paired row exceeded the geometric cap")
        count += 1
        hasher.update(canonical([k, i, [arithmetic.coords(c) for c in quo.list()]]).encode()+b"\n")
        new = source[k].leading()
        require(new < old and new[0] <= maximum and source[k].polynomial(j) == rem,
                "A complete rectangular leading position did not strictly descend")
        pool.remove(k)
        positions[k] = new
        if len(pool) > 1:
            pending.append(j)
        if new[1] < 0:
            require(attached[k].leading()[1] < 0, "An actual rectangular syzygy has a nonzero attached row")
            dropped.append(k)
        else:
            buckets[new[1]].add(k)
            if len(buckets[new[1]]) > 1:
                pending.append(new[1])
    require(len(dropped) == height-n and all(len(pool) == 1 for pool in buckets),
            "The two generators did not have full module rank")
    order = [next(iter(pool)) for pool in buckets]
    ordered = [source[i] for i in order]
    B = matrix(R, [row.as_vector() for row in ordered])
    C = matrix(R, [attached[i].as_vector() for i in order])
    pivots = [positions[i][0] for i in order]
    for i, row in enumerate(Y.rows()):
        coordinates = divide_into_rows(row, ordered, pivots)
        require(original_operator_product(coordinates, B) == row and
                original_operator_product(coordinates, C) == X.row(i),
                "An entire rectangular generator failed its paired reverse inclusion")
    return B, C, dict(actual_input_rows=height, source_rank=n, strictly_decreasing_transforms=count,
                      elementary_operation_sha256=hasher.hexdigest(), actual_zero_rows=dropped,
                      final_order=order, initial_left_ordinary_degree_cap=maximum,
                      physical_attached_weight_cap=int(maximum+max(weights)+omitted_pole_order),
                      full_coordinate_caps=[int(c) for c in caps], all_input_products_and_updates_within_caps=True,
                      complete_input_Y=polynomial_matrix_digest(Y), complete_input_X=polynomial_matrix_digest(X),
                      square_pair_sha256=[polynomial_matrix_digest(B), polynomial_matrix_digest(C)],
                      all_original_rows_roundtripped=True, every_discarded_attached_row_zero=True)


def pencil_ideals(engine, numerator, denominator, pairs, label, pole_degree, weights,
                  original_proof, expected_lengths=None):
    """Each pair is one of two globally generating physical sections in this chart."""
    require(len(pairs) == 2 and engine.dimension == len(weights), "Wrong original pair count")
    operators = []
    for h, x in pairs:
        require(engine.multiply(numerator, h) == engine.multiply(denominator, x),
                "The physical N,D failed on an actual source generator")
        H, J = engine.multiplication_matrix(h), engine.multiplication_matrix(x)
        require(engine.unit*H == h and engine.unit*J == x, "The original multiplication source changed")
        operators.append((H, J))
    Y = operators[0][0].stack(operators[1][0])
    X = operators[0][1].stack(operators[1][1])
    B, C, compression = compress_rectangular(Y, X, weights, 3 if engine.infinity_chart else 1)
    def admission(current_B, current_C, H, G):
        require(current_B is B and current_C is C, "The square original paired rows changed")
        require(H.is_hermite() and G.is_hermite() and all(H[i,i] and G[i,i] for i in range(len(weights))),
                "The full original graph failed to return both Hermite bases")
        return dict(complete_graph_for_this_full_original_function=True, route="descended basepoint-free G3 pencil",
                    actual_original_function_id=original_proof["actual_original_function_id"],
                    actual_original_endpoint=original_proof["actual_original_endpoint"],
                    actual_chart=engine.infinity_chart, complete_RR_dimension=original_proof["G3"]["actual_complete_kernel_dimension"],
                    complete_pencil_admission_sha256=digest(original_proof), actual_rectangular_graph=compression)
    positive, negative, record = projected_pair_after_proof(engine,numerator,denominator,B,C,label,admission,
                                                             pole_degree,max(weights))
    if expected_lengths is not None:
        require((int(positive.length), int(negative.length)) == expected_lengths, "Wrong physical canonical lengths")
    require(record["post_ideal_outer"]["source_row_count_verified_after_both_ideals"] == engine.dimension,
            "The full post-ideal physical return did not cover every row")
    return positive, negative, record
