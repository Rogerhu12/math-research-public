#!/usr/bin/env python3
"""Read the paid q=11 lift and compute its new complete Prym norm divisors.

No polar-divisor search or spectral square-root calculation is repeated.
The arithmetic is performed only in the named public Actions repository.
"""
import hashlib
import importlib.util
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
    raise SystemExit("The paid rational-function helper source has changed.")
spec = importlib.util.spec_from_file_location("paid_q11_two_cover", helper_path)
paid = importlib.util.module_from_spec(spec)
spec.loader.exec_module(paid)
Q, Rat, poly = paid.Q, paid.Rat, paid.poly
exact = paid.exact_division
one, zero = poly([1]), poly([])

BINDING = {
    "run": 45972624090,
    "job": 140416498782,
    "source": "c5020fcd7f026ef21d4b69735b3a47b56148d258",
    "request_id": "2026-11-27-0918-original-q11-two-cover-lift",
    "script": "topics/rank2-sha-infinitely-many-p/scripts/lift-original-q11-section-to-two-cover.py",
    "script_sha256": HELPER_SHA,
    "stdout_sha256": "b1341ed2e07961af591c0f967d660a236a53cb8a25c492439654ccad34fb510d",
    "stdout_bytes": 2484,
}
COORDINATES_SHA = "3afbc5db78bf933d28788ea282eeae2d19211a8184e3670dedd2eccbf1765a68"


def encoded(poly_value):
    return [int(c) for c in poly_value]


def monic(f):
    if f.is_zero():
        return f
    return f * pow(int(f[f.degree()]), Q-2, Q)


def xgcd(a, b):
    r0, r1, s0, s1, t0, t1 = a, b, one, zero, zero, one
    while not r1.is_zero():
        quotient, remainder = divmod(r0, r1)
        r0, r1 = r1, remainder
        s0, s1 = s1, s0-quotient*s1
        t0, t1 = t1, t0-quotient*t1
    if r0.is_zero():
        return zero, zero, zero
    scale = pow(int(r0[r0.degree()]), Q-2, Q)
    return r0*scale, s0*scale, t0*scale


def inverse_mod(a, modulus):
    d, s, _ = xgcd(a, modulus)
    if d != one:
        raise ArithmeticError("A primitive branch denominator was not invertible.")
    return s % modulus


def decode_rat(record):
    return Rat(poly(record["numerator"]), poly(record["denominator"]))


def substitute(value, at):
    return (paid.polynomial_value(encoded(value.n), at) /
            paid.polynomial_value(encoded(value.d), at))


def factor(f):
    if f.is_zero():
        raise ArithmeticError("A zero polynomial has no finite divisor factorization.")
    _, factors = f.factor(algorithm="berlekamp")
    return [(h, int(e)) for h, e in factors]


def finite_divisor(A, B, P):
    """Complete finite divisor of A(T)+B(T)y, y^2=P(T).

    Unsplit vertical rows denote the entire inverse image of an irreducible
    polynomial, with its degree and actual multiplicity, not a selected point.
    """
    common = exact(A.d * B.d, A.d.gcd(B.d))
    aa, bb = A.n * exact(common, A.d), B.n * exact(common, B.d)
    content = aa.gcd(bb)
    if content.is_zero():
        raise ArithmeticError("The named function is zero.")
    aa, bb = exact(aa, content), exact(bb, content)
    scalar = Rat(content, common)
    nn = aa**2 - P*bb**2
    if nn.is_zero() or not P.gcd(P.derivative()).is_one():
        raise ArithmeticError("The displayed quadratic curve or primitive norm is singular.")
    table = {}
    for f, which, sign in ((scalar.n, "vertical", 1),
                           (scalar.d, "vertical", -1),
                           (nn, "norm", 1)):
        for h, exponent in factor(f):
            key = tuple(encoded(h))
            item = table.setdefault(key, {"h": h, "vertical": 0, "norm": 0})
            item[which] += sign*exponent
    rows = []

    def append(kind, h, multiplicity, degree, branch=None):
        if multiplicity:
            record = {"kind": kind, "polynomial": encoded(h),
                      "multiplicity": multiplicity, "degree": degree}
            if branch is not None:
                record["y_mod_polynomial"] = encoded(branch % h)
            rows.append(record)

    for key in sorted(table, key=lambda k: (len(k), k)):
        item = table[key]
        h, e, n = item["h"], item["vertical"], item["norm"]
        ramified = (P % h).is_zero()
        if ramified:
            if n not in (0, 1):
                raise ArithmeticError("A primitive function has unexpected branch multiplicity.")
            append("ramified_point", h, 2*e+n, h.degree(), zero)
        elif n:
            root = (-aa * inverse_mod(bb, h)) % h
            if ((root**2-P) % h) != zero:
                raise ArithmeticError("The selected zero branch does not lie on the curve.")
            append("selected_branch", h, e+n, h.degree(), root)
            append("opposite_branch", h, e, h.degree(), -root)
        else:
            append("entire_unramified_inverse_image", h, e, 2*h.degree())
    return rows, scalar, aa, bb, nn


