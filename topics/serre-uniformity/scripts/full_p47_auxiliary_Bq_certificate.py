#!/usr/bin/env python3
"""Exact (B) certificate for the original full X_ns^+(47), at 283 and 4513.

Execute only in the pinned public Actions request. No L-prime, angle-Gram,
integral-generator or point-sieve computation is included.
"""
import hashlib
import json
import os
from pathlib import Path
import signal
import sys
import time
import traceback

ROOT = Path(__file__).resolve().parents[3]
REQUEST = ROOT / "topics/serre-uniformity/notes/full-p47-auxiliary-Bq-request.json"
START = time.monotonic()
STAGE = "preflight"
COMPLETED = {}
PARTIAL_FACTORS = {}
SOURCE = None
REQUEST_HASH = None


def emit(kind, **data):
    print(json.dumps(dict(kind=kind, elapsed_seconds=time.monotonic()-START, **data),
                     sort_keys=True, ensure_ascii=False), flush=True)


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True,
                          separators=(",", ":")).encode()).hexdigest()


def stop(signum, frame):
    raise TimeoutError("Mathematical budget; unfinished primes remain unresolved.")


def source_head():
    gd = ROOT / ".git"
    source = (gd / "HEAD").read_text().strip()
    if source.startswith("ref: "):
        ref = source[5:]
        if not ref.startswith("refs/") or ".." in ref.split("/"):
            raise RuntimeError("Unexpected ref.")
        path = gd / ref
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


