#!/usr/bin/env python3
"""Eight actual CM tangent rows on full X_ns^+(47), in the certified 16 linear blocks.

Only the pinned public Actions request executes arithmetic.  This consumer
rebuilds the original Hodge/Hecke coordinates and the old 235-label INPUT,
then visits eight specified elliptic models.  It never repeats the full
4513 point scan or a high CM logarithm.  Extension-field calculations remain
in python-flint; only certified prime-field integers enter Sage matrices.
"""
import hashlib
import importlib.util
from importlib.metadata import version
import json
import os
from pathlib import Path
import signal
import sys
import time
import traceback

ROOT = Path(__file__).resolve().parents[3]
PRE = "topics/serre-uniformity/"
REPO = "Rogerhu12/math-research-public"
REQUEST = ROOT/(PRE+"notes/full-p47-eight-CM-tangent-request.json")
CM_REQUEST = PRE+"notes/full-p47-CM-height-move-request.json"
TRANSFER_REQUEST = PRE+"notes/original-p47-ell4513-cuspidal-transfer-request.json"
HODGE_MODULE = PRE+"scripts/full_p47_weight_one_Hodge_certificate.py"
TRANSFER_MODULE = PRE+"scripts/original_p47_ell4513_cuspidal_transfer.py"
OLD_INPUT_MODULE = PRE+"scripts/original_p47_cuspidal_disks.py"
THIS_MODULE = PRE+"scripts/full_p47_eight_CM_tangents.py"
METHOD = PRE+"notes/2026-11-27-full-p47-eight-CM-tangents-method.md"
P, Q = 47, 4513
IDS = [0, 76, 77, 100, 108, 141, 196, 220]
START = time.monotonic()
DEADLINE = None
SOURCE = None
REQUEST_HASH = None
STAGE = "preflight"
COMPLETED = []


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def emit(kind, **data):
    # Imported consumers may use elapsed_seconds.  This worker owns a distinct
    # reserved key, so a forwarded payload cannot repeat that keyword.
    if "worker_seconds" in data:
        raise ValueError("worker_seconds is owned by this emitter.")
    print(json.dumps(dict(kind=kind, worker_seconds=time.monotonic()-START,
                          **data), sort_keys=True), flush=True)


def check_budget():
    if DEADLINE is not None and time.monotonic() >= DEADLINE:
        raise TimeoutError("The declared arithmetic reserve has been reached.")


def stop(signum, frame):
    raise TimeoutError("The declared public arithmetic budget has been reached.")