def complete_divisor(A, B, P, infinity_model):
    rows, scalar, aa, bb, nn = finite_divisor(A, B, P)
    if infinity_model == "cubic":
        # The two possible pole orders have opposite parity.
        order_a = 10**9 if A.is_zero() else 2*(A.d.degree()-A.n.degree())
        order_b = 10**9 if B.is_zero() else 2*(B.d.degree()-B.n.degree())-3
        order = min(order_a, order_b)
        if order:
            rows.append({"kind": "infinity", "degree": 1, "multiplicity": order})
    elif infinity_model == "monic_sextic":
        da, db = aa.degree(), bb.degree()+3 if not bb.is_zero() else -1
        scalar_order = scalar.d.degree()-scalar.n.degree()
        if da != db:
            orders = [-max(da, db), -max(da, db)]
        else:
            la, lb = int(aa[da]), int(bb[bb.degree()])
            plus_cancel = (la+lb) % Q == 0
            minus_cancel = (la-lb) % Q == 0
            if plus_cancel and minus_cancel:
                raise ArithmeticError("Both infinite leading coefficients vanished.")
            if plus_cancel:
                orders = [da-nn.degree(), -da]
            elif minus_cancel:
                orders = [-da, da-nn.degree()]
            else:
                orders = [-da, -da]
        for sign, order in zip((1, -1), orders):
            order += scalar_order
            if order:
                rows.append({"kind": "infinity", "y_over_T3": sign,
                             "degree": 1, "multiplicity": order})
    else:
        raise ValueError("Unknown fixed infinity model.")
    total = sum(row["degree"] * row["multiplicity"] for row in rows)
    if total != 0:
        raise ArithmeticError("The complete divisor, including infinity, has nonzero degree.")
    return {
        "rows": rows,
        "zero_degree": sum(row["degree"]*max(row["multiplicity"], 0) for row in rows),
        "pole_degree": sum(row["degree"]*max(-row["multiplicity"], 0) for row in rows),
        "primitive_numerator_1": encoded(aa),
        "primitive_numerator_y": encoded(bb),
        "scalar": scalar.encode(),
        "primitive_norm": encoded(nn),
    }


def reduced_pair(u, v, P):
    u = monic(u)
    if u.is_zero() or ((v*v-P) % u) != zero:
        raise ArithmeticError("The divisor pair does not satisfy its curve equation.")
    v %= u
    while u.degree() > 1:
        u = monic(exact(P-v*v, u))
        if u.is_one():
            return one, zero
        v = (-v) % u
    return u, v


def add_pairs(pair1, pair2, P):
    u1, v1 = pair1
    u2, v2 = pair2
    d1, e1, e2 = xgcd(u1, u2)
    d, c1, c2 = xgcd(d1, v1+v2)
    s1, s2, s3 = c1*e1, c1*e2, c2
    u = exact(u1*u2, d*d)
    if u.is_one():
        return one, zero
    v = exact(s1*u1*v2+s2*u2*v1+s3*(v1*v2+P), d) % u
    return reduced_pair(u, v, P)


def times_pair(pair, number, P):
    answer = (one, zero)
    while number:
        if number & 1:
            answer = add_pairs(answer, pair, P)
        pair = add_pairs(pair, pair, P)
        number >>= 1
    return answer


def effective_class(divisor, sign, P):
    answer = (one, zero)
    for row in divisor["rows"]:
        multiplicity = sign * row["multiplicity"]
        if multiplicity <= 0 or row["kind"] in ("infinity", "entire_unramified_inverse_image"):
            continue
        h = poly(row["polynomial"])
        root = poly(row["y_mod_polynomial"])
        point_sum = reduced_pair(h, root, P)
        answer = add_pairs(answer, times_pair(point_sum, multiplicity, P), P)
    u, v = answer
    if u.is_one():
        return {"point": "O"}
    return {"point": "affine", "x": (-int(u[0])) % Q, "y": int(v[0]) if not v.is_zero() else 0}


