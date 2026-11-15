#!/usr/bin/env python3
"""Original nine-dimensional Ay^{-1} RY pencil at fixed paid regular means.

Astra-ISP-789f / literature_audit and root; AI-assisted, GPT-6 Astra Pro.
Source-only probe: no generic nilpotence or full-Macaulay conclusion is assumed.
All physical K/J2/J3, actual tangent complement and whole11x9 products are
reconstructed. A nonzero ninth power at a point disproves uniform nilpotence;
zero at the requested points proves only those pointwise identities.
"""
import argparse
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path
import resource
import signal
import sys
import time
from flint import fmpq_mat

GENERATOR_SHA = "2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
FORMAT = "r150-original-normal-ay-inverse-ry-point-pencil-v1"


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def sha_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1048576), b""):
            h.update(b)
    return h.hexdigest()


def module_at(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def identity(n):
    return fmpq_mat([[int(i == j) for j in range(n)] for i in range(n)])


def original_point(m, s):
    K = fmpq_mat(m.ORIGINAL_K)
    J2 = m.polynomial_power_kernel(K, 2)
    J3 = m.polynomial_power_kernel(K, 3)
    J3inv = J3.inv()
    require(J3inv * J3 == identity(16), "Whole original J3 inverse")
    y = fmpq_mat([[s**i] for i in range(6)])
    p = K * y
    Y = y * y.transpose()
    translation = fmpq_mat([[comb(i, j)*s**(i-j) if i >= j else 0
                             for j in range(11)] for i in range(11)])
    require(translation.det() == 1, "Actual co-moving polynomial unit complement")
    normal = m.submatrix(translation, range(11), range(2, 11))
    tangent = m.submatrix(translation, range(11), range(2))
    B = fmpq_mat([[p[i-j, 0] if 0 <= i-j < 6 else 0
                    for j in range(11)] for i in range(16)])
    Ay = B.transpose() * J3inv * B * J2
    require(m.matrix_zero(Ay*tangent), "Both original tangent kernel columns")
    require((J2*Ay).transpose() == J2*Ay, "Actual physical self-adjointness")
    H = normal.transpose() * J2 * Ay * normal
    detH = H.det()
    require(detH != 0, "Requested original mean is actually regular")

    # RY Z = Pi(Y K Z + Z K Y); J2*Pi is the complete physical polar.
    polar = fmpq_mat(11, 9)
    for j in range(9):
        Z = m.hankel([normal[i, j] for i in range(11)])
        Q = K * (Y*K*Z + Z*K*Y) * K
        for k in range(11):
            polar[k, j] = sum(Q[a, b] for a in range(6) for b in range(6)
                               if a+b == k)
    require(m.matrix_zero(tangent.transpose()*polar),
            "RY actually lies in the image saturation of Ay; no discarded tangent row")
    physical_RY = J2.solve(polar)
    require(J2*physical_RY == polar, "Whole11x9 original polar inversion")
    normal_RY = normal.transpose()*polar
    X = H.solve(normal_RY)
    require(H*X == normal_RY, "All81 original normal unit products")
    require(Ay*normal*X == physical_RY,
            "All99 whole physical Ay products; not merely a compressed pencil")
    polynomial = X.charpoly()
    coefficients = [polynomial[i] for i in range(10)]
    require(polynomial.degree() == 9 and coefficients[9] == 1,
            "Monic actual nine-dimensional characteristic polynomial")
    powers = [identity(9)]
    power_data = []
    first_zero = None
    for k in range(1, 10):
        powers.append(powers[-1]*X)
        zero = m.matrix_zero(powers[-1])
        if zero and first_zero is None:
            first_zero = k
        witness = None
        if not zero:
            for i in range(9):
                for j in range(9):
                    if powers[-1][i, j]:
                        witness = [i, j, str(powers[-1][i, j])]
                        break
                if witness is not None:
                    break
        power_data.append({
            "power": k, "zero": zero,
            "trace": str(sum(powers[-1][i, i] for i in range(9))),
            "matrixSHA256": m.matrix_hash(powers[-1]),
            "firstNonzeroCoordinate": witness})
    cayley = fmpq_mat(9, 9)
    for k in range(10):
        cayley += coefficients[k]*powers[k]
    require(m.matrix_zero(cayley), "Every coordinate of the actual Cayley-Hamilton identity")
    nilpotent = m.matrix_zero(powers[9])
    require(nilpotent == all(not coefficients[k] for k in range(9)),
            "Characteristic polynomial and ninth-power nilpotence agree")
    return {
        "originalMeanParameter": s,
        "definition": "RY Z=Pi(YKZ+ZKY); X=(Ay|normal)^-1 RY|normal",
        "originalK": m.matrix_hash(K), "originalJ2": m.matrix_hash(J2),
        "originalJ3": m.matrix_hash(J3), "translation": m.matrix_hash(translation),
        "normalUnitH": m.matrix_hash(H), "normalUnitDeterminant": str(detH),
        "completePhysicalRY": m.matrix_hash(physical_RY),
        "normalPencilX": m.matrix_hash(X),
        "characteristicPolynomialAscending": [str(x) for x in coefficients],
        "all81NormalUnitProductsVerified": True,
        "all99WholePhysicalProductsVerified": True,
        "originalBothTangentRowsZeroVerified": True,
        "all81CayleyHamiltonProductsVerified": True,
        "powers": power_data, "nilpotentAtThisOriginalMean": nilpotent,
        "nilpotencyIndexIfNilpotent": first_zero,
        "uniformNilpotenceDisprovedIfNonNilpotent": not nilpotent,
        "pointwiseZeroNotPromotedToAllParameters": True,
        "noOriginalTargetMembershipConclusion": True,
        "noLargeOriginalMacaulayRecomputed": True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--generator", required=True)
    parser.add_argument("--points", type=int, nargs="+", default=[4])
    parser.add_argument("--out", required=True)
    parser.add_argument("--remaining-seconds", type=float, default=30)
    parser.add_argument("--memory-mib", type=int, default=512)
    args = parser.parse_args()
    require(args.remaining_seconds > 0 and 256 <= args.memory_mib <= 2048,
            "Bounded actual original nine-dimensional probe")
    require(args.points and len(set(args.points)) == len(args.points) and
            all(x in (3, 4, 5) for x in args.points),
            "Only the explicitly requested finite regular means3,4,5")
    require(sha_file(args.generator) == GENERATOR_SHA, "Pinned unchanged original generator")
    resource.setrlimit(resource.RLIMIT_AS, (args.memory_mib*1024**2, args.memory_mib*1024**2))
    sys.set_int_max_str_digits(0)
    start = time.monotonic()
    result = {"format": FORMAT, "status": "running", "parameters": {
        "inputSource": {"sha256": GENERATOR_SHA,
                        "bytes": Path(args.generator).stat().st_size},
        "selfSource": {"sha256": sha_file(__file__), "bytes": Path(__file__).stat().st_size},
        "points": args.points, "remainingSeconds": args.remaining_seconds,
        "memoryMiB": args.memory_mib, "actualPoints": [],
        "largeDataUploadedOrCommitted": False}}
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    def save():
        result["elapsedSeconds"] = time.monotonic()-start
        raw = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
        require(len(raw) < 90000, "Only the small exact receipt is published")
        tmp = path.with_name(path.name+".tmp")
        tmp.write_bytes(raw)
        tmp.replace(path)
    def timeout(signum, frame):
        raise TimeoutError("Shared original pencil budget exhausted")
    signal.signal(signal.SIGALRM, timeout)
    signal.signal(signal.SIGTERM, timeout)
    signal.setitimer(signal.ITIMER_REAL, args.remaining_seconds)
    try:
        m = module_at("r150_original_point_pencil_generator", args.generator)
        for s in args.points:
            result["parameters"]["actualPoints"].append(original_point(m, s))
            save()
        result["parameters"]["uniformNilpotenceDisprovedAtAnActualOriginalMean"] = any(
            not p["nilpotentAtThisOriginalMean"]
            for p in result["parameters"]["actualPoints"])
        result["status"] = "completed"
    except BaseException as exc:
        result["status"] = "incomplete"
        result["error"] = type(exc).__name__+": "+str(exc)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        save()
        print(json.dumps({"status": result["status"], "receipt": str(path),
            "bytes": path.stat().st_size, "sha256": sha_file(path),
            "elapsedSeconds": result["elapsedSeconds"]}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