def load_module(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT/relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def base_integer(value):
    """The only bridge from a flint extension to the Sage prime field."""
    if value.frobenius() != value:
        raise ArithmeticError("A descended coefficient is not in F_4513.")
    coeffs = [int(c) for c in value.to_list()]
    if not coeffs:
        return 0
    if any(coeffs[1:]):
        raise ArithmeticError("Prime-field descent has a nonconstant field coordinate.")
    return coeffs[0] % Q


def point_key(point):
    if point is None:
        return None
    return tuple(tuple(int(c) for c in value.to_list()) for value in point)


def point_count_trace(a, b):
    """One specified model, not a scan over j or its twists."""
    total = 0
    for x in range(Q):
        if x % 256 == 0:
            check_budget()
        r = (x*x*x+a*x+b) % Q
        if r:
            total += 1 if pow(r, (Q-1)//2, Q) == 1 else -1
    trace = -total
    if trace*trace > 4*Q:
        raise ArithmeticError("The specified model violated the Hasse bound.")
    return trace


def add_with_slope(curve, left, right):
    if left is None or right is None:
        raise ArithmeticError("An actual G1 addition unexpectedly involved O.")
    x, y = left
    xx, yy = right
    if x == xx:
        if y != yy or y.is_zero():
            raise ArithmeticError("An actual G1 addition met a vertical line.")
        slope = (3*x*x+curve.a)/(2*y)
    else:
        slope = (yy-y)/(xx-x)
    nx = slope*slope-x-xx
    out = curve.check((nx, slope*(x-nx)-y))
    return out, slope


def seed_eisenstein(curve, point):
    """The same KM 1,2,4,5,10,11,22,23,46 chain as the original CM source."""
    current, total, n = point, curve.field.zero(), 1
    for next_n in (2, 4, 5, 10, 11, 22, 23, 46):
        if next_n == 2*n:
            current, slope = add_with_slope(curve, current, current)
            total = 2*total+slope
        elif next_n == n+1:
            current, slope = add_with_slope(curve, current, point)
            total = total+slope
        else:
            raise ArithmeticError("Unexpected original G1 addition chain.")
        n = next_n
    if current != curve.neg(point):
        raise ArithmeticError("The actual 46-multiple is not -P.")
    return -total/curve.field(P)


def torsion_grid(curve, pp, qq, order, j_reduced):
    """All 2208 actual points and their original G1 heat derivatives."""
    ep, eq = seed_eisenstein(curve, pp), seed_eisenstein(curve, qq)
    points = {(1, 0): pp, (0, 1): qq}
    values = {(1, 0): ep, (0, 1): eq}
    for n in range(2, P):
        for axis, initial, ei in ((0, pp, ep), (1, qq, eq)):
            previous = (n-1, 0) if axis == 0 else (0, n-1)
            key = (n, 0) if axis == 0 else (0, n)
            point, slope = add_with_slope(curve, points[previous], initial)
            points[key] = point
            values[key] = values[previous]+ei+slope
    for b in range(1, P):
        check_budget()
        for a in range(1, P):
            key, previous = (a, b), (a-1, b)
            point, slope = add_with_slope(curve, points[previous], pp)
            points[key] = point
            values[key] = values[previous]+ep+slope
    if len(points) != P*P-1:
        raise ArithmeticError("The original torsion grid is incomplete.")
    inverse = {point_key(point): label for label, point in points.items()}
    if len(inverse) != P*P-1:
        raise ArithmeticError("Actual torsion labels collided.")
    jets, hasher = {}, hashlib.sha256()
    for label in sorted(points):
        point, e = points[label], values[label]
        x, y = curve.check(point)
        negative = (-label[0] % P, -label[1] % P)
        if points[negative] != curve.neg(point) or values[negative] != -e:
            raise ArithmeticError("The complete original odd G1 identity failed.")
        conjugate = inverse.get(point_key(curve.frobenius(point)))
        if conjugate is None or values[conjugate] != e.frobenius():
            raise ArithmeticError("The actual G1 source did not commute with Frobenius.")
        row = [e]
        if order >= 1:
            row.append(-x*e-y)
        if order >= 2:
            # Full R1090 heat flow at A2=0.  In deriving this, dA2=4A
            # is retained; A2 has NOT been frozen as a constant variable.
            row.append(-2*e*e*y-4*x*x*e-2*curve.a*e-2*x*y)
        jets[label] = tuple(row)
        hasher.update(canonical([list(label), point_key(point),
            [[int(c) for c in value.to_list()] for value in row]])+b"\n")
    automorphism = None
    if j_reduced == 1728 % Q:
        ii = curve.field(95)
        if ii*ii != -curve.field.one():
            raise ArithmeticError("The pinned Gaussian automorphism changed.")
        images = [(-point[0], ii*point[1]) for point in (pp, qq)]
        columns = [inverse[point_key(point)] for point in images]
        automorphism = [columns[0][0], columns[1][0],
                        columns[0][1], columns[1][1]]
        if automorphism != [0, P-1, 1, 0]:
            raise ArithmeticError("The actual Gaussian Cartan basis is misoriented.")
    elif j_reduced == 0:
        root3 = next(r for r in range(2, Q) if pow(r, 3, Q) == 1)
        rho = curve.field(root3)
        images = [(rho*point[0], point[1]) for point in (pp, qq)]
        columns = [inverse[point_key(point)] for point in images]
        automorphism = [columns[0][0], columns[1][0],
                        columns[0][1], columns[1][1]]
        a, b, c, d = automorphism
        if (a-d) % P or (b+c) % P or (
                (a*a+b*c) % P, (a*b+b*d) % P,
                (c*a+d*c) % P, (c*b+d*d) % P) == (1, 0, 0, 1):
            raise ArithmeticError("The cubic automorphism is not in the actual Cartan.")
        if (a+d) % P != P-1 or (a*d-b*c) % P != 1:
            raise ArithmeticError("The original order-three stabilizer changed.")
    return jets, {"point_count": len(points), "heat_order": order,
                  "grid_sha256": hasher.hexdigest(),
                  "stabilizer_matrix": automorphism,
                  "G1_normalization": "47e(P)=-sum of actual short-model slopes"}


def product_jet(left, right):
    result = [left[0]*right[0]]
    if len(left) >= 2:
        result.append(left[1]*right[0]+left[0]*right[1])
    if len(left) >= 3:
        result.append(left[2]*right[0]+2*left[1]*right[1]+left[0]*right[2])
    return result


def original_reynolds_jets(curve, jets, descriptors, order):
    """The complete two-phase, real/imaginary form source of R1090/R1091."""
    field = curve.field
    half = [(a, b) for a in range(P) for b in range(P)
            if (a or b) and (a, b) < (-a % P, -b % P)]
    groups = {h: [] for h in range(1, P)}
    for a, b in half:
        h = (a*a+b*b) % P
        if not h:
            raise ArithmeticError("A nonzero nonsplit vector had zero norm.")
        groups[h].append((a, b))
    if len(half) != 1104 or any(len(v) != 24 for v in groups.values()):
        raise ArithmeticError("The full46 norm fibers were not preserved.")
    requested = {}
    for index, (a, c, d) in enumerate(descriptors):
        requested.setdefault((int(c), int(d)), []).append((index, int(a)))
    zetas = [field(pow(2, h, Q)) for h in range(P)]
    output = {}
    for (c, d), rows in requested.items():
        check_budget()
        first, second = {}, {}
        for h, labels in groups.items():
            f = [field.zero() for _ in range(order+1)]
            g = [field.zero() for _ in range(order+1)]
            for a, b in labels:
                left = jets[a, b]
                right = jets[(d*a-c*b) % P, (c*a+d*b) % P]
                conjugate = jets[(d*a+c*b) % P, (-c*a+d*b) % P]
                fj, gj = product_jet(left, right), product_jet(left, conjugate)
                for i in range(order+1):
                    f[i] += 2*fj[i]
                    g[i] += 2*gj[i]
            first[h], second[h] = f, g
        for index, a in rows:
            total = [field.zero() for _ in range(order+1)]
            for h in range(1, P):
                for i in range(order+1):
                    total[i] += (zetas[(a*h) % P]*first[h][i]
                                 +zetas[(-a*h) % P]*second[h][i])
            output[index] = [base_integer(v) for v in total]
    if len(output) != len(descriptors):
        raise ArithmeticError("The complete certified descriptor set was not evaluated.")
    return [output[i] for i in range(len(descriptors))]


def necklace_tag(transfer, orbits, necklace, native_weil, roles, zeta0, beta_all):
    a, b, d, neg_a = necklace
    if not d:
        raise ArithmeticError("The nonsplit marking unexpectedly has zero lower entry.")
    inverse_d = pow(d, -1, P)
    products, cardinalities = [1]*23, [0]*23
    for orbit in orbits:
        labels = set()
        for u, w in orbit["coordinates"]:
            v1 = w*inverse_d % P
            v0 = (u-a*v1) % P
            norm = (v0*v0-5*v1*v1) % P
            if not norm:
                raise ArithmeticError("The original delta5 norm vanished.")
            labels.add(min(norm, P-norm))
        if len(labels) != 1:
            raise ArithmeticError("A Frobenius orbit crossed original norm classes.")
        h = labels.pop()
        products[h-1] = products[h-1]*orbit["product"] % Q
        cardinalities[h-1] += orbit["length"]
    if cardinalities != [P+1]*23:
        raise ArithmeticError("The original complete orbit products lost multiplicity.")
    zeta = pow(native_weil, d, Q)
    log0 = {pow(zeta0, i, Q): i for i in range(P)}
    alpha = log0[zeta]
    if not alpha:
        raise ArithmeticError("The actual Cartan Weil root is trivial.")
    logz = {pow(zeta, i, Q): i for i in range(P)}
    beta_actual = transfer.circle_values(zeta, roles, logz)
    logs = [logz[pow(value, (Q-1)//P, Q)] for value in products]
    tag = []
    for r in roles:
        kappa = (25-pow(5, 2*r, P)) % P
        if not kappa:
            raise ArithmeticError("An invisible smoothing character was introduced.")
        value = -pow(kappa, -1, P)*sum(
            pow(h, (-r) % (P-1), P)*logs[h-1] for h in range(1, 24)) % P
        frame = pow(alpha, (1-r) % (P-1), P)
        if frame*beta_actual[r] % P != beta_all[r]:
            raise ArithmeticError("The actual fixed-root character frame failed.")
        tag.append(frame*value % P)
    return tag


def normalize_i_basis(curve, pp, qq, necklace, native_weil, gaussian=False):
    """I=13J, I^2=-1; norm rescaling fixes the actual Weil root to 2."""
    if 13*13*5 % P != P-1:
        raise ArithmeticError("The delta5 to Gaussian Cartan conversion failed.")
    if gaussian:
        if point_key(pp) != ((653,), (525,)) or point_key(qq) != ((3860,), (232,)):
            # Some flint builds keep trailing zero coordinates even in degree1.
            if tuple(base_integer(x) for x in pp) != (653, 525) or tuple(
                    base_integer(x) for x in qq) != (3860, 232):
                raise ArithmeticError("The actual original Gaussian basis changed.")
        if curve.weil(pp, qq) != curve.field(2):
            raise ArithmeticError("The original Gaussian Weil root changed.")
        return pp, qq, {"norm_scaling": [1, 0], "weil_root": 2,
                       "basis_sha256": digest([point_key(pp), point_key(qq)]),
                       "pinned_Gaussian_basis": True}
    a, b, d, neg_a = necklace
    ip = curve.add(curve.mul(13*a % P, pp), curve.mul(13*d % P, qq))
    zeta = base_integer(curve.weil(pp, ip))
    if zeta != pow(native_weil, 13*d, Q):
        raise ArithmeticError("I=13J did not induce the actual Weil determinant.")
    target_norm = next(n for n in range(1, P) if pow(zeta, n, Q) == 2)
    rr, ss = next((r, s) for r in range(P) for s in range(P)
                  if (r*r+s*s) % P == target_norm)
    pnew = curve.add(curve.mul(rr, pp), curve.mul(ss, ip))
    qnew = curve.add(curve.mul(-ss, pp), curve.mul(rr, ip))
    if pnew is None or qnew is None or curve.mul(P, pnew) is not None or (
            curve.mul(P, qnew) is not None):
        raise ArithmeticError("Norm rescaling lost the original p-torsion basis.")
    if curve.weil(pnew, qnew) != curve.field(2):
        raise ArithmeticError("The real/imaginary grid has the wrong actual Weil root.")
    return pnew, qnew, {"norm_scaling": [rr, ss], "target_norm": target_norm,
                       "I_equals_13J": True, "weil_root": 2,
                       "basis_sha256": digest([point_key(pnew), point_key(qnew)])}


def select_actual_model(transfer, fq_default_ctx, cm, target, roles, zeta0, beta_all):
    """At most 25 necklaces, and the pinned Gaussian necklace only."""
    j = int(cm["j_rational"]) % Q
    gaussian = j == 1728 % Q
    if gaussian:
        a, b, trace, degree, half_order = 343, 0, 96, 1, 1
        matrix = (1, 0, 0, 1)
        # Relative to P=(653,525), Q=iP, this is J=13^{-1}I.
        necklaces = [(0, 18, 29, 0)]
        field = fq_default_ctx(Q, 1)
        curve = transfer.Curve(field, a, b)
        pp = curve.check((field(653), field(525)))
        qq = curve.check((field(3860), field(232)))
        if curve.mul(P, pp) is not None or curve.mul(P, qq) is not None:
            raise ArithmeticError("Pinned Gaussian points are not actual47-torsion.")
        native_weil = base_integer(curve.weil(pp, qq))
        if native_weil != 2:
            raise ArithmeticError("Pinned Gaussian Weil root is not 2.")
        native_receipt = {"pinned_basis": True, "P": [653, 525],
                          "Q": [3860, 232], "gaussian_i": 95}
    else:
        if j == 0:
            a, b = 0, 1
        else:
            scale = j*pow((1728-j) % Q, -1, Q) % Q
            a, b = 3*scale % Q, 2*scale % Q
        disc = (4*a*a*a+27*b*b) % Q
        if not disc or 6912*a*a*a*pow(disc, -1, Q) % Q != j:
            raise ArithmeticError("The specified short model has the wrong j.")
        trace = point_count_trace(a, b)
        if transfer.character(trace*trace-4, P) != -1:
            raise ArithmeticError("The actual CM model has no prescribed nonsplit fiber.")
        matrix, degree, half_order, necklaces = transfer.matrix_data(trace, False)
        if len(necklaces) not in (1, 25):
            raise ArithmeticError("An unintended auxiliary fiber was enumerated.")
        field = fq_default_ctx(Q, degree)
        curve = transfer.Curve(field, a, b)
        model = {"j": j, "A": a, "B": b, "twist": 0, "trace": trace,
                 "scalar": False, "contributes": True}
        pp, qq, native_weil, native_receipt = transfer.find_native_basis(
            curve, model, degree)
    if transfer.mm(tuple(necklaces[0]), tuple(necklaces[0])) != (5, 0, 0, 5):
        raise ArithmeticError("The original delta5 marking changed.")
    orbits = transfer.half_orbit_products(curve, pp, qq, matrix, half_order)
    matches = []
    tag_digest = hashlib.sha256()
    for necklace in necklaces:
        check_budget()
        tag = necklace_tag(transfer, orbits, necklace, native_weil, roles,
                           zeta0, beta_all)
        tag_digest.update(canonical([list(necklace), tag])+b"\n")
        if tag == target:
            matches.append(tuple(necklace))
    if len(matches) != 1:
        raise ArithmeticError("The original target CM tag did not select one necklace.")
    necklace = matches[0]
    pnew, qnew, basis_receipt = normalize_i_basis(
        curve, pp, qq, necklace, native_weil, gaussian=gaussian)
    return curve, pnew, qnew, {"model": {"j": j, "A": a, "B": b, "trace": trace},
        "field_degree": degree, "field_modulus": [int(c) for c in field.modulus()],
        "native_basis": native_receipt, "native_weil": native_weil,
        "tested_necklaces": len(necklaces), "matching_necklace": list(necklace),
        "fixed_root_target_tag": target, "tested_tags_sha256": tag_digest.hexdigest(),
        "orbit_products_sha256": digest(orbits), "Hodge_basis_marking": basis_receipt}


def coarse_tangent_vector(jets, a, b, j):
    """Coefficient of omega_F in the actual coarse parameter j-j_CM."""
    if j == 1728 % Q:
        if any(row[0] for row in jets):
            raise ArithmeticError("The actual Gaussian weight2 stabilizer failed.")
        denominator = (41472*a) % Q
        return [-row[1]*pow(denominator, -1, Q) % Q for row in jets], (
            "Gaussian: -deltaF/(41472*A), equivalent to A*[B]F/31104")
    if j == 0:
        if any(row[0] or row[1] for row in jets):
            raise ArithmeticError("The actual cubic weight2 stabilizer failed.")
        denominator = (331776*b) % Q
        return [row[2]*pow(denominator, -1, Q) % Q for row in jets], (
            "cubic: delta^2F/(331776*B), equivalent to B*[A^2]F/4608")
    disc = (4*a*a*a+27*b*b) % Q
    scale = disc*pow(124416*a*a*b % Q, -1, Q) % Q
    return [scale*row[0] % Q for row in jets], (
        "generic: (4*A^3+27*B^2)*F/(124416*A^2*B)")


def main():
    global SOURCE, REQUEST_HASH, STAGE, DEADLINE
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get(
            "GITHUB_REPOSITORY") != REPO:
        raise RuntimeError("Only this public repository's Actions may execute mathematics.")
    raw = REQUEST.read_bytes()
    REQUEST_HASH = hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH != os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("Request pin mismatch.")
    req = json.loads(raw)
    if (req["execution_id"] != "full-p47-eight-CM-tangents-v1" or
            req["prime"] != P or req["coefficient_prime"] != Q or
            req["total_seconds"] != 600 or req["reserve_seconds"] != 30 or
            req["sage_version"] != "10.6" or req["python_flint_version"] != "0.9.0" or
            req["CM_candidate_ids"] != IDS):
        raise RuntimeError("Unexpected finite request.")
    required = {CM_REQUEST, TRANSFER_REQUEST, HODGE_MODULE, TRANSFER_MODULE,
                OLD_INPUT_MODULE, THIS_MODULE, METHOD, "README.md", PRE+"README.md"}
    if not required.issubset(req["source_sha256"]):
        raise RuntimeError("An actual consumed source lacks an outer request pin.")
    for name, wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != wanted:
            raise RuntimeError("Source pin mismatch: "+name)
    cmreq = json.loads((ROOT/CM_REQUEST).read_bytes())
    trreq = json.loads((ROOT/TRANSFER_REQUEST).read_bytes())
    if cmreq["execution_id"] != "full-p47-CM-height-move-v1" or (
            trreq["execution_id"] != "p47-ell4513-original-complete-transfer-v1"):
        raise RuntimeError("Wrong original input requests.")
    for consumed, name in ((cmreq, HODGE_MODULE), (trreq, OLD_INPUT_MODULE),
                           (trreq, TRANSFER_MODULE)):
        if req["source_sha256"][name] != consumed["source_sha256"][name]:
            raise RuntimeError("An original direct input was silently replaced: "+name)
    hodge = load_module("eight_CM_original_Hodge", HODGE_MODULE)
    transfer = load_module("eight_CM_original_transfer", TRANSFER_MODULE)
    SOURCE = hodge.source_head()
    DEADLINE = START+570
    transfer.STARTED, transfer.DEADLINE = START, DEADLINE
    signal.signal(signal.SIGALRM, stop)
    signal.setitimer(signal.ITIMER_REAL, max(0.1, DEADLINE-time.monotonic()))
    emit("preflight", source=SOURCE, run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH, source_sha256=req["source_sha256"],
         arithmetic_seconds=600, reserve_seconds=30,
         scope="Eight actual CM tangent rows, 16 certified linear blocks; no high CM log.")
    from sage.all import matrix, vector, identity_matrix
    from flint import fq_default_ctx, nmod_poly
    if version("python-flint") != "0.9.0":
        raise RuntimeError("The extension-field arithmetic is pinned to python-flint0.9.0.")
    STAGE = "consume_original_Hodge_Hecke"
    source = hodge.build_source(descriptors=cmreq["Hodge_descriptors"],
                               expected_certificate=cmreq["Hodge_certificate"])
    bridge = hodge.hecke_bridge(source)
    for n in (2, 3, 5):
        if digest(hodge.integral_rows(bridge["operators"][n])) != cmreq[
                "original_Hecke_hashes"][str(n)]:
            raise ArithmeticError("Original Hecke matrix hash mismatch.")
    if bridge["H2_sha256"] != cmreq["original_Hecke_hashes"]["H2"]:
        raise ArithmeticError("Original H2 hash mismatch.")
    K, H2 = source["K"], bridge["H2"]
    identity = identity_matrix(K, 73)
    eigenvectors, linear_rows = [], cmreq["original_CM_linear_rows"]
    if len(linear_rows) != 16 or len({r["H2_eigenvalue"] for r in linear_rows}) != 16:
        raise ArithmeticError("The original16 linear blocks were changed.")
    for old in linear_rows:
        eig = K(old["H2_eigenvalue"])
        eigspace = (H2.transpose()-eig*identity).right_kernel()
        if eigspace.dimension() != 1:
            raise ArithmeticError("The original simple Hecke block lost dimension.")
        v = eigspace.basis()[0]
        v = v/next(c for c in v if c)
        if digest([int(c) for c in v]) != old["eigenform_coordinates_sha256"]:
            raise ArithmeticError("An original normalized eigenform hash changed.")
        if not K(old["q_inverse_log_Bq_u1728"]):
            raise ArithmeticError("A consumed original Gaussian linear log is zero.")
        eigenvectors.append(v)
    eigenmatrix = matrix(K, eigenvectors)
    emit("original_Hodge_Hecke_inputs_consumed",
         Hodge_certificate=source["certificate"],
         Hecke_hashes=cmreq["original_Hecke_hashes"],
         original_CM_linear_rows_sha256=digest(linear_rows),
         high_log_recomputed=False)
    STAGE = "consume_original_235_label_input"
    old, roles, character_rows, p_models, candidates = transfer.candidate_input(
        ROOT, trreq, nmod_poly)
    cm_rows = transfer.consume_known_cm(candidates, trreq["certified_cm_rows"])
    if sorted(r["candidate_id"] for r in cm_rows) != IDS:
        raise ArithmeticError("The certified eight CM inputs were changed.")
    zeta0 = next(z for z in range(2, Q) if pow(z, P, Q) == 1)
    log0 = {pow(zeta0, i, Q): i for i in range(P)}
    beta_all = transfer.circle_values(zeta0, list(range(2, P-2, 2)), log0)
    emit("original_235_label_input_consumed",
         input_run=trreq["certified_input_run"],
         original_character_sha256=trreq["certified_character_sha256"],
         original_coarse_points_sha256=trreq["certified_coarse_points_sha256"],
         roles=roles, eight_CM_ids=IDS, full4513_scan_repeated=False)
    # Gaussian first gives a short independently useful prefix if a later
    # extension-field stage exhausts the budget; all eight remain the request.
    cm_rows = sorted(cm_rows, key=lambda r: (r["candidate_id"] != 141, r["candidate_id"]))
    for cm in cm_rows:
        check_budget()
        identifier = cm["candidate_id"]
        STAGE = "actual_CM_%d_marking" % identifier
        target = [c*beta_all[r] % P
                  for c, r in zip(candidates[identifier]["vector"], roles)]
        curve, pp, qq, marking = select_actual_model(
            transfer, fq_default_ctx, cm, target, roles, zeta0, beta_all)
        model = marking["model"]
        order = 1 if model["j"] == 1728 % Q else (2 if model["j"] == 0 else 0)
        STAGE = "actual_CM_%d_short_heat" % identifier
        grid, grid_receipt = torsion_grid(curve, pp, qq, order, model["j"])
        jets = original_reynolds_jets(curve, grid, source["descriptors"], order)
        tangent95, formula = coarse_tangent_vector(
            jets, model["A"], model["B"], model["j"])
        tangent73 = source["kernel"]*vector(K, tangent95)
        tangent16 = eigenmatrix*tangent73
        rows = []
        for index, old in enumerate(linear_rows):
            e = tangent16[index]
            lam = K(old["q_inverse_log_Bq_u1728"])
            rows.append({"H2_eigenvalue": old["H2_eigenvalue"],
                         "coarse_tangent_e": int(e),
                         "consumed_lambda4": int(lam),
                         "tangent_over_lambda4": int(e/lam)})
        result = {"candidate_id": identifier, "j_rational": cm["j_rational"],
                  "coarse_parameter": "j-j_CM",
                  "marking": marking, "G1_grid": grid_receipt,
                  "coarse_KS_formula": formula,
                  "heat_jets95_sha256": digest(jets),
                  "coarse_tangent95_sha256": digest(tangent95),
                  "coarse_tangent73_sha256": digest([int(x) for x in tangent73]),
                  "linear_rows": rows, "linear_rows_sha256": digest(rows),
                  "no_CM_period_or_Bq_factor_deleted": True}
        COMPLETED.append(result)
        emit("actual_CM_tangent_certificate", **result)
    signal.setitimer(signal.ITIMER_REAL, 0)
    STAGE = "completed"
    if sorted(r["candidate_id"] for r in COMPLETED) != IDS:
        raise ArithmeticError("The requested eight actual CM rows are incomplete.")
    emit("receipt", status="complete", source=SOURCE, run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH, completed_CM_count=len(COMPLETED),
         completed_CM_ids=[r["candidate_id"] for r in COMPLETED],
         linear_blocks=16, result_sha256=digest(COMPLETED),
         high_CM_log_recomputed=False, complete_auxiliary_scan_repeated=False,
         scope="Actual eight-CM e_i/lambda4_i in the 16 certified linear blocks only; no local height alpha, QC zero or rational-point exclusion is inferred.")

if __name__ == "__main__":
    try:
        main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL, 0)
        emit("receipt", status="incomplete", stage=STAGE, source=SOURCE,
             run=os.environ.get("GITHUB_RUN_ID"), request_sha256=REQUEST_HASH,
             exception_type=type(exc).__name__, message=str(exc),
             completed_CM_ids=[r["candidate_id"] for r in COMPLETED],
             completed_CM_sha256=digest(COMPLETED),
             scope="Only the individually completed actual CM rows survive; no unfinished row or QC exclusion is claimed.")
        traceback.print_exc()
        sys.exit(1)
