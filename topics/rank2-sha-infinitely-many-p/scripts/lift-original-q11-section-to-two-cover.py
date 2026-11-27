#!/usr/bin/env python3
"""Lift the published q=11 section to the original R1031 two-cover.

The unique original section is consumed live from its pinned public receipt.
No section search or previously paid enumeration is repeated.
All function-field identities retain the complete cubic and quadratic fields.
"""

import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

if os.environ.get("GITHUB_ACTIONS") != "true" or \
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise SystemExit("Mathematical execution requires the named public GitHub Actions repository.")

from flint import nmod_poly

Q = 11
ORIGINAL = {
    "run": 45968889219,
    "job": 140404155125,
    "source": "3d702b7bc21923e82270953022b09b0950bb4adf",
    "request_id": "2026-11-27-0850-original-q11-all-minimal-poles",
    "script": "topics/rank2-sha-infinitely-many-p/scripts/check-original-q11-all-minimal-poles.py",
    "script_sha256": "ecc383aa7ae9603e5b48e6490d4273bb778994c6e5851447393f6c8a5dbc5a03",
    "stdout_sha256": "fda5154eea5725d118bc78383d6f9bac059c9384c2e0f0ee94c4abce99230ecd",
    "stdout_bytes": 3843,
    "enumeration_sha256": "af5567090bed1c212eda796cf0d8cf984b4c9085cfa19cbd03c2af152df3f357",
}

class ReceiptReadError(Exception):
    """Missing or mismatched original public evidence is an execution error."""


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def receipt_api_get(path, want_redirect=False):
    api = "https://api.github.com/repos/Rogerhu12/math-research-public"
    token = os.environ.get("RANK2_ACTIONS_READ_TOKEN", "")
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "rank2-q11-original-two-cover-receipt-reader",
        "Accept-Encoding": "identity",
    }
    if token:
        headers["Authorization"] = "Bearer " + token
    request = urllib.request.Request(api + path, headers=headers, method="GET")
    opener = urllib.request.build_opener(NoRedirect())
    try:
        response = opener.open(request, timeout=30)
    except urllib.error.HTTPError as exc:
        code, location = exc.code, exc.headers.get("Location")
        exc.close()
        if code == 302 and want_redirect and location:
            if not location.startswith("https://"):
                raise ReceiptReadError("The original log redirect is not HTTPS.")
            return location
        raise ReceiptReadError("The original public receipt API returned HTTP " + str(code))
    if want_redirect:
        response.close()
        raise ReceiptReadError("The original job log endpoint did not return a redirect.")
    with response:
        data = response.read(2000001)
    if len(data) > 2000000:
        raise ReceiptReadError("An original API metadata response exceeded its byte bound.")
    return json.loads(data)


