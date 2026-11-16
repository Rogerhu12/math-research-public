#!/usr/bin/env python3
"""Rank-eight endpoint order arithmetic. Imported only by the public Actions core.

All series have an explicit common absolute rho precision. Exact Laurent
polynomials are used only for the accumulated basis and its inverse. A zero
truncation never asserts exact zero of an underlying source function.
"""
from flint import nmod_poly

P = 1000000753
D = 8


class NeedPrecision(RuntimeError):
    def __init__(self, reason, bounds=None):
        self.reason = str(reason)
        self.bounds = {} if bounds is None else bounds
        super().__init__(self.reason)

    def to_data(self):
        return {"kind": "NeedPrecision", "reason": self.reason,
                "bounds": self.bounds, "zero_truncation_is_not_exact_zero": True}


def coefficients(value, count=None):
    if count is None:
        count = max(0, value.degree() + 1)
    return [int(value[i]) for i in range(count)]


def scalar_rows(matrix):
    return [[int(x) % P for x in row] for row in matrix]


def matmul(a, b):
    if not a:
        return []
    n, m, r = len(a), len(b), len(b[0])
    assert all(len(row) == m for row in a)
    return [[sum(a[i][k] * b[k][j] for k in range(m)) % P
             for j in range(r)] for i in range(n)]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def rref(rows, columns):
    a = [[int(x) % P for x in row] for row in rows]
    assert all(len(row) == columns for row in a)
    pivots = []
    for c in range(columns):
        k = next((i for i in range(len(pivots), len(a)) if a[i][c]), None)
        if k is None:
            continue
        t = len(pivots)
        a[t], a[k] = a[k], a[t]
        inv = pow(a[t][c], -1, P)
        a[t] = [x * inv % P for x in a[t]]
        for i in range(len(a)):
            if i != t and a[i][c]:
                x = a[i][c]
                a[i] = [(u - x * v) % P for u, v in zip(a[i], a[t])]
        pivots.append(c)
        if len(pivots) == len(a):
            break
    return a, pivots


def kernel(rows, columns=D):
    reduced, pivots = rref(rows, columns)
    free = [i for i in range(columns) if i not in pivots]
    basis = [[0] * len(free) for _ in range(columns)]
    for j, c in enumerate(free):
        basis[c][j] = 1
        for i, p in enumerate(pivots):
            basis[p][j] = (-reduced[i][c]) % P
    assert all(not x for row in matmul(rows, basis) for x in row) if rows and free else True
    return {"equation_matrix_mod_prime": scalar_rows(rows),
            "reduced_equation_matrix_mod_prime": reduced,
            "pivot_columns": pivots, "free_columns": free,
            "rank": len(pivots), "kernel_dimension": len(free),
            "kernel_basis_mod_prime": basis,
            "full_equations_times_kernel_verified": True,
            "free_coordinate_identity_preserved": True}


def inverse(a):
    n = len(a)
    assert all(len(row) == n for row in a)
    m = [[int(x) % P for x in row] + identity(n)[i] for i, row in enumerate(a)]
    det = 1
    for j in range(n):
        k = next((i for i in range(j, n) if m[i][j]), None)
        if k is None:
            raise ValueError("The selected constant basis matrix is singular")
        if k != j:
            m[j], m[k] = m[k], m[j]
            det = -det % P
        x = m[j][j]
        det = det * x % P
        inv = pow(x, -1, P)
        m[j] = [v * inv % P for v in m[j]]
        for i in range(n):
            if i != j and m[i][j]:
                x = m[i][j]
                m[i] = [(u - x * v) % P for u, v in zip(m[i], m[j])]
    answer = [row[n:] for row in m]
    assert matmul(a, answer) == identity(n) and matmul(answer, a) == identity(n)
    return answer, det


def complete_columns(basis):
    assert len(basis) == D
    r = len(basis[0])
    assert all(len(row) == r for row in basis)
    out = [row[:] for row in basis]
    used = []
    assert len(rref(out, r)[1]) == r
    for c in range(D):
        if len(out[0]) == D:
            break
        candidate = [out[i] + [int(i == c)] for i in range(D)]
        if len(rref(candidate, len(candidate[0]))[1]) == len(candidate[0]):
            out = candidate
            used.append(c)
    assert len(out[0]) == D
    inv, det = inverse(out)
    return out, inv, det, used