def main():
    started = time.monotonic()
    source = paid.read_paid_result(BINDING)
    os.environ.pop("RANK2_ACTIONS_READ_TOKEN", None)
    coordinates = source["coordinates"]
    coordinate_bytes = json.dumps(coordinates, sort_keys=True, separators=(",", ":")).encode()
    if source.get("status") != "EXACT_ORIGINAL_Q11_TWO_COVER_LIFT" or source.get("q") != 11 or \
            source.get("source_sha256") != HELPER_SHA or \
            source.get("coordinates_sha256") != COORDINATES_SHA or \
            hashlib.sha256(coordinate_bytes).hexdigest() != COORDINATES_SHA or \
            coordinates.get("a") != 5 or coordinates.get("s") != 1:
        raise paid.ReceiptReadError("The pinned input is not the exact oriented original lift.")
    root = coordinates["R_hyperelliptic_model"]
    A = decode_rat(root["coefficient_1"])
    B = decode_rat(root["coefficient_quadratic_generator"])
    z = Rat(poly([0, 1]))
    a = coordinates["a"]
    K = z**3-4
    P_C_rat = K*(z**3-16)
    P_C = P_C_rat.n
    g = z*z+a*z+a*a
    X_B = -3*z/K
    D = z-2*X_B

    R_divisor = complete_divisor(A, B, P_C, "monic_sextic")

    # R1039 (22): N_Q=U+V Z, Z=delta W_L, delta^2=-3.
    U = -1/K-g*(A*A-K*(z**3-16)*B*B)/(D*D)
    V = g*(B+A/K)/(3*D)
    # The exact (-3)-twist, not a j-only identification:
    # X_T=-3 x_L, Y_T=-3 delta y_L, z=a(X_T+12)/(X_T+3),
    # Z=9 a^2 Y_T/(X_T+3)^2.
    T = Rat(poly([0, 1]))
    z_at_T = a*(T+12)/(T+3)
    A_N = substitute(U, z_at_T)
    B_N = substitute(V, z_at_T) * (9*a*a)/(T+3)**2
    P_T = poly([-540, -108, 0, 1])
    TField = paid.quadratic_field(Rat(P_T))
    N_Q = TField(A_N, B_N)
    N_divisor = complete_divisor(A_N, B_N, P_T, "cubic")

    # A new full-function identity for this Norm, consuming the paid R.
    CField = paid.quadratic_field(P_C_rat)
    w = CField(0, 1)
    R = CField(A, B)
    u = (1-w/K)/6
    original_x = -g*R**2/(3*D**2)-u**2
    norm_rhs = 9*substitute(original_x.norm(), z_at_T)
    if N_Q.norm() != norm_rhs:
        raise ArithmeticError("The new double Norm does not return R1039 (23).")
    zero_class = effective_class(N_divisor, 1, P_T)
    pole_class = effective_class(N_divisor, -1, P_T)
    if zero_class != pole_class:
        raise ArithmeticError("The two complete effective Norm divisors have different Picard classes.")

    data = {
        "R_divisor_on_original_C": R_divisor,
        "N_Q_on_exact_minus3_twist": N_Q.encode(),
        "N_Q_divisor": N_divisor,
        "N_Q_zero_divisor_Picard_class": zero_class,
        "N_Q_pole_divisor_Picard_class": pole_class,
        "twist_model": "Y_T^2=X_T^3-108 X_T-540 over F11",
        "original_to_twist": "X_T=-3 x_L; Y_T=-3 delta y_L; delta^2=-3",
        "inverse_original_parameter": "z=a(X_T+12)/(X_T+3); delta W_L=9a^2 Y_T/(X_T+3)^2",
    }
    data_bytes = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    result = {
        "status": "EXACT_ORIGINAL_Q11_PRYM_NORM_DIVISORS",
        "q": 11,
        "input_receipt": dict(BINDING, consumed_live=True),
        "input_coordinates_sha256": COORDINATES_SHA,
        "data": data,
        "data_sha256": hashlib.sha256(data_bytes).hexdigest(),
        "identities": {
            "original_R_sign_retained": True,
            "original_two_cover_search_repeated": False,
            "original_square_root_recomputed": False,
            "full_double_norm23_returned": True,
            "finite_ramified_unramified_and_infinite_orders_retained": True,
            "all_factor_multiplicities_retained": True,
            "complete_divisor_degrees_zero": True,
            "norm_zero_and_pole_Picard_classes_equal": True,
        },
        "scope": {
            "new_general_q_point_constructed": False,
            "original_27_weighted_sum_nonzero": False,
            "ordinary_p_local_AJ_nonzero": False,
            "infinitely_many_p": False,
        },
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": time.monotonic()-started,
    }
    output = json.dumps(result, sort_keys=True, separators=(",", ":"))
    if len(output.encode()) > 60000:
        raise RuntimeError("The necessary new divisor receipt exceeds the small output bound.")
    print(output)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        error = {"status": "EXECUTION_ERROR", "error_type": type(exc).__name__,
                 "message": str(exc)}
        print(json.dumps(error, sort_keys=True, separators=(",", ":")), file=sys.stderr)
        raise
