#!/usr/bin/env python3
"""2026-11-15. Author: ChatGPT (AI), literature_audit.

Complete global I_2(A) from the 197 original p^2-divided sources and paid U7.
All 505 free observations, 315 torsion coordinates, and polynomial s-multiples
are retained. No primary projection or expected new rank is used.
"""
from __future__ import annotations
import argparse, gzip, hashlib, importlib.util, json, os, signal, struct, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
from flint import nmod_mat

P = 31
STATE_SHA = "06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf"
SELECTOR_SHA = "2d90d72ac72cc63e5531b80a6e788ef82c6bf794481b53546b27b0afcb7134ee"
READER_SHA = "8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2"
LABELS = list(range(2, 33))

class BudgetStop(Exception):
    pass

def check(ok, message):
    if not ok:
        raise ValueError(message)

def sha_file(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(1048576), b""):
            h.update(b)
    return h.hexdigest()

def canonical(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")

def atomic(path, value):
    raw = canonical(value) + b"\n"
    tmp = Path(str(path) + ".tmp")
    tmp.write_bytes(raw)
    os.replace(tmp, path)

def actual(path, expected):
    raw = Path(path).read_bytes()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    check(hashlib.sha256(raw).hexdigest() == expected, "paid input identity: " + str(path))
    return raw

def sub(M, rows, cols):
    rows, cols = list(rows), list(cols)
    out = nmod_mat(len(rows), len(cols), P)
    for i, r in enumerate(rows):
        for j, c in enumerate(cols):
            out[i, j] = M[r, c]
    return out

def from_columns(cols, rows=315):
    out = nmod_mat(rows, len(cols), P)
    for j, col in enumerate(cols):
        check(len(col) == rows, "column shape")
        for i, value in enumerate(col):
            out[i, j] = value
    return out

def serial(M):
    return bytes(int(M[i, j]) for i in range(M.nrows()) for j in range(M.ncols()))

def polynomial(poly):
    return [int(poly[i]) for i in range(poly.degree() + 1)]

def factors(poly):
    unit, ff = poly.factor()
    return {"unit": int(unit), "factors": [
        {"coefficientsAscending": polynomial(f), "exponent": int(e), "degree": int(f.degree())}
        for f, e in ff]}

def read_g_remainder(path, state):
    raw = Path(path).read_bytes()
    wide = raw[:8] == b"R150NX31"
    check((wide or raw[:8] == b"R150NF31") and struct.unpack_from("<3I", raw, 8) == (0, 31, 1034),
          "complete packed31 G remainder header")
    coordinates = {tuple(q): i for i, q in enumerate(state["coordinates"])}
    check(len(coordinates) == 820, "paid state coordinate dictionary")
    V = nmod_mat(820, 31, P)
    at = 20
    for j in range(31):
        source, label, count = struct.unpack_from("<IHI", raw, at)
        at += 10
        check(source == 0 and label == LABELS[j] and 0 <= count <= 1034,
              "actual batch G remainder label")
        previous = 0
        for _ in range(count):
            component = struct.unpack_from("<H", raw, at)[0]
            at += 2
            width = 2 if wide else 1
            length = int.from_bytes(raw[at:at + width], "little")
            at += width
            check(previous < component <= 1034 and 1 <= length <= 178,
                  "complete G component/degree")
            previous = component
            poly = raw[at:at + length]
            at += length
            check(len(poly) == length and poly[-1] and all(a < P for a in poly),
                  "canonical complete G polynomial")
            for degree, a in enumerate(poly):
                if a:
                    check((component, degree) in coordinates,
                          "high free polynomial term cannot be discarded")
                    V[coordinates[component, degree], j] = a
    check(at == len(raw), "G remainder EOF")
    return V

def main():
    ap = argparse.ArgumentParser()
    for key in ("batches", "state", "selector", "reader", "out"):
        ap.add_argument("--" + key, type=Path, required=True)
    ap.add_argument("--seconds", type=float, default=120)
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    start = time.monotonic()
    deadline = start + a.seconds
    rp = a.out / "global197-i2-closure-receipt.json"
    result = {"format": "r150-global197-original-i2-complete-closure-v1",
              "status": "running", "prime": P, "parameters": {}}
    def tick():
        if time.monotonic() >= deadline:
            raise BudgetStop("closure budget")
    def stop(signum, frame):
        raise BudgetStop("closure signal")
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    try:
        check(sha_file(a.reader) == READER_SHA, "paid torsion reader")
        state_raw = actual(a.state, STATE_SHA)
        selector = actual(a.selector, SELECTOR_SHA)
        check(selector[:8] == b"R150PHS1" and struct.unpack_from("<5I", selector, 8) == (31, 315, 15, 7, 9),
              "full original seven-source selector")
        state_file = a.out / "paid-state-input.bin"
        if not state_file.exists() or sha_file(state_file) != STATE_SHA:
            state_file.write_bytes(state_raw)
        spec = importlib.util.spec_from_file_location("global197_i2_paid_state", a.reader)
        reader = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(reader)
        state = reader.load_state(state_file)
        check((state["stateDimension"], state["torsionDimension"], state["observabilityRank"]) == (820, 315, 505),
              "full state dimensions")
        J = nmod_mat(state["matrices"]["action"], P)
        K = nmod_mat(state["matrices"]["kernelTranspose"], P).transpose()
        O = nmod_mat(state["observabilityEchelon"], P)
        check(O.nrows() == 505 and O.ncols() == 820, "all free observations retained")
        pivotset = set(state["pivotStateCoordinates"])
        check(len(pivotset) == 505 and min(pivotset) >= 1 and max(pivotset) <= 820, "paid free projection")
        free = [i for i in range(820) if i + 1 not in pivotset]
        check(len(free) == 315 and sub(K, free, range(315)) == nmod_mat([[int(i == j) for j in range(315)] for i in range(315)], P),
              "paid normalized whole torsion embedding")
        check(O * K == nmod_mat(505, 315, P), "paid whole torsion annihilates all observations")
        def block(offset, rows, cols):
            b = selector[offset:offset + rows * cols]
            check(len(b) == rows * cols and all(v < P for v in b), "selector field block")
            return nmod_mat([list(b[i * cols:(i + 1) * cols]) for i in range(rows)], P)
        U = block(7723, 315, 7)
        J7 = block(9991, 7, 7)
        check(len(selector) == 10040 and U.rank() == 7 and J * U == U * J7, "complete original U7 and s action")
        manifest = json.loads(a.batches.read_text())
        check(manifest.get("format") == "r150-global197-i2-complete-batches-v1"
              and manifest.get("status") == "completed"
              and manifest.get("originalHighKernelNumbersOneBased") == list(range(2, 199)),
              "all197 completed batch manifest")
        rows = manifest["batches"]
        check(len(rows) == 7, "seven actual packed batches")
        all_numbers = []
        seeds = [[int(U[i, j]) for i in range(315)] for j in range(7)]
        checks = []
        for bi, item in enumerate(rows):
            tick()
            active = item["activeHighKernelNumbersOneBased"]
            wanted = list(range(2 + 31 * bi, min(199, 2 + 31 * (bi + 1))))
            check(active == wanted and item["paddedColumnCount"] == 31 - len(wanted), "actual197 dictionary and padding")
            all_numbers.extend(active)
            verified = {}
            for name in ("originalMetadata", "imageMetadata", "imageRemainders", "normalForward", "normalBackward"):
                identity = item["files"][name]
                path = Path(identity["file"])
                check(path.is_file() and path.stat().st_size == identity["bytes"] and sha_file(path) == identity["sha256"],
                      "completed actual batch file: " + name)
                verified[name] = path
            check(item["files"]["normalForward"]["sha256"] == manifest["paidForwardSHA256"]
                  and item["files"]["normalBackward"]["sha256"] == manifest["paidBackwardSHA256"],
                  "identical paid F/B replay")
            orig = json.loads(verified["originalMetadata"].read_text())
            im = json.loads(verified["imageMetadata"].read_text())
            check(orig.get("status") == "completed" and orig.get("prime") == 31
                  and orig.get("modulus") == 29791 and orig.get("divisor") == 961
                  and orig.get("targetMode") == 0 and orig.get("targetCount") == 31
                  and orig.get("originalEquations") == 17 and orig.get("originalRawRows") == 6188
                  and orig.get("originalComponents") == 4367
                  and orig.get("provedSourceCostBound") == 177
                  and orig.get("allOriginalProductCoefficientsDivisible") is True
                  and orig.get("failedCoefficientCount") == 0
                  and orig.get("originalRowScaleTransportVerified") is True
                  and orig.get("allWeightedBoundsVerified") is True
                  and len(orig.get("actualSourceCosts", [])) == 31
                  and max(orig["actualSourceCosts"]) <= 177, "all original p^2 divisions")
            check(im.get("status") == "completed" and im.get("targets") == 31
                  and im.get("labels") == LABELS
                  and im.get("fullImageQuotientIdentity") is True
                  and im.get("everyRemainderIsIrreducible") is True, "whole G quotient identity")
            V = read_g_remainder(verified["imageRemainders"], state)
            D = sub(V, free, range(31))
            check(O * V == nmod_mat(505, 31, P) and K * D == V, "all505 free rows and full315 reconstruction")
            for j in range(len(active), 31):
                check(all(not V[i, j] for i in range(820)) and orig["actualSourceCosts"][j] == -1,
                      "padded zero original sources and classes")
            for j in range(len(active)):
                seeds.append([int(D[i, j]) for i in range(315)])
            checks.append({"batch": bi + 1, "activeColumns": len(active),
                           "highKernelNumbersOneBased": active,
                           "all505FreeObservationsZero": True, "all315ReconstructionVerified": True,
                           "allOriginal4367PolynomialProductsDividedBy31Squared": True,
                           "classesSHA256": hashlib.sha256(serial(sub(D, range(315), range(len(active))))).hexdigest()})
        check(all_numbers == list(range(2, 199)) and len(seeds) == 204, "no omitted or duplicated original source")
        basis = []
        pivots = []
        dag = []
        def insert(vector, origin):
            v = list(vector)
            steps = []
            for i, p in enumerate(pivots):
                c = v[p]
                if c:
                    v = [(a0 - c * b0) % P for a0, b0 in zip(v, basis[i])]
                    steps.append([i, c])
            p = next((i for i, q in enumerate(v) if q), None)
            if p is None:
                return
            scale = pow(v[p], -1, P)
            v = [q * scale % P for q in v]
            pivots.append(p)
            basis.append(v)
            dag.append({"origin": origin, "subtractBasis": steps, "scale": scale, "pivot": p})
        for j, col in enumerate(seeds):
            insert(col, {"seed": j})
        constant_rank = len(basis)
        cursor = 0
        while cursor < len(basis):
            tick()
            v = J * from_columns([basis[cursor]])
            insert([int(v[i, 0]) for i in range(315)], {"multiplyByS": cursor})
            cursor += 1
            check(len(basis) <= 315, "finite whole torsion dimension")
        B = from_columns(basis)
        rank = len(basis)
        check(rank >= 7 and B.rank() == rank, "independent complete polynomial source basis")
        Uinv = sub(B, pivots, range(rank)).inv()
        seedsM = from_columns(seeds)
        source_coordinates = Uinv * sub(seedsM, pivots, range(204))
        action = Uinv * sub(J * B, pivots, range(rank))
        check(B * source_coordinates == seedsM, "all204 original source classes in final polynomial module")
        check(B * action == J * B, "complete global s-closure")
        replay = []
        for j, node in enumerate(dag):
            origin = node["origin"]
            if "seed" in origin:
                v = list(seeds[origin["seed"]])
            else:
                parent = origin["multiplyByS"]
                check(0 <= parent < j, "source DAG s dependency")
                col = J * from_columns([replay[parent]])
                v = [int(col[i, 0]) for i in range(315)]
            for parent, c in node["subtractBasis"]:
                check(0 <= parent < j and 1 <= c < 31, "source DAG original dependency")
                v = [(x - c * y) % P for x, y in zip(v, replay[parent])]
            v = [x * node["scale"] % P for x in v]
            check(v == basis[j], "full315 polynomial original-source DAG replay")
            replay.append(v)
        characteristic = action.charpoly()
        check(characteristic.degree() == rank, "whole I2 characteristic degree")
        fullchar = J.charpoly()
        quotient, remainder = divmod(fullchar, characteristic)
        check(not remainder, "I2 characteristic divides the full315 characteristic")
        payload = {"format": "r150-global197-i2-original-polynomial-source-system-v1",
                   "binding": manifest["binding"], "temporaryOnly": True,
                   "seedDescriptors": [{"family": "paid-original-U7", "columnOneBased": j + 1} for j in range(7)]
                                      + [{"family": "global-original-R2", "highKernelNumberOneBased": j} for j in range(2, 199)],
                   "original315SeedColumns": seeds, "basisColumns315": basis,
                   "sourceDAG": dag, "basisPivotRowsZeroBased": pivots,
                   "actionRows": [[int(action[i, j]) for j in range(rank)] for i in range(rank)],
                   "sourceCoordinatesRows": [[int(source_coordinates[i, j]) for j in range(204)] for i in range(rank)]}
        body = canonical(payload) + b"\n"
        output = a.out / "complete-global197-i2-source-system.json.gz"
        tmp = Path(str(output) + ".tmp")
        with tmp.open("wb") as f:
            with gzip.GzipFile(filename="", fileobj=f, mode="wb", compresslevel=1, mtime=0) as z:
                z.write(body)
        os.replace(tmp, output)
        result.update(status="completed", elapsedSeconds=time.monotonic() - start)
        result["parameters"] = {
            "binding": manifest["binding"], "sourceSHA256": sha_file(__file__),
            "inputBatchManifestSHA256": sha_file(a.batches), "stateSHA256": STATE_SHA, "selectorSHA256": SELECTOR_SHA,
            "originalHighKernelNumbersOneBased": list(range(2, 199)),
            "originalR2ColumnCount": 197, "oldU7Rank": 7, "constantSeedRank": constant_rank,
            "completeGlobalI2Dimension": rank,
            "completeCoefficientPrimeExponentTwoMultiplicity": rank - 2,
            "allOriginal6188SourcesRetained": True,
            "all197Full4367PolynomialDivisibilitiesVerified": True,
            "all505FreeObservationsVerified": True, "all315CoordinatesRetained": True,
            "all204OriginalSeedsReconstructed": True,
            "multiplicationBySClosed": True, "wholeOriginalSourceDAGReplayed": True,
            "usesPrimaryProjection": False, "usesTruncatedParameterJets": False,
            "oldNormalFormGaussianRecomputed": False,
            "basisActionSHA256": hashlib.sha256(serial(action)).hexdigest(),
            "basisSHA256": hashlib.sha256(serial(B)).hexdigest(),
            "characteristic": {"coefficientsAscending": polynomial(characteristic), **factors(characteristic)},
            "remaining315Characteristic": {"coefficientsAscending": polynomial(quotient), **factors(quotient)},
            "batchChecks": checks,
            "temporarySystem": {"file": str(output), "bytes": output.stat().st_size, "sha256": sha_file(output),
                                "payloadBytes": len(body), "payloadSHA256": hashlib.sha256(body).hexdigest()},
            "scope": "Full global I2(A) follows from the paid complete p^2 colon theorem plus these 197 exact original divided columns and the paid U7; no claim of characteristic-zero target membership or a later p-adic lift is made."
        }
        atomic(rp, result)
        print(json.dumps({"status": "complete-global197-i2-closure", "completeGlobalI2Dimension": rank,
                          "completeCoefficientPrimeExponentTwoMultiplicity": rank - 2,
                          "elapsedSeconds": time.monotonic() - start}), flush=True)
        return 0
    except BudgetStop as exc:
        result.update(status="budget-checkpoint", errorType=type(exc).__name__, error=str(exc), elapsedSeconds=time.monotonic()-start)
        atomic(rp, result)
        return 75
    except Exception as exc:
        result.update(status="failed", errorType=type(exc).__name__, error=str(exc), elapsedSeconds=time.monotonic()-start)
        atomic(rp, result)
        raise

if __name__ == "__main__":
    raise SystemExit(main())
