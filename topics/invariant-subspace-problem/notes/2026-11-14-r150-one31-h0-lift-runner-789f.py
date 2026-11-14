#!/usr/bin/env python3
"""Lift the original fixed h0 with exactly one31-denominator at this precision.

Target31*h0 modulo29791; all equation rows remain the original17 system.
Only the final image/source/transport/product run. Old198 and old selected VQ
are reused, with all actual global315 constant identities checked beforehand.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import struct
import subprocess
import sys
import time

sys.dont_write_bytecode = True
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
CONTRACT = "2026-11-14-r150-one31-h0-lift-input-contract-789f.json"
OLD_RUNNER = "2026-11-14-r150-four-second-bockstein-runner-789f.py"
BASE = "2026-11-14-r150-second-bockstein-"
PROGRAMS = {
    "image": (BASE + "all198-global-image-mixture-789f.cpp", []),
    "source9": (BASE + "source-checkpoint-789f.cpp", ["-DR150_TARGETS=9"]),
    "transport": (BASE + "all198-global-original-transport-789f.cpp", []),
    "original": ("2026-11-14-r150-one31-h0-original-combination-789f.cpp", []),
}
RHS_BOUND = 87
SOURCE_BOUND = RHS_BOUND + 96


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as source:
        for block in iter(lambda: source.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def suffix(path, ending):
    return Path(str(path) + ending)


def negative(polys):
    return [[[-coefficient for coefficient in poly] for poly in row] for row in polys]


def scaled(polys, scalar):
    return [[[scalar * coefficient for coefficient in poly] for poly in row] for row in polys]


def verify_original_h0_system(global_path, four_path, first_path):
    def matrix(data, offset, rows, columns):
        block = data[offset:offset + rows * columns]
        if len(block) != rows * columns or any(value > 30 for value in block):
            raise ValueError("actual full315 matrix field/dimensions")
        return [list(block[i * columns:(i + 1) * columns]) for i in range(rows)]
    g, f, r = [gzip.decompress(path.read_bytes()) for path in (global_path, four_path, first_path)]
    if g[:8] != b"R150GP31" or struct.unpack_from("<4I", g, 8) != (31, 315, 9, 2):
        raise ValueError("actual selected global315 system")
    if f[:8] != b"R150D2S1" or struct.unpack_from("<5I", f, 8) != (31, 315, 4, 6, 9):
        raise ValueError("actual old four global315 system")
    if r[:8] != b"R150BI31" or struct.unpack_from("<7I", r, 8) != (31, 315, 200, 1152, 9, 2, 6):
        raise ValueError("actual original h0 first residual system")
    D = matrix(g, 24, 315, 9)
    W = matrix(g, 24 + 4 * 315 * 9, 315, 2)
    O = matrix(f, 28 + 6 * 4, 315, 4)
    if W != matrix(f, 28 + 6 * 4 + 315 * 4, 315, 2):
        raise ValueError("same actual first image basis")
    first_offset = 36 + 200 * 16 + 1152 * 8
    first_image = matrix(r, first_offset, 315, 1152)
    if W != [row[1150:1152] for row in first_image]:
        raise ValueError("same genuine beta199/beta200 source dictionary")
    R = matrix(r, first_offset + 315 * 1152, 315, 9)
    coefficients = [
        [23, 11, 28, 14, 2, 29, 5, 6, 27],
        [29, 1, 7, 26, 12, 30, 13, 10, 16],
        [0, 13, 16, 10, 13, 5, 23, 22, 15],
        [17, 6, 30, 21, 0, 8, 22, 24, 22],
        [25, 10, 17, 29, 4, 20, 11, 1, 26],
        [30, 17, 0, 3, 21, 3, 25, 10, 7],
        [3, 6, 0, 18, 7, 12, 27, 0, 10],
    ]
    U = [W[i] + O[i] + [D[i][0]] for i in range(315)]
    failures = [sum((R[i][j] - sum(U[i][k] * coefficients[k][j] for k in range(7))) % 31 != 0
                    for i in range(315)) for j in range(9)]
    if any(failures):
        raise ValueError("complete original h0 first-residual identity failed")
    polys = [[[value] if value else [] for value in row] for row in coefficients]
    beta = polys[:2] + [[[] for _ in range(9)] for _ in range(2)]
    old_four = polys[2:6]
    selected = [polys[6]] + [[[] for _ in range(9)] for _ in range(8)]
    return old_four, beta, selected, {
        "all315CoordinatesRetained": True,
        "fullOriginalH0ConstantIdentityNonzeroCounts": failures,
        "usesPrimaryProjection": False,
        "actualSourceOrder": ["beta199", "beta200", "old4001", "old4002", "old4003", "old4004", "selected2"],
        "constantCoefficientMatrix7By9": coefficients,
        "oldFourPolynomialsAscending": old_four,
        "firstBetaCorrectionPolynomialsAscending": beta,
        "selectedNinePolynomialsAscending": selected,
        "rightHandSideCostBound": RHS_BOUND,
        "provedTemporarySourceCostBound": SOURCE_BOUND,
    }


def verify_original_integer_models(first_path, higher_path):
    first = first_path.read_text().split()
    higher = higher_path.read_text().split()
    if len(first) != 4477 or first[0] != "R150_ORIGINAL_MOD961_V1":
        raise ValueError("same original integer first-residual model")
    if len(higher) != 4478 or higher[0] != "R150_ORIGINAL_PH0_MOD29791_V1":
        raise ValueError("fixed original31h0 higher model")
    if [int(value) % 961 for value in higher[1:-26]] != [int(value) for value in first[1:-25]]:
        raise ValueError("all4433 equation coefficients and18 row-scale tokens must match modulo961")
    target = list(map(int, higher[-26:]))
    if target[-1] or any(value % 31 for value in target) or [value // 31 for value in target[:-1]] != list(map(int, first[-25:])):
        raise ValueError("target31h0 must use the exact same original h0 modulo961")
    return {"all4433EquationAnd18ScaleResiduesVerifiedModulo961": True,
            "sameOriginalH0VerifiedAfterDividing31Target": True}


def uniform_original_x0(original, output):
    data = original.read_bytes()
    if data[:8] != b"R150P031" or struct.unpack_from("<5I", data, 8) != (6188, 9, 85, 217374, 24):
        raise ValueError("actual original h0 standard source header")
    expected_h0_mod961 = [0,0,0,268,904,282,438,562,685,519,163,247,499,229,433,886,851,162,370,747,926,849,435,91,242]
    if list(struct.unpack_from("<25H", data, 28)) != expected_h0_mod961:
        raise ValueError("same fixed original h0 in actual x0")
    answer = bytearray(b"R150PS31") + struct.pack("<5I", 31, 31, 6188, 9, 85) + struct.pack("<9H", *range(2, 11))
    offset = 78
    nonzero = 0
    maxcost = -1
    multipliers = []
    def enumerate_keys(left, lower, key):
        if not left:
            multipliers.append(key)
            return
        for variable in range(lower, 11):
            enumerate_keys(left - 1, variable, key + 8 ** variable)
    for degree in range(4):
        enumerate_keys(degree, 0, 0)
    for row in range(1, 6189):
        header = data[offset:offset + 15]
        if len(header) != 15:
            raise ValueError("truncated actual original source row")
        number, equation, multiplier, delta = struct.unpack("<IBQH", header)
        degree, key = 0, multiplier
        while key:
            degree += key % 8
            key //= 8
        if number != row or equation != (row - 1) % 17 or multiplier != multipliers[(row - 1) // 17] or delta != 10 * (degree + 1) + (5 if equation >= 11 else 0):
            raise ValueError("actual original6188 source dictionary")
        answer.extend(header)
        offset += 15
        for target in range(9):
            length = struct.unpack_from("<H", data, offset)[0]
            offset += 2
            polynomial = data[offset:offset + length]
            offset += length
            if len(polynomial) != length or length > 86 - delta or any(value > 30 for value in polynomial) or (length and not polynomial[-1]):
                raise ValueError("actual original x0 polynomial digits or cost")
            answer.extend(struct.pack("<H", length))
            for value in polynomial:
                answer.extend(struct.pack("<H", value))
                nonzero += value != 0
            if length:
                maxcost = max(maxcost, length - 1 + delta)
    if offset != len(data) or maxcost != 85 or nonzero != 1855617:
        raise ValueError("actual full original x0 byte conversion")
    output.write_bytes(answer)
    return {"originalSHA256": sha(original), "uniformSHA256": sha(output),
            "all6188RowsAndNineCoefficientPolynomialsPreserved": True,
            "nonzeroInitialCoefficients": nonzero, "maximumInitialSourceCost": maxcost,
            "onlyU8ToU16CoefficientEncodingChanged": True}


def main():
    parser = argparse.ArgumentParser()
    for name in ("notes-root", "t96-recovery", "all198-recovery", "out"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--math-seconds", type=int, default=120)
    parser.add_argument("--memory-mib", type=int, default=512)
    parser.add_argument("--compile-seconds", type=int, default=30)
    parser.add_argument("--resume-recovery", type=Path)
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()
    if min(args.math_seconds, args.memory_mib, args.compile_seconds) < 1:
        raise ValueError("explicit positive resource bounds required")
    root = Path(__file__).resolve().parent
    notes = args.notes_root.resolve()
    output = args.out.resolve()
    output.mkdir(parents=True, exist_ok=True)
    results, recovery, binaries = [output / name for name in ("results", "recovery", "bin")]
    if args.resume_recovery and args.resume_recovery.resolve() != recovery:
        shutil.copytree(args.resume_recovery, recovery, dirs_exist_ok=True)
    for directory in (results, recovery, binaries):
        directory.mkdir(exist_ok=True)
    inputs, cache = recovery / "inputs", recovery / "stage-cache"
    for directory in (inputs, cache):
        directory.mkdir(exist_ok=True)
    receipt_path = results / "one31-h0-second-lift-pipeline-receipt.json"
    receipt = {
        "format": "r150-one31-h0-actual-second-lift-v1",
        "status": "preparing", "prime": 31, "targetModulus": 29791,
        "targetMultiplier": "31*h0", "projectorUsed": False,
        "rightHandSideCostBound": RHS_BOUND, "provedTemporarySourceCostBound": SOURCE_BOUND,
        "fullOriginalMod29791IdentityVerified": False, "finite_budget_verified": False,
        "characteristicZeroIdentityAsserted": False,
        "old198OrSelectedNineSourceRecomputed": False,
        "fullOriginalTarget31h0Mod29791IdentityVerified": False,
        "originalh0SourceHas31DenominatorExponentAtMostOne": False,
        "sharedMathematicalSecondsLimit": args.math_seconds,
        "perChildAddressSpaceMiBLimit": args.memory_mib,
        "perCompilationSecondsLimit": args.compile_seconds,
        "deadlineRule": "Frozen input verification, saved315-array identity checks and four individually bounded compilations precede the clock. All four new native mathematical stages, their checkpoint loading and their cache checks share one deadline. Each child receives only the actual remaining time. SIGTERM has up to10seconds for an actual checkpoint before forced kill. Final lossless compression/manifests follow outside that clock.",
        "partialRecoveryPerStage": {"image": "complete-stage content cache; no internal checkpoint",
            "source": "actual VQ source array, next G row and phase; periodic and SIGTERM checkpoint",
            "transport": "complete-stage content cache; no internal checkpoint",
            "original": "actual product array, completed raw row, statistics and both complete source prefixes; SIGTERM checkpoint"},
        "inputs": {}, "sources": {}, "compilations": {}, "stages": {},
    }
    math_start = None

    def save():
        receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")

    try:
        contract = json.loads((root / CONTRACT).read_text())
        receipt["inputContractSHA256"] = sha(root / CONTRACT)
        scopes = {"notes": notes, "all198": args.all198_recovery.resolve(), "t96": args.t96_recovery.resolve()}
        found = {}
        for name, item in contract["inputs"].items():
            scope = scopes[item["scope"]]
            if "gzipRelative" in item:
                compressed = scope / item["gzipRelative"]
                if sha(compressed) != item["compressedSHA256"]:
                    raise ValueError("frozen compressed input SHA " + name)
                decoded = inputs / (name + ".bin")
                if not decoded.exists() or sha(decoded) != item["sha256"]:
                    with gzip.open(compressed, "rb") as src, decoded.open("wb") as dst:
                        shutil.copyfileobj(src, dst)
                candidates = [decoded]
            else:
                candidates = [scope / item["relative"]] if "relative" in item else sorted({p for n in item["names"] for p in scope.rglob(n)})
            candidate = next((p.resolve() for p in candidates if p.is_file() and sha(p) == item["sha256"]), None)
            if candidate is None:
                raise ValueError("missing exact saved input " + name)
            found[name] = candidate
            receipt["inputs"][name] = {"file": str(candidate), "bytes": candidate.stat().st_size, "sha256": item["sha256"]}
        for name, expected in contract["dependencies"].items():
            candidate = root / name
            if not candidate.is_file():
                candidate = notes / name
            if sha(candidate) != expected:
                raise ValueError("frozen native dependency " + name)
            receipt["sources"][name] = expected
        receipt["sources"][Path(__file__).name] = sha(Path(__file__))
        receipt["sources"][CONTRACT] = sha(root / CONTRACT)
        helper_path = root / OLD_RUNNER if (root / OLD_RUNNER).is_file() else notes / OLD_RUNNER
        spec = importlib.util.spec_from_file_location("r150_one31_h0_frozen_helper", helper_path)
        helper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(helper)
        receipt["originalIntegerModelConsistency"] = verify_original_integer_models(found["integerFirstModel"], found["integerModel"])
        found["uniformX"] = inputs / "original-h0-x0-uniform.bin"
        receipt["actualOriginalX0Conversion"] = uniform_original_x0(found["originalX0"], found["uniformX"])
        old_four, beta, selected_polys, proof = verify_original_h0_system(found["globalSystem"], found["fourFullSystem"], found["firstFullSystem"])
        receipt["originalh0SevenColumnIdentity"] = proof
        (results / "one31-h0-315-identity.json").write_text(json.dumps(proof, indent=2) + "\n")
        labels9, labels4, betalabels = list(range(2, 11)), list(range(4001, 4005)), list(range(2275, 2279))
        families = [
            {"nf": found["r1NF"], "q": found["r1Q"], "rem": found["r1Rem"], "trace": found["r1Trace"], "labels": labels9, "polys": helper.identity(9)},
            {"nf": found["selectedNF"], "q": found["selectedQ"], "rem": found["selectedRem"], "trace": found["selectedTrace"], "labels": labels9, "polys": negative(selected_polys)},
            {"nf": found["fourNF"], "q": found["fourQ"], "rem": found["fourRem"], "trace": found["fourTrace"], "labels": labels4, "polys": negative(old_four)},
            {"nf": found["betaNF"], "q": found["betaQ"], "rem": found["betaRem"], "trace": found["betaTrace"], "labels": betalabels, "polys": negative(beta)},
        ]
        mix = inputs / "one31-h0-nine-image.mix"
        helper.write_mix(mix, labels9, RHS_BOUND, families)
        executables = {}
        for name, (filename, flags) in PROGRAMS.items():
            source = root / filename if (root / filename).is_file() else notes / filename
            executable = binaries / name
            command = ["timeout", "--kill-after=10s", str(args.compile_seconds) + "s", "prlimit", "--as=" + str(args.memory_mib * 1048576), "--core=0", "--", "g++", "-O3", "-std=c++17", "-I", str(root), "-I", str(notes)] + flags + [str(source), "-o", str(executable)]
            started = time.monotonic()
            process = subprocess.run(command, capture_output=True, text=True)
            (results / ("compile-" + name + ".log")).write_text(process.stdout + process.stderr)
            receipt["compilations"][name] = {"command": command, "exitCode": process.returncode, "elapsedSeconds": time.monotonic() - started}
            save()
            if process.returncode:
                raise RuntimeError("bounded compilation failed " + name)
            executables[name] = executable
        if args.prepare_only:
            receipt["status"] = "prepared-no-native-mathematical-stage-executed"
            save()
            return
        math_start = time.monotonic()
        deadline = math_start + args.math_seconds
        receipt["status"] = "running"
        save()

        def prefix(name):
            directory = recovery / name
            directory.mkdir(exist_ok=True)
            return directory / name

        def binding(infiles, logical, program):
            return digest({"inputs": [sha(p) for p in infiles], "logical": logical,
                           "program": receipt["sources"][PROGRAMS[program][0]],
                           "headers": {k: v for k, v in receipt["sources"].items() if k.endswith(".hpp")}})

        def run_stage(name, program, arguments, marker, required, infiles, outfiles, logical):
            key = binding(infiles, logical, program)
            cachefile = cache / (name + ".json")
            if cachefile.exists():
                saved = json.loads(cachefile.read_text())
                if saved.get("inputBindingSHA256") == key and all(p.exists() and sha(p) == saved.get("outputs", {}).get(str(p.relative_to(recovery))) for p in outfiles):
                    receipt["stages"][name] = {"status": "completed", "reusedCompletedActualStage": True,
                        "inputBindingSHA256": key, "nativeStatistics": saved["nativeStatistics"], "elapsedSeconds": 0}
                    save()
                    return
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("shared mathematical deadline before " + name)
            command = ["timeout", "--kill-after=10s", f"{remaining:.3f}s", "prlimit", "--as=" + str(args.memory_mib * 1048576), "--core=0", "--", str(executables[program])] + list(map(str, arguments))
            stage = {"status": "running", "inputBindingSHA256": key, "command": command, "remainingSecondsAtStart": remaining}
            receipt["stages"][name] = stage
            save()
            started = time.monotonic()
            events = []
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
            with (results / (name + ".log")).open("w") as log:
                for line in process.stdout:
                    log.write(line)
                    log.flush()
                    print(line, end="", flush=True)
                    try:
                        event = json.loads(line)
                        events.append(event)
                        stage["lastProgress"] = event
                        save()
                    except (ValueError, TypeError):
                        pass
            code = process.wait()
            last = events[-1] if events else {}
            complete = code == 0 and last.get("status") == marker and all(last.get(k) == v for k, v in required.items()) and all(p.exists() for p in outfiles)
            stage.update(status="completed" if complete else "failed-or-incomplete", exitCode=code, elapsedSeconds=time.monotonic() - started, nativeStatistics=last)
            receipt["mathematicalElapsedSeconds"] = time.monotonic() - math_start
            save()
            if not complete:
                raise RuntimeError("actual stage failed or incomplete " + name)
            cachefile.write_text(json.dumps({"inputBindingSHA256": key, "outputs": {str(p.relative_to(recovery)): sha(p) for p in outfiles}, "nativeStatistics": last}, indent=2) + "\n")

        image = prefix("one31-h0-image")
        image_data = [found["graph"]] + [f[k] for f in families for k in ("nf", "q", "rem")]
        run_stage("image", "image", [found["graph"], mix, image], "saved-quotient-mixture-complete",
                  {"fullImageQuotientIdentity": True, "completeRHSInImage": True}, image_data,
                  [suffix(image, s) for s in ("-normal-forms.bin", "-image-quotients.bin", "-image-remainders.bin", "-image-certificate.json")],
                  {"bound": RHS_BOUND, "labels": labels9, "polynomials": [f["polys"] for f in families]})
        source = prefix("one31-h0-source")
        source_data = [found["graph"], found["originalNF"], suffix(image, "-normal-forms.bin"), suffix(image, "-image-quotients.bin"), suffix(image, "-image-remainders.bin")]
        source_key = binding(source_data, {"bound": RHS_BOUND, "targets": 9}, "source9")
        run_stage("source", "source9", source_data + [source, source_key], "packed-image-source-convolution-complete",
                  {"fullNormalFormDecompositionIdentity": True, "standardKernelNormalForm": True, "completeRHSInImage": True}, source_data,
                  [suffix(source, s) for s in ("-standard-coefficients.bin", "-source-certificate.json", "-vq-checkpoint.bin")],
                  {"bound": RHS_BOUND, "checkpointBinding": source_key})
        transport = prefix("one31-h0-transport")
        transport_data = [suffix(source, "-standard-coefficients.bin"), found["model"], found["normalTrace"], found["forward"], found["backward"]]
        run_stage("transport", "transport", transport_data + [mix, transport], "original-source-transport-complete", {},
                  transport_data + [f["trace"] for f in families],
                  [suffix(transport, "-primitive-source-mod31.bin"), suffix(transport, "-original-transport.json")],
                  {"bound": RHS_BOUND, "polynomials": [f["polys"] for f in families]})
        transported = json.loads(suffix(transport, "-original-transport.json").read_text())
        paid_bound = max([RHS_BOUND] + transported["sourceCosts"])
        if paid_bound > SOURCE_BOUND:
            raise ValueError("actual original source exceeded proved183 budget")
        final_sources = [
            {"file": found["uniformX"], "labels": labels9, "polys": helper.identity(9, 31)},
            {"file": found["selectedK2"], "labels": labels9, "polys": selected_polys},
            {"file": found["fourK2"], "labels": labels4, "polys": old_four},
            {"file": found["kernels"], "labels": betalabels, "polys": scaled(beta, 31)},
            {"file": suffix(transport, "-primitive-source-mod31.bin"), "labels": labels9, "polys": helper.identity(9, 961)},
        ]
        recipe = inputs / "one31-h0-nine-original.recipe"
        helper.write_original(recipe, labels9, paid_bound, 29791, 1, final_sources)
        original = prefix("one31-h0-original")
        original_data = [found["model"], found["integerModel"]] + [f["file"] for f in final_sources]
        logical = {"bound": paid_bound, "divisor": 29791, "targetMode": 1, "polynomials": [f["polys"] for f in final_sources]}
        original_key = binding(original_data, logical, "original")
        run_stage("original", "original", [found["model"], found["integerModel"], recipe, original, original_key], "full-original-combination-complete",
                  {"divisor": 29791, "allOriginalProductCoefficientsDivisible": True, "fullOriginalSeventeenEquationIdentityMod29791": True}, original_data,
                  [suffix(original, s) for s in ("-primitive-source-mod29791.bin", "-original-seventeen-source-mod29791.bin", "-original-product.json")],
                  {**logical, "checkpointBinding": original_key})
        conclusion = json.loads(suffix(original, "-original-product.json").read_text())
        if not all(conclusion[k] for k in ("fullOriginalSeventeenEquationIdentityMod29791", "fullOriginalMacaulayIdentityMod29791", "originalRowScaleTransportVerified", "allWeightedBoundsVerified")):
            raise ValueError("actual full original17 completion fields")
        receipt.update(status="completed", outcome="one31-denominator-h0-full-original-mod29791-certificate",
            fullOriginalMod29791IdentityVerified=True, finite_budget_verified=True,
            fullOriginalTarget31h0Mod29791IdentityVerified=True,
            originalh0SourceHas31DenominatorExponentAtMostOne=True,
            actualSourceCosts=conclusion["actualSourceCosts"], originalSeventeenConclusion=conclusion,
            mathematicalElapsedSeconds=time.monotonic() - math_start)
        save()
    except Exception as error:
        receipt.update(status="failed-or-incomplete", errorType=type(error).__name__, error=str(error))
        if math_start is not None:
            receipt["mathematicalElapsedSeconds"] = time.monotonic() - math_start
        save()
    finally:
        certificates = results / "certificates"
        certificates.mkdir(exist_ok=True)
        files = []
        for path in sorted(recovery.rglob("*")):
            if not path.is_file() or path.is_relative_to(cache):
                continue
            relative = path.relative_to(recovery)
            flat = str(relative).replace("/", "__")
            if path.suffix in (".json", ".mix", ".recipe"):
                shutil.copyfile(path, results / flat)
                continue
            temporary = recovery / (flat + ".gz.tmp")
            with path.open("rb") as src, temporary.open("wb") as dst:
                with gzip.GzipFile(filename="", mode="wb", fileobj=dst, mtime=0) as zipped:
                    shutil.copyfileobj(src, zipped)
            item = {"originalFile": str(relative), "uncompressedBytes": path.stat().st_size,
                "uncompressedSHA256": sha(path), "compressedBytes": temporary.stat().st_size,
                "compressedSHA256": sha(temporary), "parts": []}
            with temporary.open("rb") as src:
                part = 1
                while block := src.read(4_500_000):
                    target = certificates / (flat + ".gz" if item["compressedBytes"] <= 4_500_000 else flat + f".gz.part{part:03d}")
                    target.write_bytes(block)
                    item["parts"].append({"file": str(target.relative_to(results)), "bytes": len(block), "sha256": hashlib.sha256(block).hexdigest()})
                    part += 1
            temporary.unlink()
            files.append(item)
        (results / "certificate-manifest.json").write_text(json.dumps({"format": "r150-one31-h0-lossless-generated-certificates-v1",
            "pipelineStatus": receipt["status"], "partialCheckpointIsNotIdentity": True, "files": files}, indent=2) + "\n")
        recovery_files = [{"file": str(p.relative_to(recovery)), "bytes": p.stat().st_size, "sha256": sha(p)}
                          for p in sorted(recovery.rglob("*")) if p.is_file()]
        (results / "recovery-manifest.json").write_text(json.dumps({"format": "r150-one31-h0-complete-recovery-v1",
            "pipelineStatus": receipt["status"], "files": recovery_files}, indent=2) + "\n")
        receipt.update(recoveryFiles=len(recovery_files), recoveryBytes=sum(p["bytes"] for p in recovery_files),
                       losslessGeneratedBinaryFiles=len(files))
        save()
        print(json.dumps({k: receipt.get(k) for k in ("status", "outcome", "mathematicalElapsedSeconds", "projectorUsed",
            "rightHandSideCostBound", "fullOriginalMod29791IdentityVerified", "actualSourceCosts", "recoveryBytes")}), flush=True)
    if receipt["status"] not in ("completed", "prepared-no-native-mathematical-stage-executed"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
