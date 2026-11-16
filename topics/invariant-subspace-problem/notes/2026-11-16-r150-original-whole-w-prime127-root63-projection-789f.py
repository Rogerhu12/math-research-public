#!/usr/bin/env python3
"""Original 6188-source projection at (127,s-63), without a full A elimination.

AI-assisted: ChatGPT / literature_audit, 2026-11-16.
Only temporary mathematical outputs. No mathematical work on import.
The old polynomial core is used only for the original coefficient construction
and the proved 224-row compression, never its later gcd or row-module phases.
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

FORMAT = "r150-original-whole-w-prime127-root63-projection-v1"
PRIME, POINT = 127, 63
CORE = (34432, "727175cf485a8ba5b5146a4cc6e749962e109c9e42265a2dd45f58cecdf933fb")
GENERATOR = (15328, "2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186")
PRIMITIVE = (65159, "44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe")
DECODED = (158741, "fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3")
DEADLINE = float("inf")


class BudgetStop(Exception):
    pass


def require(v, message):
    if not v:
        raise AssertionError(message)


def tick():
    if time.monotonic() >= DEADLINE:
        raise BudgetStop("Budget reached at an original verification boundary")


def canonical(x):
    return (json.dumps(x, sort_keys=True, ensure_ascii=True,
                       separators=(",", ":")) + "\n").encode("ascii")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def identify(path, expected=None):
    b = Path(path).read_bytes()
    got = (len(b), sha(b))
    if expected is not None:
        require(got == expected, "Complete input identity: " + str(path))
    return {"bytes": got[0], "sha256": got[1]}


def atomic(path, obj):
    path = Path(path)
    b = canonical(obj)
    tmp = path.with_name(path.name + ".tmp-" + str(os.getpid()))
    with tmp.open("wb") as f:
        f.write(b)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)
    return {"bytes": len(b), "sha256": sha(b)}


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def dot(a, b):
    return sum(x * y for x, y in zip(a, b)) % PRIME


def mm(A, B):
    BT = list(zip(*B))
    return [[dot(a, b) for b in BT] for a in A]


def rank_profile(A):
    """Original row and column profile; all dependent rows are actually reduced."""
    basis, columns, original_rows = [], [], []
    for ri, row in enumerate(A):
        if ri % 64 == 0:
            tick()
        v = row[:]
        for c, b in zip(columns, basis):
            q = v[c]
            if q:
                v = [(a - q * z) % PRIME for a, z in zip(v, b)]
        nz = next((j for j, x in enumerate(v) if x), None)
        if nz is None:
            continue
        inv = pow(v[nz], -1, PRIME)
        v = [(x * inv) % PRIME for x in v]
        # Insertion keeps all leading positions increasing; old basis rows
        # above the insertion may have later entries, so clear the new pivot.
        pos = next((i for i, c in enumerate(columns) if c > nz), len(columns))
        for i in range(pos):
            q = basis[i][nz]
            if q:
                basis[i] = [(a - q * z) % PRIME for a, z in zip(basis[i], v)]
        basis.insert(pos, v)
        columns.insert(pos, nz)
        original_rows.insert(pos, ri)
    require(all(b[c] == 1 for b, c in zip(basis, columns)), "Pivot units")
    require(all(b[j] == 0 for b, c in zip(basis, columns) for j in range(c)),
            "Complete leading zero prefixes")
    return basis, original_rows, columns


def determinant(A):
    n = len(A)
    B = [r[:] for r in A]
    d = 1
    for j in range(n):
        k = next((k for k in range(j, n) if B[k][j]), None)
        if k is None:
            return 0
        if k != j:
            B[j], B[k] = B[k], B[j]
            d = -d
        v = B[j][j]
        d = d * v % PRIME
        inv = pow(v, -1, PRIME)
        for k in range(j + 1, n):
            q = B[k][j] * inv % PRIME
            if q:
                for c in range(j, n):
                    B[k][c] = (B[k][c] - q * B[j][c]) % PRIME
    return d % PRIME


def kernel_from_basis(basis, pivots, n):
    free = [j for j in range(n) if j not in set(pivots)]
    K = [[0] * len(free) for _ in range(n)]
    for a, f in enumerate(free):
        v = [0] * n
        v[f] = 1
        for row, p in reversed(list(zip(basis, pivots))):
            v[p] = -sum(row[j] * v[j] for j in range(p + 1, n)) % PRIME
        for j in range(n):
            K[j][a] = v[j]
    require([[K[i][j] for j in range(len(free))] for i in free]
            == [[int(i == j) for j in range(len(free))] for i in range(len(free))],
            "Full point-kernel free normalization")
    return K, free


def value(poly):
    den = int(poly.denom())
    require(den % PRIME != 0, "A whole rational polynomial denominator is a 127 unit")
    return int(poly.numer()(POINT)) * pow(den % PRIME, -1, PRIME) % PRIME


def horner(coeffs):
    y = 0
    for x in reversed(coeffs):
        y = (y * POINT + int(x)) % PRIME
    return y


def run(args, receipt):
    identities = {
        "source": identify(__file__), "polynomialCore": identify(args.core, CORE),
        "physicalGenerator": identify(args.generator, GENERATOR),
        "originalPrimitive": identify(args.primitive, PRIMITIVE),
    }
    binding_object = {"format": FORMAT, "inputs": identities, "prime": PRIME,
                      "point": POINT, "fullSources": 6188, "fullOutputs": 4367,
                      "projectedOutputs": 155, "sourceDegreeAtMost": 3,
                      "outputDegreeAtMost": 5, "ordinaryMonomials": True}
    receipt["binding"] = sha(canonical(binding_object))
    receipt["parameters"]["bindingObject"] = binding_object
    core = load_module(args.core, "paid_original_polynomial_core")
    generator = load_module(args.generator, "paid_original_physical_generator")
    core.DEADLINE = DEADLINE
    raw = gzip.decompress(Path(args.primitive).read_bytes())
    require((len(raw), sha(raw)) == DECODED, "Whole decoded original primitive identity")
    primitive = json.loads(raw)
    require(primitive["format"] == "r150-original-primitive-integer-equations-v1",
            "Original primitive format")
    equations = primitive["equations"]
    require(len(equations) == 17 and all(len(r) == 77 for r in equations),
            "All original 17 by 77 coefficient polynomials")
    denominator = int(primitive["denominator"])
    contents = [int(x) for x in primitive["contents"]]
    require(denominator == 23366320238786911411830138211362846399922176000
            and len(contents) == 17 and denominator % PRIME
            and all(x % PRIME for x in contents), "All18 original normalization units")
    scales = [denominator * pow(c % PRIME, -1, PRIME) % PRIME for c in contents]

    pure, linear, physical = core.original_polynomials(generator)
    P, pc, nc, pure_rows = core.build_P(pure, linear)
    physical_polynomials = pure + [p for ent in linear for mode in ent for p in mode]
    # Whole denominators, not just values after cancellation at this point.
    physical_values = [value(q) for q in physical_polynomials]
    require(len(physical_values) == 476, "All original pure/linear physical polynomials")
    pure_value = [value(q) for q in pure]
    linear_value = [[[value(q) for q in mode] for mode in ent] for ent in linear]
    Pfield = [[value(q) for q in row] for row in P]
    g = value(core.G)
    require(g != 0, "Actual contact factor is a unit at the chosen point")
    dlinear = value(core.DLINEAR)

    # Original parameter-binomial moment change and its inverse.
    T = [[math.comb(i, j) * pow(POINT, i-j, PRIME) % PRIME if i >= j else 0
          for j in range(11)] for i in range(11)]
    Ti = [[math.comb(i, j) * pow(-POINT, i-j, PRIME) % PRIME if i >= j else 0
           for j in range(11)] for i in range(11)]
    I = [[int(i == j) for j in range(11)] for i in range(11)]
    require(mm(T, Ti) == I and mm(Ti, T) == I, "Both full binomial inverse products")
    ordinary = [(j,) for j in range(11)] + list(itertools.combinations_with_replacement(range(11), 2))
    require(len(ordinary) == 77, "All original ordinary monomials")
    fields = []
    for eq, row in enumerate(equations):
        tick()
        f = {}
        for mon, coeff in zip(ordinary, row):
            q = horner(coeff)
            if len(mon) == 1:
                a = mon[0]
                for j in range(a + 1):
                    key = (j,)
                    f[key] = (f.get(key, 0) + q * T[a][j]) % PRIME
            else:
                a, b = mon
                for j in range(a + 1):
                    for k in range(b + 1):
                        key = tuple(sorted((j, k)))
                        f[key] = (f.get(key, 0) + q * T[a][j] * T[b][k]) % PRIME
        fields.append({k: v for k, v in f.items() if v})
        require(all(f.get(k, 0) == 0 for k in ((0,), (1,), (0, 0), (0, 1))),
                "Every original pure-plane term except d squared is zero")
        require(f.get((1, 1), 0) == scales[eq] * pure_value[eq] % PRIME,
                "Physical/primitive pure coefficient with true row unit")
        for j in range(2, 11):
            for mode, mon in enumerate(((j,), (0, j), (1, j))):
                require(f.get(mon, 0) == scales[eq] * linear_value[j-2][mode][eq] % PRIME,
                        "Every physical/primitive low coefficient with true row unit")

    targets = [tuple([0] * a + [1] * b) for a, b in pc]
    targets += [tuple([0] * a + [1] * b + [j]) for a, b, j in nc]
    require(len(targets) == len(set(targets)) == 155, "Complete original projected target dictionary")
    target_index = {m: i for i, m in enumerate(targets)}
    multipliers = [m for d in range(4)
                   for m in itertools.combinations_with_replacement(range(11), d)]
    full_targets = [m for d in range(1, 6)
                    for m in itertools.combinations_with_replacement(range(11), d)]
    require(len(multipliers) == 364 and len(full_targets) == 4367
            and sum(sum(j >= 2 for j in m) >= 2 for m in full_targets) == 4212,
            "Whole degree-three source and degree-five target dictionaries")
    source_labels, full_rows, normal_counts = [], [], [0] * 4
    lookup = {}
    for eq in range(17):
        for mon in multipliers:
            if len(full_rows) % 128 == 0:
                tick()
            row = [0] * 155
            for fmon, v in fields[eq].items():
                product = tuple(sorted(mon + fmon))
                ci = target_index.get(product)
                if ci is not None:
                    row[ci] = (row[ci] + v) % PRIME
            nd = sum(j >= 2 for j in mon)
            normal_counts[nd] += 1
            if nd >= 2:
                require(not any(row), "Every original higher-normal source has zero whole projection")
            lookup[(eq, mon)] = len(full_rows)
            source_labels.append([eq, list(mon)])
            full_rows.append(row)
    require(len(full_rows) == 6188 and normal_counts == [170, 918, 2295, 2805],
            "Complete original source coverage, including all5100 higher-normal rows")

    # Both inclusions for the genuine 224-row compression.
    checked_forward = 0
    for ri, (eq, a, b) in enumerate(pure_rows):
        mon = tuple([0] * a + [1] * b)
        require(full_rows[lookup[(eq, mon)]] == [scales[eq] * x % PRIME for x in Pfield[ri]],
                "Every original pure-multiplier row matches the compressed row")
        checked_forward += 1
    extras = [k for k in nc if k[1] >= 2]
    extra_index = {key: 170 + i for i, key in enumerate(extras)}
    for eq in range(17):
        ratio = scales[eq] * pure_value[eq] * pow(g, -1, PRIME) % PRIME
        for d in range(3):
            for a in range(d + 1):
                b = d - a
                for j in range(2, 11):
                    mon = tuple([0] * a + [1] * b + [j])
                    require(full_rows[lookup[(eq, mon)]] ==
                            [ratio * x % PRIME for x in Pfield[extra_index[(a, b+2, j)]]],
                            "Every original one-normal row matches its actual g row")
                    checked_forward += 1
    require(checked_forward == 1088, "All1088 projected original source rows, no omission")
    weights = [value(core.fmpq_poly([core.fmpq(s)])) * pow(scales[i], -1, PRIME) % PRIME
               for i, s in enumerate(physical["compressionOriginalWeights"])]
    for key, ri in extra_index.items():
        a, b, j = key
        mon = tuple([0] * a + [1] * (b-2) + [j])
        rebuilt = [sum(weights[i] * full_rows[lookup[(i, mon)]][c] for i in range(11)) % PRIME
                   for c in range(155)]
        require(rebuilt == Pfield[ri], "Every retained g row is a true original source combination")

    basis, row_profile, column_profile = rank_profile(full_rows)
    compressed_basis, _, _ = rank_profile(Pfield)
    rank = len(basis)
    require(rank == len(compressed_basis), "Independent full/224-row point ranks agree")
    minor = [[full_rows[i][j] for j in column_profile] for i in row_profile]
    minor_det = determinant(minor)
    require(minor_det != 0, "Selected actual original-source point minor is a unit")
    K, free = kernel_from_basis(basis, column_profile, 155)
    checked_products = 0
    for i, row in enumerate(full_rows):
        if i % 128 == 0:
            tick()
        nz = [(j, x) for j, x in enumerate(row) if x]
        for k in range(len(free)):
            require(sum(x * K[j][k] for j, x in nz) % PRIME == 0,
                    "Full6188-source point-kernel product")
            checked_products += 1
    require(checked_products == 6188 * (155-rank), "Every original point-kernel coordinate checked")

    data = {"format": FORMAT + "-temporary-data", "binding": receipt["binding"],
            "prime": PRIME, "point": POINT, "compressed224": Pfield,
            "originalSourceRowProfile": row_profile,
            "originalSourceLabelsOnProfile": [source_labels[i] for i in row_profile],
            "projectedTargetColumnProfile": column_profile,
            "originalUnitMinor": minor, "originalUnitMinorDeterminant": minor_det,
            "completePointKernel155": K, "freeCoordinates": free,
            "full6188By155LogicalSha256": sha(canonical(full_rows)),
            "originalSourceDictionaryLogicalSha256": sha(canonical(source_labels)),
            "originalProjectedTargetDictionaryLogicalSha256": sha(canonical(targets))}
    data_path = args.out / "original-whole-w127-root63-point-data.json"
    data_id = atomic(data_path, data)
    receipt["parameters"].update({
        "originalPrimitiveDecoded": {"bytes": len(raw), "sha256": sha(raw)},
        "originalScalarCoefficientCount": sum(len(q) for row in equations for q in row),
        "all18OriginalNormalizationConstantsAre127Units": True,
        "all476PhysicalPolynomialDenominatorsAre127Units": True,
        "wholePhysicalPrimitiveLowComparisons": 476,
        "physicalOriginalConstruction": physical,
        "sourceNormalCounts": normal_counts, "all4367OutputCoordinatesAccountedFor": True,
        "projectedOutputs": 155, "wholeWOutputCoordinates": 4212,
        "sourceBinomialChangeIsUnipotentAtEveryDegree": True,
        "both11By11MomentInverseProductsVerified": True,
        "all1088NontrivialSourceCompressionRowsVerified": True,
        "all54GSourceRowsReconstructedFromOriginalEquations": True,
        "all5100HigherNormalSourceProjectionRowsZero": True,
        "contactFactorAtPoint": g, "DlinearAtPoint": dlinear,
        "pointRankOfWhole6188Projection": rank,
        "pointRankOfCompressed224Projection": len(compressed_basis),
        "originalPointMinorSize": rank, "originalPointMinorDeterminant": minor_det,
        "completePointKernelDimension": len(free),
        "allOriginalPointKernelProductsZero": True,
        "originalPointKernelProductsChecked": checked_products,
        "temporaryData": dict(data_id, file=data_path.name, temporaryOnly=True),
        "full6188By155LogicalSha256": data["full6188By155LogicalSha256"],
        "noFull4367By6188Elimination": True, "noOldFiniteFieldPointRankUsed": True,
        "noRationalRankPromotedFromField": True,
        "moduleInterpretationRequiresPublishedWhole299AndIntegralCarrierTheorems": True,
        "newExpandedOriginalSourcesClaimed": False,
    })
    receipt["status"] = "complete"
    receipt["exitCode"] = 0


def main():
    global DEADLINE
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", required=True, type=Path)
    ap.add_argument("--generator", required=True, type=Path)
    ap.add_argument("--primitive", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--seconds", type=float, default=90)
    ap.add_argument("--memory-mib", type=int, default=768)
    args = ap.parse_args()
    require(1 <= args.seconds <= 600 and 256 <= args.memory_mib <= 2048, "Explicit resource bounds")
    args.out.mkdir(parents=True, exist_ok=True)
    resource.setrlimit(resource.RLIMIT_AS, (args.memory_mib << 20, args.memory_mib << 20))
    started = time.monotonic()
    DEADLINE = started + args.seconds
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(BudgetStop("Hard time budget")))
    signal.setitimer(signal.ITIMER_REAL, args.seconds)
    receipt = {"format": FORMAT, "status": "started", "exitCode": 1,
               "parameters": {"prime": PRIME, "point": POINT}}
    try:
        run(args, receipt)
    except BudgetStop as ex:
        receipt.update(status="budget-stop", exitCode=75)
        receipt["parameters"]["error"] = {"type": type(ex).__name__, "message": str(ex)}
    except Exception as ex:
        is_budget = type(ex).__name__ == "BudgetStop"
        receipt.update(status="budget-stop" if is_budget else "failed", exitCode=75 if is_budget else 1)
        receipt["parameters"]["error"] = {"type": type(ex).__name__, "message": str(ex)}
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        receipt["elapsedSeconds"] = time.monotonic() - started
        receipt["peakRssKiB"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        path = args.out / "original-whole-w127-root63-projection-receipt.json"
        atomic(path, receipt)
        print(json.dumps(receipt, sort_keys=True, ensure_ascii=True), flush=True)
    return receipt["exitCode"]


if __name__ == "__main__":
    sys.exit(main())
