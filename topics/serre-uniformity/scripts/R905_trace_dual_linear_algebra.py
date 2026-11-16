#!/usr/bin/env python3
"""R905/R909 finite linear algebra, executed only by the public Actions driver.

All matrices are column maps.  Polynomial coefficient lists are low to high.
This module does not read sources, select a different curve or run on import.
"""
from math import comb
from flint import nmod_mat

P = 1000000753
N = 272
EPS = [0] + [1] * 144 + [2] * 127


def mat(raw):
    return nmod_mat(raw, P)


def zero(m, n):
    return nmod_mat(m, n, P)


def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def rows(M):
    return [[int(M[i, j]) for j in range(M.ncols())]
            for i in range(M.nrows())]


def shape(raw, m, n):
    assert len(raw) == m and all(len(row) == n for row in raw)


def sub(M, I, J):
    return mat([[int(M[i, j]) for j in J] for i in I])


def hcat(A, B):
    assert A.nrows() == B.nrows()
    return mat([[int(A[i, j]) for j in range(A.ncols())] +
                [int(B[i, j]) for j in range(B.ncols())]
                for i in range(A.nrows())])


def positions(weight):
    return [(i, k) for i, e in enumerate(EPS)
            for k in range(max(0, weight - e + 1))]


def pivot_columns(reduced, rank):
    found = []
    for i in range(rank):
        j = next(j for j in range(reduced.ncols()) if reduced[i, j])
        assert int(reduced[i, j]) == 1
        found.append(j)
    assert found == sorted(set(found))
    return found


def independent_rows(M, required):
    reduced, rank = M.transpose().rref()
    if rank != required:
        return rank, []
    return rank, pivot_columns(reduced, rank)


def canonical_kernel(M):
    """One RREF gives the original free-coordinate identity kernel."""
    reduced, rank = M.rref()
    pivots = pivot_columns(reduced, rank)
    free = [j for j in range(M.ncols()) if j not in set(pivots)]
    raw = [[0] * len(free) for _ in range(M.ncols())]
    for j, original in enumerate(free):
        raw[original][j] = 1
    for i, original in enumerate(pivots):
        raw[original] = [(-int(reduced[i, j])) % P for j in free]
    K = mat(raw)
    assert M * K == zero(M.nrows(), len(free))
    return rank, pivots, free, K


def coefficient_matrices(normal, weight):
    order = positions(weight)
    assert normal.nrows() == len(order)
    raw = [[[0] * normal.ncols() for _ in range(N)]
           for _ in range(weight + 1)]
    for row, (i, k) in enumerate(order):
        raw[k][i] = [int(normal[row, j]) for j in range(normal.ncols())]
    return [mat(x) for x in raw]


def normal_matrix(coefficients, weight):
    n = coefficients[0].ncols()
    assert all(A.nrows() == N and A.ncols() == n for A in coefficients)
    for k, A in enumerate(coefficients):
        for i, e in enumerate(EPS):
            if k > weight - e:
                assert all(A[i, j] == 0 for j in range(n))
    return mat([[int(coefficients[k][i, j]) for j in range(n)]
                for i, k in positions(weight)])


def evaluate(coefficients, a):
    m, n = coefficients[0].nrows(), coefficients[0].ncols()
    answer = zero(m, n)
    for A in reversed(coefficients):
        answer = answer * a + A
    return answer


def hasse(coefficients, a, order):
    m, n = coefficients[0].nrows(), coefficients[0].ncols()
    answer = zero(m, n)
    for k in range(order, len(coefficients)):
        answer += coefficients[k] * (comb(k, order) * pow(a, k-order, P) % P)
    return answer


def evaluation_map(weight, a, hasse_order=0):
    raw = [[0] * len(positions(weight)) for _ in range(N)]
    for col, (i, k) in enumerate(positions(weight)):
        if k >= hasse_order:
            raw[i][col] = comb(k, hasse_order) * pow(a, k-hasse_order, P) % P
    return mat(raw)


def embed(lower_weight, upper_weight):
    low, high = positions(lower_weight), positions(upper_weight)
    lookup = {p: i for i, p in enumerate(high)}
    raw = [[0] * len(low) for _ in high]
    for col, pos in enumerate(low):
        raw[lookup[pos]][col] = 1
    return mat(raw)


def quotient_from_normalized_columns(U, identity_rows):
    """Return the literal free-row quotient and its standard representatives."""
    m, rank = U.nrows(), U.ncols()
    assert identity_rows == sorted(set(identity_rows)) and len(identity_rows) == rank
    assert sub(U, identity_rows, list(range(rank))) == eye(rank)
    free = [i for i in range(m) if i not in set(identity_rows)]
    q = [[0] * m for _ in free]
    section = [[0] * len(free) for _ in range(m)]
    for k, i in enumerate(free):
        q[k][i] = 1
        section[i][k] = 1
        for j, pivot in enumerate(identity_rows):
            q[k][pivot] = -int(U[i, j]) % P
    Q, S = mat(q), mat(section)
    assert Q * U == zero(len(free), rank)
    assert Q * S == eye(len(free))
    return free, Q, S


