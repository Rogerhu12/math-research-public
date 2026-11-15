#!/usr/bin/env python3
"""Exact original R150 first-connection upper bound through the transverse jet.

No large Macaulay matrix is formed.  Reconstruct the original K, J2, J3,
all eleven N coordinates and all six Gamma coordinates.  In each chart,
the co-moving linear moment change fixes the tangent plane modulo t^2.
P0,P1 have shape 170 x 135.  Q is the COMPLETE right kernel of P0.
The exact small connecting matrix is ker(P0.T).T * P1 * Q (42 x 7).
Its rank equals rank([P0,P1*Q])-rank(P0); it is an UPPER bound for
the full original 6188-source first connection, not automatically equality.

python-flint 0.9.0 API: https://python-flint.readthedocs.io/en/latest/fmpq_mat.html
Only a small JSON receipt is written.  Matrices are temporary/reconstructible.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import resource
import sys
import time

from flint import fmpq, fmpq_mat

ORIGINAL_K = [
    [0, 0, 0, 0, 5, -1],
    [0, 0, 0, -32, 5, -1],
    [0, 0, 54, -4, 5, 0],
    [0, -32, -4, -8, 0, 0],
    [5, 5, 5, 0, 0, 0],
    [-1, -1, 0, 0, 0, 0],
]
ZERO = fmpq(0)
ONE = fmpq(1)


def canonical_bytes(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"),
                      sort_keys=True).encode("utf-8")


def matrix_hash(M):
    h = hashlib.sha256()
    h.update(("%d,%d\n" % (M.nrows(), M.ncols())).encode("ascii"))
    for i in range(M.nrows()):
        h.update(("\t".join(str(M[i, j]) for j in range(M.ncols())) + "\n")
                 .encode("ascii"))
    return h.hexdigest()


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def matrix_zero(M):
    return all(not M[i, j] for i in range(M.nrows())
               for j in range(M.ncols()))


def column(values):
    return fmpq_mat(len(values), 1, list(values))


def values(M):
    require(M.ncols() == 1, "Expected column")
    return [M[i, 0] for i in range(M.nrows())]


def trace(M):
    require(M.nrows() == M.ncols(), "Expected square matrix")
    return sum((M[i, i] for i in range(M.nrows())), ZERO)


def add_vectors(*vectors):
    return [sum((v[j] for v in vectors), ZERO)
            for j in range(len(vectors[0]))]


def scale_vector(v, c):
    return [c * x for x in v]


def hankel(v):
    require(len(v) == 11, "Hankel sequence length")
    return fmpq_mat([[v[i + j] for j in range(6)] for i in range(6)])


def sequence(j, coefficient=1):
    v = [ZERO] * 11
    if 0 <= j <= 10:
        v[j] = fmpq(coefficient)
    return v


def shifted_jet(j):
    # m_i(t)=sum_k binom(i,k)t^(i-k)n_k, so n_j -> H_j+t(j+1)H_(j+1).
    return sequence(j), sequence(j + 1, j + 1)


def polynomial_power_kernel(K, power):
    base = {(i, j): int(K[i, j])
            for i in range(6) for j in range(6) if K[i, j]}
    out = {(0, 0): 1}
    for _ in range(power):
        nxt = {}
        for (i, j), a in out.items():
            for (k, l), b in base.items():
                key = (i + k, j + l)
                nxt[key] = nxt.get(key, 0) + a * b
        out = {key: a for key, a in nxt.items() if a}
    size = 5 * power + 1
    return fmpq_mat([[out.get((i, j), 0) for j in range(size)]
                     for i in range(size)])


def pivot_columns(R, rank):
    out = []
    for i in range(rank):
        j = next((j for j in range(R.ncols()) if R[i, j]), None)
        require(j is not None and R[i, j] == 1, "RREF pivot invalid")
        out.append(j)
    require(out == sorted(set(out)), "RREF pivot order invalid")
    return out


def nullspace(M):
    R, rank = M.rref()
    piv = pivot_columns(R, rank)
    free = [j for j in range(M.ncols()) if j not in set(piv)]
    Q = fmpq_mat(M.ncols(), len(free))
    for k, f in enumerate(free):
        Q[f, k] = 1
        for i, p in enumerate(piv):
            Q[p, k] = -R[i, f]
    require(matrix_zero(M * Q), "Full exact nullspace identity failed")
    for k, f in enumerate(free):
        for l, g in enumerate(free):
            require(Q[g, k] == (1 if k == l else 0),
                    "Nullspace free-coordinate normalization failed")
    return Q, rank, piv, free


def submatrix(M, rows, cols):
    return fmpq_mat([[M[i, j] for j in cols] for i in rows])


def join_columns(A, B):
    require(A.nrows() == B.nrows(), "Join row mismatch")
    return fmpq_mat([[A[i, j] for j in range(A.ncols())]
                     + [B[i, j] for j in range(B.ncols())]
                    for i in range(A.nrows())])


def original_jet_evaluator(K):
    J2 = polynomial_power_kernel(K, 2)
    J3 = polynomial_power_kernel(K, 3)
    J3inv = J3.inv()
    identity16 = fmpq_mat([[int(i == j) for j in range(16)] for i in range(16)])
    require(J3inv * J3 == identity16, "Original J3 inverse identity failed")
    require(J2.det() != 0, "Original J2 unexpectedly singular")
    p0 = [K[i, 0] for i in range(6)]
    p1 = [K[i, 1] for i in range(6)]
    B0 = fmpq_mat([[p0[i-j] if 0 <= i-j < 6 else 0
                    for j in range(11)] for i in range(16)])
    B1 = fmpq_mat([[p1[i-j] if 0 <= i-j < 6 else 0
                    for j in range(11)] for i in range(16)])
    map0, map1 = J3inv * B0 * J2, J3inv * B1 * J2
    y0, y1 = [ONE] + [ZERO] * 5, [ZERO, ONE] + [ZERO] * 4

    def lp(l, p):
        return fmpq_mat([[sum((l[i+j+k] * p[k] for k in range(6)), ZERO)
                           for j in range(6)] for i in range(6)])

    def tensor_contract(l, Q):
        return [sum((l[i+j+k] * Q[j, k]
                     for j in range(6) for k in range(6)), ZERO)
                for i in range(6)]

    def polar(N):
        Q = K * N * K
        return [sum((Q[i, j] for i in range(6) for j in range(6)
                     if i+j == degree), ZERO)
                for degree in range(11)]

    def evaluate(m0, m1):
        M0, M1 = hankel(m0), hankel(m1)
        l0 = values(map0 * column(m0))
        l1 = values(map1 * column(m0) + map0 * column(m1))
        MKM0 = M0 * K * M0
        MKM1 = M1 * K * M0 + M0 * K * M1
        N0 = 4 * MKM0 + 6 * lp(l0, p0)
        N1 = 4 * MKM1 + 6 * (lp(l1, p0) + lp(l0, p1))
        KM0, KM1 = K * M0, K * M1
        tau0, tau1 = trace(KM0 * KM0), 2 * trace(KM0 * KM1)
        gamma0 = add_vectors(
            scale_vector(y0, 2*tau0),
            scale_vector(values(MKM0 * column(p0)), 8),
            scale_vector(tensor_contract(l0, K*M0*K), -12))
        gamma1 = add_vectors(
            scale_vector(y0, 2*tau1), scale_vector(y1, 2*tau0),
            scale_vector(values(MKM1*column(p0) + MKM0*column(p1)), 8),
            scale_vector(tensor_contract(l1, K*M0*K), -12),
            scale_vector(tensor_contract(l0, K*M1*K), -12))
        return [polar(N0) + gamma0, polar(N1) + gamma1]

    return evaluate, {"J2": matrix_hash(J2), "J3": matrix_hash(J3),
                      "L_y0": matrix_hash(map0), "L_y1": matrix_hash(map1)}


def jet_add(A, B, factor=1):
    return [[A[k][i] + factor*B[k][i] for i in range(17)] for k in range(2)]


def make_projection_jets(chart):
    raw = ORIGINAL_K if chart == "zero" else [
        [ORIGINAL_K[5-i][5-j] for j in range(6)] for i in range(6)]
    K = fmpq_mat(raw)
    evaluate, original_hashes = original_jet_evaluator(K)
    tan = [shifted_jet(0), shifted_jet(1)]
    plane_cases = [
        tan[0], tan[1],
        tuple(scale_vector(v, -1) for v in tan[0]),
        tuple(scale_vector(v, -1) for v in tan[1]),
        tuple(add_vectors(tan[0][k], tan[1][k]) for k in range(2)),
    ]
    for m0, m1 in plane_cases:
        result = evaluate(m0, m1)
        require(all(not x for jet in result for x in jet),
                "Full original tangent-plane jet did not vanish")
    coeff = {}
    for j in range(2, 11):
        Z = shifted_jet(j)
        FZ = evaluate(*Z)
        FminusZ = evaluate(*(scale_vector(v, -1) for v in Z))
        constant = [[(FZ[k][i] - FminusZ[k][i])/2
                     for i in range(17)] for k in range(2)]
        affine = [constant]
        for A in tan:
            plus = evaluate(*(add_vectors(A[k], Z[k]) for k in range(2)))
            FA = evaluate(*A)
            cross = jet_add(jet_add(plus, FZ, -1), FA, -1)
            affine.append(cross)
        coeff[j] = affine
    # Columns: c^a d^b z_j with a+b <=4; rows: c^a d^b F_i with a+b<=3.
    cols = [(a, degree-a, j) for degree in range(5)
            for a in range(degree+1) for j in range(2, 11)]
    colindex = {key: i for i, key in enumerate(cols)}
    rows = [(i, a, degree-a) for i in range(17) for degree in range(4)
            for a in range(degree+1)]
    require(len(cols) == 135 and len(rows) == 170, "Small model dimensions")
    P = [fmpq_mat(170, 135), fmpq_mat(170, 135)]
    for row, (i, a, b) in enumerate(rows):
        for j in range(2, 11):
            for mode, (da, db) in enumerate([(0,0), (1,0), (0,1)]):
                col = colindex[(a+da, b+db, j)]
                for order in range(2):
                    P[order][row, col] += coeff[j][mode][order][i]
    return P[0], P[1], cols, rows, original_hashes


def chart_certificate(chart):
    started = time.monotonic()
    P0, P1, cols, rows, hashes = make_projection_jets(chart)
    Q, rank0, piv, free = nullspace(P0)
    require(rank0 == 128 and len(free) == 7, "Paid original P0 rank mismatch")
    U, rankT, sourcepiv, sourcefree = nullspace(P0.transpose())
    require(rankT == 128 and U.ncols() == 42, "Complete left-kernel dimensions")
    M = P1 * Q
    C = U.transpose() * M
    R, rankC = C.rref()
    Cpiv = pivot_columns(R, rankC)
    augmented = join_columns(P0, M)
    rank_aug = augmented.rank()
    require(rank_aug - rank0 == rankC, "Transposed connecting-rank identity")
    V, rcheck, _, vfree = nullspace(C)
    require(rcheck == rankC, "Small annihilator rank mismatch")
    # Give complete original 170-row correction, not just the reduced pairing.
    target = M * V
    block = submatrix(P0, sourcepiv, piv)
    correction = fmpq_mat(135, V.ncols())
    if V.ncols():
        correction_small = block.solve(submatrix(target, sourcepiv, range(V.ncols())))
        for i, p in enumerate(piv):
            for j in range(V.ncols()):
                correction[p, j] = correction_small[i, j]
    require(P0 * correction == target, "All 170 original correction rows failed")
    require(matrix_zero(P0 * Q), "All original P0 kernel rows")
    # A small exact minor proves the reported upper-envelope rank is sharp.
    _, _, crows, _ = nullspace(C.transpose())
    determinant = submatrix(C, crows, Cpiv).det() if rankC else ONE
    require(determinant != 0, "Small connecting-rank minor vanished")
    return {
        "chart": chart,
        "naturalParameter": "s" if chart == "zero" else "u=1/s",
        "originalMean": "(1,t,t^2,t^3,t^4,t^5)" if chart == "zero"
                        else "(t^5,t^4,t^3,t^2,t,1)",
        "coMovingMomentJet": "m_j=n_j+t*j*n_(j-1)+O(t^2); infinity after exact reversal",
        "all17OriginalEquationsRetained": True,
        "all170TangentJetCoefficientChecksZero": True,
        "P0Shape": [170, 135], "P0Rank": rank0,
        "completeRightKernelDimension": 7, "completeLeftKernelDimension": 42,
        "P0KernelFreeMonomials": [list(cols[f]) for f in free],
        "P0IndependentColumns": piv, "P0IndependentRows": sourcepiv,
        "smallConnectingShape": [42, 7],
        "transverseEnvelopeConnectionRank": rankC,
        "augmentedShape": [170, 142], "augmentedRank": rank_aug,
        "fullOriginalFirstConnectionRankUpperBound": rankC,
        "notAutomaticallyAFullOriginalLowerBound": True,
        "smallConnectionRowSpaceRref":
            [[str(R[i, j]) for j in range(7)] for i in range(rankC)],
        "smallNonzeroMinor": {"rows": crows, "columns": Cpiv,
                             "determinant": str(determinant)},
        "extraCokernelAnnihilatorsInQBasis":
            [[str(V[i, j]) for i in range(7)] for j in range(V.ncols())],
        "all170ExactCorrectionRowsVerified": True,
        "allP0NullspaceIdentitiesVerified": True,
        "matrixSha256": dict(hashes, P0=matrix_hash(P0), P1=matrix_hash(P1),
                            Q=matrix_hash(Q), leftKernel=matrix_hash(U),
                            connecting=matrix_hash(C), annihilators=matrix_hash(V),
                            originalCorrection=matrix_hash(correction)),
        "elapsedSeconds": time.monotonic()-started,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--chart", choices=("zero", "infinity", "both"), default="both")
    parser.add_argument("--out", required=True)
    parser.add_argument("--remaining-seconds", type=float, default=30.0)
    args = parser.parse_args()
    require(args.remaining_seconds > 0, "Positive shared remaining time required")
    resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2))
    started = time.monotonic()
    receipt = {
        "format": "r150-original-transverse-first-connection-v1",
        "status": "started", "arithmetic": "exact rational python-flint",
        "scriptSha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "originalK": ORIGINAL_K,
        "limits": {"sharedRemainingSeconds": args.remaining_seconds,
                   "largestMatrixEntryCount": 170*142,
                   "principalShapes": [[170,135],[135,170],[42,7],[170,142]],
                   "memoryMiBContract": 512},
        "charts": [], "largeMacaulayMatrixConstructed": False,
        "sevenSelectedOriginalKernelsUsed": False,
        "largeRecomputableDataPersisted": False,
    }
    receipt["parameters"] = {
        "charts": receipt["charts"], "limits": receipt["limits"],
        "originalK": receipt["originalK"]}
    def timeout_handler(signum, frame):
        raise TimeoutError("Shared mathematical time budget exhausted")
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.setitimer(signal.ITIMER_REAL, args.remaining_seconds)
    try:
        for chart in (("zero", "infinity") if args.chart == "both" else (args.chart,)):
            receipt["charts"].append(chart_certificate(chart))
        receipt["status"] = "completed"
    except BaseException as exc:
        receipt["status"] = "incomplete"
        receipt["error"] = type(exc).__name__ + ": " + str(exc)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        receipt["elapsedSeconds"] = time.monotonic()-started
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        raw = json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2).encode("utf-8")
        require(len(raw) < 100_000, "Receipt exceeded small-text contract")
        temporary = out.with_name(out.name + ".tmp")
        temporary.write_bytes(raw)
        os.replace(temporary, out)
        print(json.dumps({"status": receipt["status"], "receipt": str(out),
                          "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
                          "charts": [{"chart": c["chart"],
                                      "fullConnectionRankUpperBound":
                                      c["fullOriginalFirstConnectionRankUpperBound"]}
                                     for c in receipt["charts"]],
                          "elapsedSeconds": receipt["elapsedSeconds"]},
                         ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
