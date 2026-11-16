#!/usr/bin/env python3
"""Complete original projected F31 local Smith data at s=1 or s=2.

AI-assisted: ChatGPT / literature_audit, 2026-11-16.
Uses unchanged paid unit_schur/convolution only, not the old hardcoded chart
or its Smith state. Independently rebuilds all primitive polynomial rows.
Completion is actual cumulative rank142; no local spectrum is prefilled.
All mathematical arrays remain temporary.
"""
import argparse
import gzip
import hashlib
import importlib.util
import itertools
import json
import math
import os
from pathlib import Path
import resource
import signal
import sys
import time

FORMAT = "r150-original-projection-field31-local-complete-smith-v1"
P = 31
GENERIC_UPPER = 142
PINS = {
    "core": (34432, "727175cf485a8ba5b5146a4cc6e749962e109c9e42265a2dd45f58cecdf933fb"),
    "generator": (15328, "2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"),
    "schur": (37379, "dc17dc88a5f1415c648b6ba5bf3fab4f7fb810aef6cc1552a5b2ea4acacbdf79"),
    "primitive": (65159, "44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe"),
}
DECODED = (158741, "fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3")
DEADLINE = float("inf")


def require(v, message):
    if not v:
        raise AssertionError(message)


def tick():
    if time.monotonic() >= DEADLINE:
        raise TimeoutError("Complete original-field operation budget")


def canonical(x):
    return (json.dumps(x, sort_keys=True, ensure_ascii=True,
                       separators=(",", ":")) + "\n").encode("ascii")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def identity(path, pin=None):
    b = Path(path).read_bytes()
    ans = (len(b), sha(b))
    if pin is not None:
        require(ans == pin, "Full source/input identity: " + str(path))
    return {"bytes": ans[0], "sha256": ans[1]}


def atomic(path, x):
    path = Path(path)
    b = canonical(x)
    tmp = path.with_name(path.name + ".tmp-" + str(os.getpid()))
    with tmp.open("wb") as f:
        f.write(b)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)
    return {"bytes": len(b), "sha256": sha(b)}


def module_at(path, name):
    sp = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


def trim(q):
    while q and q[-1] == 0:
        q.pop()
    return q


