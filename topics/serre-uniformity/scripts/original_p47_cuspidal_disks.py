#!/usr/bin/env python3
"""Original p47 cuspidal labels on all p-local disks.

Arithmetic is restricted to the public repository's GitHub Actions.
The input is R1062/R1069/R1070/R1071, including the actual finite
first-lift construction and the normalized Miller pairing. This is not
the old p47 scalar or lowest-functional calculation.
"""
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback

P = 47
DELTA = 5
C = 5
REPO = "Rogerhu12/math-research-public"
PRE = "topics/serre-uniformity/"
REQUEST = PRE + "notes/original-p47-cuspidal-disks-request.json"
STARTED = None
DEADLINE = None
nmod_poly = None


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def emit(kind, value):
    print(kind + "=" + canonical(value).decode(), flush=True)


class MathDeadline(Exception):
    pass


def alarm_handler(signum, frame):
    raise MathDeadline("Declared public arithmetic budget reached")


def check_budget():
    if time.monotonic() >= DEADLINE:
        raise MathDeadline("Declared arithmetic reserve reached")


def poly(coeffs, modulus=P):
    return nmod_poly(coeffs, modulus)


def ints(f, n=None):
    if n is None:
        n = len(f)
    return [int(f[i]) for i in range(n)]


def inv(a, modulus=P):
    return pow(int(a) % modulus, -1, modulus)


