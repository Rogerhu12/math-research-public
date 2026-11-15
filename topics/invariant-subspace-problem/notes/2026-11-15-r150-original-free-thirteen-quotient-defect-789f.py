#!/usr/bin/env python3
"""R150: exact quotient defect J from the paid original 155 x 13 free kernels.

Author: AI (ChatGPT / literature_audit), 2026-11-15 UTC.
Only the immutable paid 157898-byte kernel phase and its small receipt are read.
No original Macaulay elimination, Hermite row module, or prior large candidate
is loaded or recomputed.  No value of dim J is an expected-answer gate.
The complete three-row maximal-minor ideals are computed over Q and F31.
All larger coefficient artifacts remain temporary in this job.

Official python-flint 0.9.0 polynomial APIs:
https://python-flint.readthedocs.io/en/latest/fmpq_poly.html
https://python-flint.readthedocs.io/en/latest/nmod_poly.html
"""
import argparse
import gzip
import hashlib
import itertools
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time
from flint import fmpq, fmpq_poly, nmod_poly

FORMAT = "r150-original-free-thirteen-quotient-defect-v1"
CORE_FORMAT = "r150-original-global-projection-polynomial-core-v1"
CORE_SOURCE_SHA256 = "727175cf485a8ba5b5146a4cc6e749962e109c9e42265a2dd45f58cecdf933fb"
CORE_BINDING = "ce358eac629541da0c9d35fd29c66424fa0d89ded97cfec93f324cf56e9d16ba"
PHASE = "free-thirteen-kernel"
PHASE_FILE = "free-thirteen-kernel-70b27882aced10d9de363b30056d93491860db2b102d3750c949659a7ad11fc0.json.gz"
PHASE_BYTES = 157898
PHASE_SHA256 = "b4cd026450d301328d4273ca7256dd9d8ee645576fcc5a5118aecd99a4fc2c51"
PAYLOAD_SHA256 = "70b27882aced10d9de363b30056d93491860db2b102d3750c949659a7ad11fc0"
MATRIX_SHA256 = "0094105c15f99860016767a662e27b7b60ddfb04b085f044f50bacfe694aabe6"
PAID_RECEIPTS = {
    (11075, "7db7d2437583105a9bb2474612cb5b4001989f7911ca79bd22992d025a056aa2"),
    (6068, "354d34109b5b1a9593b038a69c7ad59e6eaa9ddd345474797408f05117c9639b"),
}
P = 31
ZQ = fmpq_poly([])
OQ = fmpq_poly([1])
XQ = fmpq_poly([0, 1])
ZF = nmod_poly([], P)
OF = nmod_poly([1], P)
XF = nmod_poly([0, 1], P)
QFACTORS = [
    ("s", XQ), ("s-2", XQ-2), ("s+6", XQ+6),
    ("Fplus", fmpq_poly([-8, 32, -25, 5])),
    ("Fminus", fmpq_poly([864, 864, 135, 5])),
    ("E8", fmpq_poly([9600, -25472, -3392, 15936, -2888, -936, 153, 50, 5])),
]
DLINEAR = (QFACTORS[0][1]**8 * QFACTORS[1][1]**2 * QFACTORS[2][1]**2
           * QFACTORS[3][1]**3 * QFACTORS[4][1]**3 * QFACTORS[5][1]**2)
PUREFREE = [(a, 0) for a in range(1, 6)] + [(a, 1) for a in range(5)] + [(0, 2), (1, 2), (0, 3)]
DEADLINE = float("inf")

class BudgetStop(Exception):
    pass

def require(test, message):
    if not test:
        raise AssertionError(message)

def tick():
    if time.monotonic() >= DEADLINE:
        raise BudgetStop("Time budget reached at an immutable checkpoint boundary")

def alarm_handler(signum, frame):
    raise BudgetStop("Time budget signal; the last immutable checkpoint remains valid")

def canonical(obj):
    return json.dumps(obj, sort_keys=True, ensure_ascii=True, separators=(",", ":")).encode("ascii")

def sha(data):
    return hashlib.sha256(data).hexdigest()

def identity(path):
    path = Path(path)
    h = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            size += len(chunk)
            h.update(chunk)
    return {"bytes": size, "sha256": h.hexdigest()}

