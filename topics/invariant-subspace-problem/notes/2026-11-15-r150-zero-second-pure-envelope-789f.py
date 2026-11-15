#!/usr/bin/env python3
"""R150: exact second-page PURE upper bound in the true finite-zero chart.

Reuses only the paid small original transverse generator (not any large NF).
For the co-moving original equations, F2|plane = d^2 times
(2400*N8 - 960*N9 + 96*N10 in equation-coordinate notation).
S:170x10 is this pure coefficient map.  If C=U.T*P1*Q (rank4)
and Z spans ker(C.T), the full second connection has pure rank at most
rank(Z.T*U.T*S).  If the true first rank is r<=4, the remaining normal target has dimension7-r.
Thus at most7+k positive Smith exponents are <=2, where k is the pure bound.
No small tangent relation is assumed to lift to a complete original source.
Every reported pure annihilator is checked on all170 original rows by
S*v = P0*w + P1*Q*b, hence gives a genuine full left zero jet to order2.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import signal
import time

GENERATOR_SHA256 = "2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def require(x, message):
    if not x:
        raise AssertionError(message)

def read_paid_chart(path):
    obj = json.loads(Path(path).read_text())
    result = obj.get("result", obj)
    require(result.get("status") == "completed", "Paid first-connection input incomplete")
    charts = result.get("parameters", result).get("charts", [])
    found = [c for c in charts if c["chart"] == "zero"]
    require(len(found) == 1, "Expected exactly one paid finite-zero chart")
    c = found[0]
    require(c["P0Rank"] == 128 and c["transverseEnvelopeConnectionRank"] == 4,
            "Paid complete first-connection envelope mismatch")
    require(c["all170ExactCorrectionRowsVerified"] and c["allP0NullspaceIdentitiesVerified"],
            "Paid original first-connection identities missing")
    return c

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--generator", required=True)
    p.add_argument("--first-connection-receipt", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--remaining-seconds", type=float, default=10.0)
    a = p.parse_args()
    require(a.remaining_seconds > 0, "Positive shared time budget required")
    resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
    started = time.monotonic()
    result = {
        "format": "r150-original-zero-second-pure-envelope-v1",
        "status": "started",
        "arithmetic": "exact rational python-flint",
        "scriptSHA256": sha(__file__),
        "parameters": {
            "generatorSHA256": sha(a.generator),
            "paidFirstReceiptSHA256": sha(a.first_connection_receipt),
            "naturalParameter": "s",
            "chart": "finite zero, original s and co-moving moment translation",
            "sharedSeconds": a.remaining_seconds,
            "memoryMiB": 512,
        },
        "largeMacaulayMatrixConstructed": False,
        "oldNormalFormsRecomputed": False,
        "smallSourceRelationsAssumedToLift": False,
        "largeRecomputableDataPersisted": False,
    }
    def timeout_handler(signum, frame):
        raise TimeoutError("Shared second-pure-envelope budget exhausted")
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.setitimer(signal.ITIMER_REAL, a.remaining_seconds)
    try:
        require(result["parameters"]["generatorSHA256"] == GENERATOR_SHA256,
                "Paid original physical generator SHA mismatch")
        paid = read_paid_chart(a.first_connection_receipt)
        spec = importlib.util.spec_from_file_location("r150_paid_transverse_generator", a.generator)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        P0, P1, cols, rows, _ = m.make_projection_jets("zero")
        Q, rank0, pivcols, freecols = m.nullspace(P0)
        U, rankt, pivrows, _ = m.nullspace(P0.transpose())
        C = U.transpose() * P1 * Q
        Z, first_rank, _, _ = m.nullspace(C.transpose())
        require(rank0 == rankt == 128 and first_rank == 4 and Z.ncols() == 38,
                "Complete first-page dimensions changed")
        for key, M in (("P0", P0), ("P1", P1), ("Q", Q),
                       ("leftKernel", U), ("connecting", C)):
            require(m.matrix_hash(M) == paid["matrixSha256"][key],
                    "Paid matrix hash mismatch: " + key)

        # The finite-zero chart uses the original K without reversal.
        K = m.ORIGINAL_K
        p0 = [K[i][0] for i in range(6)]
        g2 = sum(i*j*K[i][j] for i in range(1,6) for j in range(1,6) if i+j == 4)
        require(g2 == 24, "True finite-zero g2 mismatch")
        seed = [4*g2*sum(p0[i]*p0[j] for i in range(6) for j in range(6) if i+j == k)
                for k in range(11)] + [0]*6
        require(seed == [0]*8 + [2400,-960,96] + [0]*6,
                "All17 pure second-jet seed mismatch")
        purecols = [(aa, degree-aa+2) for degree in range(4)
                    for aa in range(degree+1)]
        pureindex = {v:i for i,v in enumerate(purecols)}
        S = m.fmpq_mat(170, 10)
        for row, (eq, aa, bb) in enumerate(rows):
            S[row, pureindex[(aa,bb+2)]] = seed[eq]
        D = U.transpose() * S
        T = Z.transpose() * D
        R, pure_rank = T.rref()
        small_aug = m.join_columns(C, D)
        aug_rank = small_aug.rank()
        require(aug_rank-first_rank == pure_rank, "Second-page quotient-rank identity failed")

        V, rank_check, _, purefree = m.nullspace(T)
        require(rank_check == pure_rank, "Pure annihilator rank mismatch")
        original_aug = m.join_columns(P0, P1*Q)
        _, aug0_rank, acols, _ = m.nullspace(original_aug)
        _, augt_rank, arows, _ = m.nullspace(original_aug.transpose())
        require(aug0_rank == augt_rank == 132, "Original augmented rank mismatch")
        target = S * V
        correction = m.fmpq_mat(142, V.ncols())
        if V.ncols():
            unit = m.submatrix(original_aug, arows, acols)
            sol = unit.solve(m.submatrix(target, arows, range(V.ncols())))
            for i, c in enumerate(acols):
                for j in range(V.ncols()):
                    correction[c,j] = sol[i,j]
        require(original_aug * correction == target, "Full170 second-order left-jet corrections failed")
        require(m.matrix_zero(T*V), "Complete pure annihilator identity failed")
        _, _, rankrows, _ = m.nullspace(T.transpose())
        rankcols = m.pivot_columns(R, pure_rank)
        det = m.submatrix(T, rankrows, rankcols).det() if pure_rank else m.ONE
        require(det != 0, "Pure-envelope nonzero rank minor failed")
        order_lower = max(24, 31-pure_rank)
        result.update({
            "status": "completed",
            "firstConnectionRankOverQUpperBound": 4,
            "firstConnectionExactRankNotAssumed": True,
            "firstPageRemainingNormalDimension": "7-r1",
            "pureSecondJetSeedEquationOrder": seed,
            "pureTargetMonomials_c_d": [list(x) for x in purecols],
            "smallDimensions": {"S":[170,10], "U":[170,42], "Z":[42,38],
                                "pureConnection":[38,10], "smallAugmented":[42,17]},
            "pureConnectionEnvelopeRank": pure_rank,
            "smallAugmentedRank": aug_rank,
            "fullSecondConnectionRankConditionalUpperBound": "r2 <= 7-r1+k, k=pureConnectionEnvelopeRank",
            "numberPositiveSmithExponentsAtMostTwoUpperBound": min(14,7+pure_rank),
            "fullZeroMaximalMinorOrderLowerBound": order_lower,
            "notAFullSecondConnectionLowerBound": True,
            "pureConnectionRref": [[str(R[i,j]) for j in range(10)]
                                   for i in range(pure_rank)],
            "pureAnnihilatorFreeCoordinates": purefree,
            "pureAnnihilators": [[str(V[i,j]) for i in range(10)]
                                 for j in range(V.ncols())],
            "nonzeroEnvelopeMinor": {"rows":rankrows, "columns":rankcols,
                                    "determinant":str(det)},
            "all170ExactSecondLeftJetCorrectionRowsVerified": True,
            "allSmallPaidFirstPageHashesVerified": True,
            "all17PureSecondJetCoefficientsVerified": True,
            "matrixSHA256": {"S":m.matrix_hash(S), "pureConnection":m.matrix_hash(T),
                             "annihilators":m.matrix_hash(V),
                             "completeOriginalCorrection":m.matrix_hash(correction)},
        })
        for key in ("pureSecondJetSeedEquationOrder", "pureTargetMonomials_c_d", "smallDimensions", "pureConnectionRref", "pureAnnihilatorFreeCoordinates", "pureAnnihilators", "nonzeroEnvelopeMinor", "matrixSHA256"):
            result["parameters"][key] = result[key]
    except BaseException as exc:
        result["status"] = "incomplete"
        result["error"] = type(exc).__name__ + ": " + str(exc)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        result["elapsedSeconds"] = time.monotonic()-started
        path = Path(a.out)
        path.parent.mkdir(parents=True, exist_ok=True)
        raw = json.dumps(result, sort_keys=True, indent=2).encode("utf-8")
        require(len(raw) < 100000, "Small receipt size limit")
        temporary = path.with_name(path.name + ".tmp")
        temporary.write_bytes(raw)
        os.replace(temporary, path)
        print(json.dumps({
            "status":result["status"], "receipt":str(path),
            "receiptBytes":len(raw), "receiptSHA256":hashlib.sha256(raw).hexdigest(),
            "elapsedSeconds":result["elapsedSeconds"],
            "pureConnectionEnvelopeRank":result.get("pureConnectionEnvelopeRank"),
            "numberPositiveSmithExponentsAtMostTwoUpperBound":result.get("numberPositiveSmithExponentsAtMostTwoUpperBound"),
            "fullZeroMaximalMinorOrderLowerBound":result.get("fullZeroMaximalMinorOrderLowerBound"),
        }), flush=True)

if __name__ == "__main__":
    main()
