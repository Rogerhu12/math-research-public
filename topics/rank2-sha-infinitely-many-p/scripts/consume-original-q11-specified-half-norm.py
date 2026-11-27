#!/usr/bin/env python3
"""Separate the two actual three-torsion intersections inside the paid q11 Norm.

Only the already published q11 lift, original point and complete Norm divisor
are read.  The new calculation uses full local Fitting lengths, including the
double Norm zero, and then returns the specified half class on the original EL.
"""
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path
import sys
import time

if os.environ.get("GITHUB_ACTIONS") != "true" or \
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise SystemExit("Mathematical execution requires the named public GitHub Actions repository.")

HELPER_SHA = "812fd5e5a8899e2b47095c2eee50e22ba5b7063397121a0e44ec8801d1fe3b43"
helper_path = Path(__file__).with_name("lift-original-q11-section-to-two-cover.py")
if hashlib.sha256(helper_path.read_bytes()).hexdigest() != HELPER_SHA:
    raise SystemExit("The exact paid receipt helper has changed.")
spec = importlib.util.spec_from_file_location("paid_q11_reader", helper_path)
paid = importlib.util.module_from_spec(spec)
spec.loader.exec_module(paid)

from flint import fq_default_poly, fq_default_poly_ctx

NORM_BINDING = {
    "run": 45980566265,
    "job": 140443090086,
    "source": "4b315bb783233d98ce623d99fa3dffdca9228683",
    "request_id": "2026-11-27-1015-original-q11-prym-norm-divisors",
    "script": "topics/rank2-sha-infinitely-many-p/scripts/consume-original-q11-prym-norm-divisors.py",
    "script_sha256": "732332d88af3b58952a998c34c46728c9771838a58640264644cade0176622ea",
    "stdout_sha256": "2b0cb545e42234c5958484b4af29108d8562689891f40eb00321be9e798aa742",
    "stdout_bytes": 4516,
}
NORM_DATA_SHA = "1a45359417b39f1425fac1f3f3d93ad80877de7c04cc4c1fd35ab557e807ee13"
LIFT_COORDINATES_SHA = "3afbc5db78bf933d28788ea282eeae2d19211a8184e3670dedd2eccbf1765a68"

PCTX = fq_default_poly_ctx(11, 2)
GF = PCTX.base_field()
delta = GF(8).sqrt()
if delta*delta != GF(8) or delta**11 != -delta:
    raise ArithmeticError("The coefficient root is not the original inert delta.")
ZERO, ONE = PCTX.zero(), PCTX.one()


def fp(value):
    return value if isinstance(value, fq_default_poly) else PCTX([GF(value)])


def coefficients(value):
    return list(value)


def monic(value):
    return value if value.is_zero() else value * value[value.degree()].inverse()


def exact(a, b):
    q, r = divmod(a, b)
    if not r.is_zero():
        raise ArithmeticError("A required polynomial quotient is not exact.")
    return q


def encode_constant(value):
    """Return the canonical two coefficients in 1,delta, regardless of FLINT's basis."""
    d = [int(c) % 11 for c in delta.to_list()]
    v = [int(c) % 11 for c in GF(value).to_list()]
    d += [0]*(2-len(d))
    v += [0]*(2-len(v))
    if d[1] == 0:
        raise ArithmeticError("Delta was in the prime field.")
    b = v[1] * pow(d[1], 9, 11) % 11
    return [(v[0]-b*d[0]) % 11, b]


def encode_poly(value):
    return [encode_constant(c) for c in value]