def padd(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return trim([v % P for v in c])


def pscale(a, c):
    return trim([v * c % P for v in a])


def shift_add(a, b, scalar, shift):
    if not b or scalar % P == 0:
        return a
    return padd(a, [0] * shift + pscale(b, scalar))


def pmul(a, b):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % P
    return trim(out)


def reduce_poly(q):
    den = int(q.denom())
    require(den % P, "Every original whole rational polynomial denominator is a31 unit")
    inv = pow(den % P, -1, P)
    return trim([int(v) * inv % P for v in q.numer().coeffs()])


def taylor(q, center, degree):
    return [sum(q[d] * math.comb(d, k) * pow(center, d-k, P)
                for d in range(k, len(q))) % P for k in range(degree+1)]


def sparse_scaled(row, scalar):
    return {j: z for j, q in row.items() if (z := pscale(q, scalar))}


def sparse_multiple(row, polynomial):
    return {j: z for j, q in row.items() if (z := pmul(q, polynomial))}


def matrix_rows(M):
    return [[int(M[i, j]) for j in range(M.ncols())] for i in range(M.nrows())]


def construct(args, e, core, generator, rec):
    decoded = gzip.decompress(Path(args.primitive).read_bytes())
    require((len(decoded), sha(decoded)) == DECODED, "Complete primitive decoded identity")
    original = json.loads(decoded)
    require(original["format"] == "r150-original-primitive-integer-equations-v1",
            "Original primitive format")
    eqs = original["equations"]
    require(len(eqs) == 17 and all(len(r) == 77 for r in eqs), "Whole17 by77 original polynomials")
    den = int(original["denominator"])
    contents = [int(c) for c in original["contents"]]
    require(den == 23366320238786911411830138211362846399922176000
            and len(contents) == 17 and den % P and all(c % P for c in contents),
            "All18 original normalization constants are31 units")
    scales = [den * pow(c % P, -1, P) % P for c in contents]
    core.DEADLINE = DEADLINE
    pure, linear, physical = core.original_polynomials(generator)
    PP, pc, nc, pure_rows = core.build_P(pure, linear)
    puref = [reduce_poly(q) for q in pure]
    linearf = [[[reduce_poly(q) for q in mode] for mode in entry] for entry in linear]
    compressed = [{j: q for j, v in enumerate(row) if (q := reduce_poly(v))} for row in PP]
    gf = reduce_poly(core.G)

    # Exact ordinary primitive equation polynomials in all comoving coordinates.
    mons = [(i,) for i in range(11)] + list(itertools.combinations_with_replacement(range(11), 2))
    transformed = []
    scalar_count = 0
    for eq, row in enumerate(eqs):
        tick()
        f = {}
        for mon, coeff in zip(mons, row):
            scalar_count += len(coeff)
            q = trim([int(v) % P for v in coeff])
            if len(mon) == 1:
                a = mon[0]
                for j in range(a+1):
                    f[(j,)] = shift_add(f.get((j,), []), q, math.comb(a, j), a-j)
            else:
                a, b = mon
                for j in range(a+1):
                    for k in range(b+1):
                        key = tuple(sorted((j, k)))
                        f[key] = shift_add(f.get(key, []), q,
                                           math.comb(a, j)*math.comb(b, k), a+b-j-k)
        f = {k: v for k, v in f.items() if v}
        require(all(not f.get(m, []) for m in ((0,), (1,), (0, 0), (0, 1))),
                "All original pure polynomials except d squared vanish identically")
        require(f.get((1, 1), []) == pscale(puref[eq], scales[eq]),
                "Whole original physical/primitive pure identity overF31[s]")
        for j in range(2, 11):
            for mode, mon in enumerate(((j,), (0, j), (1, j))):
                require(f.get(mon, []) == pscale(linearf[j-2][mode][eq], scales[eq]),
                        "Whole original physical/primitive one-normal identity overF31[s]")
        transformed.append(f)
    require(max(len(q)-1 for f in transformed for q in f.values()) <= 25,
            "All original comoving polynomials have degree at most25")

    targets = [tuple([0]*a + [1]*b) for a, b in pc]
    targets += [tuple([0]*a + [1]*b + [j]) for a, b, j in nc]
    require(len(targets) == len(set(targets)) == 155, "Whole155 retained original output dictionary")
    ti = {v: i for i, v in enumerate(targets)}
    multipliers = [m for d in range(4) for m in itertools.combinations_with_replacement(range(11), d)]
    all_outputs = [m for d in range(1, 6) for m in itertools.combinations_with_replacement(range(11), d)]
    require(len(multipliers) == 364 and len(all_outputs) == 4367
            and sum(sum(j >= 2 for j in m) >= 2 for m in all_outputs) == 4212,
            "Complete degree-three source/degree-five output counts")
    rows, labels, lookup, counts = [], [], {}, [0]*4
    for eq in range(17):
        for mon in multipliers:
            if len(rows) % 128 == 0:
                tick()
            row = {}
            for fm, q in transformed[eq].items():
                key = tuple(sorted(mon+fm))
                col = ti.get(key)
                if col is not None:
                    row[col] = padd(row.get(col, []), q)
            row = {j: v for j, v in row.items() if v}
            nd = sum(j >= 2 for j in mon)
            counts[nd] += 1
            if nd >= 2:
                require(not row, "Each of5100 high-normal rows has zero whole polynomial projection")
            lookup[(eq, mon)] = len(rows)
            labels.append([eq, list(mon)])
            rows.append(row)
    require(len(rows) == 6188 and counts == [170, 918, 2295, 2805], "Complete original source coverage")

    for ri, (eq, a, b) in enumerate(pure_rows):
        require(rows[lookup[(eq, tuple([0]*a+[1]*b))]] == sparse_scaled(compressed[ri], scales[eq]),
                "All170 whole original pure-multiplier rows")
    extras = [x for x in nc if x[1] >= 2]
    ei = {key: 170+i for i, key in enumerate(extras)}
    for eq in range(17):
        ratio = pscale(reduce_poly(core.poly_exact(pure[eq], core.G, "whole primitive g ratio")), scales[eq])
        require(pmul(ratio, gf) == pscale(puref[eq], scales[eq]), "Whole original g ratio retains factor")
        for d in range(3):
            for a in range(d+1):
                b = d-a
                for j in range(2, 11):
                    mon = tuple([0]*a+[1]*b+[j])
                    require(rows[lookup[(eq, mon)]] == sparse_multiple(compressed[ei[(a,b+2,j)]], ratio),
                            "All918 whole original one-normal rows represented without dividing g")
    weights = []
    for i, s in enumerate(physical["compressionOriginalWeights"]):
        q = reduce_poly(core.fmpq_poly([core.fmpq(s)]))
        require(len(q) <= 1, "Constant original g compression weight")
        weights.append((q[0] if q else 0)*pow(scales[i], -1, P) % P)
    for key, ri in ei.items():
        a, b, j = key
        mon = tuple([0]*a+[1]*(b-2)+[j])
        reconstructed = {}
        for eq, w in enumerate(weights):
            for col, q in rows[lookup[(eq, mon)]].items():
                reconstructed[col] = padd(reconstructed.get(col, []), pscale(q, w))
        reconstructed = {j: q for j, q in reconstructed.items() if q}
        require(reconstructed == compressed[ri], "All54 retained g rows reconstructed from true original sources")

    N = args.degree
    sparse_taylor = [{j: taylor(q, args.center, N) for j, q in row.items()} for row in rows]
    dense_comp = [[taylor(row.get(j, []), args.center, N) for j in range(155)] for row in compressed]
    series = [e.DF.mat(224, 155, [dense_comp[i][j][k] for i in range(224) for j in range(155)])
              for k in range(N+1)]
    metadata = {
        "prime": P, "center": args.center, "TaylorDegree": N,
        "sourceNormalCounts": counts, "originalSourceCount": 6188,
        "originalOutputCount": 4367, "wholeWCoordinateCount": 4212,
        "all18OriginalNormalizationConstantsAre31Units": True,
        "all476PhysicalPrimitiveWholePolynomialIdentitiesVerified": True,
        "allWholeRationalProjectionCoefficients31Integral": True,
        "all1088WholeNontrivialProjectedRowsAnd54ReverseCombinationsVerified": True,
        "all5100HighProjectedSourceRowsIdenticallyZero": True,
        "noGFactorDividedAway": True,
        "originalIntegerScalarCoefficientCount": scalar_count,
        "wholeOriginalProjectedRowsLogicalSha256": sha(canonical(rows)),
        "sourceDictionaryLogicalSha256": sha(canonical(labels)),
        "targetDictionaryLogicalSha256": sha(canonical(targets)),
        "compressedTaylorCoefficientSha256": [e.mh(X) for X in series],
        "physicalOriginalConstruction": physical,
    }
    rec["parameters"]["originalConstruction"] = metadata
    return series, sparse_taylor


def full_product(e, rows, lift, k):
    """Every original row, including the explicitly verified high zero rows."""
    width = lift[0].ncols()
    ans = e.DF.mat(6188, width)
    cache = [matrix_rows(X) for X in lift[:k+1]]
    for i, row in enumerate(rows):
        if i % 128 == 0:
            tick()
        for j, coeff in row.items():
            for d in range(min(k, len(coeff)-1)+1):
                if k-d >= len(cache) or not coeff[d]:
                    continue
                v = coeff[d]
                for a, w in enumerate(cache[k-d][j]):
                    if w:
                        ans[i, a] = ans[i, a] + v*w
    return ans


def smith(args, e, series, original, rec):
    d, N = e.DF, args.degree
    constant_rank = e.rank(series[0])
    require(0 < constant_rank <= GENERIC_UPPER, "Actual constant rank within paid rational generic upper")
    S, lift, unit = e.unit_schur(series, d, constant_rank)
    require(e.rank(lift[0]) == 155-constant_rank and e.zero(series[0]*lift[0]),
            "Complete original constant head space")
    current, level, valid = S, 0, N
    covered = constant_rank
    positive, profiles = [], [{"order": 0, "rank": constant_rank, "unitProfile": unit}]
    while covered < GENERIC_UPPER:
        tick()
        if not current:
            break
        r = e.rank(current[0])
        if r == 0:
            profiles.append({"order": level, "rank": 0,
                             "remainingColumns": current[0].ncols()})
            current = current[1:]
            level += 1
            continue
        require(level >= 1 and covered+r <= GENERIC_UPPER, "All positive directions counted, generic upper preserved")
        require(valid >= level, "True map prefix suffices for this original positive exit")
        R0, rr = current[0].rref()
        pc = e.pivots(R0, rr)
        active = [d.sub(X, range(155), pc) for X in lift]
        nextS, transform, prof = e.unit_schur(current, d, r)
        nextvalid = min(valid, len(transform)-1)
        nextlift = e.convolution(lift, transform, nextvalid, d)
        positive.append({"exponent": level, "map": active, "validMapDegree": valid})
        covered += r
        profiles.append({"order": level, "rank": r, "cumulativeRank": covered,
                         "unitProfile": prof})
        current, lift, valid = nextS, nextlift, nextvalid
    complete = covered == GENERIC_UPPER
    if complete:
        require(lift[0].ncols() == 13 and all(e.zero(X) for X in current),
                "Actual142 units and all computed remaining residual coefficients zero")
    heads = d.cat([g["map"][0] for g in positive]+[lift[0]])
    require(heads.ncols() == 155-constant_rank and e.rank(heads) == heads.ncols(),
            "All positive and remaining original constant heads independent")

    products_zero, products_leading, lifts = 0, 0, []
    for group in positive:
        degree, L = group["exponent"], group["map"]
        width = L[0].ncols()
        require(len(L) > degree, "Original positive lift contains its actual leading order")
        for k in range(degree):
            prod = full_product(e, original, L, k)
            require(e.zero(prod), "All6188 original products below the positive exponent zero")
            products_zero += 6188*width
        lead = full_product(e, original, L, degree)
        require(e.rank(lead) == width, "Full original leading product has actual exit rank")
        products_leading += 6188*width
        lifts.append({"exponent": degree, "columns": width,
                      "validMapDegree": group["validMapDegree"],
                      "originalHeadSha256": e.mh(L[0]), "fullOriginalLeadingSha256": e.mh(lead)})
    # Every claimed free coefficient is in the true surviving prefix. No
    # zero padding of a short Schur transformation is called a formal lift.
    free_cutoff = valid if complete else min(valid, max(-1, level-1))
    for k in range(free_cutoff+1):
        prod = full_product(e, original, lift, k)
        require(e.zero(prod), "All6188 remaining original finite-jet products zero")
        products_zero += 6188*lift[0].ncols()
    exponents = [g["exponent"] for g in positive for _ in range(g["map"][0].ncols())]
    info = {
        "prime": P, "center": args.center, "complete": complete,
        "constantRank": constant_rank, "cumulativeGenericRank": covered,
        "paidRationalGenericUpper": GENERIC_UPPER,
        "positiveExponents": exponents, "positiveLength": sum(exponents),
        "maximumPositiveExponent": max(exponents, default=0),
        "remainingConstantHeadCount": lift[0].ncols(),
        "remainingTrueJetVerifiedThroughOrder": free_cutoff,
        "allPositiveAndFreeHeadsIndependentInOriginal155Coordinates": True,
        "allOriginal6188PositiveAndRemainingProductsVerified": True,
        "originalZeroProductCoordinates": products_zero,
        "originalLeadingProductCoordinates": products_leading,
        "originalPositiveLifts": lifts,
        "allUnitAndSchurRowsVerifiedAtEveryOrder": True,
        "localLengthNotPrefilled": True,
        "noFull4340Or4354Elimination": True,
        "noCoefficientPrimeSourcePageRepeated": True,
        "finiteRemainingJetsNotAssertedAsSpecifiedInfiniteKernel": True,
        "genericUpperFromIntegralOriginalPAndPaidRationalRank142": True,
        "steps": profiles,
    }
    rec["parameters"]["actualSmith"] = info
    data = {"format": FORMAT+"-temporary-data", "binding": rec["binding"],
            "summary": info,
            "positiveGroups": [{"exponent": g["exponent"], "validMapDegree": g["validMapDegree"],
                                "map": [matrix_rows(X) for X in g["map"]]} for g in positive],
            "remainingMap": [matrix_rows(X) for X in lift],
            "remainingResidual": [matrix_rows(X) for X in current]}
    path = args.out / "original-projection-field31-complete-smith-data.json"
    rec["parameters"]["temporaryData"] = dict(atomic(path, data), path=str(path), temporaryOnly=True)
    return complete


def main():
    global DEADLINE
    ap = argparse.ArgumentParser()
    for k in PINS:
        ap.add_argument("--"+k, type=Path, required=True)
    ap.add_argument("--center", type=int, choices=(1, 2), required=True)
    ap.add_argument("--degree", type=int, default=12)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--seconds", type=float, default=120)
    ap.add_argument("--memory-mib", type=int, default=768)
    args = ap.parse_args()
    require(10 <= args.degree <= 25 and 1 <= args.seconds <= 600
            and 512 <= args.memory_mib <= 2048, "Explicit finite precision and resource bounds")
    args.out.mkdir(parents=True, exist_ok=True)
    resource.setrlimit(resource.RLIMIT_AS, (args.memory_mib << 20, args.memory_mib << 20))
    started = time.monotonic()
    DEADLINE = started+args.seconds
    rec = {"format": FORMAT, "status": "started", "exitCode": 1, "parameters": {}}
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError("Hard mathematical time budget")))
    signal.setitimer(signal.ITIMER_REAL, args.seconds)
    try:
        pins = {k: identity(getattr(args, k), pin) for k, pin in PINS.items()}
        binding_input = {"format": FORMAT, "source": identity(__file__), "inputs": pins,
                         "prime": P, "center": args.center, "TaylorDegree": args.degree,
                         "originalProjectedGenericRankUpper": GENERIC_UPPER}
        rec["binding"] = sha(canonical(binding_input))
        rec["parameters"]["bindingInput"] = binding_input
        e = module_at(args.schur, "paid_field_series_arithmetic")
        core = module_at(args.core, "paid_whole_physical_polynomials")
        gen = module_at(args.generator, "paid_original_physical_generator")
        e.DEADLINE, e.STOP = DEADLINE, False
        series, original = construct(args, e, core, gen, rec)
        complete = smith(args, e, series, original, rec)
        rec.update(status="completed" if complete else "incomplete-actual-prefix", exitCode=0 if complete else 75)
    except Exception as ex:
        budget = isinstance(ex, TimeoutError) or type(ex).__name__ == "BudgetStop"
        rec.update(status="budget-stop" if budget else "failed", exitCode=75 if budget else 1)
        rec["parameters"]["error"] = {"type": type(ex).__name__, "message": str(ex)}
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        rec["elapsedSeconds"] = time.monotonic()-started
        rec["peakRssKiB"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        atomic(args.out / "original-projection-field31-local-smith-receipt.json", rec)
        print(json.dumps(rec, sort_keys=True), flush=True)
    return rec["exitCode"]


if __name__ == "__main__":
    sys.exit(main())
