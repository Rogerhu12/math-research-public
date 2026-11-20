#!/usr/bin/env python3
"""R150: V=0, all original low gradients, degree-six matched Bell certificate.

Author: Astra-ISP-b2a9acde-20261120 / literature; GPT-6 Astra Pro, AI-assisted.
This is an unexecuted certificate generator until its execution record says
otherwise. It keeps all six mean variables, all eleven normalized original
second gradients, and all six normalized original mean gradients.

For y != 0, the complete highest equation with V=0 gives
H(y) = (1/6) J2^{-1} coeff_z((Ky).v(z))^2.
At y=0 every matched Bell cubic already vanishes, for every H.

The only attempted target degree here is six: S_r(y)^2.
Rows: C(11,5)=462. Columns: 11*C(7,5)+6*C(6,5)=267.
All three matching directions are handled simultaneously in
Q[d]/(3725*d^3-43931504*d^2+6080833024*d+52565262336).
A modular result alone is never called a characteristic-zero certificate.
No arrays, multipliers, or matrix dumps are written to disk.

Dependencies: python-flint.
Documented exact APIs:
https://python-flint.readthedocs.io/en/latest/fmpq_mat.html
https://python-flint.readthedocs.io/en/latest/nmod_mat.html
"""
import argparse
import hashlib
import json
import math
import os
import resource
import signal
import sys
import time
from fractions import Fraction as Q
from pathlib import Path

def require(ok, message):
    if not ok:
        raise AssertionError(message)

def emit(obj):
    print(json.dumps(obj, ensure_ascii=False, sort_keys=True), flush=True)

def alarm_handler(signum, frame):
    raise TimeoutError("Fixed degree-six wall-time budget exhausted")

def monomials(n, degree):
    if n == 1:
        return [(degree,)]
    out = []
    for first in range(degree, -1, -1):
        for rest in monomials(n - 1, degree - first):
            out.append((first,) + rest)
    return out

ZERO_EXP = (0,) * 6
UNIT_EXPS = [tuple(int(i == j) for i in range(6)) for j in range(6)]

def clean(poly):
    return {e: c for e, c in poly.items() if c}

def add(*polys):
    out = {}
    for poly in polys:
        for e, c in poly.items():
            out[e] = out.get(e, Q(0)) + c
    return clean(out)

def scale(poly, scalar):
    scalar = Q(scalar)
    return {e: scalar * c for e, c in poly.items() if scalar * c}

def mul(a, b):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = tuple(x + y for x, y in zip(ea, eb))
            out[e] = out.get(e, Q(0)) + ca * cb
    return clean(out)

def psum(polys):
    return add(*list(polys))

def dot(a, b):
    return psum(mul(x, y) for x, y in zip(a, b))

