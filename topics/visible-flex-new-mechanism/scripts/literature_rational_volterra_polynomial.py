#!/usr/bin/env python3
"""Exact reduction modulo a prime of rational, right-anchored polynomials.

The variable t runs from 0 to 1 and xi=left+(right-left)*t.  Coefficients
are pairs in F_p[i], retaining real and imaginary parts separately.  This is
an exact reduction of Q(i) straight-line arithmetic, not a floating-point
quadrature or a probabilistic zero test.  A nonzero determinant modulo p
certifies that the corresponding rational determinant is nonzero.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
import resource
import time


class PolynomialBudgetExceeded(RuntimeError):
    pass


def is_prime(number):
    """Deterministic trial division; intended for the declared 31-bit prime."""
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor*divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


class PolynomialContext:
    def __init__(self, prime=2147483647, left=2, right=3, *, seconds=240,
                 max_degree=256, memory_mib=1024, max_operations=20000000):
        if not is_prime(prime) or prime == 2:
            raise ValueError("an explicitly checked odd prime is required")
        self.prime = prime
        self.left, self.right = F(left), F(right)
        self.width = self.right-self.left
        if self.width <= 0:
            raise ValueError("left must be smaller than right")
        self.started, self.seconds = time.monotonic(), seconds
        self.max_degree, self.memory_mib = max_degree, memory_mib
        self.max_operations, self.operations = max_operations, 0
        self.denominators = set()
        self.max_degree_seen = 0
        self.raw_atoms_evaluated = 0
        self.raw_monomials_evaluated = 0
        self.colors = {}
        self.inverse_width = self.scalar(1/self.width)
        self.width_mod = self.scalar(self.width)

    def check(self, increment=1):
        self.operations += increment
        if self.operations > self.max_operations:
            raise PolynomialBudgetExceeded("declared polynomial-operation budget")
        if self.operations % 128 == 0 or increment == 0:
            if time.monotonic()-self.started > self.seconds:
                raise PolynomialBudgetExceeded("declared polynomial elapsed-time budget")
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > self.memory_mib*1024:
                raise PolynomialBudgetExceeded("declared resident-memory polling threshold")

    def inverse(self, denominator):
        denominator = int(denominator)
        residue = denominator % self.prime
        if not residue:
            raise ZeroDivisionError("rational denominator is zero modulo the chosen prime")
        self.denominators.add(denominator)
        return pow(residue, self.prime-2, self.prime)

    def scalar(self, value):
        value = F(value)
        return value.numerator % self.prime*self.inverse(value.denominator) % self.prime

    def number(self, value):
        if isinstance(value, Polynomial):
            if value.context is not self:
                raise ValueError("polynomials must share the same prime and right anchor")
            return value
        if isinstance(value, tuple) and len(value) == 2:
            return Polynomial(self, [(self.scalar(value[0]), self.scalar(value[1]))])
        return Polynomial(self, [(self.scalar(value), 0)])

    coerce = number

    def variable(self):
        return Polynomial(self, [(0, 0), (1, 0)])

    def x(self):
        return self.number(self.left)+self.width*self.variable()

    def color(self, name):
        if name not in self.colors:
            raise ValueError("no fixed polynomial supplied for color "+name)
        return self.colors[name]

    def coefficient_report(self):
        values = sorted(self.denominators)
        serialized = json.dumps(values, separators=(",", ":")).encode()
        return {"prime": self.prime, "prime_checked_by_trial_division": True,
                "all_encountered_rational_denominators_invertible": True,
                "encountered_denominator_count": len(values),
                "encountered_denominators_sha256": hashlib.sha256(serialized).hexdigest(),
                "encountered_denominators": values,
                "max_polynomial_degree": self.max_degree_seen,
                "operation_check_calls": self.operations,
                "raw_atoms_evaluated": self.raw_atoms_evaluated,
                "raw_monomials_evaluated": self.raw_monomials_evaluated}


class Polynomial:
    """A polynomial in t with exact modular Gaussian-rational coefficients."""
    def __init__(self, context, coefficients=()):
        self.context = context
        prime = context.prime
        values = [(int(a) % prime, int(b) % prime) for a, b in coefficients]
        while values and values[-1] == (0, 0):
            values.pop()
        if len(values)-1 > context.max_degree:
            raise PolynomialBudgetExceeded("declared polynomial-degree budget")
        self.coefficients = tuple(values)
        context.max_degree_seen = max(context.max_degree_seen, len(values)-1)
        self._derivative = self._integral = None

    def key(self):
        return self.coefficients

    def __bool__(self):
        return bool(self.coefficients)

    def __add__(self, other):
        other = self.context.coerce(other)
        prime = self.context.prime
        result = list(self.coefficients)
        result.extend([(0, 0)]*(len(other.coefficients)-len(result)))
        for i, (a, b) in enumerate(other.coefficients):
            c, d = result[i]
            result[i] = ((a+c) % prime, (b+d) % prime)
        self.context.check()
        return Polynomial(self.context, result)

    __radd__ = __add__

    def __neg__(self):
        return Polynomial(self.context, [(-a, -b) for a, b in self.coefficients])

    def __sub__(self, other):
        return self+(-self.context.coerce(other))

    def __rsub__(self, other):
        return self.context.coerce(other)-self

    def __mul__(self, other):
        other = self.context.coerce(other)
        if not self or not other:
            return Polynomial(self.context)
        degree = len(self.coefficients)+len(other.coefficients)-2
        if degree > self.context.max_degree:
            raise PolynomialBudgetExceeded("declared polynomial product-degree budget")
        prime = self.context.prime
        real, imaginary = [0]*(degree+1), [0]*(degree+1)
        for i, (a, b) in enumerate(self.coefficients):
            if not (a or b):
                continue
            for j, (c, d) in enumerate(other.coefficients):
                real[i+j] += a*c-b*d
                imaginary[i+j] += a*d+b*c
            # Keep intermediate integer sizes bounded without any rounding.
            for j in range(len(other.coefficients)):
                real[i+j] %= prime
                imaginary[i+j] %= prime
        self.context.check()
        return Polynomial(self.context, zip(real, imaginary))

    __rmul__ = __mul__

    def __truediv__(self, other):
        value = F(other)
        if not value:
            raise ZeroDivisionError("scalar polynomial division")
        return self*(1/value)

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("only nonnegative polynomial powers are supported")
        result, base = self.context.number(1), self
        while exponent:
            if exponent & 1:
                result = result*base
            exponent >>= 1
            if exponent:
                base = base*base
        return result

    def D(self):
        if self._derivative is None:
            factor = self.context.inverse_width
            self._derivative = Polynomial(self.context,
                [(i*a*factor, i*b*factor) for i, (a, b) in enumerate(self.coefficients) if i])
            self.context.check()
        return self._derivative

    def I(self):
        """I_r^xi F, with the actual right endpoint r and I(r)=0."""
        if self._integral is None:
            prime, width = self.context.prime, self.context.width_mod
            coefficients = [(0, 0)]
            for i, (a, b) in enumerate(self.coefficients):
                inverse = self.context.inverse(i+1)
                coefficients.append((a*width*inverse % prime, b*width*inverse % prime))
            coefficients[0] = (-sum(a for a, _ in coefficients) % prime,
                               -sum(b for _, b in coefficients) % prime)
            self._integral = Polynomial(self.context, coefficients)
            self.context.check()
        return self._integral

    def J(self):
        return -self.I()

    def conjugate(self):
        return Polynomial(self.context, [(a, -b) for a, b in self.coefficients])

    def value(self, t):
        point = self.context.scalar(t)
        real = imaginary = 0
        for a, b in reversed(self.coefficients):
            real = (real*point+a) % self.context.prime
            imaginary = (imaginary*point+b) % self.context.prime
        self.context.check()
        return real, imaginary

    def digest(self):
        return hashlib.sha256(json.dumps(self.coefficients, separators=(",", ":")).encode()).hexdigest()


class RawExpressionEvaluator:
    """Evaluate the original Expr/primitive DAG, with no word rewriting."""
    def __init__(self, profile_algebra, context, replacements):
        self.profile_algebra = profile_algebra
        self.context, self.replacements = context, replacements
        self.atoms, self.monomials, self.jets = {}, {}, {}
        self.x = context.x()
        self.powers = {0: context.number(1), 1: self.x}

    def atom(self, identifier):
        if identifier not in self.atoms:
            node = self.profile_algebra.atoms[identifier]
            if node[0] == "jet":
                name, order = node[1], node[2]
                if name not in self.replacements:
                    raise ValueError("unbound actual color "+name)
                if name not in self.jets:
                    self.jets[name] = [self.replacements[name]]
                while len(self.jets[name]) <= order:
                    self.jets[name].append(self.jets[name][-1].D())
                value = self.jets[name][order]
            elif node[0] == "int_right":
                value = self.monomial(node[1]).I()
            else:
                raise ValueError("unsupported original profile atom: "+str(node[0]))
            self.atoms[identifier] = value
            self.context.raw_atoms_evaluated += 1
        return self.atoms[identifier]

    def monomial(self, monomial):
        if monomial not in self.monomials:
            power, atoms = monomial
            if power < 0:
                raise ValueError("this exact polynomial evaluator does not integrate rational functions")
            if power not in self.powers:
                self.powers[power] = self.x**power
            value = self.powers[power]
            for atom in atoms:
                value = value*self.atom(atom)
            self.monomials[monomial] = value
            self.context.raw_monomials_evaluated += 1
        return self.monomials[monomial]

    def expression(self, expression):
        answer = self.context.number(0)
        for monomial, coefficient in expression.terms.items():
            answer += coefficient*self.monomial(monomial)
        return answer


class EvaluatedThirdOperator:
    def __init__(self, profile_algebra, context, template):
        self.profile_algebra, self.context, self.template = profile_algebra, context, template
        self.cache = {}

    def __call__(self, exterior, first, second):
        pair = (first, second) if first.key() <= second.key() else (second, first)
        key = (exterior.key(), pair[0].key(), pair[1].key())
        if key not in self.cache:
            evaluator = RawExpressionEvaluator(self.profile_algebra, self.context,
                                               {"a": exterior, "b": pair[0], "c": pair[1]})
            self.cache[key] = evaluator.expression(self.template)
        return self.cache[key]


def determinant(matrix, prime):
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("square matrix required")
    value, rows = 1, [[x % prime for x in row] for row in matrix]
    for column in range(len(rows)):
        pivot = next((i for i in range(column, len(rows)) if rows[i][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            value = -value
        leading = rows[column][column]
        value = value*leading % prime
        inverse = pow(leading, prime-2, prime)
        for i in range(column+1, len(rows)):
            factor = rows[i][column]*inverse % prime
            if factor:
                for j in range(column, len(rows)):
                    rows[i][j] = (rows[i][j]-factor*rows[column][j]) % prime
    return value % prime


def solve(matrix, target, prime):
    size = len(matrix)
    if len(target) != size or any(len(row) != size for row in matrix):
        raise ValueError("nonsingular square solve required")
    rows = [[v % prime for v in row]+[value % prime] for row, value in zip(matrix, target)]
    for column in range(size):
        pivot = next((i for i in range(column, size) if rows[i][column]), None)
        if pivot is None:
            raise ValueError("singular modular square system")
        rows[column], rows[pivot] = rows[pivot], rows[column]
        inverse = pow(rows[column][column], prime-2, prime)
        rows[column] = [v*inverse % prime for v in rows[column]]
        for i in range(size):
            if i != column and rows[i][column]:
                factor = rows[i][column]
                rows[i] = [(v-factor*w) % prime for v, w in zip(rows[i], rows[column])]
    return [row[-1] for row in rows]


def full_column_dual(rows, target, prime):
    """Only a full-column-rank augmented minor is a negative certificate.

    The certificate's *rational* functional is
    evaluation_last - evaluation_last(A) * A_pivot^{-1} * evaluations_pivot.
    Its reduction below is computed for verification.  We never promote a
    deficient modular rank to a characteristic-zero rank upper bound.
    """
    if len(rows) != len(target) or not rows:
        raise ValueError("nonempty equally indexed matrix and target required")
    columns = len(rows[0])
    if any(len(row) != columns for row in rows):
        raise ValueError("rectangular matrix required")
    basis, selected = {}, []
    for index, row in enumerate(rows):
        value = [v % prime for v in row]
        for pivot in sorted(basis):
            factor = value[pivot]
            if factor:
                value = [(v-factor*w) % prime for v, w in zip(value, basis[pivot])]
        pivot = next((j for j, value_j in enumerate(value) if value_j), None)
        if pivot is not None:
            inverse = pow(value[pivot], prime-2, prime)
            basis[pivot] = [v*inverse % prime for v in value]
            selected.append(index)
        if len(selected) == columns:
            break
    report = {"control_columns": columns, "modular_control_rank": len(selected),
              "selected_control_rows": selected, "rational_nonmembership_certified": False}
    if len(selected) != columns:
        report["reason"] = "deficient modular rank is not a rational-rank upper bound"
        return report
    pivot_matrix = [rows[i] for i in selected]
    pivot_target = [target[i] for i in selected]
    candidate = solve(pivot_matrix, pivot_target, prime)
    last = next((i for i, (row, value) in enumerate(zip(rows, target))
                 if (value-sum(a*b for a, b in zip(row, candidate))) % prime), None)
    if last is None:
        report["reason"] = "finite evaluations modulo this prime produced no separating minor"
        report["modular_solution_is_not_a_positive_identity"] = True
        return report
    selected_all = selected+[last]
    augmented = [[*rows[i], target[i]] for i in selected_all]
    pivot_det, augmented_det = determinant(pivot_matrix, prime), determinant(augmented, prime)
    transpose = [[pivot_matrix[i][j] for i in range(columns)] for j in range(columns)]
    coefficients = solve(transpose, [-v for v in rows[last]], prime)+[1]
    annihilated = [sum(coefficients[i]*rows[row][j] for i, row in enumerate(selected_all)) % prime
                  for j in range(columns)]
    separated = sum(coefficients[i]*target[row] for i, row in enumerate(selected_all)) % prime
    if not pivot_det or not augmented_det or any(annihilated) or not separated:
        raise AssertionError("original modular separating-functional verification failed")
    if augmented_det != pivot_det*separated % prime:
        raise AssertionError("Schur complement determinant identity")
    report.update({"rational_nonmembership_certified": True,
        "selected_augmented_rows": selected_all,
        "modular_pivot_determinant": pivot_det,
        "modular_augmented_determinant": augmented_det,
        "modular_augmented_matrix": augmented,
        "modular_functional_coefficients": coefficients,
        "modular_functional_all_control_values": annihilated,
        "modular_functional_target_value": separated,
        "functional_over_Q": "ev_last - row_last(A) * inverse(A_pivot) * ev_pivot",
        "rational_functional_identity": "Lambda(A_j)=0 exactly for all original retained control columns",
        "nonzero_reason": "det(Augmented) has defined nonzero reduction modulo the checked prime"})
    return report


def small_toys():
    """Artificial algebra only: no research profile/geometry/compiler."""
    context = PolynomialContext(101, 2, 5, seconds=30, max_degree=24)
    t, x = context.variable(), context.x()
    checks = {}

    def equal(a, b, name):
        if a.key() != b.key():
            raise AssertionError(name)
        checks[name] = True

    equal(x.D(), context.number(1), "xi_derivative_has_true_interval_scale")
    equal((x*x+2*x+3).I().D(), x*x+2*x+3, "signed_right_primitive_derivative")
    if (x*x+2*x+3).I().value(1) != (0, 0):
        raise AssertionError("actual common right anchor")
    checks["right_endpoint_zero"] = True
    equal((t*(1-t)).D().I(), t*(1-t), "right_boundary_term_paid")
    equal((x+context.number((0, 1)))**2,
          x*x+context.number((0, 2))*x-1, "ordinary_complex_square_not_norm_square")
    equal((x* x.I()).I()+(x* x.I()).I(), x.I()*x.I(), "signed_right_shuffle")
    columns = [[1, 0], [0, 1], [1, 1]]
    dual = full_column_dual(columns, [2, 3, 7], 101)
    if not dual["rational_nonmembership_certified"] or dual["modular_functional_target_value"] != 2:
        raise AssertionError("artificial separating rational determinant")
    checks["full_rank_nonzero_augmented_minor"] = True
    low = full_column_dual([[1, 0], [2, 0]], [0, 1], 101)
    if low["rational_nonmembership_certified"]:
        raise AssertionError("deficient modular rank must remain undecided")
    checks["deficient_rank_not_promoted"] = True
    positive = full_column_dual(columns, [2, 3, 5], 101)
    if positive["rational_nonmembership_certified"]:
        raise AssertionError("a modular solution is not a negative certificate")
    checks["modular_fit_not_positive_function_identity"] = True
    return {"scope": "small artificial polynomial/linear-algebra toys only",
            "checks": checks, "all_passed": all(checks.values()),
            "research_compiler_called": False,
            "research_profile_or_geometry_evaluated": False,
            "artificial_dual": dual, "coefficient_arithmetic": context.coefficient_report()}