def read_paid_result(binding):
    run_id, job_id = binding["run"], binding["job"]
    run = receipt_api_get("/actions/runs/" + str(run_id))
    job = receipt_api_get("/actions/jobs/" + str(job_id))
    if run.get("id") != run_id or run.get("head_sha") != binding["source"] or \
            job.get("id") != job_id or job.get("run_id") != run_id or \
            job.get("head_sha") != binding["source"]:
        raise ReceiptReadError("The original run/job/source identity does not match.")
    for metadata in (run, job):
        if metadata.get("status") != "completed" or metadata.get("conclusion") != "success":
            raise ReceiptReadError("The original public job is not completed successfully.")

    location = receipt_api_get("/actions/jobs/" + str(job_id) + "/logs", want_redirect=True)
    # A new unauthenticated request prevents forwarding the API token to storage.
    request = urllib.request.Request(location, headers={
        "User-Agent": "rank2-q11-original-two-cover-receipt-reader",
        "Accept-Encoding": "identity"}, method="GET")
    with urllib.request.urlopen(request, timeout=30) as response:
        raw_log = response.read(2000001)
    if len(raw_log) > 2000000:
        raise ReceiptReadError("An original compact job log exceeded its byte bound.")
    pattern = re.compile(
        rb"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z "
        rb"(RANK2_EXACT_STDOUT|RANK2_PUBLIC_EXACT_CHECK) (.*)$")
    stdout_records, receipt_records = [], []
    for line in raw_log.splitlines():
        match = pattern.fullmatch(line)
        if match is None:
            continue
        tag, payload = match.groups()
        record = json.loads(payload)
        if tag == b"RANK2_EXACT_STDOUT" and record.get("script") == binding["script"]:
            stdout_records.append(record)
        if tag == b"RANK2_PUBLIC_EXACT_CHECK" and record.get("request_id") == binding["request_id"]:
            receipt_records.append(record)
    if len(stdout_records) != 1 or len(receipt_records) != 1:
        raise ReceiptReadError("The original timestamped stdout/receipt is missing or ambiguous.")
    receipt = receipt_records[0]
    if receipt.get("run_id") != run_id or receipt.get("source_commit") != binding["source"] or \
            receipt.get("outputs_persisted") is not False:
        raise ReceiptReadError("The original complete-check receipt has a mismatched identity.")
    checks = [item for item in receipt.get("checks", [])
              if item.get("script") == binding["script"]]
    if len(checks) != 1:
        raise ReceiptReadError("The original exact script check is missing or ambiguous.")
    check = checks[0]
    if check.get("script_sha256") != binding["script_sha256"] or \
            check.get("sha256") != binding["stdout_sha256"] or \
            check.get("stdout_bytes") != binding["stdout_bytes"] or \
            check.get("exit_code") != 0 or check.get("args") != [] or \
            check.get("engine") != "python3":
        raise ReceiptReadError("The original script/stdout hash, arguments, or exit status differs.")
    result = stdout_records[0]["result"]
    raw = (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if len(raw) != binding["stdout_bytes"] or \
            hashlib.sha256(raw).hexdigest() != binding["stdout_sha256"]:
        raise ReceiptReadError("The live original stdout does not match its immutable hash.")
    return result




def poly(coefficients):
    return nmod_poly([int(c) % Q for c in coefficients], Q)


def exact_division(numerator, denominator):
    quotient, remainder = divmod(numerator, denominator)
    if not remainder.is_zero():
        raise ArithmeticError("A required exact polynomial division has a remainder.")
    return quotient


class Rat:
    """F_11(T), with a monic denominator; T is named by the surrounding model."""
    __slots__ = ("n", "d")

    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, Rat):
            if denominator != 1:
                raise TypeError("Use rational-field division, not a nested constructor.")
            self.n, self.d = numerator.n, numerator.d
            return
        n = numerator if isinstance(numerator, nmod_poly) else poly([numerator])
        d = denominator if isinstance(denominator, nmod_poly) else poly([denominator])
        if d.is_zero():
            raise ZeroDivisionError("Zero polynomial denominator.")
        if n.is_zero():
            self.n, self.d = poly([]), poly([1])
            return
        common = n.gcd(d)
        n, d = exact_division(n, common), exact_division(d, common)
        scale = pow(int(d[d.degree()]), Q - 2, Q)
        self.n, self.d = n * scale, d * scale

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Rat) else Rat(value)

    def __add__(self, other):
        try:
            other = Rat.coerce(other)
        except (TypeError, ValueError):
            return NotImplemented
        return Rat(self.n * other.d + other.n * self.d, self.d * other.d)

    __radd__ = __add__

    def __neg__(self):
        return Rat(-self.n, self.d)

    def __sub__(self, other):
        return self + (-Rat.coerce(other))

    def __rsub__(self, other):
        return Rat.coerce(other) + (-self)

    def __mul__(self, other):
        try:
            other = Rat.coerce(other)
        except (TypeError, ValueError):
            return NotImplemented
        return Rat(self.n * other.n, self.d * other.d)

    __rmul__ = __mul__

    def inverse(self):
        if self.is_zero():
            raise ZeroDivisionError("Zero rational-function inverse.")
        return Rat(self.d, self.n)

    def __truediv__(self, other):
        return self * Rat.coerce(other).inverse()

    def __rtruediv__(self, other):
        return Rat.coerce(other) * self.inverse()

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        return Rat(self.n ** exponent, self.d ** exponent)

    def __eq__(self, other):
        try:
            other = Rat.coerce(other)
        except (TypeError, ValueError):
            return False
        return self.n == other.n and self.d == other.d

    def is_zero(self):
        return self.n.is_zero()

    def encode(self):
        return {"numerator": [int(c) for c in self.n],
                "denominator": [int(c) for c in self.d]}