def mm(a, b):
    return [[psum(mul(a[i][k], b[k][j]) for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def mv(a, b):
    return [dot(row, b) for row in a]

def left_k(k, a):
    return [[psum(scale(a[t][j], k[i][t]) for t in range(6))
             for j in range(len(a[0]))] for i in range(6)]

def right_k(a, k):
    return [[psum(scale(a[i][t], k[t][j]) for t in range(6))
             for j in range(6)] for i in range(len(a))]

def physical(poly):
    out = {}
    for e, c in poly.items():
        degree = sum(i * e[i] for i in range(6))
        out[degree] = out.get(degree, Q(0)) + c
    return {d: c for d, c in out.items() if c}

def primitive(poly):
    """Return integer polynomial P and nonzero rational s with P=s*poly."""
    if not poly:
        return {}, Q(1)
    den = 1
    for c in poly.values():
        den = math.lcm(den, c.denominator)
    data = {e: int(c * den) for e, c in poly.items()}
    content = 0
    for c in data.values():
        content = math.gcd(content, abs(c))
    require(content != 0, "Nonzero primitive content")
    sign = 1 if data[sorted(data)[0]] > 0 else -1
    return ({e: sign * c // content for e, c in data.items()},
            Q(sign * den, content))

def poly_record(poly):
    return [[list(e), str(poly[e])] for e in sorted(poly)]

def digest(obj):
    raw = json.dumps(obj, ensure_ascii=True, sort_keys=True,
                     separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

# Arithmetic in the free rank-three rational algebra Q[d]/(P).
DRED = (Q(-52565262336, 3725),
        Q(-6080833024, 3725),
        Q(43931504, 3725))
E0 = (Q(0), Q(0), Q(0))
E1 = (Q(1), Q(0), Q(0))
ED = (Q(0), Q(1), Q(0))

def eadd(a, b):
    return tuple(a[i] + b[i] for i in range(3))

def escale(a, c):
    c = Q(c)
    return tuple(c * a[i] for i in range(3))

def emul(a, b):
    out = [Q(0)] * 5
    for i in range(3):
        for j in range(3):
            out[i + j] += a[i] * b[j]
    for degree in (4, 3):
        c = out[degree]
        for j in range(3):
            out[degree - 3 + j] += c * DRED[j]
    return tuple(out[:3])

def epadd(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = eadd(out.get(e, E0), c)
    return {e: c for e, c in out.items() if c != E0}

def epscale(a, c):
    return {e: escale(v, c) for e, v in a.items()
            if escale(v, c) != E0}

def epmul(a, b):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = tuple(x + y for x, y in zip(ea, eb))
            out[e] = eadd(out.get(e, E0), emul(ca, cb))
    return {e: c for e, c in out.items() if c != E0}

def rational_to_flint(x, fmpq):
    x = Q(x)
    return fmpq(x.numerator, x.denominator)

def rational_matrix(a, fmpq, fmpq_mat):
    return fmpq_mat([[rational_to_flint(x, fmpq) for x in row] for row in a])

def matching_directions(fmpq, fmpq_mat):
    den = escale((Q(-704), Q(5), Q(0)), 160)
    ebasis = [E1, ED, (Q(0), Q(0), Q(1))]
    columns = [emul(den, e) for e in ebasis]
    matrix = [[columns[j][i] for j in range(3)] for i in range(3)]
    inverse_column = rational_matrix(matrix, fmpq, fmpq_mat).solve(
        rational_matrix([[1], [0], [0]], fmpq, fmpq_mat))
    deninv = tuple(Q(str(inverse_column[i, 0])) for i in range(3))
    require(emul(den, deninv) == E1, "All-root anchor denominator is a unit")
    anum = (Q(271360), Q(-46784), Q(521))
    aa = escale(emul(anum, deninv), -1)
    bb = eadd(aa, ED)
    r = [aa, bb, E0, E0, E0, E1]

    conics = [
        ((Q(5), Q(-32, 5), Q(8, 5)),
         [[279, 121, 608], [121, -521, -608], [608, -608, -1024]]),
        ((Q(-27), Q(-864, 5), Q(-864, 5)),
         [[-1769, 1369, 5024], [1369, -969, -5024],
          [5024, -5024, -1024]])
    ]
    for recurrence, c in conics:
        basis = [[Q(1), Q(0), Q(0)],
                 [Q(0), Q(1), Q(0)],
                 [Q(0), Q(0), Q(1)]]
        for i in range(3, 6):
            basis.append([
                sum(recurrence[j] * basis[i - 1 - j][k] for j in range(3))
                for k in range(3)])
        u = []
        for j in range(3):
            value = E0
            for i in range(6):
                value = eadd(value, escale(r[i], basis[i][j]))
            u.append(value)
        value = E0
        for i in range(3):
            for j in range(3):
                value = eadd(value, escale(emul(u[i], u[j]), c[i][j]))
        require(value == E0, "Original matched conic identity for all roots")
    return r

def pivot_columns(rref, rank):
    out = []
    for i in range(rank):
        found = next((j for j in range(rref.ncols()) if rref[i, j] != 0), None)
        require(found is not None, "Every rank row has a pivot")
        out.append(found)
    require(len(set(out)) == rank, "Distinct unit pivots")
    return out

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--wall-seconds", type=int, default=180)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--output", default=None,
                        help="Optional small JSON record only; no arrays are saved")
    args = parser.parse_args()
    require(1 <= args.wall_seconds <= 600, "Bounded fixed wall-time request")
    require(256 <= args.memory_mib <= 4096, "Bounded memory request")
    resource.setrlimit(resource.RLIMIT_AS,
                       (args.memory_mib * 1024**2, args.memory_mib * 1024**2))
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(args.wall_seconds)
    start = time.monotonic()
    from flint import fmpq, fmpq_mat, nmod_mat

    record = {
        "schema": "r150-vzero-degree6-matched-bell-20261120-v1",
        "author": "Astra-ISP-b2a9acde-20261120 / literature",
        "sourceSha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "modulus": 103,
        "targetPower": 2,
        "targetTotalDegree": 6,
        "rows": 462,
        "columns": 267,
        "allOriginalSecondGradients": 11,
        "allOriginalMeanGradients": 6,
        "allThreeMatchingRoots": True,
        "ordinaryISPClaim": False,
        "characteristicZeroNonmembershipClaim": False,
    }
    k = [[0, 0, 0, 0, 5, -1],
         [0, 0, 0, -32, 5, -1],
         [0, 0, 54, -4, 5, 0],
         [0, -32, -4, -8, 0, 0],
         [5, 5, 5, 0, 0, 0],
         [-1, -1, 0, 0, 0, 0]]
    require(fmpq_mat(k).det() == -25600, "Original K, no congruence substitution")
    require(all(sum(k[i][j] for i in range(6) for j in range(6)
                    if i + j == m) == 0 for m in range(11)),
            "Original physical diagonal quadratic identity")
    yy = [{UNIT_EXPS[i]: Q(1)} for i in range(6)]
    pp = [psum(scale(yy[j], k[i][j]) for j in range(6)) for i in range(6)]
    f = scale(dot(yy, pp), Q(1, 2))

    j2 = [[0] * 11 for _ in range(11)]
    nonzero_k = [(i, j, k[i][j]) for i in range(6) for j in range(6) if k[i][j]]
    for i, j, a in nonzero_k:
        for s, t, b in nonzero_k:
            j2[i + s][j + t] += a * b
    jq = fmpq_mat(j2)
    require(jq.det() == -64701092257700249600, "Binding to the published original J2")
    mono2 = monomials(6, 2)
    d2 = [psum(mul(pp[i], pp[j]) for i in range(6) for j in range(6)
               if i + j == m) for m in range(11)]
    d2matrix = [[poly.get(e, Q(0)) for e in mono2] for poly in d2]
    dq = rational_matrix(d2matrix, fmpq, fmpq_mat)
    six_h = jq.solve(dq)
    require(jq * six_h == dq, "All original highest coefficients solved exactly")
    hseq = [
        clean({e: Q(str(six_h[i, j])) / 6 for j, e in enumerate(mono2)})
        for i in range(11)]
    hmat = [[hseq[i + j] for j in range(6)] for i in range(6)]
    kh = left_k(k, hmat)
    hk = right_k(hmat, k)
    require(not psum(kh[i][i] for i in range(6)), "Original trace(KH)=0")
    hh = mv(hmat, pp)
    bpoly = dot(pp, hh)
    tau2 = psum(mul(kh[i][j], kh[j][i]) for i in range(6) for j in range(6))
    require(not add(tau2, scale(bpoly, Q(-1, 6))),
            "Highest contraction tau2=b/6 in the original six variables")
    hkh = mm(hk, hmat)
    hkhp = mv(hk, hh)
    q2 = add(mul(f, f), scale(bpoly, -2), scale(tau2, 2))
    gamma = [add(mul(q2, yy[i]), scale(mul(f, hh[i]), -4),
                 scale(hkhp[i], 8)) for i in range(6)]
    nmat = [[add(mul(f, mul(yy[i], yy[j])),
                 scale(mul(f, hmat[i][j]), -2),
                 scale(add(mul(yy[i], hh[j]), mul(hh[i], yy[j])), -2),
                 scale(hkh[i][j], 4))
             for j in range(6)] for i in range(6)]
    require(all(nmat[i][j] == nmat[j][i] for i in range(6) for j in range(6)),
            "Original normalized second-gradient matrix is symmetric")
    knk = left_k(k, right_k(nmat, k))
    second = [psum(knk[i][j] for i in range(6) for j in range(6)
                   if i + j == m) for m in range(11)]
    raw_generators = second + gamma
    require(all(all(sum(e) == (4 if i < 11 else 5) for e in poly)
                for i, poly in enumerate(raw_generators)),
            "All eleven quartics and all six quintics retained")
    require(all(not physical(poly) for poly in raw_generators),
            "Independent physical-mean control for every original low gradient")

    rr = matching_directions(fmpq, fmpq_mat)
    linear = {UNIT_EXPS[i]: rr[i] for i in range(6) if rr[i] != E0}
    quadratic = {}
    for i in range(6):
        for j in range(6):
            rij = emul(rr[i], rr[j])
            if rij == E0:
                continue
            term = {e: escale(rij, c) for e, c in hmat[i][j].items()}
            quadratic = epadd(quadratic, term)
    bell = epadd(epmul(epmul(linear, linear), linear),
                 epscale(epmul(linear, quadratic), -6))
    target = epmul(bell, bell)
    raw_targets = [
        clean({e: coeff[j] for e, coeff in target.items()}) for j in range(3)]
    require(all(all(sum(e) == 6 for e in poly) for poly in raw_targets),
            "Exact degree-six targets")
    require(all(not physical(poly) for poly in raw_targets),
            "Matched Bell square vanishes on the original physical mean curve")
    generators_with_scales = [primitive(poly) for poly in raw_generators]
    targets_with_scales = [primitive(poly) for poly in raw_targets]
    generators = [pair[0] for pair in generators_with_scales]
    targets = [pair[0] for pair in targets_with_scales]
    record.update({
        "originalHighestSolvedExactly": True,
        "allOriginalGradientControlsPassed": True,
        "matchedConicsAllRootsCheckedOverQQ": True,
        "originalKHash": digest(k),
        "originalJ2Hash": digest(j2),
        "HSubstitutionHash": digest([poly_record(p) for p in hseq]),
        "rawGeneratorHash": digest([poly_record(p) for p in raw_generators]),
        "primitiveGeneratorHash": digest([poly_record(p) for p in generators]),
        "generatorUnitScalesHash": digest([str(p[1]) for p in generators_with_scales]),
        "rawTargetHash": digest([poly_record(p) for p in raw_targets]),
        "primitiveTargetHash": digest([poly_record(p) for p in targets]),
        "targetUnitScalesHash": digest([str(p[1]) for p in targets_with_scales]),
        "rawGeneratorTerms": sum(len(p) for p in raw_generators),
        "rawTargetTerms": sum(len(p) for p in raw_targets),
        "maxPrimitiveCoefficientBits": max(
            [abs(c).bit_length() for p in generators + targets for c in p.values()]
            or [0]),
        "setupSeconds": round(time.monotonic() - start, 6),
    })
    emit({"stage": "original_source_and_target_controls", **record})

    if args.preflight_only:
        record["status"] = "preflight_only_no_membership_claim"
    else:
        rows = monomials(6, 6)
        row_index = {e: i for i, e in enumerate(rows)}
        column_specs = [(i, e) for i in range(17)
                        for e in monomials(6, 2 if i < 11 else 1)]
        require(len(rows) == 462 and len(column_specs) == 267,
                "Fixed degree-six complete source dimensions")
        matrix = [[0] * 267 for _ in rows]
        for j, (gindex, shift) in enumerate(column_specs):
            for e, c in generators[gindex].items():
                shifted = tuple(a + b for a, b in zip(e, shift))
                matrix[row_index[shifted]][j] += c
        target_matrix = [[targets[j].get(e, 0) for j in range(3)] for e in rows]
        record["fullMatrixHash"] = digest(matrix)
        record["fullTargetMatrixHash"] = digest(target_matrix)
        record["columnSpecificationHash"] = digest(column_specs)
        record["rowOrderHash"] = digest(rows)
        mod_matrix = nmod_mat([[x % 103 for x in row] for row in matrix], 103)
        rref, rank = mod_matrix.rref()
        columns = pivot_columns(rref, rank)
        require(rank > 0, "Nonzero modular source rank")
        selected = [[row[j] for j in columns] for row in matrix]
        selected_mod = nmod_mat([[x % 103 for x in row] for row in selected], 103)
        transpose_rref, transpose_rank = selected_mod.transpose().rref()
        require(transpose_rank == rank, "Independent selected source columns")
        pivot_rows = pivot_columns(transpose_rref, rank)
        minor = [[matrix[i][j] for j in columns] for i in pivot_rows]
        minor_mod = nmod_mat([[x % 103 for x in row] for row in minor], 103)
        det_mod = int(minor_mod.det())
        require(det_mod != 0, "The selected QQ minor is a verified modular unit")
        augmented_mod = nmod_mat([
            [x % 103 for x in matrix[i] + target_matrix[i]]
            for i in range(462)], 103)
        augmented_rank = augmented_mod.rank()
        record.update({
            "modularSourceRank": rank,
            "modularAugmentedRankAllThreeTargets": augmented_rank,
            "unitMinorDetMod103": det_mod,
            "unitMinorOrder": rank,
            "selectedColumnHash": digest(columns),
            "selectedRowHash": digest(pivot_rows),
            "modularAllTargetsInSourceSpan": augmented_rank == rank,
        })
        emit({"stage": "fixed_modular_unit_selection",
              "sourceRank": rank, "augmentedRank": augmented_rank,
              "minorDetMod103": det_mod,
              "elapsedSeconds": round(time.monotonic() - start, 6)})
        if augmented_rank != rank:
            record.update({
                "status": "no_degree6_certificate_candidate_at_fixed_modulus",
                "exactCertificateVerified": False,
                "QQSolveAttempted": False,
                "interpretation": (
                    "Only the fixed-modulus span test failed. No claim of "
                    "characteristic-zero nonmembership or absence of critical points.")
            })
        else:
            rhs = [[target_matrix[i][j] for j in range(3)] for i in pivot_rows]
            solution = fmpq_mat(minor).solve(fmpq_mat(rhs), algorithm="dixon")
            residual = fmpq_mat(selected) * solution - fmpq_mat(target_matrix)
            bad_counts = [sum(residual[i, j] != 0 for i in range(462))
                          for j in range(3)]
            exact = bad_counts == [0, 0, 0]
            rational_solution = [[Q(str(solution[i, j])) for j in range(3)]
                                 for i in range(rank)]
            record.update({
                "QQSolveAttempted": True,
                "QQVerifiedRowsPerTarget": 462,
                "QQVerifiedTargets": 3,
                "QQNonzeroResidualCounts": bad_counts,
                "exactCertificateVerified": exact,
                "certificateMultiplierHash": digest([
                    [str(c) for c in row] for row in rational_solution]),
                "certificateNonzeroMultipliers": sum(
                    c != 0 for row in rational_solution for c in row),
                "certificateMaxNumeratorBits": max(
                    [abs(c.numerator).bit_length() for row in rational_solution
                     for c in row] or [0]),
                "certificateMaxDenominatorBits": max(
                    [c.denominator.bit_length() for row in rational_solution
                     for c in row] or [0]),
                "status": ("exact_all_three_degree6_certificates" if exact else
                           "selected_minor_QQ_lift_failed_full_row_verification"),
                "interpretation": (
                    "All three coefficient targets have exact full-row QQ witnesses; "
                    "all matched Bell values vanish on the complete V=0 critical "
                    "stratum. This is not a global full-Jacobian power certificate."
                    if exact else
                    "No exact certificate was obtained from the selected minor; "
                    "no global or geometric nonexistence conclusion follows.")
            })
    record["elapsedSeconds"] = round(time.monotonic() - start, 6)
    record["peakRssKiB"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    signal.alarm(0)
    if args.output:
        target_path = Path(args.output)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(json.dumps(record, ensure_ascii=False, sort_keys=True,
                                          indent=2) + "\n", encoding="utf-8")
    emit({"stage": "complete", **record})

if __name__ == "__main__":
    main()