class Rat:
    __slots__ = ("n", "d")

    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, Rat):
            if denominator != 1:
                raise TypeError("Nested rational denominator.")
            self.n, self.d = numerator.n, numerator.d
            return
        n, d = fp(numerator), fp(denominator)
        if d.is_zero():
            raise ZeroDivisionError("Zero rational denominator.")
        if n.is_zero():
            self.n, self.d = ZERO, ONE
            return
        common = n.gcd(d)
        n, d = exact(n, common), exact(d, common)
        scale = d[d.degree()].inverse()
        self.n, self.d = n*scale, d*scale

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Rat) else Rat(value)

    def __add__(self, other):
        try:
            other = Rat.coerce(other)
        except (TypeError, ValueError):
            return NotImplemented
        return Rat(self.n*other.d+other.n*self.d, self.d*other.d)

    __radd__ = __add__

    def __neg__(self):
        return Rat(-self.n, self.d)

    def __sub__(self, other):
        return self+(-Rat.coerce(other))

    def __rsub__(self, other):
        return Rat.coerce(other)+(-self)

    def __mul__(self, other):
        try:
            other = Rat.coerce(other)
        except (TypeError, ValueError):
            return NotImplemented
        return Rat(self.n*other.n, self.d*other.d)

    __rmul__ = __mul__

    def inverse(self):
        if self.is_zero():
            raise ZeroDivisionError("Zero rational inverse.")
        return Rat(self.d, self.n)

    def __truediv__(self, other):
        try:
            other = Rat.coerce(other)
        except (TypeError, ValueError):
            return NotImplemented
        return self*other.inverse()

    def __rtruediv__(self, other):
        return Rat.coerce(other)*self.inverse()

    def __pow__(self, exponent):
        return Rat(self.n**exponent, self.d**exponent) if exponent >= 0 else self.inverse()**(-exponent)

    def __eq__(self, other):
        try:
            other = Rat.coerce(other)
        except (TypeError, ValueError):
            return False
        return self.n == other.n and self.d == other.d

    def is_zero(self):
        return self.n.is_zero()


def quadratic_field(Base, discriminant):
    class Quad:
        __slots__ = ("a", "b")

        def __init__(self, a=0, b=0):
            if isinstance(a, Quad):
                if b != 0:
                    raise TypeError("Nested quadratic coefficient.")
                self.a, self.b = a.a, a.b
            else:
                self.a, self.b = Base.coerce(a), Base.coerce(b)

        @staticmethod
        def coerce(value):
            return value if isinstance(value, Quad) else Quad(value)

        def __add__(self, other):
            try:
                other = Quad.coerce(other)
            except (TypeError, ValueError):
                return NotImplemented
            return Quad(self.a+other.a, self.b+other.b)

        __radd__ = __add__

        def __neg__(self):
            return Quad(-self.a, -self.b)

        def __sub__(self, other):
            return self+(-Quad.coerce(other))

        def __rsub__(self, other):
            return Quad.coerce(other)+(-self)

        def __mul__(self, other):
            try:
                other = Quad.coerce(other)
            except (TypeError, ValueError):
                return NotImplemented
            return Quad(self.a*other.a+discriminant*self.b*other.b,
                        self.a*other.b+self.b*other.a)

        __rmul__ = __mul__

        def norm(self):
            return self.a**2-discriminant*self.b**2

        def inverse(self):
            nn = self.norm()
            if nn.is_zero():
                raise ZeroDivisionError("Zero quadratic inverse.")
            return Quad(self.a/nn, -self.b/nn)

        def __truediv__(self, other):
            try:
                other = Quad.coerce(other)
            except (TypeError, ValueError):
                return NotImplemented
            return self*other.inverse()

        def __rtruediv__(self, other):
            return Quad.coerce(other)*self.inverse()

        def __pow__(self, exponent):
            if exponent < 0:
                return self.inverse()**(-exponent)
            result, power = Quad(1), self
            while exponent:
                if exponent & 1:
                    result = result*power
                power = power*power
                exponent >>= 1
            return result

        def __eq__(self, other):
            try:
                other = Quad.coerce(other)
            except (TypeError, ValueError):
                return False
            return self.a == other.a and self.b == other.b

        def is_zero(self):
            return self.a.is_zero() and self.b.is_zero()

    return Quad


def pvalue(coeffs, at):
    answer = at*0
    for c in reversed(coeffs):
        answer = answer*at+int(c)
    return answer


def eval_encoded_rat(data, at):
    return pvalue(data["numerator"], at)/pvalue(data["denominator"], at)


def common_numerator(value):
    den = exact(value.a.d*value.b.d, value.a.d.gcd(value.b.d))
    aa = value.a.n*exact(den, value.a.d)
    bb = value.b.n*exact(den, value.b.d)
    return aa, bb, den


def polynomial_order(value, h, limit=None):
    if value.is_zero():
        return limit if limit is not None else 10**9
    order = 0
    while limit is None or order < limit:
        quotient, remainder = divmod(value, h)
        if not remainder.is_zero():
            break
        value, order = quotient, order+1
    return order


