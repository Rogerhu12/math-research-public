#!/usr/bin/env python3
"""Original p47/ell4513 complete cuspidal transfer.

Consume R1072/R1074 by hash, with only their eight globally admissible CM
labels. Compute a new complete auxiliary image including R1083 scalar fibers.
Raw arrays stay in runner scratch; only independent coarse counts are points.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback

P = 47
ELL = 4513
DELTA = 5
C = 5
M = 23
PRE = "topics/serre-uniformity/"
REPO = "Rogerhu12/math-research-public"
REQUEST = PRE + "notes/original-p47-ell4513-cuspidal-transfer-request.json"
STARTED = None
DEADLINE = None


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def emit(kind, value):
    print(kind+"="+canonical(value).decode(), flush=True)


class MathDeadline(Exception):
    pass


def alarm_handler(signum, frame):
    raise MathDeadline("Declared public arithmetic budget reached")


def check_budget():
    if time.monotonic() >= DEADLINE:
        raise MathDeadline("Declared arithmetic reserve reached")


def inv(x, p=P):
    return pow(int(x) % p, -1, p)


def character(x, p):
    x %= p
    return 0 if x == 0 else (1 if pow(x, (p-1)//2, p) == 1 else -1)


def mm(a, b):
    return ((a[0]*b[0]+a[1]*b[2]) % P,
            (a[0]*b[1]+a[1]*b[3]) % P,
            (a[2]*b[0]+a[3]*b[2]) % P,
            (a[2]*b[1]+a[3]*b[3]) % P)


def matrix_data(trace, scalar=False):
    if scalar:
        assert abs(trace) == 96
        sign = 1 if trace == 96 else P-1
        a = (sign, 0, 0, sign)
        ai = a
    else:
        a = (0, P-1, 1, trace % P)
        ai = (trace % P, 1, P-1, 0)
    identity = (1, 0, 0, 1)
    neg_identity = (P-1, 0, 0, P-1)
    assert mm(a, ai) == identity
    current = identity
    half_order = None
    full_order = None
    for n in range(1, P+2):
        current = mm(current, a)
        if half_order is None and current in (identity, neg_identity):
            half_order = n
        if current == identity:
            full_order = n
            break
    assert full_order is not None and (P+1) % full_order == 0
    matrices = []
    for u in range(P):
        for d in range(1, P):
            if (u, d) > ((-u) % P, (-d) % P):
                continue
            b = (DELTA-u*u)*inv(d) % P
            j = (u, b, d, -u % P)
            assert mm(j, j) == (DELTA, 0, 0, DELTA)
            conjugate = mm(mm(a, j), ai)
            if conjugate == j or conjugate == tuple(-x % P for x in j):
                matrices.append(j)
    expected = 1081 if scalar else (25 if trace % P == 0 else 1)
    assert len(matrices) == expected
    return a, full_order, half_order, matrices


def all_models():
    primitive = next(g for g in range(2, ELL)
                     if all(pow(g, (ELL-1)//q, ELL) != 1 for q in (2, 3, 47)))
    legendre = [character(x, ELL) for x in range(ELL)]
    cubes = [x*x*x % ELL for x in range(ELL)]
    models = []
    for j in range(ELL):
        check_budget()
        if j == 0:
            pairs = [(0, pow(primitive, i, ELL), i) for i in range(6)]
        elif j == 1728 % ELL:
            pairs = [(pow(primitive, i, ELL), 0, i) for i in range(4)]
        else:
            k = j*inv(1728-j, ELL) % ELL
            pairs = [(3*k % ELL, 2*k % ELL, 0)]
        for a, b, twist in pairs:
            disc = (4*a**3+27*b*b) % ELL
            assert disc and 1728*4*a**3*inv(disc, ELL) % ELL == j
            trace = -sum(legendre[(cubes[x]+a*x+b) % ELL] for x in range(ELL))
            assert trace*trace <= 4*ELL
            scalar = j == 1728 % ELL and abs(trace) == 96
            contributes = scalar or character(trace*trace-4, P) == -1
            models.append({"j": j, "A": a, "B": b, "twist": twist,
                           "trace": trace, "scalar": scalar,
                           "contributes": contributes})
    assert len(models) == ELL-2+6+4
    assert len({x["j"] for x in models}) == ELL
    assert sorted(x["trace"] for x in models if x["j"] == 1728 % ELL) == [-96, -94, 94, 96]
    assert sorted(x["trace"] for x in models if x["j"] == 0) == [-133, -83, -50, 50, 83, 133]
    assert sum(x["scalar"] for x in models) == 2
    return models


def independent_coarse_count(models):
    # R1083 twisted Burnside: scalar Gaussian fiber 553, Eisenstein fiber 1.
    # Generic quadratic twists act identically on necklaces, so one is enough.
    generic = sum(25 if row["trace"] % P == 0 else 1
                  for row in models
                  if row["j"] not in (0, 1728 % ELL) and row["contributes"])
    return {"generic_affine": generic, "j0": 1, "j1728": 553,
            "cusps": M, "total": generic+1+553+M}


class Curve:
    def __init__(self, field, a, b):
        self.field = field
        self.a = field(a)
        self.b = field(b)

    def check(self, point):
        if point is not None:
            x, y = point
            assert y*y == x*x*x+self.a*x+self.b
        return point

    def neg(self, point):
        return None if point is None else (point[0], -point[1])

    def add(self, first, second):
        if first is None:
            return second
        if second is None:
            return first
        x1, y1 = first
        x2, y2 = second
        if x1 == x2:
            if y1 == -y2:
                return None
            assert y1 == y2 and not y1.is_zero()
            slope = (3*x1*x1+self.a)/(2*y1)
        else:
            slope = (y2-y1)/(x2-x1)
        x3 = slope*slope-x1-x2
        return x3, slope*(x1-x3)-y1

    def mul(self, n, point):
        if n < 0:
            return self.mul(-n, self.neg(point))
        result = None
        while n:
            if n & 1:
                result = self.add(result, point)
            point = self.add(point, point)
            n >>= 1
        return result

    def frobenius(self, point):
        return None if point is None else (point[0].frobenius(), point[1].frobenius())

    def line_step(self, first, second, evaluation):
        x1, y1 = first
        x2, y2 = second
        xq, yq = evaluation
        if x1 == x2 and y1 == -y2:
            value = xq-x1
            assert not value.is_zero()
            return value, None
        if first == second:
            slope = (3*x1*x1+self.a)/(2*y1)
        else:
            slope = (y2-y1)/(x2-x1)
        x3 = slope*slope-x1-x2
        y3 = slope*(x1-x3)-y1
        numerator = -yq+y1+slope*(xq-x1)
        denominator = xq-x3
        assert not numerator.is_zero() and not denominator.is_zero()
        return numerator/denominator, (x3, y3)

    def miller(self, base, evaluation):
        value = self.field.one()
        current = base
        for bit in bin(P)[3:]:
            line, current = self.line_step(current, current, evaluation)
            value = value*value*line
            if bit == "1":
                line, current = self.line_step(current, base, evaluation)
                value *= line
        assert current is None
        return value

    def weil(self, first, second):
        value = -self.miller(first, second)/self.miller(second, first)
        assert value**P == self.field.one() and value != self.field.one()
        assert value.frobenius() == value
        return value

    def division_five(self, point):
        x, y = self.check(point)
        x2, x3 = x*x, x*x*x
        x4, x6 = x2*x2, x3*x3
        a, b = self.a, self.b
        f = x3+a*x+b
        psi3 = 3*x4+6*a*x2+12*b*x-a*a
        core4 = x6+5*a*x4+20*b*x3-5*a*a*x2-4*a*b*x-8*b*b-a*a*a
        psi5 = 32*f*f*core4-psi3*psi3*psi3
        assert not psi5.is_zero()
        return psi5


def base_integer(value):
    assert value.frobenius() == value
    coeffs = [int(x) for x in value.to_list()]
    assert all(x == 0 for x in coeffs[1:])
    return coeffs[0] % ELL


def extension_point_count(trace, degree):
    previous, current = 2, trace
    if degree == 0:
        return 0
    for n in range(2, degree+1):
        previous, current = current, trace*current-ELL*previous
    return ELL**degree+1-current


def find_native_basis(curve, model, degree):
    order = extension_point_count(model["trace"], degree)
    cofactor = order
    valuation = 0
    while cofactor % P == 0:
        cofactor //= P
        valuation += 1
    assert valuation >= 2
    for trial in range(400):
        check_budget()
        seed = canonical({"model": model, "degree": degree, "trial": trial})
        raw = hashlib.shake_256(seed).digest(2*degree)
        x = curve.field([int.from_bytes(raw[2*i:2*i+2], "little") % ELL
                         for i in range(degree)])
        rhs = x*x*x+curve.a*x+curve.b
        if not rhs.is_square():
            continue
        y = rhs.sqrt()
        assert y*y == rhs
        point = curve.check((x, y))
        sylow = curve.mul(cofactor, point)
        if sylow is None:
            continue
        ppoint = None
        for _ in range(valuation):
            next_point = curve.mul(P, sylow)
            if next_point is None:
                ppoint = sylow
                break
            sylow = next_point
        assert ppoint is not None and curve.mul(P, ppoint) is None
        qpoint = curve.frobenius(ppoint)
        assert qpoint is not None and curve.mul(P, qpoint) is None
        assert curve.frobenius(qpoint) == curve.add(
            curve.neg(ppoint), curve.mul(model["trace"] % P, qpoint))
        zeta_field = curve.weil(ppoint, qpoint)
        assert curve.weil(ppoint, curve.mul(2, qpoint)) == zeta_field*zeta_field
        zeta = base_integer(zeta_field)
        assert zeta != 1 and pow(zeta, P, ELL) == 1
        return ppoint, qpoint, zeta, {"trials": trial+1, "group_order": str(order),
                                      "group_order_p_valuation": valuation,
                                      "point_sha256": digest([[int(v) for v in z.to_list()]
                                                             for z in ppoint])}
    raise RuntimeError("Deterministic nonzero p-torsion search exhausted; no conclusion")



def find_scalar_basis(curve, model, degree):
    assert model["scalar"] and abs(model["trace"]) == 96
    assert degree == (1 if model["trace"] == 96 else 2)
    sign = 1 if model["trace"] == 96 else -1
    order = extension_point_count(model["trace"], degree)
    cofactor, valuation = order, 0
    while cofactor % P == 0:
        cofactor //= P
        valuation += 1
    assert valuation >= 2
    ppoint, span = None, None
    for trial in range(800):
        check_budget()
        seed = canonical({"scalar_model": model, "degree": degree, "trial": trial})
        raw = hashlib.shake_256(seed).digest(2*degree)
        x = curve.field([int.from_bytes(raw[2*i:2*i+2], "little") % ELL
                         for i in range(degree)])
        rhs = x*x*x+curve.a*x+curve.b
        if not rhs.is_square():
            continue
        y = rhs.sqrt()
        sylow = curve.mul(cofactor, curve.check((x, y)))
        if sylow is None:
            continue
        candidate = None
        for _ in range(valuation):
            next_point = curve.mul(P, sylow)
            if next_point is None:
                candidate = sylow
                break
            sylow = next_point
        assert candidate is not None and curve.mul(P, candidate) is None
        assert curve.frobenius(candidate) == curve.mul(sign, candidate)
        if ppoint is None:
            ppoint = candidate
            span, current = [None], None
            for _ in range(1, P):
                current = curve.add(current, ppoint)
                span.append(current)
            assert len(span) == P
            continue
        if candidate in span:
            continue
        qpoint = candidate
        zeta_field = curve.weil(ppoint, qpoint)
        assert curve.weil(ppoint, curve.mul(2, qpoint)) == zeta_field*zeta_field
        zeta = base_integer(zeta_field)
        assert zeta != 1 and pow(zeta, P, ELL) == 1
        return ppoint, qpoint, zeta, {
            "trials": trial+1, "group_order": str(order),
            "group_order_p_valuation": valuation, "independent_scalar_basis": True,
            "basis_sha256": digest([[[int(v) for v in z.to_list()] for z in point]
                                    for point in (ppoint, qpoint)])}
    raise RuntimeError("Deterministic independent scalar basis search exhausted; no conclusion")


def half_rep(u, w):
    u, w = u % P, w % P
    if w > M or (w == 0 and u > M):
        return -u % P, -w % P
    return u, w


def half_orbit_products(curve, ppoint, qpoint, matrix, half_order):
    pp, qq = [None], [None]
    for _ in range(1, P):
        pp.append(curve.add(pp[-1], ppoint))
        qq.append(curve.add(qq[-1], qpoint))
    representatives = [(u, 0) for u in range(1, M+1)]
    representatives += [(u, w) for w in range(1, M+1) for u in range(P)]
    assert len(representatives) == (P*P-1)//2
    seen, orbits = set(), []
    for start in representatives:
        if start in seen:
            continue
        u, w = start
        point = curve.add(pp[u], qq[w])
        assert point is not None
        first_value = curve.division_five(point)
        value, product = first_value, curve.field.one()
        current = start
        coordinates = []
        while current not in seen:
            seen.add(current)
            coordinates.append(current)
            product *= value
            value = value.frobenius()
            u, w = current
            current = half_rep(matrix[0]*u+matrix[1]*w,
                               matrix[2]*u+matrix[3]*w)
        assert current == start and len(coordinates) == half_order
        assert value == first_value
        product_int = base_integer(product)
        assert product_int
        orbits.append({"representative": list(start), "length": len(coordinates),
                       "coordinates": coordinates, "product": product_int})
    assert seen == set(representatives)
    assert sum(o["length"] for o in orbits) == 1104
    return orbits


def circle_values(zeta, exponents, log_table):
    inverse_m = inv(M)
    result = {}
    values = []
    for h in range(1, M+1):
        x = pow(zeta, h, ELL)
        eta = pow(x, -2, ELL)*(1-pow(x, C, ELL))*inv(1-x, ELL) % ELL
        assert eta
        values.append(log_table[pow(eta, (ELL-1)//P, ELL)])
    for r in exponents:
        result[r] = inverse_m*sum(pow(h, (-r) % (P-1), P)*values[h-1]
                                 for h in range(1, M+1)) % P
    return result


def candidate_input(root, request, nmod_poly):
    spec = importlib.util.spec_from_file_location(
        "certified_p47_input", root/(PRE+"scripts/original_p47_cuspidal_disks.py"))
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    old.nmod_poly = nmod_poly
    old.STARTED, old.DEADLINE = STARTED, DEADLINE
    roles, character_rows = old.actual_characters()
    models = old.original_models()
    coarse = []
    for model in models:
        row = old.original_profile(model, roles, character_rows)
        for point in row["points"]:
            t = point["t"]
            if model["j"] == 1728 % P:
                if t > (-t) % P or (t == 0 and model["twist"] == 1):
                    continue
            coarse.append({"j": model["j"], "twist": model["twist"], "t": t,
                           "vector": point["vector"]})
    assert digest(character_rows) == request["certified_character_sha256"]
    assert digest(coarse) == request["certified_coarse_points_sha256"]
    assert len(coarse) == 235 and len({tuple(x["vector"]) for x in coarse}) == 235
    for index, point in enumerate(coarse):
        point["id"] = index
    return old, roles, character_rows, models, coarse


def consume_known_cm(coarse, requested_rows):
    """Consume the already certified R1074 identifiers, with original coordinates."""
    assert len(requested_rows) == 8
    rows = []
    for row in requested_rows:
        point = coarse[row["candidate_id"]]
        assert (point["j"], point["twist"], point["t"]) == (
            row["j_rational"] % P, row["twist"], row["t"])
        rows.append(dict(row))
    assert len({row["candidate_id"] for row in rows}) == 8
    return rows


def main():
    global STARTED, DEADLINE
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != REPO:
        raise RuntimeError("This consumer runs only in the authorized public Actions")
    root = Path(__file__).resolve().parents[3]
    raw_request = (root/REQUEST).read_bytes()
    assert hashlib.sha256(raw_request).hexdigest() == os.environ["SERRE_EXPECTED_REQUEST_SHA256"]
    request = json.loads(raw_request)
    assert request["execution_id"] == "p47-ell4513-original-complete-transfer-v1"
    assert (request["prime"], request["auxiliary_prime"], request["cartan_nonsquare"],
            request["smoothing_integer"]) == (P, ELL, DELTA, C)
    hashes = {}
    for path, expected in request["source_sha256"].items():
        got = hashlib.sha256((root/path).read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError("Source or rules pin changed: "+path)
        hashes[path] = got
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    assert source == os.environ["GITHUB_SHA"]
    budget, reserve = request["total_seconds"], request["reserve_seconds"]
    assert 0 < reserve < budget <= 600
    STARTED = time.monotonic()
    DEADLINE = STARTED+budget-reserve
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(budget)
    from flint import fq_default_ctx, nmod_poly
    from importlib.metadata import version
    assert version("python-flint") == "0.9.0"
    emit("SOURCE_RECEIPT", {"source_commit": source, "run": os.environ["GITHUB_RUN_ID"],
                           "attempt": os.environ["GITHUB_RUN_ATTEMPT"],
                           "execution_id": request["execution_id"], "source_sha256": hashes,
                           "arithmetic_seconds": budget, "reserve_seconds": reserve})
    model_rows, all_tags, surviving, witness = [], set(), set(), {}
    processed_models = 0
    try:
        old, roles, character_rows, p_models, candidates = candidate_input(root, request, nmod_poly)
        cm_rows = consume_known_cm(candidates, request["certified_cm_rows"])
        cm_ids = {x["candidate_id"] for x in cm_rows}
        active_candidates = [x for x in candidates if x["id"] in cm_ids]
        cm_reduction_witness = {}
        j0_id = next(x["candidate_id"] for x in cm_rows if x["j_rational"] == 0)
        emit("CERTIFIED_INPUT", {"source_run": request["certified_input_run"],
                                "coarse_points_sha256": request["certified_coarse_points_sha256"],
                                "certified_p_disk_count": len(candidates),
                                "globally_admissible_labels": len(active_candidates),
                                "actual_roles": roles, "consumed_known_cm_rows": cm_rows,
                                "global_sieve_run": request["certified_global_sieve_run"]})
        zeta0 = next(z for z in range(2, ELL) if pow(z, P, ELL) == 1)
        log0 = {pow(zeta0, i, ELL): i for i in range(P)}
        assert len(log0) == P
        exponents = list(range(2, P-2, 2))
        beta_all = circle_values(zeta0, exponents, log0)
        beta = [beta_all[r] for r in roles]
        emit("AUX_CIRCLE", {"ell": ELL, "zeta0": zeta0, "roles": roles,
                            "beta": beta, "zero_roles": [r for r in roles if beta_all[r] == 0]})
        projected = {}
        for candidate in active_candidates:
            target = tuple(c*b % P for c, b in zip(candidate["vector"], beta))
            projected.setdefault(target, []).append(candidate["id"])
        def accept(tag, location):
            tag = tuple(tag)
            all_tags.add(tag)
            identifiers = projected.get(tag, [])
            for identifier in identifiers:
                surviving.add(identifier)
                witness.setdefault(identifier, location)
            return identifiers
        contexts = {}
        models = all_models()
        coarse_count = independent_coarse_count(models)
        emit("INDEPENDENT_POINT_COUNT", coarse_count)
        j1728_tags = set()
        noncontributing = 0
        affine_rows = 0
        j0_tags = []
        for model in models:
            check_budget()
            processed_models += 1
            if not model["contributes"]:
                noncontributing += 1
                continue
            trace = model["trace"]
            matrix, degree, half_order, necklaces = matrix_data(trace, model["scalar"])
            if degree not in contexts:
                contexts[degree] = fq_default_ctx(ELL, degree)
                assert contexts[degree].degree() == degree
                assert int(contexts[degree].characteristic()) == ELL
            field = contexts[degree]
            curve = Curve(field, model["A"], model["B"])
            basis_finder = find_scalar_basis if model["scalar"] else find_native_basis
            ppoint, qpoint, zeta_native, point_receipt = basis_finder(curve, model, degree)
            orbits = half_orbit_products(curve, ppoint, qpoint, matrix, half_order)
            tags, local_survivors = set(), set()
            for necklace in necklaces:
                check_budget()
                a, b, d, _ = necklace
                inverse_d = inv(d)
                products = [1]*M
                cardinalities = [0]*M
                for orbit in orbits:
                    labels = set()
                    for u, w in orbit["coordinates"]:
                        v1 = w*inverse_d % P
                        v0 = (u-a*v1) % P
                        norm = (v0*v0-DELTA*v1*v1) % P
                        assert norm
                        labels.add(min(norm, P-norm))
                    assert len(labels) == 1
                    h = labels.pop()
                    products[h-1] = products[h-1]*orbit["product"] % ELL
                    cardinalities[h-1] += orbit["length"]
                assert cardinalities == [P+1]*M
                zeta = pow(zeta_native, d, ELL)
                alpha = log0[zeta]
                assert alpha
                logz = {pow(zeta, i, ELL): i for i in range(P)}
                actual_beta = circle_values(zeta, roles, logz)
                logs = [logz[pow(value, (ELL-1)//P, ELL)] for value in products]
                tag = []
                for r in roles:
                    kappa = (C*C-pow(C, 2*r, P)) % P
                    actual_d = -inv(kappa)*sum(
                        pow(h, (-r) % (P-1), P)*logs[h-1] for h in range(1, M+1)) % P
                    frame = pow(alpha, (1-r) % (P-1), P)
                    assert frame*actual_beta[r] % P == beta_all[r]
                    tag.append(frame*actual_d % P)
                location = {"kind": "affine", "model": model, "J": list(necklace)}
                identifiers = accept(tag, location)
                local_survivors.update(identifiers)
                for cm in cm_rows:
                    if cm["candidate_id"] in identifiers and cm["j_rational"] % ELL == model["j"]:
                        cm_reduction_witness.setdefault(cm["candidate_id"], location)
                tags.add(tuple(tag))
                if model["j"] == 1728 % ELL:
                    j1728_tags.add(tuple(tag))
                affine_rows += 1
                if model["j"] == 0:
                    assert j0_id in identifiers
                    j0_tags.append(tuple(tag))
            entry = {"model": model, "degree": degree, "half_orbit_length": half_order,
                     "necklace_representations": len(necklaces),
                     "canonical_tag_count": len(tags), "canonical_tags": sorted(tags),
                     "matched_candidate_ids": sorted(local_survivors),
                     "native_weil": zeta_native, "torsion_receipt": point_receipt,
                     "field_modulus": [int(x) for x in field.modulus()],
                     "half_orbit_products_sha256": digest(orbits)}
            model_rows.append(entry)
            if model["j"] in (0, 1728 % ELL):
                emit("SPECIAL_MODEL_RECEIPT", {k: entry[k] for k in (
                    "model", "degree", "half_orbit_length", "necklace_representations",
                    "canonical_tag_count", "matched_candidate_ids")})
            elif len(model_rows) % 100 == 0:
                emit("PROGRESS", {"contributing_models": len(model_rows),
                                  "processed_models": processed_models,
                                  "affine_representations": affine_rows,
                                  "surviving_candidates_so_far": len(surviving),
                                  "elapsed_seconds": time.monotonic()-STARTED})
        assert len(j0_tags) == 6 and len(set(j0_tags)) == 1
        cusp_rows = []
        for h in range(1, M+1):
            tag = []
            for r in roles:
                rr = 2*r % (P-1)
                assert rr != 0
                factor = M*pow(h, r, P)*inv(pow(-DELTA % P, r, P))*inv(pow(C, 2*r, P)-1)
                tag.append(factor*beta_all[rr] % P)
            location = {"kind": "cusp", "h": h}
            identifiers = accept(tag, location)
            cusp_rows.append({"h": h, "tag": tag, "matched_candidate_ids": identifiers})
        assert cm_ids == surviving, "A known original Q-CM candidate was incorrectly excluded"
        assert set(cm_reduction_witness) == cm_ids, "Missing CM tag at its actual reduced j"
        assert len(all_tags) <= coarse_count["total"]
        assert len(j1728_tags) <= 553
        full_tag_injective = len(all_tags) == coarse_count["total"]
        survivors = [{**candidates[i], "known_cm_j": [r["j_rational"] for r in cm_rows
                                                    if r["candidate_id"] == i],
                      "witness": witness[i]} for i in sorted(surviving)]
        payload = {"request": request, "source_commit": source,
                   "input_candidates_sha256": request["certified_coarse_points_sha256"],
                   "known_cm": cm_rows, "known_cm_reduction_witness": cm_reduction_witness,
                   "independent_coarse_point_count": coarse_count,
                   "zeta0": zeta0, "beta_all": beta_all,
                   "model_rows": model_rows, "cusps": cusp_rows,
                   "canonical_aux_tags": sorted(all_tags), "survivors": survivors}
        raw = canonical(payload)+b"\n"
        target = Path(os.environ["RUNNER_TEMP"])/"serre-original-p47-ell4513-cuspidal-transfer.json"
        target.write_bytes(raw)
        compact = [{"id": x["id"], "j": x["j"], "twist": x["twist"], "t": x["t"],
                    "known_cm_j": x["known_cm_j"]} for x in survivors]
        emit("SUMMARY", {"status": "complete", "certified_p_disks": len(candidates),
                         "input_global_candidates": len(active_candidates),
                         "all_models": len(models), "contributing_models": len(model_rows),
                         "noncontributing_models": noncontributing,
                         "affine_necklace_representations": affine_rows,
                         "cusp_representations": len(cusp_rows),
                         "unique_complete_auxiliary_tags": len(all_tags),
                         "independent_coarse_point_count": coarse_count,
                         "full_auxiliary_tag_map_is_injective": full_tag_injective,
                         "j1728_unique_tags": len(j1728_tags),
                         "all_cm_tags_found_at_correct_reduced_j": True,
                         "same_CM_reduction_transfer_proved": full_tag_injective,
                         "surviving_candidates": len(surviving),
                         "survivors": compact,
                         "all_survivors_are_identified_known_cm_labels": surviving == cm_ids,
                         "all_known_cm_labels_survive": True,
                         "survivors_sha256": digest(compact),
                         "canonical_aux_tags_sha256": digest(sorted(all_tags)),
                         "payload_sha256": hashlib.sha256(raw).hexdigest(),
                         "payload_bytes": len(raw), "runner_scratch_only": True,
                         "model_representations_are_not_point_counts": True,
                         "rational_point_classification_claimed": False,
                         "elapsed_seconds": time.monotonic()-STARTED})
        emit("BUDGET_RECEIPT", {"elapsed_seconds": time.monotonic()-STARTED,
                               "budget_seconds": budget, "within_budget": time.monotonic()-STARTED < budget})
        return 0
    except Exception as exc:
        emit("FAILED_RECEIPT", {"status": "error", "type": type(exc).__name__,
                               "message": str(exc), "processed_models": processed_models,
                               "completed_contributing_models": len(model_rows),
                               "completed_model_rows_sha256": digest(model_rows),
                               "elapsed_seconds": time.monotonic()-STARTED,
                               "traceback": traceback.format_exc(limit=8),
                               "no_mathematical_exclusion_claimed_from_failure": True})
        return 2
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    sys.exit(main())
