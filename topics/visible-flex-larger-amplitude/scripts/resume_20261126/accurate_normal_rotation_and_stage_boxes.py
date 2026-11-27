#!/usr/bin/env python3
"""Accurate rotation jets and complete normal-stage interval algebra.

This is a mathematical kernel for a separately source-bound actual-field
producer. It does not accept reported working residuals as accurate bounds.
It issues no stand-alone same-field or continuous-cover certificate. The
caller must supply complete accurate reference/current-core/radial integrals,
the whole angular cell, the actual point and all original normal stages.

All arithmetic evaluation is restricted to the public repository Actions.
Only stdlib source parsing/compilation is intended outside Actions.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json
import math
import os
from pathlib import Path

SCHEMA = "accurate-complete-normal-rotation-and-stage-interval-algebra-v1"
VECTOR_JET_KEYS = ("value", "phi", "phiphi")
EXACT_CONTROL_DIMENSION = 6
EXACT_INCREMENT_DIMENSION = 3


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Accurate field evaluation requires the actual public Actions")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (F, int, str)):
        raise TypeError("Use explicit rational input, never an implicit decimal float")
    return F(value)


def binary_word(value):
    if not isinstance(value, str):
        raise TypeError("An actual binary64 value must retain its canonical hex word")
    parsed = float.fromhex(value)
    if not math.isfinite(parsed) or parsed.hex() != value:
        raise ValueError("The supplied actual word is not finite canonical binary64")
    return F.from_float(parsed)


def down(q, bits):
    q = rational(q)
    scale = 1 << bits
    return F(q.numerator*scale//q.denominator, scale)


def up(q, bits):
    q = rational(q)
    scale = 1 << bits
    return F(-((-q.numerator*scale)//q.denominator), scale)


def sqrt_bounds(q, bits):
    q = rational(q)
    if q < 0:
        raise ValueError("Square root requires a nonnegative rational")
    scale = 1 << bits
    n = math.isqrt(q.numerator*scale*scale//q.denominator)
    lower = F(n, scale)
    return lower, lower if lower*lower == q else F(n+1, scale)


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F
    bits: int = 160

    def __post_init__(self):
        lo, hi = rational(self.lo), rational(self.hi)
        if lo > hi:
            raise ValueError("Reversed complete interval")
        if type(self.bits) is not int or not 64 <= self.bits <= 1024:
            raise ValueError("Retain one declared 64..1024 bit outward precision")
        object.__setattr__(self, "lo", down(lo, self.bits))
        object.__setattr__(self, "hi", up(hi, self.bits))

    def other(self, value):
        if isinstance(value, Interval):
            if value.bits != self.bits:
                raise ValueError("Mixed outward precision")
            return value
        q = rational(value)
        return Interval(q, q, self.bits)

    def __add__(self, other):
        other = self.other(other)
        return Interval(self.lo+other.lo, self.hi+other.hi, self.bits)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo, self.bits)

    def __sub__(self, other):
        return self+-self.other(other)

    def __rsub__(self, other):
        return self.other(other)+-self

    def __mul__(self, other):
        other = self.other(other)
        candidates = (self.lo*other.lo, self.lo*other.hi,
                      self.hi*other.lo, self.hi*other.hi)
        return Interval(min(candidates), max(candidates), self.bits)

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ValueError("An interval denominator includes zero")
        return Interval(1/self.hi, 1/self.lo, self.bits)

    def __truediv__(self, other):
        return self*self.other(other).reciprocal()

    def __rtruediv__(self, other):
        return self.other(other)*self.reciprocal()

    def __pow__(self, n):
        if type(n) is not int or n < 0:
            raise TypeError("Only nonnegative integer interval powers are supported")
        if n == 0:
            return self.other(1)
        if n % 2:
            return Interval(self.lo**n, self.hi**n, self.bits)
        upper = max(abs(self.lo), abs(self.hi))**n
        lower = 0 if self.lo <= 0 <= self.hi else min(abs(self.lo), abs(self.hi))**n
        return Interval(lower, upper, self.bits)

    def abs_upper(self):
        return max(abs(self.lo), abs(self.hi))

    def sqrt(self):
        if self.lo < 0:
            raise ValueError("The whole interval is not nonnegative")
        return Interval(sqrt_bounds(self.lo, self.bits)[0],
                        sqrt_bounds(self.hi, self.bits)[1], self.bits)

    def intersect(self, other):
        other = self.other(other)
        lo, hi = max(self.lo, other.lo), min(self.hi, other.hi)
        if lo > hi:
            raise ValueError("Independent accurate intervals are inconsistent")
        return Interval(lo, hi, self.bits)

    def json(self):
        return [str(self.lo), str(self.hi)]


def encoded(value):
    if isinstance(value, Interval):
        return value.json()
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(k): encoded(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encoded(v) for v in value]
    if value is None or type(value) in (bool, int, str):
        return value
    raise TypeError("Do not silently serialize a scientific float or unknown array")


def point(q, bits):
    q = rational(q)
    return Interval(q, q, bits)


def zero(bits):
    return point(0, bits)


def box(value, bits):
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ValueError("Supply both accurate interval endpoints")
    return Interval(rational(value[0]), rational(value[1]), bits)


def hull(values):
    values = list(values)
    if not values or any(v.bits != values[0].bits for v in values):
        raise ValueError("A nonempty interval list with one precision is required")
    return Interval(min(v.lo for v in values), max(v.hi for v in values), values[0].bits)


def shape(value):
    if isinstance(value, Interval):
        return ()
    if not isinstance(value, (list, tuple)) or not value:
        raise ValueError("Only complete nonempty interval tensors are accepted")
    child = shape(value[0])
    if any(shape(v) != child for v in value):
        raise ValueError("Ragged interval tensor")
    return (len(value),)+child


def require_shape(value, expected, bits):
    if shape(value) != tuple(expected):
        raise ValueError("The complete interval tensor shape differs")
    def visit(v):
        if isinstance(v, Interval):
            if v.bits != bits:
                raise ValueError("A tensor uses another outward precision")
        else:
            for child in v:
                visit(child)
    visit(value)
    return value


def isum(values, bits):
    result = zero(bits)
    for value in values:
        result = result+value
    return result


def dot(a, b):
    if len(a) != len(b) or not a:
        raise ValueError("Dot product needs complete equal dimensions")
    return isum((x*y for x, y in zip(a, b)), a[0].bits)


def cross(a, b):
    if len(a) != 3 or len(b) != 3:
        raise ValueError("World cross product requires three components")
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]


def vadd(a, b):
    if len(a) != len(b):
        raise ValueError("Vector dimensions differ")
    return [x+y for x, y in zip(a, b)]


def vscale(a, s):
    return [s*x for x in a]


def norm_upper(a):
    if not a:
        raise ValueError("Empty vector norm")
    q = sum((v.abs_upper()**2 for v in a), F(0))
    return sqrt_bounds(q, a[0].bits)[1]


def inf_upper(a):
    if not a:
        raise ValueError("Empty vector infinity norm")
    return max(v.abs_upper() for v in a)


def jadd(a, b):
    if len(a) != 3 or len(b) != 3:
        raise ValueError("Keep all value/first/second angular jets")
    return [a[k]+b[k] for k in range(3)]


def jmul(a, b):
    return [a[0]*b[0],
            a[1]*b[0]+a[0]*b[1],
            a[2]*b[0]+2*a[1]*b[1]+a[0]*b[2]]


def jcross(a, b):
    return [cross(a[0], b[0]),
            vadd(cross(a[1], b[0]), cross(a[0], b[1])),
            vadd(vadd(cross(a[2], b[0]), vscale(cross(a[1], b[1]), 2)),
                 cross(a[0], b[2]))]


def jvadd(a, b):
    return [vadd(a[k], b[k]) for k in range(3)]


def jsvmul(a, b):
    return [vscale(b[0], a[0]),
            vadd(vscale(b[0], a[1]), vscale(b[1], a[0])),
            vadd(vadd(vscale(b[0], a[2]), vscale(b[1], 2*a[1])),
                 vscale(b[2], a[0]))]


def jdot(a, b):
    return [dot(a[0], b[0]),
            dot(a[1], b[0])+dot(a[0], b[1]),
            dot(a[2], b[0])+2*dot(a[1], b[1])+dot(a[0], b[2])]


def matrix_product(a, b):
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("Complete matrix dimensions differ")
    bits = a[0][0].bits
    return [[isum((a[i][k]*b[k][j] for k in range(len(b))), bits)
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    if not a or any(len(row) != len(a[0]) for row in a):
        raise ValueError("A complete nonempty matrix is required")
    return [list(column) for column in zip(*a)]


def matrix_vector(a, v):
    return [dot(row, v) for row in a]


def exact_inverse(matrix):
    """Exact inverse of supplied rational proposal words; never of true J."""
    require_actions()
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("The proposal is the whole three by three matrix")
    a = [[rational(v) for v in row]+[F(int(i == j)) for j in range(3)]
         for i, row in enumerate(matrix)]
    for column in range(3):
        pivot = next((i for i in range(column, 3) if a[i][column]), None)
        if pivot is None:
            raise ArithmeticError("The actual proposal words are exactly singular")
        a[column], a[pivot] = a[pivot], a[column]
        scale = a[column][column]
        a[column] = [v/scale for v in a[column]]
        for i in range(3):
            if i != column:
                scale = a[i][column]
                a[i] = [v-scale*w for v, w in zip(a[i], a[column])]
    return [row[3:] for row in a]


class ExactRotationJets:
    """Complete accurate Exp(w cross) action and all six control columns."""

    def __init__(self, *, bits=160, first_degree=24, maximum_degree=128,
                 tail_goal=None):
        require_actions()
        if type(bits) is not int or not 64 <= bits <= 1024:
            raise ValueError("Declare the complete outward precision")
        if (type(first_degree) is not int or type(maximum_degree) is not int
                or not 3 <= first_degree <= maximum_degree <= 1024):
            raise ValueError("Keep a finite explicit complete-series budget")
        self.bits = bits
        self.first_degree = first_degree
        self.maximum_degree = maximum_degree
        self.tail_goal = rational(tail_goal) if tail_goal is not None else F(1, 1 << (bits//2))
        if self.tail_goal <= 0:
            raise ValueError("A strictly positive accurate-series tail goal is required")
        self.counts = dict(coefficient_enclosures=0, rotation_actions=0,
            complete_six_control_columns=0, radial_actions=0)
        self.maximum_degree_used = 0
        self.maximum_series_tail = F(0)

    def _tail(self, bound, degree, derivative, offset):
        n = degree+1
        falling = math.factorial(n)//math.factorial(n-derivative)
        first = F(falling, math.factorial(2*n+offset))*bound**(n-derivative)
        # The successive absolute-term ratio decreases for all n >= degree+1.
        ratio = F(n+1, n+1-derivative)*bound/F((2*n+offset+1)*(2*n+offset+2))
        if ratio >= 1:
            return None
        return first/(1-ratio)

    def coefficient_derivatives(self, q):
        require_actions()
        if not isinstance(q, Interval) or q.bits != self.bits or q.lo < 0:
            raise ValueError("Use the actual nonnegative squared-rotation-norm interval")
        chosen = None
        for degree in range(self.first_degree, self.maximum_degree+1):
            tails = [[self._tail(q.hi, degree, j, offset) for j in range(4)]
                     for offset in (1, 2)]
            if all(t is not None and t <= self.tail_goal for row in tails for t in row):
                chosen = degree, tails
                break
        if chosen is None:
            raise ArithmeticError("The complete accurate coefficient tail budget is insufficient")
        degree, tails = chosen
        result = []
        for offset, fees in zip((1, 2), tails):
            derivatives = []
            for j in range(4):
                value = zero(self.bits)
                for n in reversed(range(j, degree+1)):
                    falling = math.factorial(n)//math.factorial(n-j)
                    coefficient = F((-1)**n*falling, math.factorial(2*n+offset))
                    value = value*q+coefficient
                derivatives.append(value+Interval(-fees[j], fees[j], self.bits))
            result.append(derivatives)
        self.counts["coefficient_enclosures"] += 1
        self.maximum_degree_used = max(self.maximum_degree_used, degree)
        self.maximum_series_tail = max(self.maximum_series_tail, *(t for row in tails for t in row))
        return result[0], result[1]

    @staticmethod
    def _compose(derivatives, q):
        return [derivatives[0], derivatives[1]*q[1],
                derivatives[2]*(q[1]**2)+derivatives[1]*q[2]]

    @staticmethod
    def _variation(derivatives, q, dq):
        return [derivatives[1]*dq[0],
                derivatives[2]*dq[0]*q[1]+derivatives[1]*dq[1],
                derivatives[3]*dq[0]*(q[1]**2)
                +2*derivatives[2]*q[1]*dq[1]
                +derivatives[2]*dq[0]*q[2]+derivatives[1]*dq[2]]

    def action(self, w, vector, *, directions=None, ws=None, vector_s=None):
        """World jets; directions[l] are e,e_phi,e_phiphi for local U0[l]."""
        require_actions()
        require_shape(w, (3, 3), self.bits)
        require_shape(vector, (3, 3), self.bits)
        if directions is not None:
            require_shape(directions, (6, 3, 3), self.bits)
        if (ws is None) != (vector_s is None):
            raise ValueError("Radial rotation and reference derivatives are both required")
        if ws is not None:
            require_shape(ws, (3,), self.bits)
            require_shape(vector_s, (3,), self.bits)
        # Squared components, rather than interval x*x, retain nonnegativity.
        q = jdot(w, w)
        q[0] = isum((item**2 for item in w[0]), self.bits)
        a, b = self.coefficient_derivatives(q[0])
        aj, bj = self._compose(a, q), self._compose(b, q)
        c = jcross(w, vector)
        d = jcross(w, c)
        value = jvadd(jvadd(vector, jsvmul(aj, c)), jsvmul(bj, d))
        columns = None
        if directions is not None:
            columns = []
            for direction in directions:
                dq = [2*v for v in jdot(w, direction)]
                dc = jcross(direction, vector)
                dd = jvadd(jcross(direction, c), jcross(w, dc))
                da, db = self._variation(a, q, dq), self._variation(b, q, dq)
                variation = jvadd(jvadd(jsvmul(da, c), jsvmul(aj, dc)),
                                  jvadd(jsvmul(db, d), jsvmul(bj, dd)))
                columns.append(variation)
            self.counts["complete_six_control_columns"] += 6
        radial = None
        if ws is not None:
            qs = 2*dot(w[0], ws)
            cs = vadd(cross(ws, vector[0]), cross(w[0], vector_s))
            ds = vadd(cross(ws, c[0]), cross(w[0], cs))
            radial = vadd(vadd(vector_s, vscale(c[0], a[1]*qs)),
                vadd(vscale(cs, a[0]), vadd(vscale(d[0], b[1]*qs), vscale(ds, b[0]))))
            self.counts["radial_actions"] += 1
        self.counts["rotation_actions"] += 1
        return dict(jets=value, control_columns=columns, radial=radial)

    def corrected(self, seed, seed_s, omega, omega_s, W, Ws, controls, *,
                  complete_control_frame=True, radial=True):
        """Exp(Wu) Exp(omega) T_seed with every angular and s chain retained."""
        require_actions()
        require_shape(seed, (3, 3), self.bits)
        require_shape(seed_s, (3,), self.bits)
        require_shape(omega, (3, 3), self.bits)
        require_shape(omega_s, (3,), self.bits)
        require_shape(W, (3, 3, 6), self.bits)
        require_shape(Ws, (3, 6), self.bits)
        require_shape(controls, (3, 6), self.bits)
        inner = self.action(omega, seed, ws=omega_s if radial else None,
                            vector_s=seed_s if radial else None)
        w = [[isum((math.comb(j, k)*W[j-k][component][l]*controls[k][l]
                    for k in range(j+1) for l in range(6)), self.bits)
              for component in range(3)] for j in range(3)]
        directions = [[[W[j][component][l] for component in range(3)]
                       for j in range(3)] for l in range(6)]
        ws = [dot(row, controls[0]) for row in Ws]
        outer = self.action(w, inner["jets"],
            directions=directions if complete_control_frame else None,
            ws=ws if radial else None,
            vector_s=inner["radial"] if radial else None)
        frame = None
        if complete_control_frame:
            frame = [[[outer["control_columns"][l][j][component] for l in range(6)]
                      for component in range(3)] for j in range(3)]
        return dict(T=outer["jets"][0], Tphi=outer["jets"][1],
            Tphiphi=outer["jets"][2], Ts=outer["radial"],
            complete_control_frame=frame)

    def metadata(self):
        return encoded(dict(schema=SCHEMA, source_sha256=sha(__file__),
            precision_bits=self.bits, first_degree=self.first_degree,
            maximum_degree=self.maximum_degree, tail_goal=self.tail_goal,
            actual_counts=self.counts, maximum_degree_used=self.maximum_degree_used,
            maximum_series_tail=self.maximum_series_tail,
            accurate_entire_Rodrigues_coefficients=True,
            complete_coefficient_derivative_orders=[0, 1, 2, 3],
            actual_independent_working_Horner_coefficients_substituted=False,
            working_AD_or_working_matrix_word_equality_claimed=False,
            source_bound_reference_or_cover_verified_here=False))


def control_update(previous, frame, eta, bits):
    require_shape(previous, (3, 6), bits)
    require_shape(frame, (3, 3, 6), bits)
    require_shape(eta, (3, 3), bits)
    return [[previous[j][l]+isum(
        (math.comb(j, k)*frame[j-k][a][l]*eta[k][a]
         for k in range(j+1) for a in range(3)), bits)
        for l in range(6)] for j in range(3)]


def preconditioned_matrix_box(Y, J, bits):
    require_shape(Y, (3, 3), bits)
    require_shape(J, (3, 3), bits)
    YJ = matrix_product(Y, J)
    defect = [[point(int(i == j), bits)-YJ[i][j] for j in range(3)] for i in range(3)]
    q = max(sum((value.abs_upper() for value in row), F(0)) for row in defect)
    return defect, q


def difference_from_words(enclosure, actual):
    if shape(enclosure) != shape(actual):
        raise ValueError("Comparison shape differs")
    if isinstance(enclosure, Interval):
        return max(abs(enclosure.lo-actual.hi), abs(enclosure.hi-actual.lo))
    return [difference_from_words(a, b) for a, b in zip(enclosure, actual)]


def stage_root_box(oracle, *, previous, actual_frame, actual_eta,
                   actual_controls, actual_J3, tau, radius, control_radius, bits):
    """Complete R707 step, with oracle-generated accurate closure/frame boxes.

    Oracle.evaluate(controls) must return exact outward closure_jets (3,3)
    and complete_control_frame (3,3,6), both divided by the same true S.
    Oracle.zero_closure_jets is the separately enclosed true f(x,phi,0).
    Oracle owns the whole angular/radial domain and every upstream source.
    This kernel deliberately makes no claim that those external obligations
    were validated. Its intended actual producer performs that validation.
    """
    require_actions()
    tau, radius, control_radius = rational(tau), rational(radius), rational(control_radius)
    if not 0 < tau <= 1 or radius <= 0 or control_radius <= 0:
        raise ValueError("Retain the exact stage node and positive declared domains")
    for value, expected in ((previous, (3, 6)), (actual_frame, (3, 3, 6)),
            (actual_eta, (3, 3)), (actual_controls, (3, 6)), (actual_J3, (3, 3))):
        require_shape(value, expected, bits)
    zero_closure = require_shape(oracle.zero_closure_jets, (3, 3), bits)
    if any(v.lo != v.hi for row in actual_J3 for v in row):
        raise ValueError("The preconditioner proposal must be actual point words")
    if any(v.lo != v.hi for row in actual_eta for v in row):
        raise ValueError("Working comparison eta retains its exact input words")
    # Exact rational inversion of the actual J3 word matrix is a proposal Y.
    inverse = exact_inverse([[v.lo for v in row] for row in actual_J3])
    Y = [[point(v, bits) for v in row] for row in inverse]
    previous_eval = oracle.evaluate(previous)
    B = require_shape(previous_eval["complete_control_frame"], (3, 3, 6), bits)
    point_eta = [[point(v.lo, bits) for v in row] for row in actual_eta]
    point_eta[1] = [zero(bits) for _ in range(3)]
    point_eta[2] = [zero(bits) for _ in range(3)]
    centre_controls = control_update(previous, B, point_eta, bits)
    centre = oracle.evaluate(centre_controls)
    centre_residual = [centre["closure_jets"][0][a]-(1-tau)*zero_closure[0][a]
                       for a in range(3)]
    eta_domain = [[Interval(v.lo-radius, v.lo+radius, bits) for v in actual_eta[0]],
                  [zero(bits) for _ in range(3)], [zero(bits) for _ in range(3)]]
    domain_controls = control_update(previous, B, eta_domain, bits)
    control_norm = norm_upper(domain_controls[0])
    if control_norm >= control_radius:
        return encoded(dict(passed=False, reason="complete true control domain not strictly inside declared radius",
            tau=tau, radius=radius, actual_control_radius=control_radius,
            true_control_norm_upper=control_norm, oracle_binding_verified_here=False))
    domain = oracle.evaluate(domain_controls)
    current_A = require_shape(domain["complete_control_frame"], (3, 3, 6), bits)[0]
    J = matrix_product(current_A, transpose(B[0]))
    defect, q = preconditioned_matrix_box(Y, J, bits)
    z = inf_upper(matrix_vector(Y, centre_residual))
    margin = (1-q)*radius-z
    if q >= 1 or margin <= 0:
        return encoded(dict(passed=False, reason="complete accurate contraction inequalities not established",
            tau=tau, radius=radius, q=q, preconditioned_centre_residual_upper=z,
            strict_invariance_margin=margin, true_control_norm_upper=control_norm,
            oracle_binding_verified_here=False))
    eta0_error = z/(1-q)
    eta = [[Interval(v.lo-eta0_error, v.lo+eta0_error, bits) for v in actual_eta[0]],
           [point(v.lo, bits) for v in actual_eta[1]],
           [zero(bits) for _ in range(3)]]
    first = oracle.evaluate(control_update(previous, B, eta, bits))
    R1 = [first["closure_jets"][1][a]-(1-tau)*zero_closure[1][a] for a in range(3)]
    eta1_error = inf_upper(matrix_vector(Y, R1))/(1-q)
    eta[1] = [Interval(v.lo-eta1_error, v.lo+eta1_error, bits) for v in actual_eta[1]]
    eta[2] = [point(v.lo, bits) for v in actual_eta[2]]
    second = oracle.evaluate(control_update(previous, B, eta, bits))
    R2 = [second["closure_jets"][2][a]-(1-tau)*zero_closure[2][a] for a in range(3)]
    eta2_error = inf_upper(matrix_vector(Y, R2))/(1-q)
    eta[2] = [Interval(v.lo-eta2_error, v.lo+eta2_error, bits) for v in actual_eta[2]]
    controls = control_update(previous, B, eta, bits)
    result = dict(passed=True, tau=tau, contraction_radius=radius,
        q=q, preconditioned_centre_residual_upper=z, strict_invariance_margin=margin,
        true_control_norm_upper=control_norm, control_radius=control_radius,
        coordinate_norm="component infinity norm; Euclidean control radius enclosed separately",
        actual_J3_words_are_only_preconditioner_proposal=True,
        Y=Y, Y_exact_rational=inverse,
        accurate_cross_Jacobian=J, preconditioned_Jacobian_defect=defect,
        accurate_frame=B, frame_component_errors=difference_from_words(B, actual_frame),
        eta_jets=eta, eta_jet_infinity_errors=[eta0_error, eta1_error, eta2_error],
        controls=controls, control_component_errors=difference_from_words(controls, actual_controls),
        first_angular_residual=R1, second_angular_residual=R2,
        all_upstream_control_and_frame_angular_jets_propagated=True,
        original_comparison_arithmetic_not_assumed_exact=True,
        root_local_uniqueness_only=True, whole_declared_control_ball_uniqueness_claimed=False,
        adjacent_cell_or_periodic_or_reflected_branch_identity_verified_here=False,
        oracle_binding_verified_here=False, external_parameter_J_Jtranspose_fees_paid=False)
    return result


def physical_sixjet_boxes(*, core, cap, total_integral, partial_integral,
                          meridian, h, hp, hpp, rho0, bits):
    """The complete physical R715 lift, before any endpoint defect is discarded.

    h is the same exact 1-S5(s/S) convention as the actual complete source.
    All three true defects are retained. Their vanishing may be established
    only by a separate complete accurate final-root/reference-closure proof.
    """
    require_actions()
    for value in (core, cap, total_integral, partial_integral):
        require_shape(value, (3, 3), bits)
    for name in ("T", "Tphi", "Tphiphi", "Ts"):
        require_shape(meridian[name], (3,), bits)
    for value in (h, hp, hpp, rho0):
        if not isinstance(value, Interval) or value.bits != bits:
            raise ValueError("Use complete accurate scalar lift/chart intervals")
    defects = [[core[j][a]-cap[j][a]+total_integral[j][a] for a in range(3)]
               for j in range(3)]
    integral_fields = [[(1-h)*cap[j][a]+h*core[j][a]+partial_integral[j][a]
                        -(1-h)*total_integral[j][a] for a in range(3)]
                       for j in range(3)]
    return dict(F=integral_fields[0],
        Fs=vadd(meridian["T"], vscale(defects[0], hp)),
        Fphi=integral_fields[1],
        Fss=vadd(meridian["Ts"], vscale(defects[0], hpp)),
        Fsphi=vadd(meridian["Tphi"], vscale(defects[1], hp)),
        Fphiphi=integral_fields[2], rho0=rho0,
        all_three_raw_accurate_closure_defects=defects,
        raw_lift_or_reference_error_dropped=False,
        original_working_sixjet_words_supplied=False)