def main():
    global STAGE, SOURCE, REQUEST_HASH
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get(
            "GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("Only this public repository's Actions may execute.")
    raw = REQUEST.read_bytes()
    REQUEST_HASH = hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH != os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("Request pin mismatch.")
    req = json.loads(raw)
    for name, wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != wanted:
            raise RuntimeError("Source pin mismatch: "+name)
    SOURCE = source_head()
    if (req["prime"] != 47 or req["auxiliary_primes"] != [283, 4513]
            or req["total_seconds"] != 600 or req["reserve_seconds"] != 30
            or req["sage_version"] != "10.6"
            or req["execution_id"] != "full-p47-auxiliary-Bq-v1"):
        raise RuntimeError("Unexpected request.")
    signal.signal(signal.SIGALRM, stop)
    signal.setitimer(signal.ITIMER_REAL, max(0.1, 570-(time.monotonic()-START)))
    emit("preflight", source=SOURCE, run=os.environ.get("GITHUB_RUN_ID"),
         attempt=os.environ.get("GITHUB_RUN_ATTEMPT"), request_sha256=REQUEST_HASH,
         source_sha256=req["source_sha256"])

    from sage.all import QQ, ZZ, ModularSymbols, PolynomialRing, identity_matrix, proof
    from sage.env import SAGE_VERSION
    if SAGE_VERSION != req["sage_version"]:
        raise RuntimeError("Wrong Sage version.")
    proof.all(True)
    auxiliary = req["auxiliary_primes"]
    if any(not ZZ(q).is_prime(proof=True) or q == 47 for q in auxiliary):
        raise ArithmeticError("Bad auxiliary-prime request.")

    # Rebuild the complete original rational input, without rerunning any L value.
    # Star sign=1 is not the Fricke sign: compute the latter on every new factor.
    STAGE = "exact_full_new_Fricke_input"
    ambient = ModularSymbols(2209, 2, sign=1, base_ring=QQ)
    cusp = ambient.cuspidal_subspace()
    new = cusp.new_subspace()
    if [int(V.dimension()) for V in [ambient, cusp, new]] != [189, 165, 157]:
        raise ArithmeticError("Wrong full level-2209 rational modular-symbol input.")
    factors = list(new.decomposition())
    if sum(int(F.dimension()) for F in factors) != 157:
        raise ArithmeticError("Incomplete full new-space decomposition.")
    plus = []
    minus_dimension = 0
    fricke_rows = []
    for index, F in enumerate(factors):
        dimension = int(F.dimension())
        w = F.atkin_lehner_operator(2209).matrix()
        identity = identity_matrix(QQ, dimension)
        if w == identity:
            sign = 1
            plus.append(F)
        elif w == -identity:
            sign = -1
            minus_dimension += dimension
        else:
            raise ArithmeticError("A new factor has nonscalar Fricke action.")
        fricke_rows.append({"factor_index":index, "dimension":dimension,
                            "Fricke_sign":sign})
    plus.sort(key=lambda F:int(F.dimension()))
    if [int(F.dimension()) for F in plus] != [16, 24, 33] or minus_dimension != 84:
        raise ArithmeticError("Wrong COMPLETE original Fricke-positive space.")
    emit("exact_input", level=2209, star_sign=1, ambient_dimension=189,
         cuspidal_dimension=165, new_dimension=157, Fricke_plus_dimension=73,
         Fricke_minus_dimension=minus_dimension, factors=fricke_rows,
         completed_scope="Exact rational input only; no L-prime or old H_t rerun.")

    PR = PolynomialRing(ZZ, "X")
    for q in auxiliary:
        pieces = []
        point_count_product = ZZ.one()
        PARTIAL_FACTORS[q] = []
        for F in plus:
            dimension = int(F.dimension())
            STAGE = "T%d_factor_dimension_%d" % (q, dimension)
            operator = F.hecke_operator(q).matrix()
            if operator.nrows() != dimension or operator.ncols() != dimension:
                raise ArithmeticError("Wrong Hecke matrix dimension.")
            # Conversion to ZZ[X] is an exact integrality check, not rounding.
            polynomial = PR(operator.charpoly())
            if polynomial.degree() != dimension or not polynomial.is_monic():
                raise ArithmeticError("Wrong integral Hecke characteristic polynomial.")
            count = ZZ(polynomial(q+1))
            at_one = ZZ(polynomial(1))
            if count <= 0 or count % q != at_one % q:
                raise ArithmeticError("Exact Eichler-Shimura evaluation failed.")
            pieces.append(polynomial)
            point_count_product *= count
            row = {
                "prime":q, "newform_dimension":dimension,
                "Tq_charpoly_degree":int(polynomial.degree()),
                "integer_charpoly_sha256":digest([str(a) for a in polynomial.list()]),
                "Pq_at_1_mod_q":int(at_one % q),
                "Pq_at_q_plus_1_mod_q":int(count % q),
                "factor_point_count_sha256":digest(str(count)),
                "B_factor_holds":bool(at_one % q != 0),
            }
            PARTIAL_FACTORS[q].append(row)
            emit("factor_certificate", **row)
        STAGE = "full_B_certificate_q_%d" % q
        whole = PR.one()
        for polynomial in pieces:
            whole *= polynomial
        if len(pieces) != 3 or whole.degree() != 73 or not whole.is_monic():
            raise ArithmeticError("Incomplete 73-dimensional Tq polynomial.")
        count = ZZ(whole(q+1))
        at_one = ZZ(whole(1))
        if count != point_count_product or count <= 0 or count % q != at_one % q:
            raise ArithmeticError("Full exact point-count/product disagreement.")
        certified = {
            "prime":q, "full_original_dimension":73,
            "newform_dimensions":[16, 24, 33],
            "integer_charpoly_sha256":digest([str(a) for a in whole.list()]),
            "J_Fq_order_decimal":str(count),
            "J_Fq_order_sha256":digest(str(count)),
            "Pq_at_1_mod_q":int(at_one % q),
            "J_Fq_order_mod_q":int(count % q),
            "B_holds":bool(count % q != 0),
            "factor_certificates":list(PARTIAL_FACTORS[q]),
        }
        COMPLETED[q] = certified
        emit("full_B_certificate", **certified)
    STAGE = "completed"
    signal.setitimer(signal.ITIMER_REAL, 0)
    emit("receipt", status="complete", source=SOURCE,
         run=os.environ.get("GITHUB_RUN_ID"), request_sha256=REQUEST_HASH,
         completed_primes=sorted(COMPLETED),
         B_true_primes=[q for q in sorted(COMPLETED) if COMPLETED[q]["B_holds"]],
         B_false_primes=[q for q in sorted(COMPLETED) if not COMPLETED[q]["B_holds"]],
         unresolved_primes=[],
         completed_certificates_sha256=digest(COMPLETED),
         scope="Only exact original #J(Fq) modulo q and condition (B); no MW saturation, height unit or disk uniqueness.")


if __name__ == "__main__":
    try:
        main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL, 0)
        emit("receipt", status="incomplete", stage=STAGE, source=SOURCE,
             run=os.environ.get("GITHUB_RUN_ID"), request_sha256=REQUEST_HASH,
             exception_type=type(exc).__name__, message=str(exc),
             completed_prime_certificates=COMPLETED,
             completed_factor_certificates=PARTIAL_FACTORS,
             unresolved_primes=[q for q in [283, 4513] if q not in COMPLETED],
             scope="Completed exact certificates remain valid; no conclusion for unfinished primes.")
        traceback.print_exc()
        sys.exit(1)