class SeriesRing:
    def __init__(self, precision):
        assert isinstance(precision, int) and precision > 0
        self.N = precision
        self.p = P
        self.modulus = nmod_poly([0] * precision + [1], P)
        self.zero = nmod_poly([], P)
        self.one = nmod_poly([1], P)

    def element(self, raw):
        if isinstance(raw, int):
            return nmod_poly([raw % P], P)
        return nmod_poly([int(x) % P for x in raw[:self.N]], P)

    def cut(self, value):
        return value % self.modulus

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def neg(self, a):
        return -a

    def mul(self, a, b):
        return (a * b) % self.modulus

    def scale(self, a, c):
        return a * (int(c) % P)

    def power(self, a, n):
        assert isinstance(n, int) and n >= 0
        answer = self.one
        while n:
            if n & 1:
                answer = self.mul(answer, a)
            n //= 2
            if n:
                a = self.mul(a, a)
        return answer

    def unit_inverse(self, a):
        if not int(a[0]):
            raise NeedPrecision("The designated series denominator has no known unit constant term",
                                {"absolute_precision": self.N})
        ai = coefficients(a, self.N)
        out = [pow(ai[0], -1, P)]
        for n in range(1, self.N):
            out.append(-out[0] * sum(ai[i] * out[n-i] for i in range(1, n+1)) % P)
        b = self.element(out)
        assert self.mul(a, b) == self.one
        return b

    def valuation(self, a, label):
        for i in range(self.N):
            if int(a[i]):
                return i
        raise NeedPrecision("No nonzero coefficient is visible in " + str(label),
                            {"label": str(label), "valuation_lower_bound": self.N,
                             "absolute_precision": self.N,
                             "next_coefficient_needed_at_least": self.N})

    def pack(self, value):
        return coefficients(value, self.N)

    def determinant(self, matrix):
        n = len(matrix)
        assert all(len(row) == n for row in matrix)
        if not n:
            return self.one
        def charpoly(a):
            size = len(a)
            if size == 0:
                return [self.one]
            tail = [row[1:] for row in a[1:]]
            old = charpoly(tail)
            q = [self.one, self.neg(a[0][0])]
            v = [a[i][0] for i in range(1, size)]
            for exponent in range(size - 1):
                dot = self.zero
                for j in range(size - 1):
                    dot = self.add(dot, self.mul(a[0][j+1], v[j]))
                q.append(self.neg(dot))
                if exponent + 1 < size - 1:
                    v = [sum_poly(self, (self.mul(tail[i][j], v[j])
                                         for j in range(size-1))) for i in range(size-1)]
            return [sum_poly(self, (self.mul(q[k-j], old[j])
                         for j in range(max(0, k-size), min(k, size-1)+1)))
                    for k in range(size+1)]
        value = charpoly(matrix)[n]
        return value if n % 2 == 0 else -value


def sum_poly(R, values):
    answer = R.zero
    for value in values:
        answer = R.add(answer, value)
    return answer


# Exact finite Laurent polynomials over the selected residue field.
def lp(raw=None, lower=0):
    a = nmod_poly([] if raw is None else raw, P)
    if a.degree() < 0:
        return 0, a
    k = next(i for i in range(a.degree()+1) if int(a[i]))
    return lower + k, nmod_poly(coefficients(a)[k:], P)


def lp_add(a, b):
    if a[1].degree() < 0:
        return b
    if b[1].degree() < 0:
        return a
    low = min(a[0], b[0])
    aa = nmod_poly([0] * (a[0]-low) + coefficients(a[1]), P)
    bb = nmod_poly([0] * (b[0]-low) + coefficients(b[1]), P)
    return lp(coefficients(aa + bb), low)


def lp_mul(a, b):
    return lp(coefficients(a[1] * b[1]), a[0] + b[0])


def lp_scale(a, scalar, shift=0):
    return lp(coefficients(a[1] * (int(scalar) % P)), a[0] + shift)


def lp_pack(a):
    return {"lowest_exponent": a[0], "coefficients_ascending": coefficients(a[1]),
            "exact_finite_Laurent_polynomial_over_residue_field": True}


