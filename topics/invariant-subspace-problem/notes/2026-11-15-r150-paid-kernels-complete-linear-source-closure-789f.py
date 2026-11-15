#!/usr/bin/env python3
"""Paid infinity kernels: complete low-degree/linear source closure.

Only original source arithmetic is performed.  No original operator product,
Dixon step, or higher precision is recomputed.  Large derived source arrays
exist only in memory; only a small receipt and their canonical hashes are saved.
The caller downloads inputs before starting this mathematical budget.
"""
import argparse
import fractions
import gzip
import hashlib
import itertools
import json
import math
import resource
import signal
import time
from pathlib import Path

P = 31
NS = 6188
EXPECTED_CERT_SHA = "24913665ab0ff6f1eb41c26caf3b50d1d2fc11cf8568a5611943e91d2c29c184"


class BudgetExpired(Exception):
    pass


def sha(b):
    return hashlib.sha256(b).hexdigest()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def rational(x):
    p = str(x).split("/")
    return fractions.Fraction(int(p[0]), int(p[1]) if len(p) == 2 else 1)


def qstr(x):
    return [str(x.numerator), str(x.denominator)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--certificates", required=True)
    ap.add_argument("--selected-model", required=True)
    ap.add_argument("--native-model", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--math-seconds", type=float, default=10.0)
    ap.add_argument("--memory-mib", type=int, default=512)
    ap.add_argument("--expected-cert-sha256", default=EXPECTED_CERT_SHA)
    ap.add_argument("--expected-kernels", type=int, default=23)
    args = ap.parse_args()
    if not (0 < args.math_seconds <= 10 and 0 < args.memory_mib <= 512):
        raise ValueError("This source-only task is capped at 10 seconds and 512 MiB.")
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    paths = {"certificates": Path(args.certificates),
             "selectedModel": Path(args.selected_model),
             "nativeModel": Path(args.native_model)}
    raw = {k: p.read_bytes() for k, p in paths.items()}
    if sha(raw["certificates"]) != args.expected_cert_sha256:
        raise ValueError("wrong paid complete-source certificate bytes")
    inputs = {k: {"bytes": len(v), "sha256": sha(v)} for k, v in raw.items()}
    receipt = {"format": "R150_PAID_KERNELS_COMPLETE_LINEAR_SOURCE_CLOSURE_V2",
               "status": "running", "inputs": inputs, "events": [],
               "mathematicalBudgetSeconds": args.math_seconds,
               "memoryLimitMiB": args.memory_mib,
               "largeDataWrittenOrUploaded": False,
               "originalOperatorProductRecomputed": False}
    limit = args.memory_mib * 1024 * 1024
    resource.setrlimit(resource.RLIMIT_AS, (limit, limit))
    started = time.monotonic()
    deadline = started + max(0.1, args.math_seconds - 0.7)

    def check():
        if time.monotonic() >= deadline:
            raise BudgetExpired()

    def alarm(signum, frame):
        raise BudgetExpired()

    signal.signal(signal.SIGALRM, alarm)
    signal.setitimer(signal.ITIMER_REAL, max(0.1, args.math_seconds - 0.7))
    stage = "decode-paid-sources"
    columns = []
    atom_recipes = []

    def event(name, **data):
        receipt["events"].append({"stage": name, **data})

    def source_hash(col):
        digest = hashlib.sha256()
        digest.update(("R150_FULL_ORIGINAL_SOURCE_Q_V1\n" + str(col["den"]) + "\n").encode())
        v = col["num"]
        for r in range(NS):
            digest.update((str(v.get(r, 0)) + "\n").encode())
        return digest.hexdigest()

    def add_column(num, den, recipe, name):
        assert den > 0
        num = {r: int(v) for r, v in num.items() if v}
        assert all(0 <= r < NS for r in num)
        g = den
        for v in num.values():
            g = math.gcd(g, abs(v))
            if g == 1:
                break
        if g != 1:
            num = {r: v // g for r, v in num.items()}
            den //= g
        col = {"num": num, "den": den, "recipe": recipe, "name": name}
        columns.append(col)
        return len(columns) - 1

    def combine(ids, coeff, name):
        check()
        live = [(j, rational(a)) for j, a in zip(ids, coeff) if a]
        den = 1
        for j, a in live:
            den = math.lcm(den, columns[j]["den"] * a.denominator)
        result = {}
        recipe = []
        for j, a in live:
            scale = a.numerator * (den // (columns[j]["den"] * a.denominator))
            for r, v in columns[j]["num"].items():
                result[r] = result.get(r, 0) + scale * v
            recipe.append([j, *qstr(a)])
        return add_column(result, den, {"linearCombination": recipe}, name)

    def mod_rows(ids, rows):
        inv = [pow(columns[j]["den"], -1, P) for j in ids]
        for r in rows:
            yield r, [columns[j]["num"].get(r, 0) * iv % P for j, iv in zip(ids, inv)]

    def independent_rows(ids, rows):
        basis = {}
        labels = []
        for count, (r, values) in enumerate(mod_rows(ids, rows)):
            if count % 32 == 0:
                check()
            v = values
            for k, w in basis.items():
                a = v[k]
                if a:
                    v = [(x - a * y) % P for x, y in zip(v, w)]
            pivot = next((k for k, x in enumerate(v) if x), None)
            if pivot is not None:
                iv = pow(v[pivot], -1, P)
                basis[pivot] = [x * iv % P for x in v]
                labels.append(r)
        return labels, list(basis)

    def exact_constraint_kernel(ids, rows, name):
        """An exact nullspace, with full omitted-row verification.

        A modular minor selects independent rows.  The rational nullspace of
        those rows is accepted only after ALL constraints vanish exactly.
        Thus a bad modular specialization can never turn into a false kernel.
        """
        check()
        pivot_rows, pivot_columns = independent_rows(ids, rows)
        if not pivot_rows:
            assert all(not columns[j]["num"].get(r, 0) for j in ids for r in rows)
            return list(ids), 0
        from flint import fmpq, fmpq_mat
        a = fmpq_mat([[fmpq(columns[j]["num"].get(r, 0), columns[j]["den"])
                      for j in ids] for r in pivot_rows])
        rr, rank = a.rref()
        assert rank == len(pivot_rows)
        pivots = []
        for i in range(rank):
            pivots.append(next(j for j in range(len(ids)) if rr[i, j]))
        freecols = [j for j in range(len(ids)) if j not in set(pivots)]
        generated = []
        for k in freecols:
            coeff = [fractions.Fraction(0) for _ in ids]
            coeff[k] = fractions.Fraction(1)
            for i, j in enumerate(pivots):
                coeff[j] = -rational(rr[i, k])
            new = combine(ids, coeff, name + "-" + str(k))
            if any(columns[new]["num"].get(r, 0) for r in rows):
                raise ArithmeticError("modular rank did not determine full rational rank; no complete closure claimed")
            generated.append(new)
        event(name, rationalRank=rank, nullity=len(generated),
              allConstraintRowsVerified=True,
              modularPivotOriginalRows=[r + 1 for r in pivot_rows],
              modularPivotColumnsZeroBased=pivot_columns)
        return generated, rank

    def free_independent(ids, free):
        basis = {}
        chosen = []
        for j in ids:
            col = columns[j]
            inv = pow(col["den"], -1, P)
            v = [col["num"].get(r - 1, 0) * inv % P for r in free]
            for k, w in basis.items():
                a = v[k]
                if a:
                    v = [(x - a * y) % P for x, y in zip(v, w)]
            pivot = next((k for k, x in enumerate(v) if x), None)
            if pivot is not None:
                iv = pow(v[pivot], -1, P)
                basis[pivot] = [x * iv % P for x in v]
                chosen.append(j)
        return chosen

    try:
        cert = json.loads(gzip.decompress(raw["certificates"]))
        model = json.loads(raw["selectedModel"])
        tokens = raw["nativeModel"].decode().split()
        assert tokens[0] == "R150_NATIVE_NF_V1"
        start = 1 + 11 * (66 + 11 * 11)
        assert int(tokens[start]) == 3333
        pre = [list(map(int, tokens[start + 1 + 4*j:start + 5 + 4*j]))
               for j in range(3333)]
        selected = set(model["selectedSourceRows"]) | {r[3] for r in pre}
        assert len(model["selectedSourceRows"]) == 1021 and len(selected) == 4354
        assert len(model["independentSelectedSourceIndicesZeroBased"]) == 985
        mon = [v for degree in range(4)
               for v in itertools.combinations_with_replacement(range(11), degree)]
        mon_index = {v: i for i, v in enumerate(mon)}
        assert len(mon) * 17 == NS
        for equation, key, _, source in pre:
            t = tuple(i for i in range(11) for _ in range((key // (8**i)) % 8))
            assert source == 17 * mon_index[t] + equation + 1
        paid = cert["certificates"]
        assert cert["kernelCount"] == len(paid) == args.expected_kernels
        free = cert["normalizedFreeOriginalSourceRows"]
        assert len(free) == len(set(free)) == 36
        assert all(r in selected for r in free)
        slots = [c["slot"] for c in paid]
        assert len(slots) == len(set(slots)) and all(0 <= s < 36 for s in slots)
        degrees = []
        for index, c in enumerate(paid):
            check()
            assert c["all4367ExactIntegerProductsZero"]
            n = c["originalIntegerSourceNumerators"]
            assert len(n) == NS
            den = int(c["commonDenominator"])
            assert den > 0 and den % P
            num = {r: int(v) for r, v in enumerate(n) if int(v)}
            assert all(r + 1 in selected for r in num)
            assert all(num.get(r - 1, 0) == (den if k == c["slot"] else 0)
                       for k, r in enumerate(free))
            new = add_column(num, den, {"paidSlot": c["slot"]}, "paid-" + str(c["slot"]))
            assert new == index
            degrees.append(max(len(mon[r // 17]) for r in num))
        paid_ids = list(range(len(paid)))
        receipt.update({"paidSlots": slots, "sourceMultiplierDegrees": degrees,
                        "allOriginal6188PaidSupportChecksPassed": True,
                        "all36PaidFreeCoordinatesExactlyNormalized": True,
                        "selectedOriginalSourceCount": 4354})
        # Release source strings before allocating complete shift constraints.
        del cert, paid, tokens, raw
        stage = "complete-low-degree-subspace"
        low = [j for j, degree in enumerate(degrees) if degree <= 2]
        high_rows = list(range(17 * (1 + 11 + 66), NS))
        tr, tc = independent_rows(paid_ids, high_rows)
        if len(tr) == len(paid_ids) - len(low):
            event("complete-low-degree-subspace", dimension=len(low),
                  exactCoordinateSubspace=True,
                  paidSlots=[slots[j] for j in low],
                  topRank=len(tr),
                  modularPivotOriginalRows=[r+1 for r in tr],
                  modularPivotColumnsZeroBased=tc)
        else:
            low, top_rank = exact_constraint_kernel(paid_ids, high_rows, "complete-low-degree-subspace")
        assert all(all(len(mon[r // 17]) <= 2 for r in columns[j]["num"]) for j in low)
        stage = "all-linear-multiples-and-selected-support"
        shifts = []
        for j in low:
            for variable in range(11):
                check()
                result = {}
                for r, v in columns[j]["num"].items():
                    target_mon = tuple(sorted(mon[r // 17] + (variable,)))
                    target = 17 * mon_index[target_mon] + r % 17
                    result[target] = result.get(target, 0) + v
                shifts.append(add_column(result, columns[j]["den"],
                                         {"multiplyVariableZeroBased": variable, "column": j},
                                         "m" + str(variable) + "*" + columns[j]["name"]))
        outside = sorted({r for j in shifts for r in columns[j]["num"] if r+1 not in selected})
        individually_legal = [j for j in shifts
                              if all(r + 1 in selected for r in columns[j]["num"])]
        chosen = free_independent(paid_ids + individually_legal, free)
        event("individual-legal-multiples", lowDimension=len(low),
              allLinearMultiples=len(shifts), individuallyLegal=len(individually_legal),
              totalIndependentFreeRank=len(chosen))
        complete_closure = len(chosen) == 36
        legal_basis = individually_legal
        if not complete_closure:
            # Complete constraints include cancellations between illegal columns.
            # A common frequent case is certified without rational elimination.
            br, bc = independent_rows(shifts, outside)
            if len(br) == len(shifts) - len(individually_legal):
                legal_basis = individually_legal
                event("full-outside-selected-constraints", rationalRank=len(br),
                      nullity=len(legal_basis), exactCoordinateKernel=True,
                      modularPivotOriginalRows=[r+1 for r in br],
                      modularPivotColumnsZeroBased=bc)
            else:
                legal_basis, _ = exact_constraint_kernel(shifts, outside, "full-outside-selected-constraints")
            candidates = paid_ids + legal_basis
            chosen = free_independent(candidates, free)
            # For a negative closure result, verify exact span, not only mod p.
            if len(chosen) < 36:
                from flint import fmpq, fmpq_mat
                a = fmpq_mat([[fmpq(columns[j]["num"].get(r-1, 0), columns[j]["den"])
                              for j in candidates] for r in free])
                rr, rank = a.rref()
                if rank != len(chosen):
                    raise ArithmeticError("rational free rank exceeds mod31 rank; no final dimension claimed")
                # Chosen columns' free matrix has full column rank; select rows.
                cr, cp = independent_rows(chosen, [r-1 for r in free])
                assert len(cr) == len(chosen)
                square = fmpq_mat([[fmpq(columns[j]["num"].get(r, 0), columns[j]["den"])
                                   for j in chosen] for r in cr])
                inv = square.inv()
                for j in candidates:
                    check()
                    rhs = fmpq_mat([[fmpq(columns[j]["num"].get(r, 0), columns[j]["den"])] for r in cr])
                    coef = inv * rhs
                    test = combine(chosen, [rational(coef[i, 0]) for i in range(len(chosen))],
                                   "span-check-" + str(j))
                    assert columns[test]["num"] == columns[j]["num"] and columns[test]["den"] == columns[j]["den"]
                event("complete-selected-support-span", exactDimension=rank,
                      all6188SourceSpanIdentitiesVerified=True)
                complete_closure = True
        stage = "normalize-new-exact-kernels"
        rank = len(chosen)
        new_certificates = []
        receipt["newNormalizedKernels"] = new_certificates
        receipt["verifiedFreeRankBeforeNormalization"] = rank
        if rank == 36:
            from flint import fmpq, fmpq_mat
            free_matrix = fmpq_mat([[fmpq(columns[j]["num"].get(r-1, 0), columns[j]["den"])
                                    for j in chosen] for r in free])
            inv = free_matrix.inv()
            for slot in range(36):
                if slot in slots:
                    continue
                check()
                coef = [rational(inv[i, slot]) for i in range(36)]
                new = combine(chosen, coef, "new-normalized-slot-" + str(slot))
                col = columns[new]
                assert all(r + 1 in selected for r in col["num"])
                assert all(col["num"].get(r-1, 0) == (col["den"] if k == slot else 0)
                           for k, r in enumerate(free))
                new_certificates.append({
                    "slot": slot, "freeOriginalSource": free[slot],
                    "commonDenominator": str(col["den"]),
                    "all6188OriginalSourceCoordinatesConstructedExactly": True,
                    "same4354SourceSupportVerified": True,
                    "all36FreeCoordinatesExactIdentity": True,
                    "original4367KernelIdentityInheritedByExactSourceCombination": True,
                    "canonicalFullOriginalSourceSHA256": source_hash(col),
                    "exactBasisCombinationSHA256": sha(canonical([qstr(x) for x in coef])),
                    "basisColumnIds": chosen})
            complete_closure = True
        receipt.update({
            "status": "completed" if complete_closure else "partial",
            "resultingSelectedSupportSpanDimension": rank,
            "allThirtySixSelectedKernelDirectionsConstructed": rank == 36,
            "newNormalizedKernelCount": len(new_certificates),
            "newNormalizedKernels": new_certificates,
            "constructionDAG": [{"id": j, "name": c["name"], "recipe": c["recipe"]}
                                for j, c in enumerate(columns)
                                if not c["name"].startswith("span-check-")],
            "kernelIdentityJustification": "Exact Q-linear combinations and multiplication of paid polynomial identities by a single m_i; every new source has degree at most three and its complete selected support and 36 free coordinates are checked.",
            "ambientSelectedKernelUpperBound": {
                "dimension": 36,
                "dependency": "Already paid nonzero mod31 4318 minor of the same 4354 selected columns (3333+985); this task does not recompute it."},
            "scope": "The complete source span generated by the paid kernels and all one-variable multiples of its full degree-at-most-two part, intersected with the same 4354 original source columns. Full 36 construction, when obtained, additionally proves the selected Q-kernel is complete."})
    except BudgetExpired:
        receipt.update({"status": "budget-checkpoint", "stage": stage,
                        "uncomputedClosureNotClaimed": True})
    except Exception as exc:
        receipt.update({"status": "failed", "stage": stage,
                        "errorType": type(exc).__name__, "error": str(exc),
                        "uncomputedClosureNotClaimed": True})
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        receipt["elapsedMathematicalSeconds"] = time.monotonic() - started
        # Recipes are reproducible data.  Never save an oversized receipt.
        if len(canonical(receipt)) > 90000 and "constructionDAG" in receipt:
            dag = receipt.pop("constructionDAG")
            receipt["constructionDAGSHA256"] = sha(canonical(dag))
            receipt["constructionDAGReconstruction"] = "Rerun this deterministic script with the three pinned inputs; no large result is archived."
        data = (json.dumps(receipt, ensure_ascii=False, indent=2) + "\n").encode()
        if len(data) > 99000:
            compact = canonical(receipt) + b"\n"
            assert len(compact) <= 99000
            data = compact
        target = out / "paid-kernels-linear-source-closure-receipt-789f.json"
        target.write_bytes(data)
        summary = {k: receipt[k] for k in
                   ("status", "stage", "resultingSelectedSupportSpanDimension",
                    "newNormalizedKernelCount", "allThirtySixSelectedKernelDirectionsConstructed",
                    "elapsedMathematicalSeconds") if k in receipt}
        summary.update({"receiptBytes": len(data), "receiptSHA256": sha(data),
                        "largeDataWrittenOrUploaded": False})
        print(json.dumps(summary))
    if receipt["status"] not in ("completed", "budget-checkpoint"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