def quadratic_field(discriminant):
    class Quad:
        """a+b*v, v^2=the exact displayed discriminant."""
        __slots__ = ("a", "b")

        def __init__(self, a=0, b=0):
            if isinstance(a, Quad):
                if b != 0:
                    raise TypeError("Use quadratic-field addition.")
                self.a, self.b = a.a, a.b
            else:
                self.a, self.b = Rat.coerce(a), Rat.coerce(b)

        @staticmethod
        def coerce(value):
            return value if isinstance(value, Quad) else Quad(value)

        def __add__(self, other):
            try:
                other = Quad.coerce(other)
            except (TypeError, ValueError):
                return NotImplemented
            return Quad(self.a + other.a, self.b + other.b)

        __radd__ = __add__

        def __neg__(self):
            return Quad(-self.a, -self.b)

        def __sub__(self, other):
            try:
                other = Quad.coerce(other)
            except (TypeError, ValueError):
                return NotImplemented
            return self + (-other)

        def __rsub__(self, other):
            return Quad.coerce(other) + (-self)

        def __mul__(self, other):
            try:
                other = Quad.coerce(other)
            except (TypeError, ValueError):
                return NotImplemented
            return Quad(self.a * other.a + discriminant * self.b * other.b,
                        self.a * other.b + self.b * other.a)

        __rmul__ = __mul__

        def norm(self):
            return self.a ** 2 - discriminant * self.b ** 2

        def inverse(self):
            nn = self.norm()
            if nn.is_zero():
                raise ZeroDivisionError("Zero quadratic-field inverse.")
            return Quad(self.a / nn, -self.b / nn)

        def __truediv__(self, other):
            try:
                other = Quad.coerce(other)
            except (TypeError, ValueError):
                return NotImplemented
            return self * other.inverse()

        def __rtruediv__(self, other):
            return Quad.coerce(other) * self.inverse()

        def __pow__(self, exponent):
            if exponent < 0:
                return self.inverse() ** (-exponent)
            answer, power = Quad(1), self
            while exponent:
                if exponent & 1:
                    answer = answer * power
                power = power * power
                exponent >>= 1
            return answer

        def __eq__(self, other):
            try:
                other = Quad.coerce(other)
            except (TypeError, ValueError):
                return False
            return self.a == other.a and self.b == other.b

        def is_zero(self):
            return self.a.is_zero() and self.b.is_zero()

        def encode(self):
            return {"coefficient_1": self.a.encode(),
                    "coefficient_quadratic_generator": self.b.encode()}

    return Quad


def polynomial_value(coefficients, at):
    answer = at * 0
    for coefficient in reversed(coefficients):
        answer = answer * at + int(coefficient)
    return answer