def lp_unpack(raw):
    assert raw["exact_finite_Laurent_polynomial_over_residue_field"] is True
    return lp(raw["coefficients_ascending"], raw["lowest_exponent"])


def lp_sum(values):
    answer = lp()
    for value in values:
        answer = lp_add(answer, value)
    return answer


def lp_matmul(a, b):
    return [[lp_sum(lp_mul(a[i][k], b[k][j]) for k in range(D))
             for j in range(D)] for i in range(D)]


def lp_identity():
    return [[lp([int(i == j)]) for j in range(D)] for i in range(D)]


class Order:
    """An exact source-defined integral order, represented to known rho precision."""
    def __init__(self, precision, table, one, basis=None, basis_inverse=None,
                 index_length=0, determinant_unit=1, initial_h=0):
        self.R = SeriesRing(precision)
        self.N = precision
        self.table = table
        self.one = one
        self.basis = lp_identity() if basis is None else basis
        self.basis_inverse = lp_identity() if basis_inverse is None else basis_inverse
        self.index_length = int(index_length)
        self.determinant_unit = int(determinant_unit) % P
        self.initial_h = int(initial_h)
        assert self.determinant_unit

    @classmethod
    def primitive(cls, coefficients_monic, precision, initial_h):
        R = SeriesRing(precision)
        c = [R.element(x) for x in coefficients_monic]
        assert len(c) == D+1 and c[-1] == R.one
        powers = [[R.element(int(i == j)) for i in range(D)] for j in range(D)]
        for degree in range(D, 2*D-1):
            previous = powers[-1]
            value = [R.zero] + previous[:-1]
            value = [R.sub(value[i], R.mul(previous[-1], c[i])) for i in range(D)]
            powers.append(value)
        table = [[powers[i+j][:] for j in range(D)] for i in range(D)]
        return cls(precision, table, powers[0][:], initial_h=initial_h)

    @classmethod
    def unpack(cls, data):
        R = SeriesRing(data["absolute_rho_precision"])
        table = [[[R.element(x) for x in row] for row in plane]
                 for plane in data["multiplication_structure_coefficients"]]
        one = [R.element(x) for x in data["one_coordinates"]]
        basis = [[lp_unpack(x) for x in row] for row in data["basis_in_primitive_Theta_powers"]]
        inverse_basis = [[lp_unpack(x) for x in row] for row in data["primitive_Theta_powers_in_basis"]]
        return cls(R.N, table, one, basis, inverse_basis, data["total_index_length"],
                   data["basis_determinant_unit_mod_prime"], data["initial_Theta_rho_power"])

    def pack(self):
        R = self.R
        return {"rank": D, "prime": P, "absolute_rho_precision": self.N,
            "structure_convention": "table[left][right][output], columns are coordinates",
            "multiplication_structure_coefficients": [[[R.pack(x) for x in row]
                  for row in plane] for plane in self.table],
            "one_coordinates": [R.pack(x) for x in self.one],
            "basis_in_primitive_Theta_powers": [[lp_pack(x) for x in row] for row in self.basis],
            "primitive_Theta_powers_in_basis": [[lp_pack(x) for x in row] for row in self.basis_inverse],
            "total_index_length": self.index_length,
            "basis_determinant_unit_mod_prime": self.determinant_unit,
            "initial_Theta_rho_power": self.initial_h,
            "basis_determinant_rho_order_relative_to_original_U_powers": 28*self.initial_h-self.index_length,
            "all_factors_and_nilpotents_retained": True,
            "expanded_characteristic_zero_order_basis": False}

    def multiply(self, a, b):
        R = self.R
        answer = [R.zero for _ in range(D)]
        for i in range(D):
            if a[i] == R.zero:
                continue
            for j in range(D):
                if b[j] == R.zero:
                    continue
                c = R.mul(a[i], b[j])
                for k in range(D):
                    answer[k] = R.add(answer[k], R.mul(c, self.table[i][j][k]))
        return answer

    def verify_basis_and_unit(self):
        R = self.R
        assert lp_matmul(self.basis, self.basis_inverse) == lp_identity()
        assert lp_matmul(self.basis_inverse, self.basis) == lp_identity()
        for j in range(D):
            ej = [R.element(int(i == j)) for i in range(D)]
            assert self.multiply(self.one, ej) == ej and self.multiply(ej, self.one) == ej
        assert all(self.table[i][j] == self.table[j][i] for i in range(D) for j in range(D))

    def trace_gram(self):
        R = self.R
        traces = [sum_poly(R, (self.table[i][j][j] for j in range(D))) for i in range(D)]
        gram = [[sum_poly(R, (R.mul(self.table[i][j][k], traces[k]) for k in range(D)))
                 for j in range(D)] for i in range(D)]
        assert all(gram[i][j] == gram[j][i] for i in range(D) for j in range(D))
        return traces, gram

    def discriminant(self):
        traces, gram = self.trace_gram()
        disc = self.R.determinant(gram)
        d = self.R.valuation(disc, "the complete rank8 trace discriminant")
        assert d >= 4 and d % 2 == 0
        return {"traces": [self.R.pack(x) for x in traces],
                "trace_gram_matrix": [[self.R.pack(x) for x in row] for row in gram],
                "discriminant_series": self.R.pack(disc), "discriminant_order": d,
                "discriminant_leading_mod_prime": int(disc[d]),
                "division_free_determinant": True, "absolute_rho_precision": self.N}, gram

    def idealizer(self, gram):
        if self.N < 2:
            raise NeedPrecision("The idealizer needs the actual coefficients at orders zero and one",
                                {"absolute_precision": self.N, "required_coefficient_count": 2})
        trace_zero = [[int(x[0]) for x in row] for row in gram]
        radical = kernel(trace_zero)
        r = radical["kernel_dimension"]
        C, Cinv, determinant_C, complement = complete_columns(radical["kernel_basis_mod_prime"])
        transported = []
        for basis_index in range(D):
            data = []
            for order in (0, 1):
                matrix = [[int(self.table[basis_index][j][i][order]) for j in range(D)] for i in range(D)]
                data.append(matmul(matmul(Cinv, matrix), C))
            transported.append(data)
        rows, labels = [], []
        for i in range(D):
            for j in range(D):
                orders = [0] if (i < r and j < r) or (i >= r and j >= r) else [0, 1] if i >= r and j < r else []
                for order in orders:
                    rows.append([transported[v][order][i][j] for v in range(D)])
                    labels.append({"output_row": i, "input_column": j, "rho_order": order})
        answer = kernel(rows)
        Cnew, Cnewinv, detnew, new_complement = complete_columns(answer["kernel_basis_mod_prime"])
        return {"trace_radical": radical, "trace_radical_basis_completion": C,
            "trace_radical_basis_completion_inverse": Cinv,
            "trace_radical_basis_completion_determinant": determinant_C,
            "trace_radical_standard_complement_indices": complement,
            "equation_labels": labels, "idealizer_quotient_kernel": answer,
            "new_basis_constant_matrix": Cnew, "new_basis_constant_inverse": Cnewinv,
            "new_basis_constant_determinant": detnew,
            "new_basis_standard_complement_indices": new_complement,
            "index_length_increment": answer["kernel_dimension"],
            "only_original_current_table_orders_zero_and_one_used": True,
            "all_four_block_idealizer_conditions_included": True}

    def enlarge(self, data):
        k0 = data["index_length_increment"]
        assert 0 < k0 <= D
        if self.N <= 2:
            raise NeedPrecision("A further idealizer enlargement can consume two rho orders",
                                {"absolute_precision": self.N, "required_coefficient_count_at_least": 3})
        C, Cinv = data["new_basis_constant_matrix"], data["new_basis_constant_inverse"]
        e = [int(i < k0) for i in range(D)]
        R = self.R
        first = [[[sum_poly(R, (R.scale(self.table[a][b][c], C[a][i]) for a in range(D)))
                   for c in range(D)] for b in range(D)] for i in range(D)]
        second = [[[sum_poly(R, (R.scale(first[i][b][c], C[b][j]) for b in range(D)))
                    for c in range(D)] for j in range(D)] for i in range(D)]
        constant_table = [[[sum_poly(R, (R.scale(second[i][j][c], Cinv[k][c]) for c in range(D)))
                           for k in range(D)] for j in range(D)] for i in range(D)]
        newR = SeriesRing(self.N - 2)
        negative_checks = []
        table = []
        for i in range(D):
            plane = []
            for j in range(D):
                row = []
                for k in range(D):
                    shift = e[k]-e[i]-e[j]
                    value = constant_table[i][j][k]
                    if shift < 0:
                        for n in range(-shift):
                            assert not int(value[n]), (i,j,k,n)
                        negative_checks.append([i,j,k,-shift])
                    row.append(newR.element([int(value[n-shift]) if n-shift >= 0 else 0
                                             for n in range(newR.N)]))
                plane.append(row)
            table.append(plane)
        one_constant = [sum_poly(R, (R.scale(self.one[j], Cinv[i][j]) for j in range(D))) for i in range(D)]
        one = [newR.element([int(one_constant[i][n-e[i]]) if n >= e[i] else 0
                            for n in range(newR.N)]) for i in range(D)]
        basis = [[lp_scale(lp_sum(lp_scale(self.basis[i][a], C[a][j]) for a in range(D)), 1, -e[j])
                  for j in range(D)] for i in range(D)]
        inverse_basis = [[lp_scale(lp_sum(lp_scale(self.basis_inverse[a][j], Cinv[i][a]) for a in range(D)), 1, e[i])
                          for j in range(D)] for i in range(D)]
        result = Order(newR.N, table, one, basis, inverse_basis,
            self.index_length+k0, self.determinant_unit*data["new_basis_constant_determinant"] % P,
            self.initial_h)
        result.verify_basis_and_unit()
        return result, {"all_possible_negative_structure_coefficients_vanish": True,
            "negative_coefficient_checks": negative_checks,
            "lowest_possible_shift": -2, "old_precision": self.N,
            "new_precision": newR.N, "uniform_precision_loss": 2,
            "both_exact_Laurent_basis_inverse_products_verified": True,
            "all_eight_left_and_right_unit_products_verified": True,
            "complete_512_structure_coefficients_transported": True}

    def primitive_coordinate(self, power):
        assert 0 <= power < D
        answer = []
        for row in self.basis_inverse:
            low, poly = row[power]
            if low < 0:
                assert all(not int(poly[n]) for n in range(min(-low, max(0,poly.degree()+1))))
            answer.append(self.R.element([int(poly[n-low]) if n >= low else 0 for n in range(self.N)]))
        return answer

    def verify_original_monic_relation(self, monic):
        R = self.R
        theta = self.primitive_coordinate(1)
        value = [R.zero for _ in range(D)]
        for c in reversed(monic):
            value = self.multiply(value, theta)
            cc = R.element(c)
            value = [R.add(x, R.mul(cc,u)) for x,u in zip(value,self.one)]
        assert all(x == R.zero for x in value)
        return True

    def special_fibre(self):
        _, gram = self.trace_gram()
        rad = kernel([[int(x[0]) for x in row] for row in gram])
        basis = rad["kernel_basis_mod_prime"]
        assert rad["kernel_dimension"] == 4
        columns = [[basis[i][j] for i in range(D)] for j in range(4)]
        def product(a,b):
            return [sum(a[i]*b[j]*int(self.table[i][j][k][0]) for i in range(D) for j in range(D)) % P
                    for k in range(D)]
        squares = [product(a,b) for a in columns for b in columns]
        square_rank = len(rref(squares,D)[1])
        assert square_rank == 2
        cubes = [product(a,b) for a in columns for b in squares]
        assert all(not x for row in cubes for x in row)
        return {"dimension": D,
            "complete_structure_constants_mod_rho": [[[int(x[0]) for x in row] for row in plane]
                                                     for plane in self.table],
            "one_mod_rho": [int(x[0]) for x in self.one], "trace_radical": rad,
            "radical_square_generating_rows": squares, "radical_square_dimension": square_rank,
            "all_radical_cube_products_zero": True,
            "original_geometric_length_pattern": [1,1,3,3],
            "geometric_pattern_asserted_from_original_modular_source": True,
            "all_factors_and_nilpotents_retained": True,
            "reduced_quotient_substituted_for_full_fibre": False}
