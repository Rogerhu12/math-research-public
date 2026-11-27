#!/usr/bin/env python3
"""Original Gaussian CM logarithm on full X_ns^+(47), via R1091.

All arithmetic is restricted to the pinned public Actions request.
Series and regenerated Hodge inputs remain in runner memory only.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import signal
import sys
import time
import traceback

ROOT = Path(__file__).resolve().parents[3]
PRE = "topics/serre-uniformity/"
REQUEST = ROOT / (PRE+"notes/full-p47-Gaussian-CM-log-request.json")
Q = 4513
P = 47
A = 343
N = Q
START = time.monotonic()
STAGE = "preflight"
SOURCE = None
REQUEST_HASH = None
COMPLETED = {}
DEADLINE = None


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def emit(kind, **data):
    print(json.dumps(dict(kind=kind, elapsed_seconds=time.monotonic()-START,
                         **data), sort_keys=True), flush=True)


def check_budget():
    if DEADLINE is not None and time.monotonic() >= DEADLINE:
        raise TimeoutError("Declared mathematical reserve reached.")


def stop(signum, frame):
    raise TimeoutError("Declared mathematical budget reached.")


def source_head():
    gd = ROOT/".git"
    actual = (gd/"HEAD").read_text().strip()
    if actual.startswith("ref: "):
        ref = actual[5:]
        if not ref.startswith("refs/") or ".." in ref.split("/"):
            raise RuntimeError("Unexpected checkout ref.")
        if (gd/ref).exists():
            actual = (gd/ref).read_text().strip()
        else:
            matches = [line.split(" ", 1)[0]
                       for line in (gd/"packed-refs").read_text().splitlines()
                       if line.endswith(" "+ref)]
            if len(matches) != 1:
                raise RuntimeError("Ambiguous checkout.")
            actual = matches[0]
    if len(actual) != 40 or actual != os.environ.get("GITHUB_SHA"):
        raise RuntimeError("Actual checkout/GITHUB_SHA mismatch.")
    return actual


class BaseCurve:
    """Only the actual E_0/F_4513, in short coordinates dx/(2y)."""
    def check(self, point):
        if point is not None:
            x, y = point
            if (y*y-x*x*x-A*x) % Q:
                raise ArithmeticError("Point is not on the original CM curve.")
        return point

    def neg(self, point):
        return None if point is None else (point[0], -point[1] % Q)

    def add(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        x, y = left
        xx, yy = right
        if x == xx:
            if (y+yy) % Q == 0:
                return None
            if y != yy or y == 0:
                raise ArithmeticError("Invalid doubling.")
            m = (3*x*x+A)*pow(2*y, -1, Q) % Q
        else:
            m = (yy-y)*pow(xx-x, -1, Q) % Q
        nx = (m*m-x-xx) % Q
        ny = (m*(x-nx)-y) % Q
        return self.check((nx, ny))

    def mul(self, n, point):
        out = None
        while n:
            if n & 1:
                out = self.add(out, point)
            point = self.add(point, point)
            n >>= 1
        return out

    def line(self, left, right, at):
        if left is None or right is None:
            raise ArithmeticError("Unexpected zero in Miller line.")
        x, y = left
        xx, yy = right
        xt, yt = at
        total = self.add(left, right)
        if x == xx and (y+yy) % Q == 0:
            value = (xt-x) % Q
        else:
            m = ((3*x*x+A)*pow(2*y, -1, Q) if x == xx
                 else (yy-y)*pow(xx-x, -1, Q)) % Q
            numerator = (yt-y-m*(xt-x)) % Q
            denominator = 1 if total is None else (xt-total[0]) % Q
            if not denominator:
                raise ArithmeticError("Miller evaluation met a pole.")
            value = numerator*pow(denominator, -1, Q) % Q
        if not value:
            raise ArithmeticError("Miller evaluation met a zero.")
        return value, total

    def miller(self, point, at):
        out, current = 1, point
        for bit in bin(P)[3:]:
            value, current = self.line(current, current, at)
            out = out*out*value % Q
            if bit == "1":
                value, current = self.line(current, point, at)
                out = out*value % Q
        if current is not None:
            raise ArithmeticError("Miller base did not have order 47.")
        return out

    def weil(self, left, right):
        return -self.miller(left, right)*pow(
            self.miller(right, left), -1, Q) % Q


def original_base():
    curve = BaseCurve()
    squares = {}
    for y in range(Q):
        squares.setdefault(y*y % Q, y)
    i = squares[Q-1]
    if i*i % Q != Q-1:
        raise ArithmeticError("Wrong Gaussian automorphism.")
    for x in range(Q):
        rhs = (x*x*x+A*x) % Q
        if rhs not in squares:
            continue
        point = curve.mul(2, curve.check((x, squares[rhs])))
        if point is not None:
            if curve.mul(P, point) is not None:
                raise ArithmeticError("Original scalar Frobenius input failed.")
            break
    else:
        raise ArithmeticError("No original torsion point found.")
    ipoint = curve.check((-point[0] % Q, i*point[1] % Q))
    if any(curve.mul(n, point) == ipoint for n in range(P)):
        raise ArithmeticError("Gaussian torsion basis is dependent.")
    zeta = curve.weil(point, ipoint)
    if zeta == 1 or pow(zeta, P, Q) != 1 or pow(2, P, Q) != 1:
        raise ArithmeticError("Invalid original Weil root.")
    target_norm = next(n for n in range(1, P) if pow(zeta, n, Q) == 2)
    pair = next((r, s) for r in range(P) for s in range(P)
                if (r*r+s*s) % P == target_norm)
    point = curve.add(curve.mul(pair[0], point), curve.mul(pair[1], ipoint))
    ipoint = curve.check((-point[0] % Q, i*point[1] % Q))
    if curve.weil(point, ipoint) != 2:
        raise ArithmeticError("Actual norm rescaling did not preserve the pinned Weil root.")
    if curve.mul(P, point) is not None or curve.mul(P, ipoint) is not None:
        raise ArithmeticError("Actual selected basis has wrong order.")
    emit("original_CM_basis", A=A, B=0, trace_consumed=96,
         P=list(point), Q=list(ipoint), gaussian_i=i, weil_root=2,
         initial_weil_root=zeta, norm_scaling=list(pair))
    return point, ipoint, i


class Series:
    """Explicit truncation, multiplication and Newton inverses in F_q[z]."""
    def __init__(self, ring, precision):
        self.ring = ring
        self.field = ring.base_ring()
        self.n = precision
        self.z = ring.gen()
        self.zero = ring.zero()
        self.one = ring.one()

    def mul(self, f, g):
        return f._mul_trunc_(g, self.n)

    def sq(self, f):
        return self.mul(f, f)

    def inv(self, f):
        if not f[0]:
            raise ZeroDivisionError("A required fine-family denominator is not a unit.")
        result = self.ring(1/f[0])
        known = 1
        while known < self.n:
            known = min(2*known, self.n)
            product = f._mul_trunc_(result, known)
            result = result._mul_trunc_(2-product, known)
        return result

    def div(self, f, g):
        return self.mul(f, self.inv(g))

    def flip(self, f):
        return self.ring([c if j % 2 == 0 else -c
                          for j, c in enumerate(f.list())])

    def check_point(self, point):
        x, y = point
        if self.sq(y) != (self.mul(self.sq(x), x)+A*x+self.z).truncate(self.n):
            raise ArithmeticError("Hensel/group point missed the original family.")
        return point

    def add(self, left, right, doubling=False):
        x, y = left
        xx, yy = right
        if doubling:
            if x != xx or y != yy:
                raise ArithmeticError("Wrong doubling operands.")
            slope = self.div(3*self.sq(x)+A, 2*y)
        else:
            slope = self.div(yy-y, xx-x)
        nx = (self.sq(slope)-x-xx).truncate(self.n)
        ny = (self.mul(slope, x-nx)-y).truncate(self.n)
        return (nx, ny), slope


def psi47_dual(series, x):
    """Original normalized division-polynomial recurrence and d/dx."""
    S = series
    zero, one, z = S.zero, S.one, S.z
    def add(f, g):
        return (f[0]+g[0], f[1]+g[1])
    def sub(f, g):
        return (f[0]-g[0], f[1]-g[1])
    def scale(f, a):
        return (a*f[0], a*f[1])
    def mul(f, g):
        return (S.mul(f[0], g[0]),
                (S.mul(f[1], g[0])+S.mul(f[0], g[1])).truncate(S.n))
    def sq(f):
        return mul(f, f)
    def cube(f):
        return mul(sq(f), f)
    X = (x, one)
    Z = (z, zero)
    x2, x3 = sq(X), cube(X)
    x4, x6 = sq(x2), sq(x3)
    f = add(add(x3, scale(X, A)), Z)
    four_y_four = scale(sq(f), 16)
    psi3 = sub(add(add(scale(x4, 3), scale(x2, 6*A)),
                   scale(mul(Z, X), 12)), (A*A*one, zero))
    core4 = add(x6, scale(x4, 5*A))
    core4 = add(core4, scale(mul(Z, x3), 20))
    core4 = sub(core4, scale(x2, 5*A*A))
    core4 = sub(core4, scale(mul(Z, X), 4*A))
    core4 = sub(core4, scale(sq(Z), 8))
    core4 = sub(core4, (A*A*A*one, zero))
    memo = {0:(zero, zero), 1:(one, zero), 2:(one, zero),
            3:psi3, 4:scale(core4, 2)}
    def get(n):
        if n in memo:
            return memo[n]
        if n % 2:
            m = (n-1)//2
            left = mul(get(m+2), cube(get(m)))
            right = mul(get(m-1), cube(get(m+1)))
            result = (sub(mul(four_y_four, left), right)
                      if m % 2 == 0 else sub(left, mul(four_y_four, right)))
        else:
            m = n//2
            left = mul(get(m+2), sq(get(m-1)))
            right = mul(get(m-2), sq(get(m+1)))
            result = mul(get(m), sub(left, right))
        memo[n] = result
        return result
    return get(P)


def hensel_point(ring, point):
    x = ring(point[0])
    known = 1
    while known < N:
        check_budget()
        length = min(2*known, N)
        S = Series(ring, length)
        f, derivative = psi47_dual(S, x)
        if not derivative[0]:
            raise ArithmeticError("Original 47-division root was not simple.")
        if f.truncate(known):
            raise ArithmeticError("Hensel input precision was lost.")
        x = (x-S.div(f, derivative)).truncate(length)
        known = length
    S = Series(ring, N)
    f, derivative = psi47_dual(S, x)
    if f or not derivative[0]:
        raise ArithmeticError("Complete original division polynomial failed.")
    rhs = (S.mul(S.sq(x), x)+A*x+S.z).truncate(N)
    y = ring(point[1])
    known = 1
    while known < N:
        length = min(2*known, N)
        local = Series(ring, length)
        y = ((y+local.div(rhs.truncate(length), y))/ring.base_ring()(2)).truncate(length)
        known = length
    return S.check_point((x, y))


def seed_eisenstein(S, point):
    """G1 of P from the exact chain 1,2,4,5,10,11,22,23,46."""
    current, total, n = point, S.zero, 1
    for next_n in (2, 4, 5, 10, 11, 22, 23, 46):
        if next_n == 2*n:
            current, slope = S.add(current, current, doubling=True)
            total = 2*total+slope
        elif next_n == n+1:
            current, slope = S.add(current, point)
            total = total+slope
        else:
            raise ArithmeticError("Unexpected original addition chain.")
        total = total.truncate(N)
        n = next_n
    if current != (point[0], -point[1]):
        raise ArithmeticError("The 46-multiple is not the actual negative point.")
    return -total/S.field(P)


def torsion_eisenstein_grid(ring, base_p, base_q, i):
    global STAGE
    S = Series(ring, N)
    STAGE = "original_P_Hensel"
    pp = hensel_point(ring, base_p)
    qq = S.check_point((-S.flip(pp[0]), i*S.flip(pp[1])))
    if (int(qq[0][0]), int(qq[1][0])) != base_q:
        raise ArithmeticError("Automorphism did not lift the actual second basis point.")
    ep = seed_eisenstein(S, pp)
    eq = -i*S.flip(ep)
    # Both initial G1 values are read from actual KM addition chains.
    if seed_eisenstein(S, qq) != eq:
        raise ArithmeticError("G1 normalization or Gaussian transport mismatch.")
    STAGE = "original_full_torsion_G1_grid"
    points = {(1,0):pp, (0,1):qq}
    values = {(1,0):ep, (0,1):eq}
    for n in range(2, P):
        for step, initial, einitial in ((0, pp, ep), (1, qq, eq)):
            previous_key = (n-1, 0) if step == 0 else (0, n-1)
            key = (n, 0) if step == 0 else (0, n)
            point, slope = S.add(points[previous_key], initial, doubling=(n == 2))
            points[key] = point
            values[key] = (values[previous_key]+einitial+slope).truncate(N)
    for b in range(1, P):
        check_budget()
        for a in range(1, P):
            previous_key = (a-1, b)
            key = (a, b)
            point, slope = S.add(points[previous_key], pp)
            points[key] = point
            values[key] = (values[previous_key]+ep+slope).truncate(N)
        if b % 8 == 0:
            emit("torsion_grid_progress", completed_rows=b, precision=N)
    if len(points) != P*P-1 or len(values) != P*P-1:
        raise ArithmeticError("Incomplete original torsion grid.")
    constants = set()
    hasher = hashlib.sha256()
    for key in sorted(points):
        check_budget()
        point = S.check_point(points[key])
        value = values[key]
        constants.add((int(point[0][0]), int(point[1][0])))
        negative = (-key[0] % P, -key[1] % P)
        gaussian = (-key[1] % P, key[0])
        if points[negative] != (point[0], -point[1]) or values[negative] != -value:
            raise ArithmeticError("Original -1 action failed.")
        if values[gaussian] != -i*S.flip(value):
            raise ArithmeticError("Original i action failed.")
        row = [list(key), [[int(c) for c in f.list()]
                          for f in (point[0], point[1], value)]]
        hasher.update(canonical(row)+b"\n")
    if len(constants) != P*P-1:
        raise ArithmeticError("Original grid constants are not distinct.")
    result = {"points":P*P-1, "precision":N, "weil_root":2,
              "grid_sha256":hasher.hexdigest(),
              "P_G1_sha256":digest([int(c) for c in ep.list()])}
    COMPLETED["original_grid"] = result
    emit("original_torsion_G1_certificate", **result)
    return S, values


def coefficient_weight(S):
    global STAGE
    STAGE = "original_KS_Hasse_weight"
    m = (Q-1)//2
    factorial = [1]
    for n in range(1, m+1):
        factorial.append(factorial[-1]*n % Q)
    inverse_factorial = [pow(x, -1, Q) for x in factorial]
    coeffs = [0]*(2*(2*m//3)-m+1)
    for j in range((m+1)//2, 2*m//3+1):
        k, ell = 2*m-3*j, 2*j-m
        coeffs[ell] = (factorial[m]*inverse_factorial[j]*
                       inverse_factorial[k]*inverse_factorial[ell]*pow(A, k, Q)) % Q
    H = S.ring(coeffs)
    if int(H[0]) != 96 or S.flip(H) != H:
        raise ArithmeticError("Original Hasse value/parity disagrees with R1086.")
    den = 4*A*A*A+27*S.z*S.z
    k = -3*A*S.inv(S.ring(den))
    hinv = S.inv(H)
    integrand = S.mul(k, S.sq(hinv)).truncate(Q-1)
    # No term of degree q-1 is integrated: no division by q.
    icoeffs = [0]+[int(integrand[j])*pow(j+1, -1, Q) % Q
                   for j in range(Q-1)]
    I = S.ring(icoeffs)
    if I[0] or I.derivative() != integrand or S.flip(I) != -I:
        raise ArithmeticError("Original short primitive or its full parity failed.")
    W = S.mul(k, I)/k[0]*23
    payload = {"H0":int(H[0]), "k0":int(k[0]),
               "H_degree":int(H.degree()), "precision":N,
               "H_sha256":digest([int(c) for c in H.list()]),
               "k_sha256":digest([int(c) for c in k.list()]),
               "I_sha256":digest([int(c) for c in I.list()]),
               "23kI_over_k0_sha256":digest([int(c) for c in W.list()])}
    COMPLETED["coefficient_weight"] = payload
    emit("original_CM_weight_certificate", **payload)
    return W


def original_forms_moments(S, values, descriptors, W):
    """Full Reynolds source. Descriptor rho=d+c*i; grid key is real,imag."""
    global STAGE
    output = {}
    grouped = {}
    for index, (a, c, d) in enumerate(descriptors):
        grouped.setdefault((int(c), int(d)), []).append((index, int(a)))
    by_norm = {h:[] for h in range(1, P)}
    for x in range(P):
        for y in range(P):
            if (x,y) == (0,0) or (x,y) > (-x % P, -y % P):
                continue
            norm = (x*x+y*y) % P
            if not norm:
                raise ArithmeticError("A nonzero original Cartan vector has zero norm.")
            by_norm[norm].append((x,y))
    if any(len(v) != 24 for v in by_norm.values()):
        raise ArithmeticError("Incomplete original norm fibers.")
    zetas = [S.field(pow(2, h, Q)) for h in range(P)]
    form_hash = hashlib.sha256()
    for c, d in grouped:
        check_budget()
        STAGE = "original_CM_Reynolds_rho_%d_%d" % (c,d)
        first, second = {}, {}
        for h in range(1, P):
            first[h], second[h] = S.zero, S.zero
            for x, y in by_norm[h]:
                left = values[(x,y)]
                right = values[((d*x-c*y) % P, (c*x+d*y) % P)]
                right_bar = values[((d*x+c*y) % P, (-c*x+d*y) % P)]
                first[h] += 2*S.mul(left, right)
                second[h] += 2*S.mul(left, right_bar)
        for index, a in grouped[(c,d)]:
            F = S.zero
            for h in range(1, P):
                F += zetas[(a*h) % P]*first[h]+zetas[(-a*h) % P]*second[h]
            F = F.truncate(N)
            if S.flip(F) != -F:
                raise ArithmeticError("Actual descended CM weight-two form is not odd.")
            # R1091: coefficient of z^(q-1) in F*(23*k*I/k0).
            result = int(S.mul(F, W)[Q-1])
            output[index] = result
            form_hash.update(canonical([index, [int(c) for c in F.list()]])+b"\n")
        emit("CM_form_progress", rho=[c,d], completed_forms=len(output),
             total_forms=len(descriptors))
    if len(output) != len(descriptors):
        raise ArithmeticError("Incomplete original CM moment vector.")
    moments = [output[i] for i in range(len(descriptors))]
    payload = {"moment_vector_sha256":digest(moments),
               "original_forms_sha256":form_hash.hexdigest(),
               "descriptor_sha256":digest(descriptors),
               "moment_vector_length":len(moments)}
    COMPLETED["logarithm_source"] = payload
    emit("original_CM_moment_source", **payload)
    return moments


def polynomial_action(f, M, v):
    out = v.parent().zero()
    for a in reversed(f.list()):
        out = M*out+a*v
    return out


def actual_hecke_coordinates(source, module, request):
    global STAGE
    STAGE = "actual_Hodge_Hecke_bridge"
    bridge = module.hecke_bridge(source, callback=emit)
    M = bridge["H2"]
    chi = M.charpoly("X")
    factors = sorted(list(chi.factor()),
                     key=lambda fe:(int(fe[0].degree()), tuple(int(c) for c in fe[0].list())))
    degrees = sorted(int(f.degree()) for f, e in factors)
    if any(e != 1 for f, e in factors) or degrees != request["Hecke_factor_degrees"]:
        raise ArithmeticError("Actual Hodge H2 does not have the certified R1081 factor pattern.")
    linear_roots = sorted(int(-f[0]/f[1]) for f, e in factors if f.degree() == 1)
    if linear_roots != request["Hecke_linear_roots"]:
        raise ArithmeticError("Actual Hodge H2 linear roots disagree with R1081.")
    record = {"H2_sha256":bridge["H2_sha256"],
              "characteristic_polynomial_sha256":digest([int(c) for c in chi.list()]),
              "factor_degrees":degrees, "linear_roots":linear_roots,
              "factor_coefficients_sha256":digest([[int(c) for c in f.list()] for f,e in factors]),
              "convention":"row_action_on_actual_original_differentials"}
    COMPLETED["actual_Hecke_bridge"] = record
    emit("actual_Hecke_bridge_certificate", **record)
    return M, chi, factors


def read_actual_blocks(source, M, chi, factors, moments):
    from sage.all import identity_matrix, vector
    global STAGE
    STAGE = "actual_integral_Hecke_CM_blocks"
    K = source["K"]
    values = source["kernel"]*vector(K, moments)
    all_rows, linear_rows, total = [], [], values.parent().zero()
    for f, exponent in factors:
        check_budget()
        g = chi//f
        projector = (g*g.inverse_mod(f)) % chi
        projected = polynomial_action(projector, M, values)
        if not polynomial_action(f, M, projected).is_zero():
            raise ArithmeticError("Actual block projector missed its factor.")
        total += projected
        nonzero = not projected.is_zero()
        first = next((j for j,v in enumerate(projected) if v), None)
        row = {"factor":[int(c) for c in f.list()], "degree":int(f.degree()),
               "first_log_nonzero":nonzero,
               "projected_vector_sha256":digest([int(c) for c in projected]),
               "first_nonzero_coordinate":None if first is None else
                    [first, int(projected[first])]}
        if f.degree() == 1:
            root = -f[0]/f[1]
            kernel = (M.transpose()-root*identity_matrix(K, 73)).right_kernel()
            if kernel.dimension() != 1:
                raise ArithmeticError("An actual simple linear Hodge block is not one-dimensional.")
            eigenform = kernel.basis()[0]
            leading = next(c for c in eigenform if c)
            eigenform = eigenform/leading
            if eigenform*M != root*eigenform:
                raise ArithmeticError("Original left eigenform normalization failed.")
            value = eigenform.dot_product(values)
            if bool(value) != nonzero:
                raise ArithmeticError("Linear eigenform and full CRT projector disagree.")
            linear = {"H2_eigenvalue":int(root),
                      "q_inverse_log_Bq_u1728":int(value),
                      "first_log_nonzero":bool(value),
                      "eigenform_coordinates_sha256":digest([int(c) for c in eigenform]),
                      "normalization":"first nonzero actual73-Hodge coordinate is one"}
            linear_rows.append(linear)
            emit("actual_linear_CM_block", **linear)
        all_rows.append(row)
    if total != values:
        raise ArithmeticError("The full set of original integral blocks did not sum to the logarithm.")
    payload = {"Hodge_CM_vector_sha256":digest([int(c) for c in values]),
               "full_blocks":all_rows, "linear_blocks":sorted(linear_rows,key=lambda r:r["H2_eigenvalue"]),
               "full_block_count":len(all_rows),
               "nonzero_block_count":sum(r["first_log_nonzero"] for r in all_rows),
               "linear_nonzero_count":sum(r["first_log_nonzero"] for r in linear_rows),
               "operator_retained":"Bq=q+1-Tq",
               "q":Q,"original_divisor":"u1728=23*y1728-C_infinity"}
    COMPLETED["actual_CM_blocks"] = payload
    emit("actual_full_CM_blocks", **payload)
    return payload


def main():
    global SOURCE, REQUEST_HASH, STAGE, DEADLINE
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get(
            "GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("Mathematics is restricted to this public repository's Actions.")
    raw = REQUEST.read_bytes()
    REQUEST_HASH = hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH != os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("Request pin mismatch.")
    req = json.loads(raw)
    if (req["execution_id"] != "full-p47-Gaussian-CM-log-v1" or
        req["prime"] != P or req["coefficient_prime"] != Q or
        req["short_model_A"] != A or req["precision"] != N or
        req["root_of_unity"] != 2 or req["sage_version"] != "10.6" or
        req["total_seconds"] != 1800 or req["reserve_seconds"] != 60):
        raise RuntimeError("Unexpected explicit CM request.")
    for name, wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != wanted:
            raise RuntimeError("Source pin mismatch: "+name)
    SOURCE = source_head()
    DEADLINE = START+1740
    signal.signal(signal.SIGALRM, stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,DEADLINE-time.monotonic()))
    emit("preflight",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,source_sha256=req["source_sha256"],
         consumed_Hodge_run=req["Hodge_source_run"])
    from sage.all import PolynomialRing, proof
    from sage.env import SAGE_VERSION
    if SAGE_VERSION != "10.6":
        raise RuntimeError("The CM consumer is pinned to Sage10.6.")
    proof.all(True)
    spec = importlib.util.spec_from_file_location("original_hodge",
        ROOT/(PRE+"scripts/full_p47_weight_one_Hodge_certificate.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    STAGE = "rebuild_only_certified_original_Hodge_inputs"
    source = module.build_source(descriptors=req["Hodge_descriptors"],
        expected_certificate=req["Hodge_certificate"],callback=emit)
    if not source["complete"]:
        raise ArithmeticError("Certified Hodge input was not rebuilt.")
    COMPLETED["Hodge_input_consumed"] = source["certificate"]
    M, chi, factors = actual_hecke_coordinates(source, module, req)
    STAGE = "actual_Gaussian_torsion_marking"
    pp, qq, i = original_base()
    ring = PolynomialRing(source["K"],"z")
    S, eisenstein = torsion_eisenstein_grid(ring, pp, qq, source["K"](i))
    W = coefficient_weight(S)
    moments = original_forms_moments(S,eisenstein,source["descriptors"],W)
    result = read_actual_blocks(source,M,chi,factors,moments)
    signal.setitimer(signal.ITIMER_REAL,0)
    STAGE = "completed"
    emit("receipt",status="complete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,completed=COMPLETED,
         result_sha256=digest(result),
         scope="Actual original Gaussian CM first logarithm in all integral4513 Hecke blocks, with Bq retained. No p-adic height or rational-point uniqueness claimed.")


if __name__ == "__main__":
    try:
        main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("receipt",status="incomplete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
             request_sha256=REQUEST_HASH,stage=STAGE,completed=COMPLETED,
             exception_type=type(exc).__name__,message=str(exc),
             scope="Only explicitly completed stages survive; unfinished CM targets remain open.")
        traceback.print_exc()
        sys.exit(1)
