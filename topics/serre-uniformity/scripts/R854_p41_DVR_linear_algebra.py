#!/usr/bin/env python3
"""R854 arithmetic helper: original L_41, residue rank and DVR row saturation.

No arithmetic is executed on import.  All arithmetic entry points enforce the
public repository Actions environment.  Rank/inverse/rref are used ONLY over
the prime 41; composite-modulus matrices are used only for +, -, and products.
The caller owns source identities, atomic stage IO and budget checks.
"""
from __future__ import annotations

import os

P = 41
E = 7
DIM = 14
REPOSITORY = "Rogerhu12/math-research-public"
_AUTHORIZED = False


class NeedPrecision(RuntimeError):
    pass


def authorize():
    global _AUTHORIZED
    if _AUTHORIZED:
        return
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise RuntimeError("New arithmetic is restricted to public GitHub Actions.")
    if os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        raise RuntimeError("Wrong public arithmetic repository.")
    import flint
    if flint.__version__ != "0.9.0":
        raise RuntimeError("The source-bound backend is python-flint 0.9.0.")
    _AUTHORIZED = True


def v41(n):
    authorize()
    n = abs(int(n))
    if not n:
        return None
    result = 0
    while n % P == 0:
        n //= P
        result += 1
    return result


def matrix(nrows, ncols, values, modulus):
    authorize()
    from flint import nmod_mat, fmpz_mod_mat, fmpz_mod_ctx
    values = [int(x) % modulus for x in values]
    assert len(values) == nrows*ncols
    if modulus < 2**63:
        return nmod_mat(nrows, ncols, values, modulus)
    return fmpz_mod_mat(nrows, ncols, values, fmpz_mod_ctx(modulus))


def zeros(nrows, ncols, modulus):
    return matrix(nrows, ncols, [0]*(nrows*ncols), modulus)


def identity(n, modulus=P):
    return matrix(n, n, [int(i == j) for i in range(n) for j in range(n)], modulus)


def change_modulus(a, modulus):
    return matrix(a.nrows(), a.ncols(), a.entries(), modulus)


def select(a, rows, columns=None, modulus=None):
    rows = list(rows)
    columns = list(range(a.ncols())) if columns is None else list(columns)
    modulus = int(a.modulus()) if modulus is None else int(modulus)
    return matrix(len(rows), len(columns),
                  [a[i, j] for i in rows for j in columns], modulus)


def vstack(a, b):
    assert a.ncols() == b.ncols() and a.modulus() == b.modulus()
    return matrix(a.nrows()+b.nrows(), a.ncols(),
                  list(a.entries())+list(b.entries()), int(a.modulus()))


class FqMatrix:
    """A+s B over F_41, s^2=-3.  Components always have modulus exactly 41."""
    def __init__(self, a, b):
        authorize()
        assert a.nrows() == b.nrows() and a.ncols() == b.ncols()
        assert int(a.modulus()) == int(b.modulus()) == P
        self.a, self.b = a, b
        self.nrows, self.ncols = a.nrows(), a.ncols()

    @classmethod
    def zero(cls, nrows, ncols):
        return cls(zeros(nrows, ncols, P), zeros(nrows, ncols, P))

    @classmethod
    def eye(cls, n):
        return cls(identity(n), zeros(n, n, P))

    def __eq__(self, other):
        return isinstance(other, FqMatrix) and self.a == other.a and self.b == other.b

    def __sub__(self, other):
        return FqMatrix(self.a-other.a, self.b-other.b)

    def __mul__(self, other):
        assert self.ncols == other.nrows
        aa, bb = self.a*other.a, self.b*other.b
        cross = (self.a+self.b)*(other.a+other.b)-aa-bb
        return FqMatrix(aa-3*bb, cross)

    def select(self, rows, columns=None):
        return FqMatrix(select(self.a, rows, columns), select(self.b, rows, columns))

    def restriction(self):
        # Interleaved pairs, so a complete original coordinate is never split
        # by a successful rank profile.
        values = []
        for i in range(self.nrows):
            for j in range(self.ncols):
                values.extend((int(self.a[i, j]), -3*int(self.b[i, j])))
            for j in range(self.ncols):
                values.extend((int(self.b[i, j]), int(self.a[i, j])))
        return matrix(2*self.nrows, 2*self.ncols, values, P)

    @classmethod
    def from_restriction(cls, raw):
        assert int(raw.modulus()) == P
        assert raw.nrows() % 2 == raw.ncols() % 2 == 0
        nr, nc = raw.nrows()//2, raw.ncols()//2
        aa, bb = [], []
        for i in range(nr):
            for j in range(nc):
                a, b = int(raw[2*i, 2*j]), int(raw[2*i+1, 2*j])
                assert int(raw[2*i, 2*j+1]) == -3*b % P
                assert int(raw[2*i+1, 2*j+1]) == a
                aa.append(a)
                bb.append(b)
        return cls(matrix(nr, nc, aa, P), matrix(nr, nc, bb, P))

    def inverse(self):
        assert self.nrows == self.ncols
        original = self.restriction()
        raw = original.inv()             # Prime 41, never a composite modulus.
        assert original*raw == identity(2*self.nrows)
        result = FqMatrix.from_restriction(raw)
        assert self*result == FqMatrix.eye(self.nrows)
        return result

    def to_data(self):
        return {"shape": [self.nrows, self.ncols], "prime": P,
                "basis": "1,s; s^2=-3",
                "a": [[int(self.a[i, j]) for j in range(self.ncols)]
                      for i in range(self.nrows)],
                "b": [[int(self.b[i, j]) for j in range(self.ncols)]
                      for i in range(self.nrows)]}

    @classmethod
    def from_data(cls, data):
        assert data["prime"] == P and data["basis"] == "1,s; s^2=-3"
        nr, nc = data["shape"]
        assert len(data["a"]) == len(data["b"]) == nr
        assert all(len(row) == nc for row in data["a"]+data["b"])
        return cls(matrix(nr, nc, [x for row in data["a"] for x in row], P),
                   matrix(nr, nc, [x for row in data["b"] for x in row], P))


