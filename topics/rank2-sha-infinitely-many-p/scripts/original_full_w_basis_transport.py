#!/usr/bin/env sage-python
"""Complete original W on all 306 weighted basis rows, from original R3.

R942 section 13: a proved weighted degree bound, one full constant-field
inverse, all Taylor coefficients up to that bound, every original source
row returned as a polynomial, and a complete polynomial inverse.
This helper never creates a normalization or a different constant field.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
import time
from pathlib import Path
from sage.all import GF, PolynomialRing, diagonal_matrix, identity_matrix, matrix, vector
from section_quotient_algebra import canonical, digest
from original_section_ring_embedding import (
    finite_coordinates, polynomial_matrix_digest, polynomial_vector_digest)

SOURCE_DEPENDENCIES = (
    "original_full_w_basis_transport.py",
    "original_section_ring_embedding.py",
    "section_quotient_algebra.py",
)


def _progress(callback, stage, **record):
    if callback is not None:
        callback(stage, **record)


def _field_matrix_digest(M):
    field = M.base_ring()
    return digest(dict(
        rows=int(M.nrows()), columns=int(M.ncols()),
        prime=int(field.characteristic()), constant_degree=int(field.degree()),
        coefficients=[[finite_coordinates(c, field) for c in row] for row in M.rows()]))


def _weighted_check(value, weights, bound):
    assert len(value) == len(weights)
    assert all(not p or int(p.degree())+weights[i] <= int(bound)
               for i, p in enumerate(value))
    return value


def _homogeneous_substitute(p, degree, numerator, denominator):
    """denominator^degree * p(numerator/denominator), without fractions."""
    degree = int(degree)
    R = numerator.parent()
    assert denominator.parent() is R and p.parent() is R
    if not p:
        return R.zero()
    assert degree >= 0 and int(p.degree()) <= degree
    answer = R.zero()
    for exponent, coefficient in enumerate(p.list()):
        if coefficient:
            answer += coefficient*numerator**exponent*denominator**(degree-exponent)
    return answer


def _polynomial_degree(M):
    return max([int(p.degree()) for p in M.list() if p]+[0])


def _coefficient_matrix(M, degree):
    field = M.base_ring().base_ring()
    return matrix(field, M.nrows(), M.ncols(),
                  lambda i, j:M[i, j][degree])


def _whole_product_return(A, B, target, *, label):
    """Check EVERY coefficient of the full polynomial matrix product."""
    R = A.base_ring()
    assert B.base_ring() is R and target.base_ring() is R
    assert A.ncols() == B.nrows()
    assert target.nrows() == A.nrows() and target.ncols() == B.ncols()
    field = R.base_ring()
    da, db, dt = (_polynomial_degree(M) for M in (A, B, target))
    aa = [_coefficient_matrix(A, i) for i in range(da+1)]
    bb = [_coefficient_matrix(B, j) for j in range(db+1)]
    full_degree = max(da+db, dt)
    for degree in range(full_degree+1):
        actual = matrix(field, A.nrows(), B.ncols())
        for i in range(max(0, degree-db), min(da, degree)+1):
            actual += aa[i]*bb[degree-i]
        assert actual == _coefficient_matrix(target, degree), (label, degree)
    return dict(
        label=label, original_source_rows=int(A.nrows()),
        complete_middle_dimension=int(A.ncols()), target_columns=int(B.ncols()),
        complete_polynomial_coefficient_degrees=list(range(full_degree+1)),
        every_coefficient_of_every_source_row_returned=True,
        target_sha256=polynomial_matrix_digest(target))


def _to_exact_prime_coefficients(M, original_fp):
    """Use only the given original prime field and verify its exact embedding."""
    R, k = M.base_ring(), M.base_ring().base_ring()
    prime = int(original_fp.characteristic())
    assert int(original_fp.cardinality()) == prime
    assert int(k.characteristic()) == prime
    assert int(k.degree()) in (1, 2)
    F = PolynomialRing(original_fp, "r942_same_prime_parameter")
    entries = []
    for p in M.list():
        coefficients = []
        for c in p.list():
            cc = finite_coordinates(c, k)
            assert all(x == 0 for x in cc[1:])
            f = original_fp(cc[0])
            assert k(f) == c and c**prime == c
            coefficients.append(f)
        entries.append(F(coefficients))
    answer = matrix(F, M.nrows(), M.ncols(), entries)
    # Every original coefficient, including every whole source row, returns.
    assert matrix(R, M.nrows(), M.ncols(),
                  [R([k(c) for c in p.list()]) for p in answer.list()]) == M
    return answer


def _recover_complete_matrix(P_original, weights, original_fp, progress=None):
    """Private exact algebra, also used by the small constructed API fixture."""
    R, k = P_original.base_ring(), P_original.base_ring().base_ring()
    weights = tuple(int(d) for d in weights)
    n, m = len(weights), int(P_original.nrows())
    assert P_original.ncols() == n and m >= n
    assert all(0 <= d <= 5 for d in weights)
    source_degree, max_weight = 12, max(weights)
    for row in P_original.rows():
        _weighted_check(row, weights, source_degree)
    P_all = _to_exact_prime_coefficients(P_original, original_fp)
    F, fp = P_all.base_ring(), original_fp
    t, h = F.gen(), F.gen()-1
    at_two = matrix(fp, m, n, lambda i, j:P_all[i, j](fp(2)))
    selected = tuple(int(i) for i in at_two.transpose().pivots())
    # The original-source caller has the complete-fibre RR proof for this rank.
    assert len(selected) == n
    Q_all = matrix(F, m, n, lambda i, j:_homogeneous_substitute(
        P_all[i, j], source_degree-weights[j], t+3, h))
    P, Q = P_all.matrix_from_rows(selected), Q_all.matrix_from_rows(selected)
    Q_zero = matrix(fp, n, n, lambda i, j:Q[i, j](fp(5)))
    expected_Q_zero = at_two.matrix_from_rows(selected)*diagonal_matrix(
        fp, [fp(4)**(source_degree-d) for d in weights])
    assert Q_zero == expected_Q_zero
    inverse = Q_zero.inverse()
    one = identity_matrix(fp, n)
    assert inverse*Q_zero == one and Q_zero*inverse == one
    shifted_P = matrix(F, n, n, lambda i, j:P[i, j](t+5))
    shifted_Q = matrix(F, n, n, lambda i, j:Q[i, j](t+5))
    pp = [_coefficient_matrix(shifted_P, degree) for degree in range(max_weight+1)]
    qq = [_coefficient_matrix(shifted_Q, degree) for degree in range(max_weight+1)]
    assert qq[0] == Q_zero
    coefficients = []
    scalar = fp(4)**6
    for degree in range(max_weight+1):
        right = scalar*pp[degree]
        for j in range(1, degree+1):
            right -= qq[j]*coefficients[degree-j]
        coefficients.append(inverse*right)
    C = matrix(F, n, n, lambda i, j:sum(
        (coefficients[d][i, j]*(t-5)**d for d in range(max_weight+1)), F.zero()))
    assert all(not C[i, j] or int(C[i, j].degree()) <= weights[i]-weights[j]
               for i in range(n) for j in range(n))
    _progress(progress, "complete weighted W matrix reconstructed",
              original_source_rows=m, original_basis_dimension=n,
              exact_taylor_coefficients=max_weight+1)
    source_return = _whole_product_return(
        Q_all, C, scalar*P_all, label="all ordered original central R3 rows")
    C_star = matrix(F, n, n, lambda i, j:_homogeneous_substitute(
        C[i, j], weights[i]-weights[j], t+3, h))
    diagonal = diagonal_matrix(F, [F(fp(4)**d) for d in weights])
    star_return = _whole_product_return(
        C_star, C, diagonal, label="whole weighted W involution")
    inverse_C = diagonal_matrix(F, [F(fp(4)**(-d)) for d in weights])*C_star
    unit_F = identity_matrix(F, n)
    inverse_left = _whole_product_return(
        inverse_C, C, unit_F, label="whole polynomial inverse on all source rows")
    inverse_right = _whole_product_return(
        C, inverse_C, unit_F, label="whole polynomial inverse on all target columns")

    # Return to the CALLER'S original coefficient field and polynomial ring.
    C_original = matrix(R, n, n, [
        R([k(c) for c in p.list()]) for p in C.list()])
    assert _to_exact_prime_coefficients(C_original, fp).list() == C.list()
    record = dict(
        method="original complete source and proved weighted degree; constant inverse plus exact coefficients",
        original_source_rows=m, original_basis_dimension=n,
        full_source_section_weight=source_degree, maximum_original_basis_weight=max_weight,
        exact_taylor_center=5, exact_full_fibre_source_center=2,
        exact_taylor_coefficient_degrees=list(range(max_weight+1)),
        original_selected_source_row_indices=list(selected),
        original_all_source_rows_sha256=polynomial_matrix_digest(P_original),
        original_full_fibre_matrix_sha256=_field_matrix_digest(at_two),
        selected_constant_matrix_sha256=_field_matrix_digest(Q_zero),
        full_constant_inverse_sha256=_field_matrix_digest(inverse),
        complete_original_W_matrix_sha256=polynomial_matrix_digest(C_original),
        whole_source_return=source_return, whole_star_return=star_return,
        whole_polynomial_inverse_left_return=inverse_left,
        whole_polynomial_inverse_right_return=inverse_right,
        every_input_coefficient_checked_in_the_given_original_prime_field=True,
        no_new_constant_field_or_root=True,
        every_weighted_entry_degree_bound_checked=True,
        every_original_source_row_returned_as_a_full_polynomial=True,
        complete_polynomial_inverse_verified=True,
        point_values_or_short_taylor_prefix_used_as_global_certificate=False)
    return C_original, record


def _complete_original_central_R3_rows(embedding, progress=None):
    """All 528 original rows, with each uncached full M2 operator built once."""
    maps = embedding["original_map_sections_context"]
    operations = embedding["operations"]
    R, k = operations["affine_polynomial_ring"], embedding["constants"]
    weights = tuple(int(d) for d in embedding["original_affine_context"]["basis_weights"])
    n, j = len(weights), 2
    assert n == 306 and R.base_ring() is k
    assert maps["kind"] == "rank2_original_map_section_fractions_context"
    assert maps["constants"] is k and maps["local_context"]["constants"] is k
    assert embedding["original_omega"] is maps["original_omega"]
    assert tuple(embedding["sigma_a_index"]) == tuple(maps["sigma_a_index"])
    recipes = tuple(tuple(int(i) for i in recipe)
                    for recipe in maps["complete_RR_product_recipes"][3])
    assert len(recipes) == len(maps["complete_RR_product_series"][3]) == 528
    assert all(len(recipe) == 3 and all(0 <= i < 120 for i in recipe)
               for recipe in recipes)
    canonical_recipes = tuple(tuple(sorted(recipe)) for recipe in recipes)
    pulls = embedding["base_M2_pullback_coordinates"][2]
    assert pulls.base_ring() is R and pulls.nrows() == 120 and pulls.ncols() == n
    needed = {()}
    for recipe in canonical_recipes:
        needed.update(recipe[start:] for start in range(len(recipe)+1))
    products = {():vector(R, operations["unit"])}
    for recipe in sorted(r for r in needed if len(r) == 1):
        products[recipe] = _weighted_check(vector(R, pulls.row(recipe[0])), weights, 4)
    groups = {}
    for recipe in sorted(r for r in needed if len(r) >= 2):
        groups.setdefault(recipe[0], {}).setdefault(len(recipe), []).append(recipe)
    original_cache = embedding["actual_multiplier_cache"]
    assert isinstance(original_cache, dict)
    original_cache_keys = set(original_cache)
    operator_records, batch_records = [], []
    started = time.monotonic()
    # Sorted factors ensure a suffix begins with a >= head. Descending head,
    # then ascending length, makes every full suffix available before use.
    for head in sorted(groups, reverse=True):
        key = (j, int(head))
        reused = key in original_cache
        operator = (original_cache[key] if reused else
                    operations["multiplication_matrix"](pulls.row(head)))
        assert operator.base_ring() is R and operator.nrows() == operator.ncols() == n
        assert operations["unit"]*operator == pulls.row(head)
        operator_record = dict(
            original_degeneracy=j, original_M2_index=int(head),
            original_embedding_cache_entry_reused=reused,
            entire_original_operator_sha256=polynomial_matrix_digest(operator),
            original_M2_pullback_sha256=polynomial_vector_digest(pulls.row(head)),
            every_operator_row_and_column_retained=True)
        operator_records.append(operator_record)
        for degree in sorted(groups[head]):
            current_recipes = groups[head][degree]
            for start in range(0, len(current_recipes), 32):
                current = current_recipes[start:start+32]
                assert all(recipe[1:] in products for recipe in current)
                left = matrix(R, [products[recipe[1:]] for recipe in current])
                values = left*operator
                assert values.nrows() == len(current) and values.ncols() == n
                for i, recipe in enumerate(current):
                    assert recipe not in products
                    products[recipe] = _weighted_check(
                        vector(R, values.row(i)), weights, 4*degree)
                batch_records.append(dict(
                    original_M2_index=int(head), section_power=degree,
                    complete_recipe_tuples=[list(recipe) for recipe in current],
                    complete_source_sha256=polynomial_matrix_digest(left),
                    complete_output_sha256=polynomial_matrix_digest(values)))
                _progress(progress, "whole central R3 source through one original M2 operator",
                          original_M2_index=int(head), section_power=degree,
                          completed_suffix_products=len(products)-1,
                          full_required_suffix_products=len(needed)-1,
                          seconds=time.monotonic()-started)
        if reused:
            assert operator is original_cache[key]
        del operator
    assert set(products) == needed
    assert embedding["actual_multiplier_cache"] is original_cache
    assert set(original_cache) == original_cache_keys
    P_all = matrix(R, [products[recipe] for recipe in canonical_recipes])
    assert P_all.nrows() == 528 and P_all.ncols() == 306
    slots = tuple((i, e) for i in range(n) for e in range(13-weights[i]))
    assert len(slots) == 3114
    t = R.gen()
    for index, recipe in enumerate(canonical_recipes):
        row = P_all.row(index)
        _weighted_check(row, weights, 12)
        returned = vector(R, n)
        for i, exponent in slots:
            returned[i] += row[i][exponent]*t**exponent
        assert returned == row == products[recipe]
    record = dict(
        method="all original central R3 recipes; descending heads and complete suffix returns",
        original_degeneracy=2, original_logarithmic_differential_multiplier=8,
        original_recipe_count=528, original_coordinate_count=306,
        complete_weighted_coordinate_count=3114,
        original_ordered_recipes_sha256=digest([list(r) for r in recipes]),
        commutative_factor_order_sha256=digest([list(r) for r in canonical_recipes]),
        every_original_recipe_row_in_unchanged_order=True,
        every_original_weighted_coordinate_returned=True,
        complete_original_source_matrix_sha256=polynomial_matrix_digest(P_all),
        complete_original_operators=operator_records,
        complete_product_batches=len(batch_records),
        complete_product_batches_sha256=digest(batch_records),
        original_embedding_cache_unchanged=True,
        each_uncached_full_operator_constructed_exactly_once=True,
        uncached_operator_released_after_all_its_full_suffix_batches=True)
    return P_all, record


def build_original_w_basis_transport(embedding, progress=None):
    """Build the actual W transport from the same authenticated embedding."""
    assert embedding["kind"] == "rank2_original_section_ring_embedding_context"
    operations, k, fp = (embedding["operations"], embedding["constants"],
                         embedding["original_fp"])
    R = operations["affine_polynomial_ring"]
    S = operations["infinity_polynomial_ring"]
    weights = tuple(int(d) for d in embedding["original_affine_context"]["basis_weights"])
    prime, n = int(k.characteristic()), len(weights)
    assert prime in (29, 41) and int(k.cardinality()) == prime**2
    assert int(fp.cardinality()) == prime and n == 306
    assert max(weights) <= (4 if prime == 29 else 5)
    assert R.base_ring() is S.base_ring() is k
    t, s = R.gen(), S.gen()
    unit = vector(R, operations["unit"])
    assert embedding["original_SY_coordinates"] == (t*t+3)**2*unit
    P_all, source_receipt = _complete_original_central_R3_rows(embedding, progress)
    C, recovery_receipt = _recover_complete_matrix(P_all, weights, fp, progress)
    assert unit*C == unit
    D = matrix(S, n, n, lambda i, j:sum(
        (k(c)*s**(weights[i]-weights[j]-e)
         for e, c in enumerate(C[i, j].list()) if c), S.zero()))
    assert all(not D[i, j] or int(D[i, j].degree()) <= weights[i]-weights[j]
               for i in range(n) for j in range(n))
    reversed_back = matrix(R, n, n, lambda i, j:sum(
        (k(c)*t**(weights[i]-weights[j]-e)
         for e, c in enumerate(D[i, j].list()) if c), R.zero()))
    assert reversed_back == C
    D_star = matrix(S, n, n, lambda i, j:_homogeneous_substitute(
        D[i, j], weights[i]-weights[j], 1-s, 1+3*s))
    # Whole other-chart inverse follows and is also explicitly returned.
    infinity_star_return = _whole_product_return(
        _to_exact_prime_coefficients(D_star, fp),
        _to_exact_prime_coefficients(D, fp),
        _to_exact_prime_coefficients(
            diagonal_matrix(S, [S(k(4)**d) for d in weights]), fp),
        label="whole other-chart weighted W involution")

    def weighted_transport(value, bound, infinity=False):
        """Return g^bound W(value) in the same whole chart; keep g^bound."""
        ring, transform = (S, D) if infinity else (R, C)
        x = ring.gen()
        numerator, denominator = ((1-x, 1+3*x) if infinity else (x+3, x-1))
        value = vector(ring, value)
        bound = int(bound)
        assert bound >= 0
        _weighted_check(value, weights, bound)
        coefficients = vector(ring, [
            _homogeneous_substitute(value[i], bound-weights[i],
                                    numerator, denominator) for i in range(n)])
        answer = coefficients*transform
        _weighted_check(answer, weights, bound)
        return answer, denominator**bound

    # The true geometric W exchanges pi1/pi4 and fixes pi2. Naturality of
    # logarithmic differential pullback and W*J=h^4 J/16 require every
    # original M2 row, including its original j multiplier, to return.
    original_M2_returns = []
    C_fp = _to_exact_prime_coefficients(C, fp)
    pulls_by_j = embedding["base_M2_pullback_coordinates"]
    for j, partner in ((1, 4), (2, 2), (4, 1)):
        pulls, other = pulls_by_j[j], pulls_by_j[partner]
        assert pulls.nrows() == other.nrows() == 120
        assert pulls.ncols() == other.ncols() == n
        for row in pulls.rows():
            _weighted_check(row, weights, 4)
        transformed_coefficients = matrix(R, 120, n, lambda i, column:
            _homogeneous_substitute(pulls[i, column], 4-weights[column], t+3, t-1))
        returned = _whole_product_return(
            _to_exact_prime_coefficients(transformed_coefficients, fp), C_fp,
            _to_exact_prime_coefficients(k(16)*other, fp),
            label="every original M2 row pi_%d to pi_%d" % (j, partner))
        returned.update(
            original_source_degeneracy=j, original_target_degeneracy=partner,
            original_logarithmic_differential_multipliers_preserved=True,
            entire_original_pulled_M2_source_sha256=polynomial_matrix_digest(pulls),
            entire_original_pulled_M2_target_sha256=polynomial_matrix_digest(other))
        original_M2_returns.append(returned)

    receipt = dict(
        kind="rank2_original_complete_weighted_W_basis_transport",
        status="actual_original_source_all_rows_and_complete_polynomial_inverse_verified",
        prime=prime, original_basis_dimension=n,
        actual_original_source=source_receipt,
        exact_complete_matrix_recovery=recovery_receipt,
        original_finite_chart_W_matrix_sha256=polynomial_matrix_digest(C),
        original_infinity_chart_W_matrix_sha256=polynomial_matrix_digest(D),
        full_other_chart_involution_return=infinity_star_return,
        full_other_chart_coefficient_reversal_returned=True,
        complete_original_M2_three_degeneracy_returns=original_M2_returns,
        every_row_of_all_three_actual_120_M2_pullbacks_returned=True,
        same_original_unit_and_central_SY_returned=True,
        complete_original_basis_transport_constructed=True,
        arbitrary_ideal_saturation_claimed_to_recover_missing_primary_part=False,
        original_endpoint_pole_divisors_claimed=False,
        original_four_intersections_or_shadow_claimed=False,
        helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    return dict(
        kind="rank2_original_complete_weighted_W_basis_transport_context",
        original_embedding=embedding, constants=k, original_fp=fp,
        finite_matrix=C, infinity_matrix=D, basis_weights=weights,
        weighted_transport=weighted_transport, certificate=receipt), receipt


def complete_w_matrix_recovery_preflight():
    """Small constructed free-module API only, not the original Y."""
    fp = GF(29)
    R = PolynomialRing(fp, "constructed_parameter")
    t = R.gen()
    weights = (0, 1, 2, 4)
    n = len(weights)
    U = identity_matrix(R, n)
    for i in range(1, n):
        U[i, i-1] = t**(weights[i]-weights[i-1])+1
    nilpotent = U-identity_matrix(R, n)
    inverse_U = identity_matrix(R, n)
    term = identity_matrix(R, n)
    for exponent in range(1, n):
        term = term*(-nilpotent)
        inverse_U += term
    assert U*inverse_U == inverse_U*U == identity_matrix(R, n)
    P = diagonal_matrix(R, [(t+1)**(12-d) for d in weights])*inverse_U
    P_all = P.stack(matrix(R, [P.row(0)+P.row(2),
                              P.row(1)+P.row(3), P.row(0)+2*P.row(3)]))
    recovered, receipt = _recover_complete_matrix(P_all, weights, fp)
    U_star = matrix(R, n, n, lambda i, j:_homogeneous_substitute(
        U[i, j], weights[i]-weights[j], t+3, t-1))
    expected = U_star*diagonal_matrix(R, [R(fp(2)**d) for d in weights])*inverse_U
    assert recovered == expected and any(p.degree() > 0 for p in recovered.list() if p)
    # Force the extra source rows to participate in the final full return:
    # a term divisible by (t-5)^5 changes no recovery coefficient but must fail.
    corrupted = matrix(R, P_all)
    corrupted[n, 0] += (t-5)**5
    rejected = False
    try:
        _recover_complete_matrix(corrupted, weights, fp)
    except AssertionError:
        rejected = True
    assert rejected
    return dict(
        kind="constructed_complete_weighted_W_matrix_api_only",
        original_Y_normalization_or_W_matrix_computed=False,
        constructed_dimension=n, constructed_source_rows=int(P_all.nrows()),
        constructed_nonconstant_weighted_matrix_recovered=True,
        complete_constructed_source_and_inverse_returns=receipt,
        changed_extra_source_row_with_zero_low_taylor_prefix_rejected=True)