def inverse_hasse_three(F, a, inverse0):
    """Reuse the already certified inverse; form only new orders one and two."""
    F0, F1, F2 = [hasse(F, a, k) for k in range(3)]
    assert F0 * inverse0 == eye(N) and inverse0 * F0 == eye(N)
    G1 = -(inverse0 * F1 * inverse0)
    G2 = -(inverse0 * (F1 * G1 + F2 * inverse0))
    G = [inverse0, G1, G2]
    FF = [F0, F1, F2]
    for k in (1, 2):
        left, right = zero(N, N), zero(N, N)
        for j in range(k + 1):
            left += FF[j] * G[k-j]
            right += G[j] * FF[k-j]
        assert left == right == zero(N, N)
    return FF, G


def principal_part_matrix(G, a):
    """All690 test rows, all670 trace-dual differentials; the R909 minus sign."""
    PP = [evaluation_map(3, a, k) for k in range(3)]
    C = []
    for k in range(3):
        value = zero(N, 690)
        for j in range(k + 1):
            value += G[j] * PP[k-j]
        C.append(value)
    labels = [(i, k) for i in range(N)
              for k in range(2 if i < 146 else 3)]
    assert len(labels) == 670
    M = mat([[(-int(C[2-k][i, row])) % P for i, k in labels]
             for row in range(690)])
    return labels, M


def divide_by_auxiliary_section(F, a, inverse0):
    """The exact linear polynomial division V3 -> V2, not a quotient inverse."""
    identity = eye(690)
    original = coefficient_matrices(identity, 3)
    constant = inverse0 * evaluation_map(3, a)
    remainder = [original[k] - F[k] * constant for k in range(4)]
    assert evaluate(remainder, a) == zero(N, 690)
    quotient = [zero(N, 690) for _ in range(3)]
    quotient[2] = remainder[3]
    quotient[1] = remainder[2] + quotient[2] * a
    quotient[0] = remainder[1] + quotient[1] * a
    assert remainder[0] == -(quotient[0] * a)
    L = normal_matrix(quotient, 2)
    residual = [-(quotient[0] * a), quotient[0] - quotient[1] * a,
                quotient[1] - quotient[2] * a, quotient[2]]
    assert all(residual[k] + F[k] * constant == original[k] for k in range(4))
    return L, constant


def auxiliary_power_vector(a, power, weight):
    assert power <= weight
    lookup = {pos: i for i, pos in enumerate(positions(weight))}
    raw = [[0] for _ in positions(weight)]
    for k in range(power + 1):
        raw[lookup[(0, k)]][0] = comb(power, k) * pow(-a, power-k, P) % P
    return mat(raw)


def weight_one_section(parameter):
    return mat([[pow(parameter, j, P)] for j in range(146)])


def weight_one_fibre_vector(parameter, a):
    return evaluation_map(1, a) * weight_one_section(parameter)


def multiplier_at_original_cyclic_point(W, K, inverse_K, v, budget):
    """A new section multiplier, with the old inverse used as given."""
    columns = []
    current = v
    for j in range(N):
        if j % 32 == 0:
            budget()
        columns.append([int(current[i, 0]) for i in range(N)])
        if j + 1 < N:
            current = W * current
    C = mat([[columns[j][i] for j in range(N)] for i in range(N)])
    product = C * inverse_K
    assert product * K == C
    assert sub(product, list(range(N)), [0]) == v
    assert product * W == W * product
    return product


def interpolate_four(values, nodes):
    """Four scalar Lagrange polynomials, applied to whole coefficient blocks."""
    assert len(nodes) == len(values) == 4 and len(set(nodes)) == 4
    output = [zero(N, N) for _ in range(4)]
    for a, V in zip(nodes, values):
        coefficients = [1]
        denominator = 1
        for b in nodes:
            if b == a:
                continue
            new = [0] * (len(coefficients) + 1)
            for k, c in enumerate(coefficients):
                new[k] = (new[k] - b*c) % P
                new[k+1] = (new[k+1] + c) % P
            coefficients = new
            denominator = denominator * (a-b) % P
        factor = pow(denominator, -1, P)
        for k, c in enumerate(coefficients):
            output[k] += V * (c*factor % P)
    for a, V in zip(nodes, values):
        assert evaluate(output, a) == V
    for k, V in enumerate(output):
        for i in range(N):
            for j in range(N):
                if k > 1 + EPS[j] - EPS[i]:
                    assert V[i, j] == 0
    return output