def lifted_root(h, root, P, precision):
    current, root = 1, root % h
    while current < precision:
        target = min(2*current, precision)
        modulus = h**target
        root = (root+(P-root*root)*(2*root).inverse_mod(modulus)) % modulus
        current = target
    return root


def local_order(numerator, h, root, P, bound):
    aa, bb, den = numerator
    den_order = polynomial_order(den, h)
    precision = bound+den_order+1
    modulus = h**precision
    yy = lifted_root(h, root, P, precision)
    val = (aa+bb*yy) % modulus
    num_order = polynomial_order(val, h, precision)
    return min(bound, num_order-den_order)


def maximal_minors(F, L, g):
    columns = ((F.a, F.b), (g*F.b, F.a),
               (L.a, L.b), (g*L.b, L.a))
    return [common_numerator(columns[i][0]*columns[j][1]-columns[j][0]*columns[i][1])
            for i, j in itertools.combinations(range(4), 2)]


def xgcd(a, b):
    r0, r1, s0, s1, t0, t1 = a, b, ONE, ZERO, ZERO, ONE
    while not r1.is_zero():
        quotient, remainder = divmod(r0, r1)
        r0, r1 = r1, remainder
        s0, s1 = s1, s0-quotient*s1
        t0, t1 = t1, t0-quotient*t1
    if r0.is_zero():
        return ZERO, ZERO, ZERO
    scale = r0[r0.degree()].inverse()
    return r0*scale, s0*scale, t0*scale


def reduced_pair(u, v, P):
    u = monic(u)
    if u.is_zero() or not ((v*v-P) % u).is_zero():
        raise ArithmeticError("The selected divisor pair is not on the exact twist.")
    v %= u
    while u.degree() > 1:
        u = monic(exact(P-v*v, u))
        if u.is_one():
            return ONE, ZERO
        v = (-v) % u
    return u, v


def add_pairs(pair1, pair2, P):
    u1, v1 = pair1
    u2, v2 = pair2
    d1, e1, e2 = xgcd(u1, u2)
    d, c1, c2 = xgcd(d1, v1+v2)
    u = exact(u1*u2, d*d)
    if u.is_one():
        return ONE, ZERO
    numerator = c1*e1*u1*v2+c1*e2*u2*v1+c2*(v1*v2+P)
    v = exact(numerator, d) % u
    return reduced_pair(u, v, P)


def multiplied_pair(pair, n, P):
    result = (ONE, ZERO)
    while n:
        if n & 1:
            result = add_pairs(result, pair, P)
        pair = add_pairs(pair, pair, P)
        n >>= 1
    return result


def point_from_pair(pair):
    u, v = pair
    return None if u.is_one() else (-u[0], v[0] if not v.is_zero() else GF(0))


def encode_point(point):
    return {"point": "O"} if point is None else {
        "point": "affine", "x": encode_constant(point[0]), "y": encode_constant(point[1])}


def el_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 == -y2:
        return None
    slope = (3*x1*x1-12)/(2*y1) if P == Q else (y2-y1)/(x2-x1)
    xx = slope*slope-x1-x2
    return xx, slope*(x1-xx)-y1


def el_times(P, n):
    result = None
    while n:
        if n & 1:
            result = el_add(result, P)
        P = el_add(P, P)
        n >>= 1
    return result