def legendre(a):
    a %= P
    return 0 if a == 0 else (1 if pow(a, (P-1)//2, P) == 1 else -1)


def actual_characters():
    """S_psi=-J(psi,eta) B_2,psi^2 /4, with the pole case retained."""
    from fractions import Fraction
    from math import comb, factorial
    bern = [Fraction(1)]
    for n in range(1, P-2):
        bern.append(-sum(Fraction(comb(n+1, i))*bern[i]
                         for i in range(n)) / (n+1))
    teich = [0] + [pow(a, P, P*P) for a in range(1, P)]
    actual, good, rows = [], [], []
    forced = {P-1-2*j for j in range(1, P//4)}
    for r in range(2, P-2, 2):
        jmod = sum(pow(x, (-r) % (P-1), P)*legendre(1-x)
                   for x in range(1, P)) % P
        e2 = (-2*r) % (P-1)
        s2 = sum(a*a*pow(teich[a], e2, P*P)
                 for a in range(1, P)) % (P*P)
        s1 = sum(a*pow(a, e2, P) for a in range(1, P)) % P
        exceptional = (r == (P+1)//2)
        if exceptional:
            assert jmod == 0 and s2 % P != 0
            included, b2 = False, None
        else:
            assert s2 % P == 0
            b2 = (s2//P-s1) % P
            included = (jmod == 0 or b2 == 0)
        br = bern[r].numerator*inv(bern[r].denominator) % P
        kap = (C*C-pow(C, 2*r, P)) % P
        row = {"R": r, "J_mod_p": jmod, "B2_mod_p": b2,
               "exceptional_pole": exceptional, "actual_V": included,
               "Bernoulli_mod_p": br, "kappa": kap}
        if included:
            assert kap != 0
            actual.append(r)
            if br:
                good.append(r)
                row["circle_without_gamma"] = (
                    br*(pow(C, r, P)-1)*inv(r*factorial(r))) % P
                assert row["circle_without_gamma"] != 0
        rows.append(row)
    assert forced.issubset(actual)
    # The following is a computed condition, not an imported regularity claim.
    assert actual == good, "A bad actual character needs its separate global input"
    return actual, rows


def model_for_j(j):
    if j == 0:
        return 0, 1
    if j == 1728 % P:
        return 1, 0
    k = j*inv(1728-j) % P
    return 3*k % P, 2*k % P


def original_models():
    models = []
    for j in range(P):
        a, b = model_for_j(j)
        discr = (4*a**3+27*b*b) % P
        assert discr
        assert 1728*4*a**3*inv(discr) % P == j
        hasse = int(poly([b, a, 0, 1]).pow_trunc((P-1)//2, P)[P-1])
        if hasse:
            continue
        trace = -sum(legendre(x*x*x+a*x+b) for x in range(P))
        assert trace == 0
        models.append({"j": j, "A": a, "B": b, "twist": 0})
        if j == 1728 % P:
            a2 = DELTA
            hasse2 = int(poly([0, a2, 0, 1]).pow_trunc((P-1)//2, P)[P-1])
            trace2 = -sum(legendre(x*x*x+a2*x) for x in range(P))
            assert hasse2 == 0 and trace2 == 0
            models.append({"j": j, "A": a2, "B": 0, "twist": 1})
    assert legendre(DELTA) == -1
    assert {pow(C, i, P) for i in range(P-1)} == set(range(1, P))
    return models


def first_lift_series(a, b, nmax):
    """nmax is the highest q=z^2 index needed; division by p uses mod p^2."""
    modulus = P*P
    length = nmax+1
    w = poly([1], modulus)
    precision = 1
    while precision < length:
        precision = min(2*precision, length)
        w2 = w.mul_low(w, precision)
        w3 = w2.mul_low(w, precision)
        eq = (w3-w2+a*w.left_shift(2)+poly([b], modulus).left_shift(3)).truncate(precision)
        derivative = (3*w2-2*w+poly([a], modulus).left_shift(2)).truncate(precision)
        w = (w-eq.mul_low(derivative.inverse_series_trunc(precision), precision)).truncate(precision)
    w2 = w.mul_low(w, length)
    energy = (w2.mul_low(w, length)-w2+a*w.left_shift(2)
              +poly([b], modulus).left_shift(3)).truncate(length)
    assert energy.is_zero()
    omega = (poly([1], modulus)-w.derivative().left_shift(1).mul_low(
        w.inverse_series_trunc(length), length)).truncate(length)
    u = []
    p_blocks = []
    for n in range(length):
        denominator = 2*n+1
        numerator = int(omega[n])
        assert denominator < P*P
        if denominator % P == 0:
            assert numerator % P == 0
            coefficient = numerator//P*inv(denominator//P) % P
            p_blocks.append({"degree": denominator, "omega_mod_p2": numerator,
                             "log_mod_p": coefficient})
        else:
            coefficient = numerator*inv(denominator) % P
        u.append(coefficient)
    assert u[0] == 1
    # The entire low formal-log differential identity, including all p-blocks.
    assert all(((2*n+1)*u[n]-int(omega[n])) % P == 0
               for n in range(length))
    return poly(ints(w)), poly(u), p_blocks


def division_five_unit(w, a, b, length):
    powers = [poly([1])]
    for _ in range(6):
        powers.append(powers[-1].mul_low(w, length))
    p3 = (3*powers[4]+6*a*powers[2].left_shift(2)
          +12*b*powers[1].left_shift(3)
          -poly([a*a]).left_shift(4)).truncate(length)
    p4 = (powers[6]+5*a*powers[4].left_shift(2)
          +20*b*powers[3].left_shift(3)
          -5*a*a*powers[2].left_shift(4)
          -4*a*b*powers[1].left_shift(5)
          -poly([8*b*b+a**3]).left_shift(6)).truncate(length)
    # q^3 (x^3+Ax+B)=w^2 by the checked original Weierstrass equation.
    v = (32*powers[4].mul_low(p4, length)
         -p3.mul_low(p3, length).mul_low(p3, length))*inv(5)
    v = v.truncate(length)
    assert int(v[0]) == 1
    h = (poly([-24])+2*v.derivative().left_shift(1).mul_low(
        v.inverse_series_trunc(length), length)).truncate(length)
    return v, h


class F2Series:
    """a(h)+s*b(h), s^2=DELTA, exact modulo h^length."""
    def __init__(self, a, b=None, length=P+2):
        self.length = length
        self.a = (a if isinstance(a, nmod_poly) else poly(a)).truncate(length)
        self.b = (poly([]) if b is None else
                  b if isinstance(b, nmod_poly) else poly(b)).truncate(length)

    def __add__(self, other):
        return F2Series(self.a+other.a, self.b+other.b, self.length)

    def __neg__(self):
        return F2Series(-self.a, -self.b, self.length)

    def __sub__(self, other):
        return self+(-other)

    def __mul__(self, other):
        n = self.length
        return F2Series(self.a.mul_low(other.a, n)+DELTA*self.b.mul_low(other.b, n),
                        self.a.mul_low(other.b, n)+self.b.mul_low(other.a, n), n)

    def scale(self, scalar):
        a, b = scalar
        return F2Series(a*self.a+DELTA*b*self.b,
                        a*self.b+b*self.a, self.length)

    def inverse(self):
        n = self.length
        den = (self.a.mul_low(self.a, n)-DELTA*self.b.mul_low(self.b, n)).truncate(n)
        assert int(den[0]) != 0
        di = den.inverse_series_trunc(n)
        return F2Series(self.a.mul_low(di, n), -self.b.mul_low(di, n), n)

    def __truediv__(self, other):
        return self*other.inverse()

    def coeff(self, index):
        return int(self.a[index]), int(self.b[index])

    def is_zero(self):
        return self.a.is_zero() and self.b.is_zero()


def f2_mul(x, y):
    return ((x[0]*y[0]+DELTA*x[1]*y[1]) % P,
            (x[0]*y[1]+x[1]*y[0]) % P)


def f2_pow(x, n):
    if n < 0:
        norm = (x[0]*x[0]-DELTA*x[1]*x[1]) % P
        x = (x[0]*inv(norm) % P, -x[1]*inv(norm) % P)
        n = -n
    result = (1, 0)
    while n:
        if n & 1:
            result = f2_mul(result, x)
        x = f2_mul(x, x)
        n >>= 1
    return result


def miller_coordinate_series(w, u):
    length = P+3
    t = poly([0, 1])
    log = poly([0]+[int(u[(i-1)//2]) if i % 2 else 0
                    for i in range(1, length)])
    inverse_log = t
    precision = 2
    while precision < length:
        precision = min(2*precision, length)
        modulus = t**precision
        err = log.compose_mod(inverse_log, modulus)-t
        derivative = log.derivative().compose_mod(inverse_log, modulus)
        inverse_log = (inverse_log-err.mul_low(
            derivative.inverse_series_trunc(precision), precision)).truncate(precision)
    assert log.compose_mod(inverse_log, t**length) == t
    n = P+2
    zg = inverse_log.right_shift(1).truncate(n)
    w_at_z = w.truncate((n+1)//2).compose_mod(
        inverse_log.mul_low(inverse_log, n), t**n)
    zi = zg.inverse_series_trunc(n)
    xnorm = w_at_z.mul_low(zi.mul_low(zi, n), n)
    ynorm = -xnorm.mul_low(zi, n)
    assert int(xnorm[0]) == 1 and int(ynorm[0]) == P-1
    return xnorm, ynorm


def actual_weil_gamma(a, b, xnorm, ynorm, qscale=1):
    n = P+2
    h4 = F2Series(poly([a]).left_shift(4), length=n)
    point_cache = {}
    def point(scalar):
        if scalar in point_cache:
            return point_cache[scalar]
        # h^2 x(scalar*h), h^3 y(scalar*h), with their actual leading units.
        xa, xb, ya, yb = [], [], [], []
        xp, yp = f2_pow(scalar, -2), f2_pow(scalar, -3)
        for i in range(n):
            xi, yi = int(xnorm[i]), int(ynorm[i])
            xa.append(xi*xp[0] % P); xb.append(xi*xp[1] % P)
            ya.append(yi*yp[0] % P); yb.append(yi*yp[1] % P)
            xp, yp = f2_mul(xp, scalar), f2_mul(yp, scalar)
        result = F2Series(xa, xb, n), F2Series(ya, yb, n)
        # Laurent-normalized original curve equation.
        x, y = result
        original_eq = y*y-x*x*x-h4*x-F2Series(poly([b]).left_shift(6), length=n)
        assert original_eq.is_zero()
        point_cache[scalar] = result
        return result
    def multiple(base, integer):
        return (base[0]*integer % P, base[1]*integer % P)
    def function(base, evaluation):
        xq, yq = point(evaluation)
        f = F2Series([1], length=n)
        current, pole = 1, 0
        def line(i, j):
            xa, ya = point(multiple(base, i))
            if (i+j) % P == 0:
                return xq-xa, 2
            xb, yb = point(multiple(base, j))
            if i == j:
                slope = ((xa*xa).scale((3, 0))+h4)/ya.scale((2, 0))
            else:
                slope = (yb-ya)/(xb-xa)
            numerator = -yq+ya+slope*(xq-xa)
            xc, _ = point(multiple(base, i+j))
            denominator = xq-xc
            assert numerator.coeff(0) != (0, 0)
            assert denominator.coeff(0) != (0, 0)
            return numerator/denominator, 1
        for bit in bin(P)[3:]:
            factor, order = line(current, current)
            f = f*f*factor
            pole = 2*pole+order
            current *= 2
            if bit == "1":
                factor, order = line(current, 1)
                f = f*factor
                pole += order
                current += 1
        assert current == P and pole == P
        return f
    base, other = (1, 0), (0, qscale % P)
    pairing = -(function(base, other)/function(other, base))
    assert pairing.coeff(0) == (1, 0)
    assert all(pairing.coeff(i) == (0, 0) for i in range(1, P+1))
    gamma = pairing.coeff(P+1)
    assert gamma != (0, 0)
    assert f2_pow(gamma, P-1) == (P-1, 0)
    assert f2_pow(gamma, P) == ((-gamma[0]) % P, (-gamma[1]) % P)
    return gamma


def original_profile(model, roles, character_rows):
    from math import comb
    a, b = model["A"], model["B"]
    nmax = (P+1)*max(roles)//2
    w, u, p_blocks = first_lift_series(a, b, nmax)
    v, h = division_five_unit(w, a, b, nmax+1)
    iu = u.inverse_series_trunc(nmax+1)
    ad = {}
    def coefficient(d):
        if d not in ad:
            assert 0 < d < P*P and d % 2 == 0
            half = d//2
            power = iu.truncate(half+1).pow_trunc(d, half+1)
            ad[d] = int(h.truncate(half+1).mul_low(power, half+1)[half])
        return ad[d]
    assert coefficient(4) == (pow(C, 4, P)-C*C)*a*inv(15) % P
    assert coefficient(6) == (pow(C, 6, P)-C*C)*b*inv(35) % P
    xnorm, ynorm = miller_coordinate_series(w, u)
    gamma = actual_weil_gamma(a, b, xnorm, ynorm)
    gamma_twice = actual_weil_gamma(a, b, xnorm, ynorm, qscale=2)
    assert gamma_twice == (2*gamma[0] % P, 2*gamma[1] % P)
    chars = {r["R"]: r for r in character_rows}
    profiles = []
    for r in roles:
        check_budget()
        total = (P+1)*r
        bound = min(r, P-r)
        kap = chars[r]["kappa"]
        circle0 = chars[r]["circle_without_gamma"]
        gr = f2_pow(gamma, r)
        assert gr[1] == 0
        circle = circle0*gr[0] % P
        assert circle
        coeffs = [coefficient(total)*inv(total) % P]
        for i in range(1, bound+1):
            d = total-(P-1)*i
            value = ((-1)**i*coefficient(d)*comb(d-1, i-1)*inv(i)) % P
            coeffs.append(value)
            if d % P == 0:
                assert coefficient(d) == coefficient(d//P)
        # Check the exact Lucas-eliminated portion, without reading irrelevant A_d.
        for i in range(bound+1, total//(P-1)+1):
            d = total-(P-1)*i
            assert d > 0
            assert i > d or comb(d-1, i-1) % P == 0
        factor = inv(2*kap*circle)
        coeffs = [x*factor % P for x in coeffs]
        if model["j"] == 0:
            assert all(x == 0 for i, x in enumerate(coeffs) if i % 3)
        if model["j"] == 1728 % P:
            assert all(x == 0 for i, x in enumerate(coeffs) if i % 2)
        degree = max((i for i, x in enumerate(coeffs) if x), default=-1)
        profiles.append({"R": r, "coeffs": coeffs, "degree": degree,
                         "circle_leading": circle, "fine_bound": bound})
    # A separately derived paper Hurwitz recurrence in the new cuspidal source.
    # This does not consume or recompute the old p47 f_N or CM lowest functional.
    if model["j"] == 0 and a == 0 and b == 1:
        assert coefficient(P-5) == 31
    points = []
    for parameter in range(P):
        vector = []
        for profile in profiles:
            value = 0
            for coefficient_value in reversed(profile["coeffs"]):
                value = (value*parameter+coefficient_value) % P
            vector.append(value)
        points.append({"t": parameter, "vector": vector})
    return {"model": model, "gamma": list(gamma), "profiles": profiles,
            "p_block_receipt_sha256": digest(p_blocks),
            "finite_series_sha256": digest({"w": ints(w), "u": ints(u), "v": ints(v)}),
            "A_d_sha256": digest(sorted(ad.items())), "points": points}


def main():
    global STARTED, DEADLINE, nmod_poly
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != REPO:
        raise RuntimeError("This mathematical consumer runs only in the authorized public Actions")
    root = Path(__file__).resolve().parents[3]
    request_bytes = (root/REQUEST).read_bytes()
    assert hashlib.sha256(request_bytes).hexdigest() == os.environ["SERRE_EXPECTED_REQUEST_SHA256"]
    request = json.loads(request_bytes)
    assert request["execution_id"] == "p47-original-cuspidal-all-disks-v1"
    assert request["prime"] == P and request["cartan_nonsquare"] == DELTA
    assert request["smoothing_integer"] == C
    actual_hashes = {}
    for path, expected in request["source_sha256"].items():
        got = hashlib.sha256((root/path).read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError("Source or rules pin changed: "+path)
        actual_hashes[path] = got
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    assert source == os.environ["GITHUB_SHA"]
    budget = request["total_seconds"]
    reserve = request["reserve_seconds"]
    assert 0 < reserve < budget <= 600
    STARTED = time.monotonic()
    DEADLINE = STARTED+budget-reserve
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(budget)
    from flint import nmod_poly as imported_nmod_poly
    from importlib.metadata import version
    assert version("python-flint") == "0.9.0"
    nmod_poly = imported_nmod_poly
    emit("SOURCE_RECEIPT", {"source_commit": source, "execution_id": request["execution_id"],
                           "run": os.environ["GITHUB_RUN_ID"],
                           "attempt": os.environ["GITHUB_RUN_ATTEMPT"],
                           "source_sha256": actual_hashes,
                           "arithmetic_seconds": budget, "reserve_seconds": reserve})
    rows, summaries, coarse = [], [], []
    try:
        roles, char_rows = actual_characters()
        emit("CHARACTERS", {"all_actual_V": roles, "all_actual_are_good": True,
                            "character_receipt_sha256": digest(char_rows)})
        models = original_models()
        emit("MODELS", {"models": models, "ss_j_count": len({x["j"] for x in models})})
        center_1728 = None
        for model in models:
            check_budget()
            row = original_profile(model, roles, char_rows)
            rows.append(row)
            j = model["j"]
            if j == 1728 % P:
                center = tuple(row["points"][0]["vector"])
                if center_1728 is None:
                    center_1728 = center
                else:
                    assert center == center_1728
            for point in row["points"]:
                t = point["t"]
                if j == 1728 % P:
                    if t > (-t) % P:
                        continue
                    if t == 0 and model["twist"] == 1:
                        continue
                coarse.append({"j": j, "twist": model["twist"], "t": t,
                               "vector": point["vector"]})
            histogram = {}
            for point in row["points"]:
                key = tuple(point["vector"])
                histogram[key] = histogram.get(key, 0)+1
            multiplicities = {}
            for count in histogram.values():
                multiplicities[count] = multiplicities.get(count, 0)+1
            summary = {"model": model, "gamma": row["gamma"],
                       "degrees": [[x["R"], x["degree"]] for x in row["profiles"]],
                       "fine_unique_vectors": len(histogram),
                       "fine_fiber_multiplicities": multiplicities,
                       "profile_sha256": digest(row),
                       "elapsed_seconds": time.monotonic()-STARTED}
            summaries.append(summary)
            emit("MODEL_RECEIPT", summary)
        ss_count = len({x["j"] for x in models})
        assert len(coarse) == P*ss_count
        fibers = {}
        for point in coarse:
            key = tuple(point["vector"])
            fibers.setdefault(key, []).append({k: v for k, v in point.items() if k != "vector"})
        histogram = {}
        for value in fibers.values():
            histogram[len(value)] = histogram.get(len(value), 0)+1
        collisions = [value for value in fibers.values() if len(value) > 1]
        payload = {"request": request, "source_commit": source,
                   "character_rows": char_rows, "rows": rows, "coarse_points": coarse,
                   "collision_classes": collisions}
        raw = canonical(payload)+b"\n"
        target = Path(os.environ["RUNNER_TEMP"])/"serre-original-p47-cuspidal-disks.json"
        target.write_bytes(raw)
        emit("SUMMARY", {"status": "complete", "all_actual_V": roles,
                         "all_actual_are_good": True, "ss_j_count": ss_count,
                         "fine_models": len(models), "original_coarse_disks": len(coarse),
                         "unique_global_candidate_vectors": len(fibers),
                         "coarse_fiber_multiplicities": histogram,
                         "collision_class_count": len(collisions),
                         "coarse_points_sha256": digest(coarse),
                         "collision_classes_sha256": digest(collisions),
                         "payload_sha256": hashlib.sha256(raw).hexdigest(),
                         "payload_bytes": len(raw), "runner_scratch_only": True,
                         "old_scalar_window_recomputed": False,
                         "rational_point_classification_claimed": False,
                         "elapsed_seconds": time.monotonic()-STARTED})
        emit("BUDGET_RECEIPT", {"elapsed_seconds": time.monotonic()-STARTED,
                               "budget_seconds": budget, "within_budget": time.monotonic()-STARTED < budget})
        return 0
    except Exception as exc:
        emit("FAILED_RECEIPT", {"status": "error", "type": type(exc).__name__,
                               "message": str(exc), "completed_models": len(rows),
                               "completed_models_sha256": digest(rows),
                               "elapsed_seconds": time.monotonic()-STARTED,
                               "traceback": traceback.format_exc(limit=6),
                               "no_mathematical_conclusion_from_failure": True})
        return 2
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    sys.exit(main())
