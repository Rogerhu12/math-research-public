#!/usr/bin/env python3
"""Actual small odd Hecke basis of full X_ns^+(47), in the original Hodge frame.

New public-CI scope: canonical coordinates of T_n, greedy 73 odd indices,
and the determinant/hash of their change of basis. No height is computed.
The importable build_basis API also supports a fixed-index, hash-pinned rebuild.
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
REQUEST = ROOT/(PRE+"notes/full-p47-small-odd-Hecke-basis-request.json")
HEIGHT_INPUT = PRE+"notes/full-p47-CM-height-move-request.json"
HODGE_MODULE = PRE+"scripts/full_p47_weight_one_Hodge_certificate.py"
HEIGHT_INPUT_HASH = "bc89913668d6b3d209719a720c7562a7914459441526b6a565fc69edbfc2b7e6"
HODGE_MODULE_HASH = "fe2e4f6b2420389b534fab0b2d1976dc6ac7cb2b1fe8ad98c07112ecd860afac"
HODD_HASH = "e0105e4915c8685dcac366c72bdad0d0c7ff2e5b0b72768d06fd5573fc31cfbf"
HODD_POLY_HASH = "990a3205813f9785f40b97a754092530d9797edaee616b2814f2382530d06b37"
PREFIXES = [256, 512, 1024, 2256]
START = time.monotonic()
SOURCE = None
REQUEST_HASH = None
STAGE = "preflight"
COMPLETED = {}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                          separators=(",", ":")).encode()).hexdigest()


def emit(kind, **data):
    print(json.dumps(dict(kind=kind, elapsed_seconds=time.monotonic()-START,
                          **data), sort_keys=True), flush=True)


def stop(signum, frame):
    raise TimeoutError("The declared mathematical reserve has been reached.")


def ci_only():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get(
            "GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("Only this public repository's Actions may execute mathematics.")


def source_head():
    gd = ROOT/".git"
    source = (gd/"HEAD").read_text().strip()
    if source.startswith("ref: "):
        ref = source[5:]
        if not ref.startswith("refs/") or ".." in ref.split("/"):
            raise RuntimeError("Unexpected checkout ref.")
        path = gd/ref
        if path.exists():
            source = path.read_text().strip()
        else:
            rows = [s.split(" ", 1)[0] for s in (gd/"packed-refs").read_text().splitlines()
                    if s.endswith(" "+ref)]
            if len(rows) != 1:
                raise RuntimeError("Ambiguous actual checkout.")
            source = rows[0]
    if len(source) != 40 or source != os.environ.get("GITHUB_SHA"):
        raise RuntimeError("Actual checkout/GITHUB_SHA mismatch.")
    return source


def validate_request(req):
    if (req["execution_id"] != "full-p47-small-odd-Hecke-basis-v1" or
        req["prime"] != 47 or req["coefficient_prime"] != 4513 or
        req["sage_version"] != "10.6" or
        req["total_seconds"] != 900 or req["reserve_seconds"] != 30 or
        req["precision_prefixes"] != PREFIXES or req["random_seed"] != 0 or
        req["height_move_request_path"] != HEIGHT_INPUT or
        req["height_move_request_sha256"] != HEIGHT_INPUT_HASH or
        req["Hodd_matrix_sha256"] != HODD_HASH or
        req["Hodd_characteristic_polynomial_sha256"] != HODD_POLY_HASH):
        raise RuntimeError("Unexpected finite small-odd-basis request.")
    for name, wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != wanted:
            raise RuntimeError("Source pin mismatch: "+name)
    if hashlib.sha256((ROOT/HEIGHT_INPUT).read_bytes()).hexdigest() != HEIGHT_INPUT_HASH:
        raise RuntimeError("Certified CM-height-move input changed.")
    if hashlib.sha256((ROOT/HODGE_MODULE).read_bytes()).hexdigest() != HODGE_MODULE_HASH:
        raise RuntimeError("Original Hodge-source module changed.")


def integral_rows(M):
    return [[int(x) for x in row] for row in M.rows()]


def evaluate_matrix(poly, H, identity):
    """Polynomial evaluation in the certified ROW-action matrix."""
    result = 0*identity
    for coefficient in reversed(poly.list()):
        result = result*H+coefficient*identity
    return result


class OrbitCoordinates:
    """One exact normalized orbit, changed to h=a3+a5 before reduction."""

    def __init__(self, factor, coefficient_prime):
        from sage.all import QQ, ZZ, PolynomialRing
        self.factor = factor
        self.dimension = int(factor.dimension())
        self.name = "alpha_%d" % self.dimension
        self.q = coefficient_prime
        self.f = None
        self.precision = 0
        self.QQ = QQ
        self.PRZ = PolynomialRing(ZZ, "X")
        self.cache = {}

    def extend(self, precision):
        from sage.all import QQ, ZZ, matrix, identity_matrix
        if precision <= self.precision:
            return
        old = self.f
        new = self.factor.q_eigenform(precision, names=self.name)
        if new.prec() < precision or new[0] != 0 or new[1] != 1:
            raise ArithmeticError("Incomplete or nonnormalized newform expansion.")
        if old is not None:
            if new.base_ring() != old.base_ring():
                raise ArithmeticError("Coefficient field changed during cached extension.")
            if any(new[n] != old[n] for n in range(self.precision)):
                raise ArithmeticError("A cached Fourier prefix changed.")
        self.f = new
        self.precision = precision
        if any(new[n] != 0 for n in range(47, precision, 47)):
            raise ArithmeticError("An exact-level 47^2 newform has a nonzero 47-multiple coefficient.")
        if old is not None:
            if self.K(new[3]+new[5]) != self.h:
                raise ArithmeticError("The canonical h=a3+a5 changed.")
            return
        self.K = new.base_ring()
        d = self.dimension
        if int(self.K.degree()) != d:
            raise ArithmeticError("The coefficient field has the wrong full orbit degree.")
        self.h = self.K(new[3]+new[5])
        self.powers = [self.h**j for j in range(d)]
        self.C = matrix(QQ, [[a[k] for k in range(d)] for a in self.powers])
        self.Cinv = self.C.inverse()
        # Exact ZZ coercion checks integrality of h's minimal polynomial.
        self.P = self.PRZ(self.h.minpoly())
        if self.P.degree() != d or not self.P.is_monic():
            raise ArithmeticError("h does not generate the full coefficient field.")
        if any(ZZ(a) != a for a in self.P.list()):
            raise ArithmeticError("Nonintegral minimal polynomial.")
        if self.C*self.Cinv != identity_matrix(QQ, d):
            raise ArithmeticError("The exact h-power coordinate change failed.")

    def coefficients(self, n):
        from sage.all import vector
        if n in self.cache:
            return self.cache[n]
        if n < 1 or n >= self.precision:
            raise ValueError("A coefficient was requested beyond the completed prefix.")
        a = self.K(self.f[n])
        original = vector(self.QQ, [a[k] for k in range(self.dimension)])
        result = original*self.Cinv
        if result*self.C != original:
            raise ArithmeticError("Exact h-coordinate reconstruction failed.")
        if any(c.denominator() % self.q == 0 for c in result):
            raise ArithmeticError("A canonical Hecke coordinate is not q-integral.")
        self.cache[n] = result
        return result


def build_basis(request, indices=None, expected_certificate=None, callback=None):
    """Build the new basis or reconstruct certified indices without searching.

    indices=None: only the fixed precision prefixes 256,512,1024,2256 are used;
    stop at the first 73 independent odd, prime-to47 coefficient rows.
    indices=<73 sorted integers>: use only precision max(indices)+1, no greedy
    search; an exact previous certificate is mandatory.

    The caller owns the time budget. This API does not change signal timers.
    All raw matrices, number fields and Fourier coefficients stay in the runner.
    """
    global STAGE
    ci_only()
    validate_request(request)
    from sage.all import (QQ, ZZ, ModularSymbols, PolynomialRing, identity_matrix,
                          matrix, vector, proof, set_random_seed)
    from sage.env import SAGE_VERSION
    if SAGE_VERSION != "10.6":
        raise RuntimeError("Wrong Sage version.")
    proof.all(True)
    set_random_seed(request["random_seed"])

    def note(kind, **payload):
        global STAGE
        STAGE = kind
        if callback is not None:
            callback(kind, **payload)

    fixed = indices is not None
    if fixed:
        indices = list(map(int, indices))
        if (len(indices) != 73 or indices != sorted(set(indices)) or
            any(n < 1 or n > 2255 or n % 2 == 0 or n % 47 == 0 for n in indices)):
            raise ValueError("A fixed rebuild requires 73 certified admissible indices.")
        if expected_certificate is None or expected_certificate.get("indices") != indices:
            raise ValueError("A fixed rebuild must pin its complete previous certificate.")

    # Rebuild only the already fixed Hodge input; no descriptor or old H search.
    STAGE = "consume_original_Hodge_source"
    old = json.loads((ROOT/HEIGHT_INPUT).read_text())
    spec = importlib.util.spec_from_file_location("original_hodge_small_odd",
                                                ROOT/HODGE_MODULE)
    hodge = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hodge)
    source = hodge.build_source(descriptors=old["Hodge_descriptors"],
                               expected_certificate=old["Hodge_certificate"])
    bridge = hodge.hecke_bridge(source)
    for n in (2, 3, 5):
        if digest(integral_rows(bridge["operators"][n])) != old["original_Hecke_hashes"][str(n)]:
            raise ArithmeticError("Original Hecke matrix hash mismatch.")
    if bridge["H2_sha256"] != old["original_Hecke_hashes"]["H2"]:
        raise ArithmeticError("Original H2 matrix hash mismatch.")
    k = source["K"]
    M2, M3, M5 = [bridge["operators"][n] for n in (2, 3, 5)]
    H = M3+M5
    identity = identity_matrix(k, 73)
    chi = H.charpoly("X")
    if digest(integral_rows(H)) != HODD_HASH or digest(
            [int(c) for c in chi.list()]) != HODD_POLY_HASH:
        raise ArithmeticError("Original Hodd input hash mismatch.")
    note("original_inputs_consumed", height_move_request_sha256=HEIGHT_INPUT_HASH,
         original_Hecke_hashes=old["original_Hecke_hashes"],
         Hodd_matrix_sha256=HODD_HASH,
         Hodd_characteristic_polynomial_sha256=HODD_POLY_HASH)

    # Exact original rational input, star sign distinguished from Fricke sign.
    STAGE = "exact_original_Fricke_input"
    ambient = ModularSymbols(2209, 2, sign=1, base_ring=QQ)
    cusp = ambient.cuspidal_subspace()
    new = cusp.new_subspace()
    if [int(A.dimension()) for A in (ambient, cusp, new)] != [189, 165, 157]:
        raise ArithmeticError("Wrong original modular-symbol dimensions.")
    factors = list(new.decomposition())
    if sum(int(A.dimension()) for A in factors) != 157:
        raise ArithmeticError("Incomplete new-space decomposition.")
    plus = []
    minus_dimension = 0
    fricke_rows = []
    for A in factors:
        d = int(A.dimension())
        w = A.atkin_lehner_operator(2209).matrix()
        one = identity_matrix(QQ, d)
        if w == one:
            plus.append(A)
            sign = 1
        elif w == -one:
            minus_dimension += d
            sign = -1
        else:
            raise ArithmeticError("Nonscalar Fricke action on a simple new factor.")
        fricke_rows.append([d, sign])
    plus.sort(key=lambda A: int(A.dimension()))
    if [int(A.dimension()) for A in plus] != [16, 24, 33] or minus_dimension != 84:
        raise ArithmeticError("Wrong complete Fricke-positive original input.")
    note("exact_original_input", new_dimension=157, Fricke_plus_dimension=73,
         Fricke_minus_dimension=minus_dimension,
         complete_factor_dimensions_and_signs=fricke_rows)
    orbits = [OrbitCoordinates(A, 4513) for A in plus]
    PR = PolynomialRing(k, "X")
    P = None
    idempotents = None
    coordinate_cache = {}
    chosen = [] if not fixed else list(indices)
    chosen_rows = []
    echelon = {}
    next_index = 1
    precisions = [max(6, indices[-1]+1)] if fixed else list(PREFIXES)

    def canonical_polynomial(n):
        if n in coordinate_cache:
            return coordinate_cache[n]
        answer = PR.zero()
        for orbit, E in zip(orbits, idempotents):
            rational = orbit.coefficients(n)
            small = PR([k(c.numerator())/k(c.denominator()) for c in rational])
            answer += E*small
        answer %= P
        coordinate_cache[n] = answer
        return answer

    for precision in precisions:
        STAGE = "new_exact_Fourier_prefix_%d" % precision
        for orbit in orbits:
            orbit.extend(precision)
            note("exact_orbit_prefix", orbit_dimension=orbit.dimension,
                 completed_precision=precision,
                 h_minpoly_sha256=digest([str(c) for c in orbit.P.list()]))
        if P is None:
            parts = [PR(orbit.P) for orbit in orbits]
            P = PR.one()
            for part in parts:
                P *= part
            if P.degree() != 73 or P != PR(chi) or digest(
                    [int(c) for c in P.list()]) != HODD_POLY_HASH:
                raise ArithmeticError("New h-coordinate polynomial disagrees with actual Hodd.")
            if P.gcd(P.derivative()).degree() != 0:
                raise ArithmeticError("The consumed canonical polynomial is not squarefree.")
            for i, first in enumerate(parts):
                for second in parts[i+1:]:
                    if first.gcd(second).degree() != 0:
                        raise ArithmeticError("Distinct original orbit factors meet modulo q.")
            idempotents = []
            for part in parts:
                other = P//part
                E = (other*other.inverse_mod(part)) % P
                if (E*E-E) % P != 0:
                    raise ArithmeticError("CRT idempotent failed.")
                idempotents.append(E)
            if sum(idempotents, PR.zero()) % P != PR.one():
                raise ArithmeticError("CRT factors do not cover the full original space.")
            for n, actual in ((1, identity), (2, M2), (3, M3), (5, M5)):
                if evaluate_matrix(canonical_polynomial(n), H, identity) != actual:
                    raise ArithmeticError("Canonical T%d coordinates fail the actual Hodge bridge." % n)
            if (canonical_polynomial(3)+canonical_polynomial(5)-PR.gen()) % P != 0:
                raise ArithmeticError("The h=a3+a5 identity failed.")
            note("new_actual_coordinate_bridge", canonical_polynomial_sha256=HODD_POLY_HASH,
                 orbit_dimensions=[16, 24, 33],
                 exact_q_integral_h_coordinates=True,
                 actual_row_matrix_checks=[1, 2, 3, 5])

        if fixed:
            chosen_rows = [vector(k, [canonical_polynomial(n)[j] for j in range(73)])
                           for n in chosen]
            break

        checked = 0
        for n in range(next_index, precision, 2):
            if n % 47 == 0:
                continue
            original = vector(k, [canonical_polynomial(n)[j] for j in range(73)])
            reduced = vector(k, original)
            for pivot in sorted(echelon):
                if reduced[pivot]:
                    reduced -= reduced[pivot]*echelon[pivot]
            pivot = next((j for j, c in enumerate(reduced) if c), None)
            checked += 1
            if pivot is not None:
                echelon[pivot] = reduced/reduced[pivot]
                chosen.append(n)
                chosen_rows.append(original)
                if len(chosen) == 73:
                    break
        next_index = precision+1
        note("new_greedy_prefix", completed_precision=precision,
             new_admissible_rows_checked=checked, selected_count=len(chosen),
             last_selected_index=(chosen[-1] if chosen else None),
             selected_indices_sha256=digest(chosen))
        if len(chosen) == 73:
            break

    if len(chosen_rows) != 73:
        raise ArithmeticError("The full proved finite source did not yield 73 independent rows.")
    Csmall = matrix(k, chosen_rows)
    determinant = Csmall.det()
    if not determinant:
        raise ArithmeticError("The selected original Hecke basis is not integral.")
    cert = {
        "prime":47, "coefficient_prime":4513, "dimension":73,
        "indices":chosen, "index_sum":sum(chosen), "maximum_index":max(chosen),
        "all_indices_odd_prime_to_47_and_4513":True,
        "coordinate_convention":"rows T_n; columns 1,Hodd,...,Hodd^72",
        "basis_coordinates_sha256":digest(integral_rows(Csmall)),
        "basis_determinant_mod4513":int(determinant),
        "Hodd_matrix_sha256":HODD_HASH,
        "Hodd_characteristic_polynomial_sha256":HODD_POLY_HASH,
        "height_move_request_sha256":HEIGHT_INPUT_HASH,
        "rational_orbit_dimensions":[16,24,33],
        "orbit_h_minpoly_sha256":[digest([str(c) for c in O.P.list()]) for O in orbits],
        "actual_row_matrix_checks":[1,2,3,5],
    }
    if fixed and cert != expected_certificate:
        raise ArithmeticError("Fixed-index reconstruction disagrees with the pinned certificate.")
    note("small_odd_basis_certificate" if not fixed else "fixed_odd_basis_consumed",
         mode="fixed_indices_no_search" if fixed else "bounded_greedy_search",
         certificate=cert, certificate_sha256=digest(cert))
    return {
        "indices":chosen, "coordinate_matrix":Csmall,
        "polynomial":P, "Hodd":H, "Hodge_operators":bridge["operators"],
        "hecke_polynomials":{n:canonical_polynomial(n) for n in (2,3,5)},
        "certificate":cert,
    }


def main():
    global SOURCE, REQUEST_HASH, STAGE
    ci_only()
    raw = REQUEST.read_bytes()
    REQUEST_HASH = hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH != os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("Request pin mismatch.")
    req = json.loads(raw)
    validate_request(req)
    SOURCE = source_head()
    signal.signal(signal.SIGALRM, stop)
    signal.setitimer(signal.ITIMER_REAL, max(0.1, 870-(time.monotonic()-START)))
    emit("preflight", source=SOURCE, run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH, source_sha256=req["source_sha256"],
         budget_seconds=900, reserve_seconds=30)

    def progress(kind, **data):
        global STAGE
        STAGE = kind
        if kind == "new_greedy_prefix":
            COMPLETED["latest_complete_prefix"] = data
        elif kind == "new_actual_coordinate_bridge":
            COMPLETED["coordinate_bridge"] = data
        elif kind == "small_odd_basis_certificate":
            COMPLETED["small_odd_basis"] = data["certificate"]
        emit(kind, **data)

    built = build_basis(req, callback=progress)
    signal.setitimer(signal.ITIMER_REAL, 0)
    STAGE = "completed"
    emit("receipt", status="complete", source=SOURCE,
         run=os.environ.get("GITHUB_RUN_ID"), request_sha256=REQUEST_HASH,
         certificate=built["certificate"], certificate_sha256=digest(built["certificate"]),
         scope="New actual small odd Hecke indices and integral coordinate certificate only. No height, CM series, rank, MW saturation or rational-point conclusion.")

if __name__ == "__main__":
    try:
        main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL, 0)
        emit("receipt", status="incomplete", source=SOURCE,
             run=os.environ.get("GITHUB_RUN_ID"), request_sha256=REQUEST_HASH,
             stage=STAGE, completed=COMPLETED,
             exception_type=type(exc).__name__, message=str(exc))
        traceback.print_exc()
        sys.exit(1)