def atomic_bytes(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp-" + str(os.getpid()))
    with tmp.open("wb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(tmp, path)

def atomic_json(path, obj):
    atomic_bytes(path, canonical(obj))

def encp(poly, field="Q"):
    if field == "Q":
        return [str(x) for x in poly.coeffs()]
    return [int(x) for x in poly.coeffs()]

def decp(coefficients, field):
    if field == "Q":
        return fmpq_poly([fmpq(x) for x in coefficients])
    return nmod_poly([int(x) for x in coefficients], P)

def encm(matrix):
    return [[encp(poly) for poly in row] for row in matrix]

def phash(matrix):
    return sha(canonical(encm(matrix)))

def monic(poly, field):
    if not poly:
        return poly
    if field == "Q":
        return poly / poly.leading_coefficient()
    return poly * pow(int(poly.leading_coefficient()), -1, P)

def integral_at_31(poly, where):
    denominator = int(poly.denom())
    require(denominator > 0 and denominator % P != 0,
            "A nonunit coefficient denominator at 31: " + where)
    return denominator

def reduce31(poly, where):
    denominator = integral_at_31(poly, where)
    inv = pow(denominator % P, -1, P)
    return nmod_poly([(int(x) % P) * inv % P for x in poly.numer().coeffs()], P)

def exact_divide(a, b, where):
    quotient, remainder = divmod(a, b)
    require(not remainder, "Nonexact polynomial division: " + where)
    return quotient

class Cache:
    def __init__(self, directory, binding):
        self.root = Path(directory)
        self.root.mkdir(parents=True, exist_ok=True)
        self.path = self.root / "j-quotient-checkpoint-manifest.json"
        self.binding = binding
        if self.path.exists():
            self.manifest = json.loads(self.path.read_text())
            require(self.manifest.get("format") == FORMAT and
                    self.manifest.get("binding") == binding,
                    "J consumer checkpoint semantic binding")
        else:
            self.manifest = {"format": FORMAT, "binding": binding, "phases": {}}
            atomic_json(self.path, self.manifest)

    def has(self, name):
        return name in self.manifest["phases"]

    def get(self, name):
        rec = self.manifest["phases"][name]
        path = self.root / rec["file"]
        require(identity(path) == {"bytes": rec["bytes"], "sha256": rec["sha256"]},
                "Immutable J phase identity: " + name)
        data = path.read_bytes()
        obj = json.loads(data)
        require(obj.get("format") == FORMAT and obj.get("binding") == self.binding
                and obj.get("phase") == name, "Immutable J phase content: " + name)
        return obj["payload"]

    def put(self, name, payload, verified, summary):
        obj = {"format": FORMAT, "binding": self.binding, "phase": name,
               "verified": bool(verified), "payload": payload}
        data = canonical(obj)
        digest = sha(data)
        path = self.root / (name + "-" + digest + ".json")
        if not path.exists():
            atomic_bytes(path, data)
        else:
            require(identity(path) == {"bytes": len(data), "sha256": digest},
                    "Existing immutable J phase content")
        rec = {"file": path.name, "bytes": len(data), "sha256": digest,
               "verified": bool(verified), "temporaryOnly": True, "summary": summary}
        self.manifest["phases"][name] = rec
        atomic_json(self.path, self.manifest)
        return rec

def paid_kernel(core_receipt, checkpoint_dir):
    receipt_identity = identity(core_receipt)
    require((receipt_identity["bytes"], receipt_identity["sha256"]) in PAID_RECEIPTS,
            "Pinned paid core receipt identity")
    outer = json.loads(Path(core_receipt).read_text())
    paid = outer.get("result", outer)
    require(paid.get("status") == "completed" and paid.get("binding") == CORE_BINDING,
            "Paid core completion and semantic binding")
    rec = paid["parameters"]["checkpointPhases"][PHASE]
    require(rec["file"] == PHASE_FILE and rec["bytes"] == PHASE_BYTES and
            rec["sha256"] == PHASE_SHA256 and rec["payloadSha256"] == PAYLOAD_SHA256
            and rec["verified"] is True, "Pinned paid free-kernel phase metadata")
    summary = rec["summary"]
    require(summary["all2912OriginalProductsZero"] is True and
            summary["freeNormalization"] == "Dlinear^2 I13" and
            summary["matrix"]["logicalSha256"] == MATRIX_SHA256,
            "Paid original-source identity and full-free normalization")
    path = Path(checkpoint_dir) / PHASE_FILE
    require(identity(path) == {"bytes": PHASE_BYTES, "sha256": PHASE_SHA256},
            "Pinned free-kernel compressed bytes")
    with gzip.open(path, "rb") as stream:
        raw = stream.read()
    require(sha(raw) == PAYLOAD_SHA256, "Pinned free-kernel decompressed payload")
    obj = json.loads(raw)
    require(obj.get("format") == CORE_FORMAT and obj.get("binding") == CORE_BINDING
            and obj.get("phase") == PHASE and obj.get("verified") is True,
            "Paid free-kernel immutable payload binding")
    matrix = [[fmpq_poly([fmpq(x) for x in poly]) for poly in row]
              for row in obj["payload"]["matrix"]]
    require(len(matrix) == 155 and all(len(row) == 13 for row in matrix),
            "All 155 by 13 original polynomial coordinates")
    require(phash(matrix) == MATRIX_SHA256, "Canonical original polynomial-matrix identity")
    return matrix, {"paidReceipt": receipt_identity,
                    "paidCoreSourceSHA256": CORE_SOURCE_SHA256,
                    "paidCoreBinding": CORE_BINDING,
                    "kernelPhase": {"file": PHASE_FILE, "bytes": PHASE_BYTES,
                                    "sha256": PHASE_SHA256, "payloadSha256": PAYLOAD_SHA256,
                                    "logicalSha256": MATRIX_SHA256},
                    "inheritedPaid2912OriginalProductsZero": True}

def original_structure(Q):
    pc = [(a, degree-a) for degree in range(1, 6) for a in range(degree+1)]
    nc = [(a, degree-a, j) for degree in range(5)
          for a in range(degree+1) for j in range(2, 11)]
    pi = {key: i for i, key in enumerate(pc)}
    ni = {key: 20+i for i, key in enumerate(nc)}
    require(len(pc) == 20 and len(nc) == 135 and len(PUREFREE) == 13,
            "Original target coordinate dictionary")
    denominator_checks = 0
    for i, row in enumerate(Q):
        for j, poly in enumerate(row):
            integral_at_31(poly, "Q[" + str(i) + "," + str(j) + "]")
            denominator_checks += len(poly.coeffs())
    d = DLINEAR**2
    require(int(DLINEAR.degree()) == 46 and int(d.degree()) == 92 and
            int(DLINEAR.leading_coefficient()) % P != 0,
            "Degree46 linear divisor with unit leading coefficient at31")
    expected = [[ZQ for j in range(13)] for i in range(155)]
    for f, key in enumerate(PUREFREE):
        expected[pi[key]][f] = d
    vectors = []
    for j in range(2, 11):
        a, b, c = Q[ni[(0, 0, j)]][10:13]
        vectors.append((a, b, c))
        exact_divide(a, DLINEAR, "Saved a_i has the actual Dlinear factor")
        expected[ni[(0, 0, j)]][10:13] = [a, b, c]
        expected[ni[(1, 0, j)]][11] = a
        expected[ni[(0, 1, j)]][12] = a
    require(Q == expected, "All2015 original entries: ten isolated axes and exact3x30 structure")
    require(all(Q[pi[key]][j] == (d if j == i else ZQ)
                for i, key in enumerate(PUREFREE) for j in range(13)),
            "Entire Dlinear^2 I13 free block")
    isolated_rows = [pi[key] for key in PUREFREE[:10]]
    for column, target_row in enumerate(isolated_rows):
        require(all(Q[i][column] == (d if i == target_row else ZQ) for i in range(155)),
                "Each of the ten pure-axis columns has no other support")
        require(all(not Q[target_row][j] for j in range(10, 13)),
                "The last three columns vanish on all ten isolated axes")
    selected_rows = [pi[key] for key in PUREFREE[10:13]]
    selected_rows += [ni[(0, 0, j)] for j in range(2, 11)]
    selected_rows += [ni[(1, 0, j)] for j in range(2, 11)]
    selected_rows += [ni[(0, 1, j)] for j in range(2, 11)]
    require(len(selected_rows) == 30 and len(set(selected_rows)) == 30,
            "Thirty distinct original target coordinates")
    small = [[Q[r][10+i] for r in selected_rows] for i in range(3)]
    wanted_columns = [(d, ZQ, ZQ), (ZQ, d, ZQ), (ZQ, ZQ, d)]
    wanted_columns += vectors
    wanted_columns += [(ZQ, v[0], ZQ) for v in vectors]
    wanted_columns += [(ZQ, ZQ, v[0]) for v in vectors]
    require(small == [list(row) for row in zip(*wanted_columns)],
            "Exact original transpose restriction is the complete3x30 presentation")
    nonzero = sum(bool(poly) for row in Q for poly in row)
    maxdegree = max(int(poly.degree()) for row in Q for poly in row if poly)
    require(nonzero == 58 and maxdegree == 116, "Paid exact nonzero and degree profile")
    return d, vectors, {
        "all2015OriginalPolynomialEntriesVerified": True,
        "allOriginalCoefficientDenominatorsAre31Units": True,
        "numberOfOriginalRationalCoefficientsChecked": denominator_checks,
        "tenAxesHaveNoOtherOriginalSupport": True,
        "lastThreeColumnsVanishOnTenAxes": True,
        "fullFree13BlockIsDlinearSquaredIdentity": True,
        "smallOriginalTargetRowsOneBased": [i+1 for i in selected_rows],
        "smallMatrixShape": [3, 30],
        "smallMatrixLogicalSHA256": phash(small),
        "originalNonzeroEntries": nonzero,
        "originalMaximumDegree": maxdegree,
        "DlinearDegree": 46,
        "DlinearSquaredDegree": 92,
        "separatedDFreeAxes": 10,
        "separatedDFreeRank": 920,
    }

def descriptors():
    out = [("q3",)]
    for i in range(9):
        out += [("dqb", i), ("dqc", i)]
    for i, j in itertools.combinations(range(9), 2):
        out += [("qab", i, j), ("qac", i, j)]
    for i, j in itertools.combinations(range(9), 2):
        out.append(("dbc", i, j))
    for i, j, k in itertools.combinations(range(9), 3):
        out.append(("det", i, j, k))
    require(len(out) == 211, "Complete211-expression maximal-minor formula")
    return out

DESCRIPTORS = descriptors()

def expression(desc, d, q, vectors):
    tag = desc[0]
    if tag == "q3":
        return q**3
    if tag in ("dqb", "dqc"):
        return d*q*vectors[desc[1]][1 if tag == "dqb" else 2]
    if tag in ("qab", "qac", "dbc"):
        a, b, c = vectors[desc[1]]
        aa, bb, cc = vectors[desc[2]]
        if tag == "qab":
            return q*(a*bb-aa*b)
        if tag == "qac":
            return q*(a*cc-aa*c)
        return d*(b*cc-bb*c)
    a, b, c = vectors[desc[1]]
    aa, bb, cc = vectors[desc[2]]
    aaa, bbb, ccc = vectors[desc[3]]
    return a*(bb*ccc-bbb*cc)-aa*(b*ccc-bbb*c)+aaa*(b*cc-bb*c)

def complete_gcd(field, d, vectors, cache):
    zero = ZQ if field == "Q" else ZF
    q = d
    for a, b, c in vectors:
        q = q.gcd(a)
    q = monic(q, field)
    require(bool(q), "Nonzero axial gcd")
    name = "rational-complete-minors" if field == "Q" else "field31-complete-minors"
    inputs = {"field": field, "d": encp(d, field),
              "vectors": [[encp(x, field) for x in v] for v in vectors],
              "q": encp(q, field), "descriptors": DESCRIPTORS}
    input_hash = sha(canonical(inputs))
    if cache.has(name):
        state = cache.get(name)
        require(state["inputLogicalSHA256"] == input_hash and
                state["field"] == field, "Complete-minor restored input identity")
        current = decp(state["currentMonicGcd"], field)
    else:
        state = {"field": field, "inputLogicalSHA256": input_hash,
                 "nextExpression": 0, "verifiedDivisions": 0,
                 "currentMonicGcd": [], "degreeDropProfile": [],
                 "expressionChainSHA256": sha(b"r150-complete-211-minors"),
                 "axialMonicGcd": encp(q, field)}
        current = zero

    def save():
        state["currentMonicGcd"] = encp(current, field)
        completed = state["nextExpression"] == 211 and state["verifiedDivisions"] == 211
        cache.put(name, state, completed,
                  {"field": field, "processedExpressions": state["nextExpression"],
                   "verifiedFinalDivisions": state["verifiedDivisions"],
                   "completeExpressionCount": 211,
                   "currentGcdDegree": int(current.degree()) if current else -1,
                   "gcdLogicalSHA256": sha(canonical(encp(current, field))),
                   "completeMaximalMinorIdealComputed": completed})

    for index in range(state["nextExpression"], 211):
        tick()
        value = expression(DESCRIPTORS[index], d, q, vectors)
        previous_degree = int(current.degree()) if current else -1
        current = monic(current.gcd(value), field)
        require(bool(current), "Nonzero maximal-minor gcd")
        state["nextExpression"] = index+1
        state["expressionChainSHA256"] = sha(canonical(
            [state["expressionChainSHA256"], list(DESCRIPTORS[index]), encp(value, field)]))
        if int(current.degree()) != previous_degree:
            state["degreeDropProfile"].append(
                {"afterExpression": index+1, "degree": int(current.degree())})
            save()
        elif (index+1) % 16 == 0:
            save()
    save()
    for index in range(state["verifiedDivisions"], 211):
        tick()
        value = expression(DESCRIPTORS[index], d, q, vectors)
        exact_divide(value, current, field + " final divisor expression " + str(index))
        state["verifiedDivisions"] = index+1
        if (index+1) % 16 == 0:
            save()
    save()
    require(state["nextExpression"] == 211 and state["verifiedDivisions"] == 211,
            "Every expression incorporated and verified")
    return current, {"field": field,
                     "degree": int(current.degree()),
                     "polynomialSHA256": sha(canonical(encp(current, field))),
                     "axialGcdDegree": int(q.degree()),
                     "axialGcdSHA256": sha(canonical(encp(q, field))),
                     "completeMaximalMinorIdeal": True,
                     "expressionsIncorporated": 211,
                     "finalExactDivisionsVerified": 211,
                     "expressionChainSHA256": state["expressionChainSHA256"],
                     "degreeDropProfile": state["degreeDropProfile"]}

def support_factorization(poly, factors, field):
    remaining = monic(poly, field)
    one = OQ if field == "Q" else OF
    result = []
    reconstructed = one
    for name, factor in factors:
        factor = monic(factor, field)
        exponent = 0
        while True:
            quotient, remainder = divmod(remaining, factor)
            if remainder:
                break
            remaining = quotient
            exponent += 1
        result.append({"factor": name, "degree": int(factor.degree()),
                       "exponent": exponent})
        reconstructed *= factor**exponent
    require(remaining == one and reconstructed == monic(poly, field),
            field + " complete known-support factorization")
    require(sum(r["degree"]*r["exponent"] for r in result) == int(poly.degree()),
            field + " full factorization degree")
    return result

def finish(gq, gf, structure, cache):
    integral_at_31(gq, "Complete monic rational H3 characteristic polynomial")
    require(gq == monic(gq, "Q"), "Rational characteristic polynomial is monic")
    reduced = reduce31(gq, "Complete monic rational characteristic reduction")
    require(int(reduced.degree()) == int(gq.degree()) and
            int(reduced.leading_coefficient()) == 1,
            "Degree-preserving reduction of the full rational characteristic polynomial")
    jpoly = exact_divide(gf, reduced, "Characteristic difference for J=H[p]")
    require(jpoly == monic(jpoly, "F31"), "Monic exact characteristic quotient")
    qsupport = support_factorization(gq, QFACTORS, "Q")
    e6 = nmod_poly([30, 15, 0, 2, 18, 13, 1], P)
    fplus = monic(reduce31(QFACTORS[3][1], "Fplus"), "F31")
    fminus = monic(reduce31(QFACTORS[4][1], "Fminus"), "F31")
    ffactors = [("s", XF), ("s-1", XF-1), ("s-2", XF-2),
                ("s+6", XF+6), ("Pplus", fplus), ("Pminus", fminus), ("E6", e6)]
    require(reduce31(QFACTORS[5][1], "E8") == 5*(XF-1)*(XF-2)*e6,
            "Exact E8 residue collision at both1 and2")
    for i, (name, factor) in enumerate(ffactors):
        lc, parts = factor.factor()
        require(len(parts) == 1 and int(parts[0][1]) == 1 and
                monic(parts[0][0], "F31") == monic(factor, "F31"),
                "Every reported F31 primary factor is irreducible: " + name)
        for other_name, other in ffactors[:i]:
            require(factor.gcd(other) == OF,
                    "Distinct reported primary factors are coprime")
    fsupport = support_factorization(gf, ffactors, "F31")
    rsupport = support_factorization(reduced, ffactors, "F31")
    jsupport = support_factorization(jpoly, ffactors, "F31")
    qexp = {r["factor"]: r["exponent"] for r in qsupport}
    collision = {"s": qexp["s"], "s-1": qexp["E8"],
                 "s-2": qexp["s-2"]+qexp["E8"], "s+6": qexp["s+6"],
                 "Pplus": qexp["Fplus"], "Pminus": qexp["Fminus"], "E6": qexp["E8"]}
    require(all(r["exponent"] == collision[r["factor"]] for r in rsupport),
            "All rational factors transported with their actual residue collisions")
    primary = []
    for field_row, rational_row, jrow in zip(fsupport, rsupport, jsupport):
        require(field_row["factor"] == rational_row["factor"] == jrow["factor"],
                "Matching primary labels")
        difference = field_row["exponent"]-rational_row["exponent"]
        require(difference >= 0 and difference == jrow["exponent"],
                "Every actual primary length difference is nonnegative and exact")
        primary.append({"factor": jrow["factor"], "factorDegree": jrow["degree"],
                        "rationalCharacteristicReductionMultiplicity": rational_row["exponent"],
                        "fieldCharacteristicMultiplicity": field_row["exponent"],
                        "JPrimaryLength": difference,
                        "JDimensionOverF31": difference*jrow["degree"]})
    jdim = int(jpoly.degree())
    require(jdim == int(gf.degree())-int(gq.degree()) ==
            sum(row["JDimensionOverF31"] for row in primary),
            "Exact total quotient-defect dimension")
    exact_data = {"rationalSmallCharacteristic": encp(gq),
                  "fieldSmallCharacteristic": encp(gf, "F31"),
                  "reducedRationalSmallCharacteristic": encp(reduced, "F31"),
                  "JCharacteristic": encp(jpoly, "F31"),
                  "rationalSupport": qsupport, "primaryLengths": primary}
    cache.put("complete-J-characteristic", exact_data, True,
              {"JTotalDimension": jdim, "rationalSmallLength": int(gq.degree()),
               "fieldSmallLength": int(gf.degree()),
               "allCompleteCharacteristicIdentitiesVerified": True})
    return {
        "rationalSmallCharacteristicDegree": int(gq.degree()),
        "fieldSmallCharacteristicDegree": int(gf.degree()),
        "rationalFullHCharacteristicDegree": 920+int(gq.degree()),
        "fieldFullHCharacteristicDegree": 920+int(gf.degree()),
        "rationalSmallCharacteristicSHA256": sha(canonical(encp(gq))),
        "fieldSmallCharacteristicSHA256": sha(canonical(encp(gf, "F31"))),
        "reducedRationalCharacteristicSHA256": sha(canonical(encp(reduced, "F31"))),
        "JCharacteristicSHA256": sha(canonical(encp(jpoly, "F31"))),
        "JTotalDimension": jdim,
        "rationalSupport": qsupport,
        "primaryLengths": primary,
        "monicRationalCharacteristicHasOnly31UnitDenominators": True,
        "rationalReductionPreservesFullDegree": True,
        "completeCharacteristicQuotientIsExact": True,
        "allSevenReportedPrimaryFactorsAreIrreducibleAndCoprime": True,
        "E8CollisionAtOneAndTwoVerified": True,
        "allReportedPrimaryLengthsSumToJDimension": True,
        "tenSeparatedAxesAreDFree": True,
        "noExpectedJDimensionWasSupplied": True,
        "noNewOriginalNineTargetMembershipClaim": True,
    }

def main():
    global DEADLINE
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--core-receipt", required=True)
    ap.add_argument("--checkpoint-dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--remaining-seconds", type=float, default=120.0)
    ap.add_argument("--memory-mib", type=int, default=1024)
    args = ap.parse_args()
    require(1 <= args.remaining_seconds <= 600, "Time budget range")
    require(256 <= args.memory_mib <= 4096, "Memory budget range")
    start = time.monotonic()
    DEADLINE = start + args.remaining_seconds
    requested = args.memory_mib * 1024 * 1024
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    effective = requested if hard == resource.RLIM_INFINITY else min(requested, hard)
    resource.setrlimit(resource.RLIMIT_AS, (effective, effective))
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, args.remaining_seconds)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    receipt = {"format": FORMAT, "status": "started",
               "parameters": {"limits": {"seconds": args.remaining_seconds,
                                         "memoryMiB": effective//(1024*1024)},
                              "allNewFilesTemporaryOnly": True}}
    cache = None
    exit_code = 1
    try:
        Q, paid_identity = paid_kernel(args.core_receipt, args.checkpoint_dir)
        d, vectors, structure = original_structure(Q)
        self_id = identity(Path(__file__))
        binding_data = {"format": FORMAT, "consumerSHA256": self_id["sha256"],
                        "paidCoreSourceSHA256": CORE_SOURCE_SHA256,
                        "paidCoreBinding": CORE_BINDING,
                        "paidKernelPayloadSHA256": PAYLOAD_SHA256,
                        "paidKernelMatrixSHA256": MATRIX_SHA256,
                        "smallMatrixLogicalSHA256": structure["smallMatrixLogicalSHA256"],
                        "prime": P, "completeMinorExpressionCount": 211}
        binding = sha(canonical(binding_data))
        receipt["binding"] = binding
        receipt["parameters"].update({"consumerSource": self_id, "inputFiles": paid_identity,
                                      "bindingInputs": binding_data,
                                      "originalStructure": structure})
        cache = Cache(out/"checkpoints", binding)
        cache.put("original-structure", structure, True, structure)
        tick()
        gq, q_summary = complete_gcd("Q", d, vectors, cache)
        receipt["parameters"]["rationalCompleteMinors"] = q_summary
        df = reduce31(d, "Original d")
        vectors_f = [tuple(reduce31(poly, "Original vector") for poly in v) for v in vectors]
        gf, f_summary = complete_gcd("F31", df, vectors_f, cache)
        receipt["parameters"]["fieldCompleteMinors"] = f_summary
        tick()
        receipt["parameters"]["result"] = finish(gq, gf, structure, cache)
        receipt["status"] = "completed"
        exit_code = 0
    except BudgetStop as exc:
        receipt["status"] = "budget-checkpoint"
        receipt["parameters"]["errorType"] = type(exc).__name__
        receipt["parameters"]["errorMessage"] = str(exc)
        exit_code = 75
    except Exception as exc:
        receipt["status"] = "failed"
        receipt["parameters"]["errorType"] = type(exc).__name__
        receipt["parameters"]["errorMessage"] = str(exc)
        exit_code = 1
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        receipt["elapsedSeconds"] = time.monotonic()-start
        if cache is not None:
            receipt["parameters"]["checkpointManifest"] = identity(cache.path)
            receipt["parameters"]["checkpointPhases"] = cache.manifest["phases"]
        require(len(canonical(receipt)) < 90000, "Small receipt must preserve all required metadata")
        atomic_json(out/"j-quotient-defect-receipt.json", receipt)
        print(json.dumps(receipt, sort_keys=True, separators=(",", ":")), flush=True)
    return exit_code

if __name__ == "__main__":
    sys.exit(main())
