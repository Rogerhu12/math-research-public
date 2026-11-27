#!/usr/bin/env python3
"""Exact full-level-47 new Fricke-positive factors and certified L'(1).
Run only in this public repository's GitHub Actions. No data artifacts.
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
REQUEST = ROOT / "topics/serre-uniformity/notes/full-p47-rank-request.json"
START = time.monotonic()
STAGE = "preflight"
COMPLETED = []

def emit(kind, **data):
    print(json.dumps({"kind": kind, "elapsed_seconds": time.monotonic()-START,
                      **data}, sort_keys=True, ensure_ascii=False), flush=True)

def timeout_handler(signum, frame):
    raise TimeoutError("Mathematical budget reached; unfinished factors unresolved.")

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True,
                          separators=(",", ":")).encode()).hexdigest()

def main():
    global STAGE
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise RuntimeError("Public GitHub Actions required.")
    if os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("Wrong repository.")
    expected = os.environ.get("SERRE_EXPECTED_REQUEST_SHA256", "")
    if len(expected) != 64 or sha(REQUEST) != expected:
        raise RuntimeError("Request SHA-256 mismatch.")
    req = json.loads(REQUEST.read_text())
    if req["prime"] != 47 or req["level"] != 2209:
        raise RuntimeError("Unexpected mathematical scope.")
    for name, wanted in req["source_sha256"].items():
        if sha(ROOT / name) != wanted:
            raise RuntimeError("Source pin mismatch: " + name)
    # The pinned Sage image has no git executable. Read the actual checkout
    # metadata from the same read-only mount; do not trust an extra caller SHA.
    gitdir = ROOT / ".git"
    if not gitdir.is_dir():
        raise RuntimeError("Expected the normal Actions checkout git directory.")
    source = (gitdir / "HEAD").read_text().strip()
    if source.startswith("ref: "):
        refname = source[5:]
        if not refname.startswith("refs/") or ".." in refname.split("/"):
            raise RuntimeError("Unexpected checkout ref.")
        loose = gitdir / refname
        if loose.exists():
            source = loose.read_text().strip()
        else:
            matches = [line.split(" ", 1)[0]
                       for line in (gitdir / "packed-refs").read_text().splitlines()
                       if line.endswith(" "+refname)]
            if len(matches) != 1:
                raise RuntimeError("Checkout ref was not uniquely resolved.")
            source = matches[0]
    if len(source) != 40 or any(c not in "0123456789abcdef" for c in source):
        raise RuntimeError("Invalid actual checkout SHA.")
    if source != os.environ.get("GITHUB_SHA"):
        raise RuntimeError("Checkout is not the run's source commit.")
    total = int(req["total_seconds"])
    reserve = int(req["reserve_seconds"])
    if total != 600 or reserve != 30:
        raise RuntimeError("Unexpected budget.")
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.setitimer(signal.ITIMER_REAL, max(0.1, total-reserve-(time.monotonic()-START)))
    emit("preflight", source=source, run=os.environ.get("GITHUB_RUN_ID"),
         attempt=os.environ.get("GITHUB_RUN_ATTEMPT"), request_sha256=expected,
         source_sha256=req["source_sha256"], mathematical_seconds=total-reserve,
         reserve_seconds=reserve)
    STAGE = "sage_import"
    from sage.all import (AA, QQ, ModularSymbols, ComplexBallField,
                          RealBallField, RealIntervalField, identity_matrix, proof)
    from sage.env import SAGE_VERSION
    if SAGE_VERSION != req["sage_version"]:
        raise RuntimeError("Unexpected Sage version: " + SAGE_VERSION)
    proof.all(True)
    p = int(req["prime"])
    level = int(req["level"])
    cutoff = int(req["coefficient_cutoff"])
    bits = int(req["ball_precision_bits"])

    # sign=1 is the star involution, NOT the Fricke sign.
    STAGE = "exact_cuspidal_new_space"
    ambient = ModularSymbols(level, 2, sign=1, base_ring=QQ)
    cusp = ambient.cuspidal_subspace()
    space = cusp.new_subspace()
    dim = int(space.dimension())
    emit("space", level=level, weight=2, star_sign=1,
         ambient_dimension=int(ambient.dimension()),
         cuspidal_dimension=int(cusp.dimension()), new_dimension=dim,
         sturm_bound=int(space.sturm_bound()))
    STAGE = "exact_fricke"
    W = space.atkin_lehner_operator(level).matrix()
    identity = identity_matrix(QQ, dim)
    if W*W != identity:
        raise ArithmeticError("Fricke is not an involution.")
    plusdim = (QQ(dim)+W.trace())/2
    if plusdim.denominator() != 1:
        raise ArithmeticError("Nonintegral Fricke eigenspace dimension.")
    plusdim = int(plusdim)
    minusdim = dim-plusdim
    emit("fricke", trace=str(W.trace()), plus_dimension=plusdim,
         minus_dimension=minusdim, involution_verified=True)
    STAGE = "exact_hecke_decomposition"
    factors = list(space.decomposition())
    if sum(int(f.dimension()) for f in factors) != dim:
        raise ArithmeticError("Incomplete Hecke decomposition.")
    selected = []
    rows = []
    for idx, factor in enumerate(factors):
        d = int(factor.dimension())
        w = factor.atkin_lehner_operator(level).matrix()
        ident = identity_matrix(QQ, d)
        if w == ident:
            sign = 1
            selected.append((idx, factor))
        elif w == -ident:
            sign = -1
        else:
            raise ArithmeticError("Fricke is not scalar on an exact simple factor.")
        rows.append({"factor": idx, "dimension": d, "fricke": sign})
    if sum(int(f.dimension()) for _, f in selected) != plusdim:
        raise ArithmeticError("Fricke-positive coverage incomplete.")
    emit("factor_decomposition", rows=rows, positive_dimension=plusdim,
         negative_dimension=minusdim, all_new_factors_covered=True)

    # E_1 is the certified Arb/acb generalized exponential integral.
    # No symbolic or mpmath numerical evaluator is used.
    STAGE = "certified_E1_weights"
    RB = RealBallField(bits)
    CB = ComplexBallField(bits)
    RI = RealIntervalField(bits)
    c = 2*RB.pi()/p
    weights = [RB(0)]
    for n in range(1, cutoff+1):
        z = CB(c*n).exp_integral_e(1)
        if not z.imag().contains_zero() or not (z.real() > 0):
            raise ArithmeticError("Invalid real E1 enclosure.")
        weights.append(2*z.real()/n)
    # Deligne: |a_n| <= d(n)sqrt(n) <= 2n, in EVERY embedding.
    # E1(cn) <= exp(-cn)/(cn), so this bounds the infinite remainder.
    tail = 4*(-c*(cutoff+1)).exp() / (
        c*(cutoff+1)*(1-(-c).exp()))
    if not tail > 0:
        raise ArithmeticError("Invalid tail enclosure.")
    emit("analytic_bound", cutoff=cutoff, precision_bits=bits,
         uniform_tail_bound=str(tail),
         formula="2*sum(a_n/n*E1(2*pi*n/47))",
         bound="4*exp(-c*(M+1))/(c*(M+1)*(1-exp(-c)))")

    totalcert = 0
    all_exact_hash = hashlib.sha256()
    all_interval_hash = hashlib.sha256()
    all_nonzero = True
    for idx, factor in selected:
        STAGE = "factor_%d_q_eigenform" % idx
        d = int(factor.dimension())
        emit("factor_start", factor=idx, dimension=d)
        form = factor.q_eigenform(cutoff+1, names="a%d" % idx)
        K = form.base_ring()
        degree = int(K.degree())
        if degree != d:
            raise ArithmeticError("Coefficient degree does not equal factor dimension.")
        coeff = [form[n] for n in range(cutoff+1)]
        if coeff[0] != 0 or coeff[1] != 1 or coeff[p] != 0:
            raise ArithmeticError("Normalization or p^2-new local relation failed.")
        if K is QQ:
            pol = ["0", "1"]
            vectors = [[QQ(a)] for a in coeff]
            embeddings = [None]
        else:
            pol = [str(a) for a in K.defining_polynomial().list()]
            vectors = [list(a.list()) for a in coeff]
            embeddings = list(K.embeddings(AA))
        if len(embeddings) != degree:
            raise ArithmeticError("All totally real coefficient embeddings required.")
        exact_data = {"factor": idx, "dimension": d, "field_polynomial": pol,
                      "q_coefficients": [[str(a) for a in v] for v in vectors]}
        qhash = digest(exact_data)
        all_exact_hash.update(qhash.encode())
        STAGE = "factor_%d_rigorous_Lprime" % idx
        intervals = []
        certified = 0
        for embidx, emb in enumerate(embeddings):
            root = RB(0) if emb is None else RB(RI(emb(K.gen())))
            val = RB(0)
            for n in range(1, cutoff+1):
                an = RB(0)
                for a in reversed(vectors[n]):
                    an = an*root+RB(a)
                val += an*weights[n]
            enclosure = val.add_error(tail)
            positive = bool(enclosure > 0)
            negative = bool(enclosure < 0)
            nonzero = positive or negative
            certified += int(nonzero)
            intervals.append({"embedding": embidx,
                              "generator_ball": str(root),
                              "Lprime_ball": str(enclosure),
                              "nonzero": nonzero, "positive": positive})
        intervalhash = digest(intervals)
        all_interval_hash.update(intervalhash.encode())
        totalcert += certified
        all_nonzero = all_nonzero and certified == degree
        item = {"factor": idx, "dimension": d, "field_polynomial": pol,
                "q_coefficients_sha256": qhash, "intervals_sha256": intervalhash,
                "certified_nonzero_embeddings": certified, "embeddings": degree,
                "intervals": intervals}
        COMPLETED.append({k: v for k, v in item.items() if k != "intervals"})
        emit("factor_certificate", **item)

    if sum(x["dimension"] for x in COMPLETED) != plusdim:
        raise ArithmeticError("Final factor coverage incomplete.")
    STAGE = "completed"
    signal.setitimer(signal.ITIMER_REAL, 0)
    emit("receipt", status="complete",
         full_positive_dimension=plusdim, factors=len(selected),
         certified_nonzero_embeddings=totalcert,
         all_Lprime_nonzero=all_nonzero,
         exact_coefficients_digest=all_exact_hash.hexdigest(),
         intervals_digest=all_interval_hash.hexdigest(),
         source=source, run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=expected,
         scope="Full new Fricke-positive level 2209, no MW saturation or point classification.")

if __name__ == "__main__":
    try:
        main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL, 0)
        emit("receipt", status="incomplete", stage=STAGE,
             exception_type=type(exc).__name__, message=str(exc),
             completed_factors=COMPLETED,
             scope="No conclusion for unfinished factors; no rational-point classification.")
        traceback.print_exc()
        sys.exit(1)
