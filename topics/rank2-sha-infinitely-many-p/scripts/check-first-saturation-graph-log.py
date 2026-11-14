#!/usr/bin/env python3
"""R200: the same p=23,D=7,k=30 images versus their graph-log row spaces."""

import importlib.util
from math import comb
from pathlib import Path

from flint import ctx, fmpq, fmpq_series as Series


path = Path(__file__).with_name("check-theta-plane-saturated-jets.py")
spec = importlib.util.spec_from_file_location("actual_plane", path)
plane = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plane)


def reduction(value, prime):
    denominator = int(value.denominator) % prime
    assert denominator, value
    return int(value.numerator) % prime * pow(denominator, -1, prime) % prime


def row_space(rows, prime):
    matrix = [[int(value) % prime for value in row] for row in rows]
    rank = 0
    for col in range(len(matrix[0])):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][col], -1, prime)
        matrix[rank] = [value * inverse % prime for value in matrix[rank]]
        for i in range(len(matrix)):
            if i != rank:
                multiple = matrix[i][col]
                matrix[i] = [(x-multiple*y) % prime
                             for x, y in zip(matrix[i], matrix[rank])]
        rank += 1
        if rank == len(matrix):
            break
    return matrix[:rank]


def main():
    prime, degree, r, q, k = 23, 7, 6, 5, 30
    columns, s_rows = plane.actual_rows(degree)
    cap = ctx.cap
    s = Series([0, 1], prec=cap)
    period = Series([fmpq(comb(2*n, n), 4**n*(4*n+1))
                     for n in range(cap)], prec=cap)
    s_of_w = (s*period**4).reversion()
    values = [Series([row[col] for row in s_rows], prec=cap)(s_of_w)
              for col in range(len(columns))]
    division_depths = {
        "first_saturation": [int(m+c >= r) for m, c in columns],
        "original_weight_strips": [(m+c)//r for m, c in columns],
    }
    actual = {}
    for name, depths in division_depths.items():
        actual[name] = [
            [reduction(prime**(n//r)*values[col][n]/prime**depth, prime)
             for col, depth in enumerate(depths)]
            for n in range(k)
        ]

    first = values[columns.index((1, 0))]
    difference = values[columns.index((1, 1))]
    # R199: these exact short raw coefficients equal the true axis coefficients.
    axis_f = Series([first[n] if n <= r else fmpq(0) for n in range(cap)], prec=cap)
    axis_c = Series([difference[n] if n <= r+1 else fmpq(0)
                     for n in range(cap)], prec=cap)
    y0 = axis_f.reversion()
    phi = axis_c(y0)
    phi_coefficients = [phi[n+2] for n in range(r)]
    y_coefficients = [y0[n+1] for n in range(r)]
    derivative = fmpq(1, 3)
    for n in range(1, r):
        derivative *= fmpq(4*n+1, 4*n+3)
    tau = reduction(prime*derivative/r, prime)
    assert tau
    scalar = 17*tau

    ctx.cap = r
    parameter = Series([0, 1], prec=r)
    Phi = Series(phi_coefficients, prec=r)
    Y = Series(y_coefficients, prec=r)
    delta = lambda series: Series([n*series[n] for n in range(r)], prec=r)
    L = -Phi-delta(Phi)
    assert Phi[0] == -22 and L[0] == 22 and Y[0] == 1
    E = {1: 1/L}
    M = {0: 1/(scalar*Y**r)}
    for j in range(1, q):
        E[j+1] = (j*E[j]-delta(E[j]))/((j+1)*L)
    for j in range(q):
        M[j+1] = ((r+j)*M[j]-delta(M[j]))/((j+1)*L)
    phi_powers = [Series([1], prec=r)]
    for _ in range(degree):
        phi_powers.append(phi_powers[-1]*Phi)
    l_powers = [Series([1], prec=r)]
    for _ in range(q):
        l_powers.append(l_powers[-1]*L)

    # Strip t uses (eta/(a*y^r))^t, with no t! denominator.
    # After extracting A^(-rt-2j), these are ordinary convolutions in Z.
    zero = lambda: Series([0], prec=r)
    unit = lambda: Series([1], prec=r)
    base_jet = [
        sum((E[b]*M[j-b] for b in range(1, j+1)), zero())
        for j in range(q)
    ]
    powers = [[unit()]+[zero() for _ in range(q-1)]]
    max_depth = max(max(depths) for depths in division_depths.values())
    for depth in range(1, max_depth+1):
        powers.append([
            sum((powers[depth-1][i]*base_jet[j-i]
                 for i in range(j+1)), zero())
            for j in range(q)
        ])

    for name, depths in division_depths.items():
        graph_rows = []
        for j in range(q):
            graph_columns = []
            for (m, c), depth in zip(columns, depths):
                value = sum(
                    (comb(c, i)*phi_powers[c-i]*powers[depth][j-i]
                     for i in range(min(c, j)+1)), zero())
                value *= parameter**(m+c-r*depth)*l_powers[j]
                graph_columns.append(value)
            for angular in range(r):
                graph_rows.append([reduction(value[angular], prime)
                                   for value in graph_columns])

        actual_space = row_space(actual[name], prime)
        graph_space = row_space(graph_rows, prime)
        assert actual_space == graph_space
        assert len(actual_space) == k == 30
        assert len(columns)-len(actual_space) == 6
        print({"p": prime, "D": degree, "k": k, "source_lattice": name,
               "source_rank": len(columns), "actual_rank": len(actual_space),
               "graph_log_rank": len(graph_space), "common_kernel_rank": 6,
               "full_row_space_equal": True})


if __name__ == "__main__":
    main()