def rational_square_root(value):
    """Return a root in F_11(T), or None; never enlarge the field."""
    value = Rat.coerce(value)
    if value.is_zero():
        return Rat(0)
    nlead, nfactors = value.n.factor(algorithm="berlekamp")
    dlead, dfactors = value.d.factor(algorithm="berlekamp")
    if any(exponent % 2 for _, exponent in nfactors + dfactors):
        return None
    scalar = int(nlead) * pow(int(dlead), Q - 2, Q) % Q
    roots = [c for c in range(Q) if c * c % Q == scalar]
    if not roots:
        return None
    nn, dd = poly([min(roots)]), poly([1])
    for factor, exponent in nfactors:
        nn = nn * factor ** (exponent // 2)
    for factor, exponent in dfactors:
        dd = dd * factor ** (exponent // 2)
    result = Rat(nn, dd)
    if result ** 2 != value:
        raise ArithmeticError("Polynomial factorization did not return the stated square root.")
    return result


def quadratic_square_root(value, discriminant, Quad):
    """The full norm formula, including zero cross-coefficient branches."""
    if value.b.is_zero():
        root = rational_square_root(value.a)
        if root is not None:
            return Quad(root)
        root = rational_square_root(value.a / discriminant)
        if root is not None:
            return Quad(0, root)
        return None
    norm_root = rational_square_root(value.norm())
    if norm_root is None:
        return None
    for signed_norm in (norm_root, -norm_root):
        aa = rational_square_root((value.a + signed_norm) / 2)
        if aa is None or aa.is_zero():
            continue
        bb = value.b / (2 * aa)
        result = Quad(aa, bb)
        if result ** 2 == value:
            return result
    return None


def cubic_field(Base, c):
    class Cubic:
        """The full original field with z^3=4-c*z, including its fixed basis."""
        __slots__ = ("v",)

        def __init__(self, a=0, b=0, d=0):
            if isinstance(a, Cubic):
                if b != 0 or d != 0:
                    raise TypeError("Use cubic-field addition.")
                self.v = a.v
            else:
                self.v = (Base.coerce(a), Base.coerce(b), Base.coerce(d))

        @staticmethod
        def coerce(value):
            return value if isinstance(value, Cubic) else Cubic(value)

        def __add__(self, other):
            other = Cubic.coerce(other)
            return Cubic(*(self.v[i] + other.v[i] for i in range(3)))

        __radd__ = __add__

        def __neg__(self):
            return Cubic(*(-v for v in self.v))

        def __sub__(self, other):
            return self + (-Cubic.coerce(other))

        def __rsub__(self, other):
            return Cubic.coerce(other) + (-self)

        def __mul__(self, other):
            other = Cubic.coerce(other)
            out = [Base(0) for _ in range(5)]
            for i in range(3):
                for j in range(3):
                    out[i+j] = out[i+j] + self.v[i] * other.v[j]
            out[1] = out[1] + 4 * out[4] - c * out[3]
            out[2] = out[2] - c * out[4]
            out[0] = out[0] + 4 * out[3]
            return Cubic(*out[:3])

        __rmul__ = __mul__

        def multiplication_matrix(self):
            a, b, d = self.v
            return ((a, 4*d, 4*b),
                    (b, a-c*d, 4*d-c*b),
                    (d, b, a-c*d))

        def norm(self):
            m = self.multiplication_matrix()
            return (m[0][0] * (m[1][1]*m[2][2] - m[1][2]*m[2][1])
                    - m[0][1] * (m[1][0]*m[2][2] - m[1][2]*m[2][0])
                    + m[0][2] * (m[1][0]*m[2][1] - m[1][1]*m[2][0]))

        def inverse(self):
            a, b, d = self.v
            nn = self.norm()
            if nn.is_zero():
                raise ZeroDivisionError("Zero original cubic-field inverse.")
            return Cubic(((a-c*d)**2 - b*(4*d-c*b))/nn,
                         (4*d**2-a*b)/nn,
                         (b**2-a*d+c*d**2)/nn)

        def __truediv__(self, other):
            return self * Cubic.coerce(other).inverse()

        def __rtruediv__(self, other):
            return Cubic.coerce(other) * self.inverse()

        def __pow__(self, exponent):
            if exponent < 0:
                return self.inverse() ** (-exponent)
            answer, power = Cubic(1), self
            while exponent:
                if exponent & 1:
                    answer = answer * power
                power = power * power
                exponent >>= 1
            return answer

        def __eq__(self, other):
            other = Cubic.coerce(other)
            return all(self.v[i] == other.v[i] for i in range(3))

        def is_zero(self):
            return all(item.is_zero() for item in self.v)

        def trace(self):
            return 3*self.v[0] - 2*c*self.v[2]

    return Cubic


def original_section(record, X, Y):
    xnum = sum((polynomial_value(co, Y) * X**i
                for i, co in enumerate(record["x_numerator_basis_1_X_X2"])), X*0)
    wnum = sum((polynomial_value(co, Y) * X**i
                for i, co in enumerate(record["W_numerator_basis_1_X_X2"])), X*0)
    return (xnum / polynomial_value(record["x_denominator"], Y),
            wnum / polynomial_value(record["W_denominator"], Y))


def main():
    started = time.monotonic()
    source = read_paid_result(ORIGINAL)
    os.environ.pop("RANK2_ACTIONS_READ_TOKEN", None)
    if source.get("q") != Q or source.get("source_sha256") != ORIGINAL["script_sha256"] or \
            source.get("enumeration_sha256") != ORIGINAL["enumeration_sha256"] or \
            source.get("normalized_solution_count") != 1 or \
            source.get("mathematical_status") != "ACTUAL_ORIGINAL_HEIGHT_22_OVER_3_SECTION_FOUND" or \
            len(source.get("representatives", [])) != 1:
        raise ReceiptReadError("The pinned live record does not supply the unique original section.")
    point = source["representatives"][0]

    # First model: F_11(z)[w]/(w^2-(z^3-4)(z^3-16)).
    variable = Rat(poly([0, 1]))
    discriminant_C = (variable**3 - 4) * (variable**3 - 16)
    CField = quadratic_field(discriminant_C)
    z, w = CField(variable), CField(0, 1)
    X_C = -3*z / (z**3 - 4)
    Y_C = (w*(z**3 + 2)/(z**3 - 4)**2 - 1)/2
    if Y_C**2 + Y_C != X_C**3:
        raise ArithmeticError("The original spectral map does not return B.")
    x_C, _ = original_section(point, X_C, Y_C)
    roots_a = [a for a in range(Q) if a**3 % Q == 4]
    if len(roots_a) != 1:
        raise ArithmeticError("The stated inert cubic root is not unique.")
    a = roots_a[0]
    g_C = z**2 + a*z + a**2
    u_C = (1 - w/(z**3 - 4))/6
    target_square = -3*(z-2*X_C)**2*(x_C+u_C**2)/g_C
    lift_C = quadratic_square_root(target_square, discriminant_C, CField)
    if lift_C is None or lift_C**2 != target_square:
        raise ArithmeticError("The original primitive section has no square root in its exact spectral field.")

    # Second model: k=F_11(X)[v]/(v^2-4X^3-1), v=2Y+1,
    # and the full original cubic k[z]/(z^3+3z/X-4).
    discriminant_B = 4*variable**3 + 1
    Base = quadratic_field(discriminant_B)
    X, v = Base(variable), Base(0, 1)
    Y = (v-1)/2
    c = 3/X
    Cubic = cubic_field(Base, c)
    zz = Cubic(0, 1, 0)
    ww = Cubic(v*c**2)*zz**2/(6-c*zz)
    if zz**3 + c*zz != 4 or ww**2 != (zz**3-4)*(zz**3-16):
        raise ArithmeticError("The change to the fixed original spectral basis failed.")

    def eval_rat_at_z(rat):
        return (polynomial_value([int(k) for k in rat.n], zz) /
                polynomial_value([int(k) for k in rat.d], zz))

    lift = eval_rat_at_z(lift_C.a) + ww*eval_rat_at_z(lift_C.b)
    x_source, W_source = original_section(point, X, Y)
    g = zz**2 + a*zz + a**2
    identity20 = -9*Cubic(x_source)*(zz-2*X)**2 - (Y*zz+X)**2 - 3*g*lift**2
    if not identity20.is_zero():
        raise ArithmeticError("The lift does not satisfy the original full cubic identity (20).")

    def returned_W(r):
        return -a*r.norm()/(3*X*v**2)

    W_return = returned_W(lift)
    sign_changed = False
    if W_return != W_source:
        if W_return != -W_source:
            raise ArithmeticError("The original Norm returns neither allowed W orientation.")
        lift, lift_C = -lift, -lift_C
        W_return = returned_W(lift)
        sign_changed = True

    A0, B1, C1 = lift.v
    U0 = A0**2 + 8*B1*C1
    U1 = 2*A0*B1 - 2*c*B1*C1 + 4*C1**2
    U2 = B1**2 + 2*A0*C1 - c*C1**2
    G0 = a*a*U0 + 4*U1 + 4*a*U2
    G1 = a*U0 + (a*a-c)*U1 + (4-a*c)*U2
    G2 = U0 + a*U1 + (a*a-c)*U2
    quadric1 = 3*G0 - 12*X**2*G2 - X**2*(4*Y**2-1)
    quadric2 = 3*G1 + 12*X*G2 + 2*X*Y*v
    x_return = -G2/3 - Y**2/9
    if not quadric1.is_zero() or not quadric2.is_zero() or \
            x_return != x_source or W_return != W_source:
        raise ArithmeticError("The original two quadrics or full coordinate return failed.")
    if -3*W_return**2 != 4*x_return**3+(x_return-Y/27)**2:
        raise ArithmeticError("The returned original point is not on the original curve.")
    if g.norm() != (3*a/X)**2 or (zz-2*X).norm() != -2*v**2:
        raise ArithmeticError("The fixed two Norm constants are not the original ones.")

    coordinates = {
        "s": 1,
        "R_basis_1_z_z2": [entry.encode() for entry in lift.v],
        "coefficient_model": "F11(X)[v]/(v^2-4X^3-1); v=2Y+1",
        "spectral_relation": "z^3+3z/X-4=0",
        "R_hyperelliptic_model": lift_C.encode(),
        "hyperelliptic_model": "F11(z)[w]/(w^2-(z^3-4)(z^3-16))",
        "a": a,
    }
    coordinate_bytes = json.dumps(coordinates, sort_keys=True, separators=(",", ":")).encode()
    result = {
        "status": "EXACT_ORIGINAL_Q11_TWO_COVER_LIFT",
        "q": Q,
        "input_receipt": dict(ORIGINAL, consumed_live=True, section_search_repeated=False),
        "coordinates": coordinates,
        "coordinates_sha256": hashlib.sha256(coordinate_bytes).hexdigest(),
        "identities": {
            "full_original_spectral_identity20_zero": [True, True, True],
            "two_original_quadrics19_zero": [True, True],
            "x_return22_equals_original": True,
            "W_return24_equals_original_with_fixed_Norm_sign": True,
            "g_Norm_equals_9_a2_over_X2": True,
            "z_minus_2X_Norm_equals_minus2_v2": True,
            "exact_rational_functions_not_point_samples": True,
            "all_thick_poles_and_boundary_extensions_preserved_by_identity": True,
        },
        "root_sign_changed_to_original_W": sign_changed,
        "original_y_return": "(delta*W-x-t)/2; delta^2=-3",
        "scope": {
            "original_two_cover_rational_point_paid": True,
            "new_general_q_section_constructed": False,
            "Frobenius_stable_k_line_claimed": False,
            "original_27_weighted_pairs_nonzero": False,
            "ordinary_p_local_comparison_paid": False,
            "infinitely_many_p": False,
        },
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": time.monotonic()-started,
    }
    encoded = json.dumps(result, sort_keys=True, separators=(",", ":"))
    if len(encoded.encode()) > 60000:
        raise RuntimeError("The necessary coordinate receipt exceeds the public small-runner output budget.")
    print(encoded)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        error = {"status": "EXECUTION_ERROR", "error_type": type(exc).__name__, "message": str(exc)}
        print(json.dumps(error, sort_keys=True, separators=(",", ":")), file=sys.stderr)
        raise
