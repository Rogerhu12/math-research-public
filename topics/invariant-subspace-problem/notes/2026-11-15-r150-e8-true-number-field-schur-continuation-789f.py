#!/usr/bin/env python3
"""Exact E8 local Schur steps in the actual number field, without 408x288 RREF.

Astra-ISP-789f / literature_audit; AI-assisted, GPT-6 Astra Pro.
All original low rows and the proved full224-row embedding are rebuilt by the
pinned original driver. Only identically zero columns and nonzero rational row
contents are removed. Number-field Bareiss selects a genuine constant unit;
all Taylor right-hand sides are solved in that unit and multiplied back.
Temporary checkpoints save complete field arrays after each Bareiss pivot,
LU, solved Taylor coefficient, and verified Schur phase. No big data is published.

APIs: python-flint0.9 fmpq_poly divmod and xgcd, official documentation:
https://python-flint.readthedocs.io/en/latest/fmpq_poly.html
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from math import comb, gcd
from pathlib import Path
import resource
import signal
import sys
import time
from flint import fmpq, fmpq_poly

BASE_SHA = "4d215c80fa40d5f3548fd604e4ed77c6317db44b5b80518a03cf15e2ceeffa2f"
GENERATOR_SHA = "2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACTIONS_SHA = "2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
FORMAT = "r150-e8-true-number-field-schur-v1"
E8 = [9600, -25472, -3392, 15936, -2888, -936, 153, 50, 5]


def require(ok, text):
    if not ok:
        raise AssertionError(text)


def sha_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1048576), b""):
            h.update(chunk)
    return h.hexdigest()


def module_at(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def atom(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=1, mtime=0) as out:
            out.write(canonical(obj))
    tmp.replace(path)


class Field:
    def __init__(self):
        self.degree = 8
        self.modulus = fmpq_poly([fmpq(x, 5) for x in E8])
        self.zero = fmpq_poly([])
        self.one = fmpq_poly([1])
        self.alpha = fmpq_poly([0, 1])
        require(self.modulus.degree() == 8 and self.modulus[8] == 1,
                "Original E8/5 is the exact monic field polynomial")
        self.mul_count = 0
        self.inv_count = 0

    def mul(self, a, b):
        if not a or not b:
            return self.zero
        self.mul_count += 1
        return (a * b) % self.modulus

    def inv(self, a):
        require(bool(a), "Only nonzero actual field elements may be inverted")
        self.inv_count += 1
        g, s, t = a.xgcd(self.modulus)
        require(g.degree() == 0 and bool(g),
                "The previously proved irreducible E8 gives a field")
        require(s * a + t * self.modulus == g,
                "Official xgcd Bezout identity checked before inversion")
        z = (s / g[0]) % self.modulus
        require(self.mul(a, z) == self.one, "Actual field inverse identity")
        return z

    def encode(self, a):
        return [str(x) for x in a.coeffs()]

    def decode(self, a):
        z = fmpq_poly([fmpq(x) for x in a])
        require(z.degree() < self.degree, "Canonical field coefficient degree")
        return z

    def matrix_json(self, a):
        return [[self.encode(x) for x in row] for row in a]

    def matrix_from_json(self, a):
        require(isinstance(a, list), "Actual field matrix array")
        cols = len(a[0]) if a else 0
        require(all(len(r) == cols for r in a), "Rectangular field matrix")
        return [[self.decode(x) for x in row] for row in a]

    def matrix_hash(self, a):
        return hashlib.sha256(canonical({
            "rows": len(a), "columns": len(a[0]) if a else 0,
            "degree": self.degree, "entries": self.matrix_json(a)})).hexdigest()

    def score(self, a):
        return (max((abs(int(x)).bit_length() for x in a.numer().coeffs()),
                    default=0) + abs(int(a.denom())).bit_length(),
                a.degree())


def shape(a):
    return len(a), len(a[0]) if a else 0


def zeros(F, r, c):
    return [[F.zero for _ in range(c)] for _ in range(r)]


def identity(F, n):
    a = zeros(F, n, n)
    for i in range(n):
        a[i][i] = F.one
    return a


def zero_matrix(a):
    return all(not x for row in a for x in row)


def submatrix(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def subtract(a, b):
    require(shape(a) == shape(b), "Matrix subtraction shape")
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def product(F, a, b):
    nr, nk = shape(a)
    nk2, nc = shape(b)
    require(nk == nk2, "Complete field product shape")
    out = zeros(F, nr, nc)
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        out[i][j] = out[i][j] + F.mul(x, y)
    return out


class Cache:
    def __init__(self, directory, binding):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.binding = binding
        self.path = self.directory / "manifest.json"
        if self.path.exists():
            self.manifest = json.loads(self.path.read_text())
            require(self.manifest["format"] == FORMAT and
                    self.manifest["binding"] == binding,
                    "Portable checkpoint semantic binding")
        else:
            self.manifest = {"format": FORMAT, "binding": binding, "stages": {}}
            self.flush()

    def flush(self):
        raw = canonical(self.manifest)
        tmp = self.path.with_name("manifest.json.tmp")
        tmp.write_bytes(raw)
        tmp.replace(self.path)

    def put(self, name, obj, verified):
        require("/" not in name, "Local phase checkpoint name")
        payload = {"format": FORMAT, "binding": self.binding,
                   "stage": name, "verified": bool(verified), "payload": obj}
        # Immutable generations keep the previous complete manifest valid if
        # interrupted after the array write and before its atomic update.
        generation = hashlib.sha256(canonical(payload)).hexdigest()
        path = self.directory / (name + "-" + generation + ".json.gz")
        atom(path, payload)
        record = {"file": path.name, "bytes": path.stat().st_size,
                  "sha256": sha_file(path), "verified": bool(verified)}
        self.manifest["stages"][name] = record
        self.flush()
        return record

    def get(self, name):
        record = self.manifest["stages"].get(name)
        if record is None:
            return None
        path = self.directory / record["file"]
        require(path.stat().st_size == record["bytes"] and
                sha_file(path) == record["sha256"], "Actual saved field-array bytes")
        with gzip.open(path, "rt") as f:
            obj = json.load(f)
        require(obj["format"] == FORMAT and obj["binding"] == self.binding and
                obj["stage"] == name and obj["verified"] == record["verified"],
                "Complete phase binding")
        return obj["payload"]


def normalize_and_taylor(F, small, order):
    nr, nc = small[0].nrows(), small[0].ncols()
    require((nr, nc) == (51, 36), "All51 original low rows and36 columns")
    zero_cols = [j for j in range(nc)
                 if all(not small[k][i, j] for k in range(26) for i in range(nr))]
    keep = [j for j in range(nc) if j not in zero_cols]
    require(len(zero_cols) == 6, "Exactly six polynomial zero pure columns")
    row_units = []
    for i in range(nr):
        values = [small[k][i, j] for k in range(26) for j in keep if small[k][i, j]]
        if not values:
            row_units.append(fmpq(1))
            continue
        den = 1
        for x in values:
            q = int(x.q)
            den = den // gcd(den, q) * q
        numer = 0
        for x in values:
            numer = gcd(numer, abs(int(x.p) * (den // int(x.q))))
        unit = fmpq(numer, den)
        require(bool(unit), "Only a nonzero rational row content is removed")
        row_units.append(unit)
    powers = [F.one]
    for _ in range(25):
        powers.append(F.mul(powers[-1], F.alpha))
    out = [zeros(F, nr, len(keep)) for _ in range(order + 1)]
    for i in range(nr):
        for jj, j in enumerate(keep):
            vals = [small[k][i, j] / row_units[i] for k in range(26)]
            for k in range(26):
                require(vals[k] * row_units[i] == small[k][i, j],
                        "Original rational row-content identity")
            for ell in range(order + 1):
                z = F.zero
                for k in range(ell, 26):
                    if vals[k]:
                        z = z + vals[k] * comb(k, ell) * powers[k - ell]
                out[ell][i][jj] = z
    return out, {
        "all51OriginalLowRowsRetained": True,
        "originalPolynomialZeroRowsRetained": [i for i in range(nr) if not
            any(small[k][i, j] for k in range(26) for j in keep)],
        "sixIdenticallyZeroOriginalColumns": zero_cols,
        "retainedOriginalLowColumns": keep,
        "nonzeroRationalRowContents": [str(x) for x in row_units],
        "allOriginalRowContentIdentitiesVerified": True,
        "fieldTaylorCoefficientsBuiltDirectlyFromAll26OriginalCoefficients": True,
        "numberFieldTaylorCoefficientSHA256": [F.matrix_hash(a) for a in out],
        "numberFieldMatrixShape": [nr, len(keep)],
        "regularRepresentationRREFUsed": False}


def bareiss_profile(F, a, cache, prefix, report):
    nr, nc = shape(a)
    key = prefix + "-bareiss"
    old = cache.get(key)
    if old is None:
        b = [row[:] for row in a]
        rows, cols = list(range(nr)), list(range(nc))
        k, prev = 0, F.one
    else:
        require(old["inputSHA256"] == F.matrix_hash(a), "Same constant field matrix")
        b = F.matrix_from_json(old["matrix"])
        rows, cols = old["rowPermutation"], old["columnPermutation"]
        k, prev = old["pivots"], F.decode(old["previousPivot"])
        if old["complete"]:
            return rows[:k], cols[:k], old
    while k < min(nr, nc):
        candidates = [(F.score(b[i][j]), i, j)
                      for i in range(k, nr) for j in range(k, nc) if b[i][j]]
        if not candidates:
            break
        _, ii, jj = min(candidates)
        b[k], b[ii] = b[ii], b[k]
        rows[k], rows[ii] = rows[ii], rows[k]
        if jj != k:
            for row in b:
                row[k], row[jj] = row[jj], row[k]
            cols[k], cols[jj] = cols[jj], cols[k]
        pivot = b[k][k]
        invprev = F.inv(prev)
        for i in range(k + 1, nr):
            left = b[i][k]
            for j in range(k + 1, nc):
                numerator = F.mul(pivot, b[i][j]) - F.mul(left, b[k][j])
                b[i][j] = F.mul(numerator, invprev)
            b[i][k] = F.zero
        prev = pivot
        k += 1
        data = {"inputSHA256": F.matrix_hash(a), "matrix": F.matrix_json(b),
                "rowPermutation": rows, "columnPermutation": cols,
                "pivots": k, "previousPivot": F.encode(prev), "complete": False}
        cache.put(key, data, False)
        report("constant-profile", k)
    require(zero_matrix(submatrix(b, range(k, nr), range(k, nc))),
            "Complete trailing constant block, no original row dropped")
    data = {"inputSHA256": F.matrix_hash(a), "matrix": F.matrix_json(b),
            "rowPermutation": rows, "columnPermutation": cols,
            "pivots": k, "previousPivot": F.encode(prev), "complete": True}
    cache.put(key, data, False)
    return rows[:k], cols[:k], data


def lu_factor(F, a, cache, prefix):
    key = prefix + "-unit-lu"
    old = cache.get(key)
    if old is not None:
        require(old["inputSHA256"] == F.matrix_hash(a), "Same actual field unit")
        return F.matrix_from_json(old["L"]), F.matrix_from_json(old["U"]), old["rows"]
    n, nc = shape(a)
    require(n == nc, "Only the actual square field unit is factored")
    u = [row[:] for row in a]
    l = identity(F, n)
    rows = list(range(n))
    for k in range(n):
        options = [(F.score(u[i][k]), i) for i in range(k, n) if u[i][k]]
        require(options, "Actual selected constant unit is nonsingular")
        _, ii = min(options)
        if ii != k:
            u[k], u[ii] = u[ii], u[k]
            rows[k], rows[ii] = rows[ii], rows[k]
            for j in range(k):
                l[k][j], l[ii][j] = l[ii][j], l[k][j]
        inv = F.inv(u[k][k])
        for i in range(k + 1, n):
            if not u[i][k]:
                continue
            q = F.mul(u[i][k], inv)
            l[i][k] = q
            for j in range(k + 1, n):
                u[i][j] = u[i][j] - F.mul(q, u[k][j])
            u[i][k] = F.zero
    require(product(F, l, u) == [a[i] for i in rows],
            "Full original selected constant unit LU product")
    cache.put(key, {"inputSHA256": F.matrix_hash(a), "L": F.matrix_json(l),
                    "U": F.matrix_json(u), "rows": rows,
                    "allOriginalUnitEntriesVerified": True}, True)
    return l, u, rows


def lu_solve(F, factor, b):
    l, u, rows = factor
    n, q = shape(b)
    require(len(rows) == n, "Unit right-hand-side row count")
    y = [[b[rows[i]][j] for j in range(q)] for i in range(n)]
    for i in range(n):
        for k in range(i):
            if l[i][k]:
                for j in range(q):
                    y[i][j] = y[i][j] - F.mul(l[i][k], y[k][j])
    x = [row[:] for row in y]
    for i in range(n - 1, -1, -1):
        for k in range(i + 1, n):
            if u[i][k]:
                for j in range(q):
                    x[i][j] = x[i][j] - F.mul(u[i][k], x[k][j])
        inv = F.inv(u[i][i])
        for j in range(q):
            x[i][j] = F.mul(x[i][j], inv)
    return x


def field_schur(F, series, exponent, cache, report):
    prefix = "phase-" + str(exponent)
    source_hashes = [F.matrix_hash(a) for a in series]
    done = cache.get(prefix + "-schur")
    if done is not None:
        require(done["sourceSHA256"] == source_hashes, "Same entire input Taylor series")
        return [F.matrix_from_json(a) for a in done["residual"]], done["phase"]
    a0 = series[0]
    nr, nc = shape(a0)
    rows, cols, _ = bareiss_profile(F, a0, cache, prefix, report)
    rank = len(rows)
    remrows = [i for i in range(nr) if i not in set(rows)]
    remcols = [j for j in range(nc) if j not in set(cols)]
    if not rank:
        residual = [[row[:] for row in a] for a in series]
        require(zero_matrix(residual[0]), "Zero constant block before division")
        phase = {"exponent": exponent, "rows": nr, "columns": nc, "rank": 0,
                 "selectedUnitRows": [], "selectedUnitColumns": [],
                 "allOriginalSchurEntriesVerified": True,
                 "sourceSHA256": source_hashes,
                 "residualSHA256": [F.matrix_hash(a) for a in residual]}
        cache.put(prefix + "-schur", {"sourceSHA256": source_hashes,
                                     "residual": [F.matrix_json(a) for a in residual],
                                     "phase": phase}, True)
        return residual, phase
    unit = [submatrix(a, rows, cols) for a in series]
    rhs = [submatrix(a, rows, remcols) for a in series]
    lower = [submatrix(a, remrows, cols) for a in series]
    lower_right = [submatrix(a, remrows, remcols) for a in series]
    factor = lu_factor(F, unit[0], cache, prefix)
    solutions = []
    residual = []
    for k in range(len(series)):
        key = prefix + "-solution-" + str(k)
        old = cache.get(key)
        b = [row[:] for row in rhs[k]]
        for ell in range(1, k + 1):
            b = subtract(b, product(F, unit[ell], solutions[k - ell]))
        if old is not None:
            require(old["rhsSHA256"] == F.matrix_hash(b) and
                    old["unitSHA256"] == F.matrix_hash(unit[0]),
                    "Every resumed actual Taylor right-hand side")
            x = F.matrix_from_json(old["solution"])
        else:
            x = lu_solve(F, factor, b)
            cache.put(key, {"rhsSHA256": F.matrix_hash(b),
                            "unitSHA256": F.matrix_hash(unit[0]),
                            "solution": F.matrix_json(x)}, False)
        require(product(F, unit[0], x) == b,
                "Every original selected-unit coordinate multiplied back")
        cache.put(key, {"rhsSHA256": F.matrix_hash(b),
                        "unitSHA256": F.matrix_hash(unit[0]),
                        "solution": F.matrix_json(x),
                        "allOriginalUnitEntriesVerified": True}, True)
        solutions.append(x)
        r = [row[:] for row in lower_right[k]]
        for ell in range(k + 1):
            r = subtract(r, product(F, lower[ell], solutions[k - ell]))
        require(shape(r) == (nr - rank, nc - rank), "All complementary original rows")
        residual.append(r)
        report("actual-taylor-unit-solution", k)
    require(zero_matrix(residual[0]),
            "The full complementary constant Schur block vanishes")
    phase = {"exponent": exponent, "rows": nr, "columns": nc, "rank": rank,
             "selectedUnitRows": rows, "selectedUnitColumns": cols,
             "allOriginalUnitEntriesVerified": True,
             "allOriginalSchurEntriesVerified": True,
             "originalSchurScalarCoordinates": (nr-rank)*(nc-rank)*len(series),
             "sourceSHA256": source_hashes,
             "residualSHA256": [F.matrix_hash(a) for a in residual]}
    cache.put(prefix + "-schur", {"sourceSHA256": source_hashes,
                                 "residual": [F.matrix_json(a) for a in residual],
                                 "phase": phase}, True)
    return residual, phase


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base-driver", required=True)
    p.add_argument("--generator", required=True)
    p.add_argument("--jet-actions", required=True)
    p.add_argument("--checkpoint", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--remaining-seconds", type=float, default=300)
    p.add_argument("--memory-mib", type=int, default=2048)
    p.add_argument("--max-order", type=int, default=4)
    args = p.parse_args()
    require(args.remaining_seconds > 0 and 512 <= args.memory_mib <= 8192
            and 1 <= args.max_order <= 7, "Bounded genuine-field continuation")
    identities = {}
    for label, path, expected in (("base", args.base_driver, BASE_SHA),
                                  ("generator", args.generator, GENERATOR_SHA),
                                  ("actions", args.jet_actions, ACTIONS_SHA)):
        require(sha_file(path) == expected, "Pinned original source: " + label)
        identities[label] = {"bytes": Path(path).stat().st_size, "sha256": expected}
    identities["self"] = {"bytes": Path(__file__).stat().st_size,
                           "sha256": sha_file(__file__)}
    binding = hashlib.sha256(canonical({
        "format": FORMAT, "inputFiles": identities, "maxOrder": args.max_order,
        "minimalPolynomial": E8, "coordinate": "s=alpha+t"})).hexdigest()
    resource.setrlimit(resource.RLIMIT_AS,
                       (args.memory_mib * 1024**2, args.memory_mib * 1024**2))
    sys.set_int_max_str_digits(0)
    start = time.monotonic()
    F = Field()
    cache = Cache(args.checkpoint, binding)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    result = {"format": FORMAT, "status": "running", "parameters": {
        "binding": binding, "inputFiles": identities, "maxOrder": args.max_order,
        "field": "Q[alpha]/E8(alpha)", "minimalPolynomialAscending": E8,
        "paidFullOriginalLengthUpperBound": 5, "paidLowGenericRank": 27,
        "paidLowConstantRank": 25, "paidFullProjectionGenericRank": 142,
        "regularRepresentationRREFUsed": False, "exactTaylorPhases": [],
        "largeDataUploadedOrCommitted": False}}
    def save():
        result["elapsedSeconds"] = time.monotonic() - start
        result["parameters"]["checkpointManifest"] = {
            "bytes": cache.path.stat().st_size, "sha256": sha_file(cache.path),
            "stages": cache.manifest["stages"]}
        result["parameters"]["fieldMultiplications"] = F.mul_count
        result["parameters"]["fieldInversions"] = F.inv_count
        raw = canonical(result)
        require(len(raw) < 90000, "Small proof receipt below publisher limit")
        tmp = out.with_name(out.name + ".tmp")
        tmp.write_bytes(raw)
        tmp.replace(out)
    def report(stage, k):
        result["parameters"]["currentStage"] = stage
        result["parameters"]["currentIndex"] = k
        save()
    def stop(signum, frame):
        raise TimeoutError("Shared genuine E8 field budget exhausted")
    signal.signal(signal.SIGALRM, stop)
    signal.signal(signal.SIGTERM, stop)
    signal.setitimer(signal.ITIMER_REAL, args.remaining_seconds)
    try:
        base = module_at("r150_e8_field_original_base", args.base_driver)
        m = module_at("r150_e8_field_original_generator", args.generator)
        actions = module_at("r150_e8_field_original_actions", args.jet_actions)
        small, coeff, physical = base.original_low_polynomial_model(m, actions)
        result["parameters"].update(physical)
        _, field_meta = base.field_model(m, coeff)
        result["parameters"].update(field_meta)
        series, normalization = normalize_and_taylor(F, small, args.max_order)
        result["parameters"].update(normalization)
        cache.put("original-field-series",
                  {"series": [F.matrix_json(a) for a in series],
                   "normalization": normalization}, True)
        save()
        covered = 0
        length = 0
        for exponent in range(args.max_order + 1):
            residual, phase = field_schur(F, series, exponent, cache, report)
            rank = phase["rank"]
            if exponent == 0:
                require(rank == 25, "Actual E8 low constant rank25")
            covered += rank
            require(covered <= 27, "Paid low generic rank27")
            length += exponent * rank
            lower = length + (exponent + 1) * (27 - covered)
            require(lower <= 5, "Embedded small length below paid full E8 length5")
            phase.update({"coveredRank": covered, "smallLengthLowerBound": lower})
            result["parameters"]["exactTaylorPhases"].append(phase)
            result["parameters"].update({
                "smallTorsionLengthLowerBound": lower,
                "projectedOriginalLengthLowerBound": lower,
                "fullOriginalLocalLengthLowerBound": lower})
            save()
            if covered == 27:
                require(all(zero_matrix(a) for a in residual),
                        "Remaining original field jets vanish at generic rank27")
                result["parameters"].update({
                    "smallGenericRankReached": True,
                    "smallTorsionLengthExact": length,
                    "smallFreeRankIncludingSixExactColumns": 9})
                break
            if exponent == args.max_order:
                result["parameters"].update({
                    "smallGenericRankReached": False,
                    "smallTorsionLengthExact": None,
                    "unresolvedSmallPositiveFactors": 27-covered,
                    "smallFreeRankIncludingSixExactColumns": 9})
                break
            require(zero_matrix(residual[0]), "Only a genuine t factor divided")
            series = residual[1:]
        lower = result["parameters"]["smallTorsionLengthLowerBound"]
        gap = 5 - lower
        result["parameters"].update({
            "allOriginalLowAndFullProjectedEmbeddingsVerified": True,
            "allTaylorUnitAndFullSchurIdentitiesVerified": True,
            "lowerBoundUsesJetInjectionPlusFourExactPureColumns": True,
            "smallSupportNotClaimedToCaptureAllFullCorrections": True,
            "fullOriginalWKernelLengthUpperBound": gap,
            "allNineActualH0TargetsLocallyInOriginalSource": gap <= 1,
            "allTransverseSquareOutputsLocallyInOriginalSource": gap == 0,
            "fullOriginalE8LengthExactIfLowerFive": 5 if lower == 5 else None,
            "improvedTwoPointFullLengthUpperBound": 32-lower,
            "twoPointImprovementUsesWholeE8DivisorAndUnitLeadingFive": True,
            "desiredH0LocalExponent": 1,
            "noGlobalPolynomialMembershipClaimed": True,
            "insufficientLowThresholdIsNotAFullModuleObstruction": True})
        result["status"] = "completed"
    except BaseException as exc:
        result["status"] = "incomplete"
        result["error"] = type(exc).__name__ + ": " + str(exc)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        save()
        print(json.dumps({
            "status": result["status"], "receipt": str(out),
            "bytes": out.stat().st_size, "sha256": sha_file(out),
            "elapsedSeconds": result["elapsedSeconds"],
            "smallTorsionLengthLowerBound": result["parameters"].get(
                "smallTorsionLengthLowerBound")}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