def weight_one_times_V2(multiplier):
    lookup = {p: k for k, p in enumerate(positions(3))}
    output = [[0] * 418 for _ in range(690)]
    for col, (input_i, shift) in enumerate(positions(2)):
        for k, A in enumerate(multiplier):
            for i in range(N):
                c = int(A[i, input_i])
                if c:
                    assert (i, k+shift) in lookup
                    row = lookup[(i, k+shift)]
                    output[row][col] = (output[row][col] + c) % P
    return mat(output)


def H_quotient_multiplication(product_map):
    v2, v3 = positions(2), positions(3)
    ix2, ix3 = {p:i for i,p in enumerate(v2)}, {p:i for i,p in enumerate(v3)}
    I = [ix3[(i, 3-EPS[i])] for i in range(N)]
    J = [ix2[(i, 2-EPS[i])] for i in range(N)]
    return sub(product_map, I, J)


def H_test_function_map():
    ix = {p:i for i,p in enumerate(positions(3))}
    raw = [[0] * 690 for _ in range(N)]
    for i in range(N):
        raw[i][ix[(i, 3-EPS[i])]] = 1
    return mat(raw)


def cyclic_trace(M, unit, budget):
    """Keep the whole algebra, including nilpotents; no factor removal."""
    columns = []
    current = unit
    for j in range(N + 1):
        if j % 32 == 0:
            budget()
        if j < N:
            columns.append([int(current[i, 0]) for i in range(N)])
        else:
            next_column = current
        if j < N:
            current = M * current
    K = mat([[columns[j][i] for j in range(N)] for i in range(N)])
    determinant = int(K.det())
    answer = {"multiplication_matrix_mod_prime":rows(M),
              "unit_vector_mod_prime":rows(unit),
              "power_basis_matrix_mod_prime":rows(K),
              "next_power_column_mod_prime":rows(next_column),
              "actual_power_basis_determinant_mod_prime":determinant,
              "actual_primitive_unit":determinant != 0,
              "whole_algebra_dimension":N,
              "factor_removal_or_reduced_support_replacement":False}
    if not determinant:
        _, rank = K.rref()
        answer["actual_power_span_rank"] = rank
        return answer
    inverse_K = K.inv()
    assert K * inverse_K == eye(N) and inverse_K * K == eye(N)
    relation = inverse_K * next_column
    companion = [[0]*N for _ in range(N)]
    for j in range(N-1):
        companion[j+1][j] = 1
    for i in range(N):
        companion[i][N-1] = int(relation[i, 0])
    C = mat(companion)
    assert M * K == K * C and K * relation == next_column
    ascending = [(-int(relation[i, 0])) % P for i in range(N)] + [1]
    descending = list(reversed(ascending))
    traces = [N]
    for m in range(1, N):
        rhs = m * descending[m]
        for j in range(1, m):
            rhs += descending[j] * traces[m-j]
        traces.append(-rhs % P)
    trace_row = mat([traces]) * inverse_K
    assert int((trace_row * unit)[0, 0]) == N
    assert trace_row * K == mat([traces])
    answer.update({
        "actual_power_span_rank":N,
        "inverse_power_basis_mod_prime":rows(inverse_K),
        "both_power_basis_inverse_products_verified":True,
        "all272_complete_companion_relations_verified":True,
        "characteristic_coefficients_ascending_T":ascending,
        "power_traces_mod_prime":traces,
        "canonical_quotient_trace_row_mod_prime":rows(trace_row)[0],
        "trace_of_unit_equals_whole_length272":True,
        "trace_computation":"Newton identities on the certified full companion algebra",
    })
    return answer


def selected_solution(M, b, required_rank):
    """A new finite chart with all columns free except the selected pivots."""
    reduced, rank = M.rref()
    if rank != required_rank:
        return {"actual_rank":rank,"rank_is_required":False}
    J = pivot_columns(reduced, rank)
    row_rank, I = independent_rows(sub(M, list(range(M.nrows())), J), rank)
    assert row_rank == rank
    square = sub(M, I, J)
    determinant = int(square.det())
    assert determinant != 0
    rhs = sub(b, I, [0])
    solved, augmented_rank = hcat(square, rhs).rref()
    assert augmented_rank == rank
    assert sub(solved, list(range(rank)), list(range(rank))) == eye(rank)
    chosen = sub(solved, list(range(rank)), [rank])
    assert square * chosen == rhs
    raw = [[0] for _ in range(M.ncols())]
    for k, j in enumerate(J):
        raw[j][0] = int(chosen[k, 0])
    solution = mat(raw)
    full_product = M * solution
    return {"actual_rank":rank,"rank_is_required":True,
            "selected_rows":I,"selected_columns":J,
            "selected_minor_determinant_mod_prime":determinant,
            "selected_minor_mod_prime":rows(square),
            "solution_coefficients_mod_prime":[x[0] for x in raw],
            "full_product_mod_prime":rows(full_product),
            "all_original_rows_multiplied_back":full_product == b,
            "free_coefficients_set_to_zero":True,
            "full_selected_inverse_materialized":False}