def main():
    started = time.monotonic()
    norm_record = paid.read_paid_result(NORM_BINDING)
    norm_data = norm_record["data"]
    norm_bytes = json.dumps(norm_data, sort_keys=True, separators=(",", ":")).encode()
    if norm_record.get("status") != "EXACT_ORIGINAL_Q11_PRYM_NORM_DIVISORS" or \
            norm_record.get("data_sha256") != NORM_DATA_SHA or \
            hashlib.sha256(norm_bytes).hexdigest() != NORM_DATA_SHA:
        raise paid.ReceiptReadError("The paid full Norm divisor is not the pinned one.")
    lift = paid.read_paid_result(norm_record["input_receipt"])
    coordinates = lift["coordinates"]
    encoded_coordinates = json.dumps(coordinates, sort_keys=True, separators=(",", ":")).encode()
    if lift.get("coordinates_sha256") != LIFT_COORDINATES_SHA or \
            hashlib.sha256(encoded_coordinates).hexdigest() != LIFT_COORDINATES_SHA:
        raise paid.ReceiptReadError("The paid oriented R coordinates differ.")
    original = paid.read_paid_result(lift["input_receipt"])
    if original.get("normalized_solution_count") != 1 or len(original.get("representatives", [])) != 1:
        raise paid.ReceiptReadError("The original unique section is missing.")
    point = original["representatives"][0]
    os.environ.pop("RANK2_ACTIONS_READ_TOKEN", None)

    T = Rat(PCTX.gen())
    P = PCTX([-540, -108, 0, 1])
    ELT = quadratic_field(Rat, Rat(P))
    zz = ELT(5*(T+12)/(T+3))
    Z = ELT(0, 9*25/(T+3)**2)
    K = zz**3-4
    X = -3*zz/K
    g = zz**2+5*zz+25
    Cover = quadratic_field(ELT, g)
    ss = Cover(0, 1)
    w = ss*(Z/ELT(delta))
    Y = (w*(zz**3+2)/K**2-1)/2
    X_cov = Cover(X)
    z_cov = Cover(zz)
    root = coordinates["R_hyperelliptic_model"]
    R = eval_encoded_rat(root["coefficient_1"], z_cov) + \
        w*eval_encoded_rat(root["coefficient_quadratic_generator"], z_cov)
    u = (1-w/K)/6
    F = ss*R/(z_cov-2*X_cov)+u*Cover(delta)
    W_num = sum((pvalue(co, Y)*X_cov**i
                 for i, co in enumerate(point["W_numerator_basis_1_X_X2"])), Cover(0))
    W = W_num/pvalue(point["W_denominator"], Y)
    t = -Y/27
    selector_plus = W*Cover(delta)-t
    selector_minus = W*Cover(delta)+t
    paid_N = norm_data["N_Q_on_exact_minus3_twist"]
    N = ELT(eval_encoded_rat(paid_N["coefficient_1"], T),
            eval_encoded_rat(paid_N["coefficient_quadratic_generator"], T))
    if F.norm() != N:
        raise ArithmeticError("The original r-Norm and the paid exact twist function disagree.")

    plus_minors = maximal_minors(F, selector_plus, g)
    minus_minors = maximal_minors(F, selector_minus, g)
    places = []
    for row in norm_data["N_Q_divisor"]["rows"]:
        if row["multiplicity"] <= 0:
            continue
        if row["kind"] == "infinity":
            raise ArithmeticError("The pinned Norm has an unhandled zero at infinity.")
        h0 = PCTX(row["polynomial"])
        _, factors = h0.factor()
        for h, exponent in factors:
            if int(exponent) != 1:
                raise ArithmeticError("The paid irreducible base factor became inseparable.")
            if row["kind"] == "entire_unramified_inverse_image":
                if h.degree() != 1:
                    raise ArithmeticError("The pinned uniform positive inverse image is not linear.")
                xvalue = -h[0]/h[1]
                yvalue = P(xvalue).sqrt()
                roots = (PCTX([yvalue]), PCTX([-yvalue]))
            else:
                roots = (PCTX(row["y_mod_polynomial"]) % h,)
            for root_value in roots:
                places.append((monic(h), root_value, row["multiplicity"]))
    places.sort(key=lambda item: (
        tuple(tuple(c) for c in encode_poly(item[0])),
        tuple(tuple(c) for c in encode_poly(item[1]))))

    plus_sum, minus_sum = (ONE, ZERO), (ONE, ZERO)
    plus_degree = minus_degree = total_degree = 0
    divided_rows = []
    for h, root_value, multiplicity in places:
        if not (2*root_value).gcd(h).is_one():
            raise ArithmeticError("A paid zero needs a ramified x-parameter.")
        if local_order(common_numerator(g), h, root_value, P, 1) != 0:
            raise ArithmeticError("The paid zero is not in the integral étale r-chart.")
        mplus = min(local_order(item, h, root_value, P, multiplicity) for item in plus_minors)
        mminus = min(local_order(item, h, root_value, P, multiplicity) for item in minus_minors)
        if mplus < 0 or mminus < 0 or mplus+mminus != multiplicity:
            raise ArithmeticError("The full local Fitting lengths do not partition the original zero.")
        div_pair = reduced_pair(h, root_value, P)
        plus_sum = add_pairs(plus_sum, multiplied_pair(div_pair, mplus, P), P)
        minus_sum = add_pairs(minus_sum, multiplied_pair(div_pair, mminus, P), P)
        plus_degree += h.degree()*mplus
        minus_degree += h.degree()*mminus
        total_degree += h.degree()*multiplicity
        divided_rows.append({
            "polynomial": encode_poly(h), "Y_T_mod_polynomial": encode_poly(root_value),
            "degree": h.degree(), "full_multiplicity": multiplicity,
            "Q_equals_P3_length": mplus, "Q_equals_minusP3_length": mminus,
        })
    if (plus_degree, minus_degree, total_degree) != (12, 12, 24):
        raise ArithmeticError("The specified two three-torsion intersections do not have degree 12 each.")
    if not add_pairs(plus_sum, minus_sum, P)[0].is_one():
        raise ArithmeticError("The two complete half Norm divisors do not add to the paid zero class.")

    plus_twist, minus_twist = point_from_pair(plus_sum), point_from_pair(minus_sum)

    def untwist(point_value):
        return None if point_value is None else (-point_value[0]/3, point_value[1]*delta/9)

    A_Q = untwist(plus_twist)
    minus_Q = untwist(minus_twist)
    if A_Q is not None:
        xx, yy = A_Q
        if yy*yy != xx**3-12*xx+20 or xx**11 != xx or yy**11 != yy:
            raise ArithmeticError("The actual specified half class does not descend to the original EL.")
    if el_add(A_Q, minus_Q) is not None:
        raise ArithmeticError("The returned opposite original half class has the wrong sign.")

    G = (GF(-2), GF(-6))
    if el_times(G, 16) is not None or el_times(G, 8) is None:
        raise ArithmeticError("The named rational reference point does not have exact order 16 at q11.")
    matches = [n for n in range(16) if el_times(G, n) == A_Q]
    if len(matches) != 1:
        raise ArithmeticError("The half class is not uniquely in the original order16 reference subgroup.")
    k_G = matches[0]
    order = 1
    while el_times(A_Q, order) is not None:
        order *= 2
        if order > 16:
            raise ArithmeticError("The original q11 half class has unexpected order.")

    data = {
        "specified_local_partition": divided_rows,
        "degrees": {"plus": plus_degree, "minus": minus_degree, "full": total_degree},
        "half_class_on_exact_minus3_twist": encode_point(plus_twist),
        "opposite_half_class_on_exact_minus3_twist": encode_point(minus_twist),
        "A_Q_on_original_EL": encode_point(A_Q),
        "opposite_class_on_original_EL": encode_point(minus_Q),
        "A_Q_equals_k_times_G": k_G,
        "G_original_EL": {"x": -2, "y": -6},
        "G_reduction_order": 16,
        "A_Q_reduction_order": order,
        "coefficient_encoding": "pairs [a,b] mean a+b*delta, delta^2=-3, delta^11=-delta",
    }
    data_bytes = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    result = {
        "status": "EXACT_ORIGINAL_Q11_SPECIFIED_HALF_NORM_CLASS",
        "q": 11, "input_receipt": dict(NORM_BINDING, consumed_live=True),
        "input_norm_data_sha256": NORM_DATA_SHA,
        "input_lift_coordinates_sha256": LIFT_COORDINATES_SHA,
        "data": data, "data_sha256": hashlib.sha256(data_bytes).hexdigest(),
        "identities": {
            "original_delta_W_equals_plus_or_minus_t_used": True,
            "full_local_Fitting_multiplicities_preserved": True,
            "double_Norm_zero_not_assigned_to_one_half_by_guess": True,
            "both_original_halves_have_degree_q_plus_one": True,
            "two_half_classes_add_to_full_zero_class": True,
            "specified_A_Q_on_original_EL_is_F11_rational": True,
            "old_section_search_and_square_root_not_repeated": True,
        },
        "scope": {
            "general_q_half_class_formula_proved_by_this_run": False,
            "original_27_weighted_sum_nonzero": False,
            "ordinary_p_local_AJ_nonzero": False,
            "infinitely_many_p": False,
        },
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": time.monotonic()-started,
    }
    output = json.dumps(result, sort_keys=True, separators=(",", ":"))
    if len(output.encode()) > 60000:
        raise RuntimeError("The specified necessary divisor receipt exceeds the small output budget.")
    print(output)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"status": "EXECUTION_ERROR", "error_type": type(exc).__name__,
                          "message": str(exc)}, sort_keys=True, separators=(",", ":")), file=sys.stderr)
        raise