def fp_pivots(raw):
    assert int(raw.modulus()) == P
    rr, rank = raw.rref()                 # Prime 41 only.
    pivots, previous = [], -1
    for i in range(rank):
        j = previous+1
        while j < rr.ncols() and not rr[i, j]:
            j += 1
        assert j < rr.ncols() and int(rr[i, j]) == 1
        pivots.append(j)
        previous = j
    return pivots


def unpair(pivots):
    assert len(pivots) % 2 == 0
    result = []
    for k in range(0, len(pivots), 2):
        assert pivots[k] % 2 == 0 and pivots[k+1] == pivots[k]+1
        result.append(pivots[k]//2)
    return result


def residue_profile(a, budget=lambda: None):
    """Produce a full verified row-combination certificate, not just a rank."""
    authorize()
    assert isinstance(a, FqMatrix)
    budget()
    raw = a.restriction()
    independent = unpair(fp_pivots(raw.transpose()))
    rank = len(independent)
    dependent = [i for i in range(a.nrows) if i not in set(independent)]
    del raw
    if not rank:
        assert a == FqMatrix.zero(a.nrows, a.ncols)
        return {"rank": 0, "independent_rows": [], "dependent_rows": dependent,
                "pivot_columns": [], "minor_inverse": FqMatrix.eye(0),
                "combinations": FqMatrix.zero(a.nrows, 0),
                "full_residue_row_identity_verified": True}
    top = a.select(independent)
    budget()
    columns = list(range(a.ncols)) if rank == a.ncols else unpair(fp_pivots(top.restriction()))
    assert len(columns) == rank
    square = top.select(range(rank), columns)
    budget()
    inverse = square.inverse()
    combinations = a.select(dependent, columns)*inverse
    budget()
    assert a.select(dependent) == combinations*top
    return {"rank": rank, "independent_rows": independent,
            "dependent_rows": dependent, "pivot_columns": columns,
            "minor_inverse": inverse, "combinations": combinations,
            "full_residue_row_identity_verified": True}


class DVR:
    def __init__(self, original_integral_B_minimal_polynomial):
        authorize()
        self.f = [int(c) for c in original_integral_B_minimal_polynomial]
        assert len(self.f) == 8 and self.f[7] == 1
        assert v41(self.f[0]) == 1
        assert all(c % P == 0 for c in self.f[:7])

    def exponent(self, precision):
        assert isinstance(precision, int) and precision > 0
        return (precision+6)//7

    def modulus(self, precision):
        return P**self.exponent(precision)

    def cap(self, precision, B_degree):
        return P**max(0, (precision-B_degree+6)//7)

    def matrix(self, coefficients, precision):
        return IntegralMatrix(self, coefficients, precision)

    def zero(self, nrows, ncols, precision):
        q = self.modulus(precision)
        return self.matrix([zeros(nrows, ncols, q) for _ in range(DIM)], precision)

    def from_data(self, data):
        assert data["basis"] == "B^0..B^6,s*B^0..s*B^6; s^2=-3"
        assert data["uniformizer"] == "original B=lambda*b"
        assert data["ramification_index"] == 7 and data["p"] == P
        nr, nc = data["shape"]
        precision = int(data["absolute_B_precision"])
        coeffs = data["coefficients"]
        assert len(coeffs) == DIM
        q = self.modulus(precision)
        result = []
        for k, rows in enumerate(coeffs):
            assert len(rows) == nr and all(len(row) == nc for row in rows)
            cap = self.cap(precision, k % E)
            values = [int(x) for row in rows for x in row]
            assert all(0 <= x < cap for x in values)
            result.append(matrix(nr, nc, values, q))
        return self.matrix(result, precision)


class IntegralMatrix:
    """Matrix modulo B^N.  Coefficients are arbitrary lifts at a common 41^q."""
    def __init__(self, field, coefficients, precision):
        authorize()
        self.field, self.N = field, int(precision)
        self.q = field.modulus(self.N)
        assert len(coefficients) == DIM
        self.coeff = tuple(coefficients)
        self.nrows, self.ncols = self.coeff[0].nrows(), self.coeff[0].ncols()
        assert all(c.nrows() == self.nrows and c.ncols() == self.ncols and
                   int(c.modulus()) == self.q for c in self.coeff)

    def truncate(self, precision):
        assert 0 < precision <= self.N
        q = self.field.modulus(precision)
        coeff = self.coeff if q == self.q else [change_modulus(c, q) for c in self.coeff]
        return IntegralMatrix(self.field, coeff, precision)

    def select(self, rows, columns=None):
        return IntegralMatrix(self.field,
            [select(c, rows, columns) for c in self.coeff], self.N)

    def __sub__(self, other):
        assert self.field.f == other.field.f
        precision = min(self.N, other.N)
        a, b = self.truncate(precision), other.truncate(precision)
        return IntegralMatrix(self.field, [x-y for x, y in zip(a.coeff, b.coeff)], precision)

    def __add__(self, other):
        assert self.field.f == other.field.f
        precision = min(self.N, other.N)
        a, b = self.truncate(precision), other.truncate(precision)
        return IntegralMatrix(self.field, [x+y for x, y in zip(a.coeff, b.coeff)], precision)

    def scale_integer(self, scalar):
        return IntegralMatrix(self.field,
            [c*(int(scalar) % self.q) for c in self.coeff], self.N)

    def canonical_equal(self, other):
        if self.field.f != other.field.f or (self.nrows, self.ncols) != (other.nrows, other.ncols):
            return False
        N = min(self.N, other.N)
        for k, (a, b) in enumerate(zip(self.coeff, other.coeff)):
            cap = self.field.cap(N, k % E)
            if any((int(x)-int(y)) % cap for x, y in zip(a.entries(), b.entries())):
                return False
        return True

    def is_zero(self):
        for k, a in enumerate(self.coeff):
            cap = self.field.cap(self.N, k % E)
            if any(int(x) % cap for x in a.entries()):
                return False
        return True

    def valuation_lower_bound(self):
        answer = self.N
        for k, a in enumerate(self.coeff):
            i = k % E
            cap = self.field.cap(self.N, i)
            for x in a.entries():
                value = int(x) % cap
                if value:
                    answer = min(answer, 7*v41(value)+i)
        return answer

    def residue(self):
        return FqMatrix(change_modulus(self.coeff[0], P), change_modulus(self.coeff[7], P))

    def multiply_pi(self, precision=None):
        N = self.N+1 if precision is None else int(precision)
        assert 0 < N <= self.N+1
        q = self.field.modulus(N)
        old = [change_modulus(c, q) for c in self.coeff]
        result = []
        for off in (0, E):
            top = old[off+6]
            result.append(top*(-self.field.f[0] % q))
            for i in range(1, E):
                result.append(old[off+i-1]-top*(self.field.f[i] % q))
        return IntegralMatrix(self.field, result, N)

    def divide_pi(self, verify=True):
        if self.N <= 1:
            raise NeedPrecision("Division by B requires another known uniformizer digit.")
        assert self.residue() == FqMatrix.zero(self.nrows, self.ncols)
        N = self.N-1
        q = self.field.modulus(N)
        inv_unit = pow(self.field.f[0]//P, -1, q)
        result = []
        for off in (0, E):
            constants = [int(x) for x in self.coeff[off].entries()]
            assert all(x % P == 0 for x in constants)
            last = matrix(self.nrows, self.ncols,
                          [-(x//P)*inv_unit for x in constants], q)
            for i in range(E-1):
                result.append(change_modulus(self.coeff[off+i+1], q)
                              +last*(self.field.f[i+1] % q))
            result.append(last)
        answer = IntegralMatrix(self.field, result, N)
        if verify:
            assert answer.multiply_pi(self.N).canonical_equal(self)
        return answer

    def divide_pi_power(self, power, budget=lambda: None):
        result = self
        for _ in range(int(power)):
            budget()
            result = result.divide_pi()
        return result

    def unramified_left(self, left, budget=lambda: None):
        """Lift Fq coefficients to 0..40 + s(0..40), then multiply exactly."""
        assert left.ncols == self.nrows
        aa, bb = change_modulus(left.a, self.q), change_modulus(left.b, self.q)
        result_a, result_b = [], []
        for i in range(E):
            budget()
            x, y = self.coeff[i], self.coeff[i+E]
            ax, by = aa*x, bb*y
            result_a.append(ax-3*by)
            result_b.append((aa+bb)*(x+y)-ax-by)
        return IntegralMatrix(self.field, result_a+result_b, self.N)

    def unramified_right(self, right, budget=lambda: None):
        assert self.ncols == right.nrows
        aa, bb = change_modulus(right.a, self.q), change_modulus(right.b, self.q)
        result_a, result_b = [], []
        for i in range(E):
            budget()
            x, y = self.coeff[i], self.coeff[i+E]
            ax, by = x*aa, y*bb
            result_a.append(ax-3*by)
            result_b.append((x+y)*(aa+bb)-ax-by)
        return IntegralMatrix(self.field, result_a+result_b, self.N)

    @staticmethod
    def concatenate(top, bottom):
        assert top.field.f == bottom.field.f and top.ncols == bottom.ncols
        N = min(top.N, bottom.N)
        top, bottom = top.truncate(N), bottom.truncate(N)
        return IntegralMatrix(top.field,
            [vstack(a, b) for a, b in zip(top.coeff, bottom.coeff)], N)

    def to_data(self):
        rows = []
        for k, a in enumerate(self.coeff):
            cap = self.field.cap(self.N, k % E)
            rows.append([[str(int(a[i, j]) % cap) for j in range(self.ncols)]
                         for i in range(self.nrows)])
        return {"shape": [self.nrows, self.ncols], "p": P,
                "basis": "B^0..B^6,s*B^0..s*B^6; s^2=-3",
                "uniformizer": "original B=lambda*b", "ramification_index": E,
                "absolute_B_precision": self.N,
                "absolute_p41_precision_rational": [self.N, E],
                "coefficients": rows}


def saturation_step(a, right_numerator, bounds, profile, budget=lambda: None):
    """One exact row operation and B-division; rhs represents B^-h numerator.

    The returned rhs represents B^-(h+1) times the returned numerator.  Rank
    profiles and input matrices must be complete source-bound stages owned by
    the caller.  No unknown or zero-precision row is silently divided.
    """
    authorize()
    assert profile["full_residue_row_identity_verified"] is True
    I, J = profile["independent_rows"], profile["dependent_rows"]
    assert len(bounds) == a.nrows == right_numerator.nrows
    assert sorted(I+J) == list(range(a.nrows))
    assert len(I) == profile["rank"] < a.ncols
    combinations = profile["combinations"]
    top, bottom = a.select(I), a.select(J)
    difference = bottom-top.unramified_left(combinations, budget)
    assert difference.residue() == FqMatrix.zero(len(J), a.ncols)
    budget()
    new_bottom = difference.divide_pi()
    new_a = IntegralMatrix.concatenate(top.truncate(new_bottom.N), new_bottom)
    bv_top, bv_bottom = right_numerator.select(I), right_numerator.select(J)
    rhs_bottom = bv_bottom-bv_top.unramified_left(combinations, budget)
    rhs_top = bv_top.multiply_pi(right_numerator.N)
    new_rhs = IntegralMatrix.concatenate(rhs_top, rhs_bottom)
    new_bounds = [int(bounds[i]) for i in I]
    for j, old_row in enumerate(J):
        used = [bounds[old_row]]
        for k, source_row in enumerate(I):
            if combinations.a[j, k] or combinations.b[j, k]:
                used.append(bounds[source_row])
        new_bounds.append(int(min(used))-1)
    assert len(new_bounds) == new_a.nrows
    return new_a, new_rhs, new_bounds, {
        "row_order": I+J, "unchanged_row_count": len(I),
        "divided_row_count": len(J), "division_uniformizer": "original B",
        "matrix_input_absolute_B_precision": a.N,
        "matrix_output_absolute_B_precision": new_a.N,
        "right_numerator_absolute_B_precision": new_rhs.N,
        "right_common_B_exponent_change": -1,
        "row_transform_lower_bounds": new_bounds,
        "full_residue_row_identity_verified": True,
        "division_multiplied_back_at_all_known_digits": True,
    }


def dixon_digit(unit_matrix, inverse_residue, residual, budget=lambda: None):
    """Return exactly the next digit and next integral residual."""
    authorize()
    assert unit_matrix.nrows == unit_matrix.ncols == residual.nrows
    assert inverse_residue.nrows == inverse_residue.ncols == unit_matrix.nrows
    assert residual.N <= unit_matrix.N
    budget()
    digit = inverse_residue*residual.residue()
    difference = residual-unit_matrix.truncate(residual.N).unramified_right(digit, budget)
    assert difference.residue() == FqMatrix.zero(residual.nrows, residual.ncols)
    if difference.N <= 1:
        return digit, None
    return digit, difference.divide_pi()


def digits_to_integral(field, digits, precision, budget=lambda: None):
    """Finite Horner sum of already completed uniformizer digits, not a lift."""
    assert digits
    nrows, ncols = digits[0].nrows, digits[0].ncols
    assert len(digits) >= precision > 0
    answer = field.zero(nrows, ncols, precision)
    q = field.modulus(precision)
    for digit in reversed(digits[:precision]):
        budget()
        assert digit.nrows == nrows and digit.ncols == ncols
        answer = answer.multiply_pi(precision)
        coeff = list(answer.coeff)
        coeff[0] = coeff[0]+change_modulus(digit.a, q)
        coeff[7] = coeff[7]+change_modulus(digit.b, q)
        answer = IntegralMatrix(field, coeff, precision)
    return answer


def polynomial_matrix_product(left, right, budget=lambda: None):
    """General integral product with 13 ordinary evaluations, no ring inverse.

    Polynomial degrees in B are <=6.  Interpolation denominators are 1..12,
    all units at 41.  The output product in B has degree <=12 before reduction.
    Matrix multiplication may be noncommutative; the scalar evaluation and
    interpolation argument still applies.  The right side is usually a vector.
    """
    authorize()
    assert left.field.f == right.field.f and left.ncols == right.nrows
    N = min(left.N, right.N)
    left, right = left.truncate(N), right.truncate(N)
    q = left.q

    def evaluate(coeff, off, point):
        out = coeff[off+6]
        for i in range(5, -1, -1):
            out = out*point+coeff[off+i]
        return out

    values_a, values_b = [], []
    for point in range(13):
        budget()
        la, lb = evaluate(left.coeff, 0, point), evaluate(left.coeff, 7, point)
        ra, rb = evaluate(right.coeff, 0, point), evaluate(right.coeff, 7, point)
        aa, bb = la*ra, lb*rb
        values_a.append(aa-3*bb)
        values_b.append((la+lb)*(ra+rb)-aa-bb)

    def interpolate(values):
        divided = list(values)
        for order in range(1, 13):
            inverse = pow(order, -1, q)
            for j in range(12, order-1, -1):
                divided[j] = (divided[j]-divided[j-1])*inverse
        coeff = [divided[12]]
        for k in range(11, -1, -1):
            next_coeff = [coeff[0]*(-k % q)]
            for j in range(1, len(coeff)):
                next_coeff.append(coeff[j-1]-coeff[j]*k)
            next_coeff.append(coeff[-1])
            next_coeff[0] = next_coeff[0]+divided[k]
            coeff = next_coeff
        assert len(coeff) == 13
        # All original interpolation nodes, with exact modular matrix equality.
        for point, expected in enumerate(values):
            value = coeff[-1]
            for c in reversed(coeff[:-1]):
                value = value*point+c
            assert value == expected
        for degree in range(12, 6, -1):
            leading = coeff[degree]
            for j in range(7):
                coeff[degree-7+j] = coeff[degree-7+j]-leading*(left.field.f[j] % q)
        return coeff[:7]

    return IntegralMatrix(left.field, interpolate(values_a)+interpolate(values_b), N)


def certified_left_inverse_bound(row_bounds, selected_rows):
    authorize()
    assert selected_rows and all(0 <= i < len(row_bounds) for i in selected_rows)
    bound = min(int(row_bounds[i]) for i in selected_rows)
    return {"minimum_left_inverse_entry_valuation_lower_bound": bound,
            "conservative_B_precision_loss": max(0, -bound),
            "bound_uses_selected_unit_rows_only": True,
            "characteristic_zero_inverse_materialized": False}

