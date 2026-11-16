#!/usr/bin/env python3
"""Complete original two-atom Macaulay rank at fixed prime 127.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

Reconstruct the already verified exact 17-equation model from its original
producer and require its complete paid logical SHA.  This does not depend on
the lifetime of an earlier Actions job.  Reduce only with the exact, verified
17 constant row scales, all units at 127.  The native program constructs every
one of the 17*364 source products and all 4367 positive target monomials.
No full-rank outcome is assumed.  A nonfull completed result includes the
complete original field cokernel, checked against all 6188 rows.
"""
import argparse
import gzip
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path
import resource
import struct
import subprocess
import sys
import time

FORMAT = "r150-original-nonrankone-two-atom-macaulay-field-v1"
PRODUCER_NAME = "2026-11-16-r150-original-nonrankone-two-atom-gradient-789f.py"
PRODUCER_SHA = "3729a351a361039e286b2435571da8c2c91d09d9822cc79cacb9cecf887928cc"
CPP_NAME = "2026-11-16-r150-original-nonrankone-two-atom-macaulay-rank-native-789f.cpp"
CPP_SHA = "a09439dd1e68b737b09d09d792158f6cd48ce8c6bad4e899746e584ef4822099"
HEADER_NAME = "2026-11-15-r150-original-f127-bitplane-789f.hpp"
HEADER_SHA = "03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3"
PAID_MODEL_BINDING = "2343a3e3f632236b0a5dc425f30a5f1ce27bfd10ff4add1d4c30c75ae692bcf9"
PAID_MODEL_LOGICAL_SHA = "1f93dcd7db76f433df57536d4bd0b51417ae2a12137e08136141b4a9689a8d8d"
PAID_MODEL_LOGICAL_BYTES = 173045
PAID_EQUATIONS_SHA = "d7056c0546a4b1379a019d70e7f81632539e4866c7e3e5bddde0da1b27692832"
PAID_LINEAR_SHA = "48708f39da70539929308f20e710907d5c0bce411b47e2a84783ed7e8406462d"
PAID_T3_SHA = "065706fcc695fd03762a049c03949e3b42f806845606aa228de0324e18017aa5"
P, NV, NE, NS, NT = 127, 11, 17, 6188, 4367


class Budget(Exception):
    pass


def need(ok, msg):
    if not ok:
        raise ValueError(msg)


def canon(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def descriptor(path):
    return {"path": path.name, "bytes": path.stat().st_size,
            "sha256": file_sha(path)}


def write_raw(path, raw):
    temp = path.with_name(path.name+".tmp")
    temp.write_bytes(raw)
    os.replace(temp, path)


def save_json(path, obj):
    raw = json.dumps(obj, ensure_ascii=False, sort_keys=True,
                     indent=2).encode("utf-8")
    write_raw(path, raw)
    return {"path": path.name, "bytes": len(raw), "sha256": sha(raw)}


def read_small(path, limit=100000):
    raw = path.read_bytes()
    need(len(raw) <= limit, "bounded small JSON: "+path.name)
    return json.loads(raw)


def import_source(path):
    spec = importlib.util.spec_from_file_location("r150_paid_nonrankone_model", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def monomials(lo, hi):
    return [t for degree in range(lo, hi+1)
            for t in itertools.combinations_with_replacement(range(NV), degree)]


def monomial_code(t):
    return sum(1 << (3*j) for j in t)


def rebuild_or_reuse_model(module, out):
    started = time.monotonic()
    path = out/"paid-original-seventeen-model.json.gz"
    reused = path.exists()
    if reused:
        with gzip.open(path, "rb") as stream:
            raw = stream.read(PAID_MODEL_LOGICAL_BYTES+1)
        need(len(raw) == PAID_MODEL_LOGICAL_BYTES
             and sha(raw) == PAID_MODEL_LOGICAL_SHA,
             "whole cached original model equals the paid exact data")
        payload = json.loads(raw)
        reran_original_identities = False
    else:
        model, flags = module.original_model()
        need(flags["originalLinearRank"] == 11
             and flags["T3LinearRank"] == 11
             and flags["fullLinearCertificateObtained"]
             and flags["allOriginalRowScales127Units"],
             "all paid original small-model gates rebuilt")
        binding = sha(module.canonical({
            "format": module.FORMAT, "sourceSha256": PRODUCER_SHA,
            "literalK": module.KRAW, "mean": module.Y_FIXED,
            "atomicH0": [str(x) for x in module.H0_FIXED],
            "sixOriginalMeanDirections": 6,
            "elevenOriginalHankelDirections": 11,
        }))
        need(binding == PAID_MODEL_BINDING, "paid original model semantic binding")
        payload = {"format": module.FORMAT+"-model", "binding": binding,
                   "data": model}
        raw = module.canonical(payload)
        need(len(raw) == PAID_MODEL_LOGICAL_BYTES
             and sha(raw) == PAID_MODEL_LOGICAL_SHA,
             "complete exact model recreated with the original paid SHA")
        write_raw(path, gzip.compress(raw, compresslevel=1, mtime=0))
        reran_original_identities = True
    need(payload["format"] == module.FORMAT+"-model"
         and payload["binding"] == PAID_MODEL_BINDING,
         "original producer model format and binding")
    data = payload["data"]
    need(data["completeEquationsSha256"] == PAID_EQUATIONS_SHA
         and data["linearPartSha256"] == PAID_LINEAR_SHA
         and data["T3MapSha256"] == PAID_T3_SHA,
         "all paid original matrix hashes")
    return data, {
        "paidLogicalBytes": len(raw), "paidLogicalSha256": sha(raw),
        "paidModelBinding": PAID_MODEL_BINDING,
        "reusedIdenticalTemporaryModel": reused,
        "allOriginalRationalModelIdentitiesRerun": reran_original_identities,
        "elapsedSeconds": time.monotonic()-started,
        "temporaryModel": descriptor(path),
    }


def prepare_native_input(module, data, out):
    qmon = monomials(1, 2)
    mul = monomials(0, 3)
    target = monomials(1, 5)
    need(len(qmon) == 77 and len(mul) == 364 and len(target) == NT,
         "whole original monomial degree dictionaries")
    need(data["polynomialMonomials"] == [[]]+[list(t) for t in qmon],
         "paid model ordinary monomial ordering")
    need(len(data["equations"]) == NE
         and len(data["primitiveIntegerEquations"]) == NE,
         "all seventeen original rows present")
    blob = bytearray(struct.pack("<8s9I", b"R15NAM01", 1, P, NV, NE, 3, 5, NS, NT, 77))
    ratios = []
    exact_checks = field_checks = 0
    max_integer_bits = 0
    for i, row in enumerate(data["primitiveIntegerEquations"]):
        coeff = row["coefficients"]
        need(len(coeff) == 77 and all(isinstance(v, int) for v in coeff),
             "entire primitive integer equation")
        original = {}
        for key, value in data["equations"][i]:
            key = tuple(key)
            need(key in qmon and key not in original, "whole positive original equation")
            original[key] = module.fmpq(value)
        ratio = module.fmpq(row["originalPerPrimitive"])
        num, den = int(ratio.numer()), int(ratio.denom())
        need(num % P and den % P, "every original row transport is a 127 unit")
        ratio_field = (num % P)*pow(den % P, -1, P) % P
        ratios.append(str(ratio))
        blob.extend(struct.pack("<2I", i, 77))
        for key, value in zip(qmon, coeff):
            exact = original.get(key, module.fmpq(0))
            need(ratio*value == exact, "all 1309 original exact row coordinates")
            exact_checks += 1
            en, ed = int(exact.numer()), int(exact.denom())
            need(ed % P, "all original exact coefficients are 127-integral")
            v = value % P
            need((en % P)*pow(ed % P, -1, P) % P == ratio_field*v % P,
                 "all original field coefficient transports")
            field_checks += 1
            max_integer_bits = max(max_integer_bits, abs(value).bit_length())
            blob.extend(struct.pack("<QB", monomial_code(key), v))
    need(exact_checks == 1309 and field_checks == 1309,
         "whole original coefficient transport counts")
    native = out/"all-seventeen-original-primitive-equations-f127.bin"
    if native.exists():
        need(native.read_bytes() == bytes(blob), "same complete native input on continuation")
    else:
        write_raw(native, bytes(blob))
    source_dictionary = [[list(t), i] for t in mul for i in range(NE)]
    need(len(source_dictionary) == NS, "all original source multiplier pairs")
    return native, {
        "nativeInput": descriptor(native),
        "all1309ExactOriginalRowTransportCoordinatesVerified": True,
        "all1309OriginalFieldRowTransportCoordinatesVerified": True,
        "all17RowTransportScalarsAre127Units": True,
        "originalPerPrimitiveScalars": ratios,
        "maximumPrimitiveIntegerCoefficientBits": max_integer_bits,
        "sourceDictionarySha256": sha(canon(source_dictionary)),
        "outputDictionarySha256": sha(canon([list(t) for t in target])),
        "sourceDictionaryOrder": "multiplier total degree 0..3, tuple lexicographic; then original equation 0..16",
        "outputDictionaryOrder": "ordinary monomial total degree 1..5, tuple lexicographic",
        "sourceRows": NS, "targetColumns": NT,
        "all17Times364SourcesRetained": True,
        "allPositiveMonomialsThroughDegreeFiveRetained": True,
    }, target


def compile_native(cpp, header, out, budget):
    executable = out/"original-nonrankone-macaulay-native"
    marker = out/"compiled-native-identity.json"
    flags = ["-std=c++17", "-O2"]
    identity = {"sourceSha256": CPP_SHA, "headerSha256": HEADER_SHA,
                "flags": flags, "compiler": "g++"}
    started = time.monotonic()
    if executable.exists() and marker.exists():
        previous = read_small(marker)
        need(previous["identity"] == identity
             and previous["executableSha256"] == file_sha(executable),
             "exact compiled native identity on continuation")
        return executable, {"reused": True, "elapsedSeconds": time.monotonic()-started,
                            "executable": descriptor(executable)}
    command = ["g++"]+flags+["-I", str(header.parent), str(cpp), "-o", str(executable)]
    completed = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               text=True, timeout=budget, check=False)
    need(completed.returncode == 0, "native compilation: "+completed.stdout[-12000:])
    save_json(marker, {"identity": identity, "executableSha256": file_sha(executable)})
    return executable, {"reused": False, "elapsedSeconds": time.monotonic()-started,
                        "executable": descriptor(executable), "logTail": completed.stdout[-4000:]}


def inspect_checkpoint(out):
    index = out/"checkpoint-index.txt"
    if not index.exists():
        return None
    fields = index.read_text().split()
    need(len(fields) == 3 and fields[0] == "R150_NONRANKONE_INDEX1",
         "atomic complete checkpoint index")
    generation, slot = int(fields[1]), int(fields[2])
    need(generation > 0 and slot == generation % 2, "checkpoint slot generation")
    state = out/("state-slot-%d.bin" % slot)
    need(state.exists(), "complete active native checkpoint exists")
    return {"generation": generation, "slot": slot,
            "state": descriptor(state), "index": descriptor(index)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--producer", required=True)
    parser.add_argument("--native-source", required=True)
    parser.add_argument("--header", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--seconds", type=float, default=180)
    parser.add_argument("--memory-mib", type=int, default=2048)
    parser.add_argument("--compile-seconds", type=float, default=30)
    args = parser.parse_args()
    need(10 <= args.seconds <= 1800 and 512 <= args.memory_mib <= 4096
         and 5 <= args.compile_seconds <= 60, "bounded complete-rank resources")
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    resource.setrlimit(resource.RLIMIT_AS,
                       (args.memory_mib*1024**2, args.memory_mib*1024**2))
    started = time.monotonic()
    self_sha = file_sha(Path(__file__))
    receipt = {"format": FORMAT, "status": "started", "sourceSha256": self_sha,
               "parameters": {"prime": P, "seconds": args.seconds,
                              "memoryMiB": args.memory_mib,
                              "compileSecondsBudget": args.compile_seconds,
                              "allOriginalSourceCount": NS,
                              "allOriginalTargetCount": NT,
                              "rankNotPrespecified": True,
                              "historicalLargeArraysNeeded": False,
                              "paidSmallModelProducerSha256": PRODUCER_SHA}}
    exit_code = 1
    try:
        producer, cpp, header = map(Path, (args.producer, args.native_source, args.header))
        for path, name, expected in [
            (producer, PRODUCER_NAME, PRODUCER_SHA),
            (cpp, CPP_NAME, CPP_SHA),
            (header, HEADER_NAME, HEADER_SHA)]:
            need(path.name == name and file_sha(path) == expected,
                 "exact frozen source: "+name)
        need(cpp.parent.resolve() == header.parent.resolve(),
             "native quoted include is the exact verified header")
        module = import_source(producer)
        data, model_record = rebuild_or_reuse_model(module, out)
        receipt["parameters"]["originalModelReconstruction"] = model_record
        native_input, input_record, target = prepare_native_input(module, data, out)
        receipt["parameters"]["completeOriginalInput"] = input_record
        semantic = {
            "format": FORMAT, "sourceSha256": self_sha, "nativeSha256": CPP_SHA,
            "headerSha256": HEADER_SHA, "producerSha256": PRODUCER_SHA,
            "paidOriginalModelSha256": PAID_MODEL_LOGICAL_SHA,
            "nativeInputSha256": input_record["nativeInput"]["sha256"],
            "sourceDictionarySha256": input_record["sourceDictionarySha256"],
            "outputDictionarySha256": input_record["outputDictionarySha256"],
            "field": P, "sourceRows": NS, "targetColumns": NT,
            "nativeInputProtocol": "R15NAM01/version1",
            "nativeCheckpointProtocol": "R15NAC01/version1",
        }
        binding = sha(canon(semantic))
        receipt["binding"] = binding
        binding_path = out/"complete-mathematical-binding.json"
        if binding_path.exists():
            old = read_small(binding_path)
            need(old == {"binding": binding, "semantic": semantic},
                 "same complete mathematical input and code on continuation")
        else:
            save_json(binding_path, {"binding": binding, "semantic": semantic})
        receipt["parameters"]["previousCheckpoint"] = inspect_checkpoint(out)
        executable, compile_record = compile_native(cpp, header, out, args.compile_seconds)
        receipt["parameters"]["compilation"] = compile_record
        remaining = args.seconds-(time.monotonic()-started)-5
        if remaining < 5:
            raise Budget("preparation exhausted the bounded native budget")
        command = [str(executable), str(native_input), str(out),
                   format(remaining, ".9f"), binding]
        native_started = time.monotonic()
        process = subprocess.Popen(command, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT, text=True)
        terminated = False
        try:
            native_stdout, _ = process.communicate(timeout=remaining+15)
        except subprocess.TimeoutExpired:
            terminated = True
            process.terminate()
            try:
                native_stdout, _ = process.communicate(timeout=20)
            except subprocess.TimeoutExpired:
                process.kill()
                native_stdout, _ = process.communicate()
        receipt["parameters"]["nativeWallSeconds"] = time.monotonic()-native_started
        receipt["parameters"]["nativeExitCode"] = process.returncode
        receipt["parameters"]["nativeTerminationRequested"] = terminated
        receipt["parameters"]["nativeLogTail"] = native_stdout[-16000:]
        native_receipt_path = out/"original-nonrankone-macaulay-native-receipt.json"
        need(native_receipt_path.exists(), "actual bounded native receipt exists")
        native = read_small(native_receipt_path)
        receipt["parameters"]["nativeReceipt"] = descriptor(native_receipt_path)
        receipt["parameters"]["nativeStatistics"] = native.get("parameters", {})
        need(native.get("binding") == binding
             and native.get("format") == "r150-original-nonrankone-macaulay-field-native-v1",
             "actual native result has the complete current binding")
        receipt["parameters"]["lastWholeCheckpoint"] = inspect_checkpoint(out)
        if process.returncode == 75 and native.get("status") == "budget-checkpoint":
            receipt["status"] = "budget-checkpoint"
            exit_code = 75
        else:
            need(process.returncode == 0 and native.get("status") == "completed",
                 "native did not complete: "+str(native.get("parameters", {}).get("error", {})))
            stats = native["parameters"]
            rank = stats["rank"]
            need(stats["originalLinearFieldRank"] == 11
                 and stats["sourceRowsCompleted"] == NS
                 and stats["allOriginalSourceRowsProcessed"]
                 and stats["completeRankObtained"]
                 and stats["allOriginalSourceKernelProductsVerified"]
                 and stats["checkpointPhase"] == 3
                 and 0 <= rank <= NT, "complete original finite-field rank and kernel gates")
            k = NT-rank
            need(stats["originalKernelProductCoordinates"] == NS*k
                 and stats["freeIdentityCoordinates"] == k*k,
                 "full original source kernel counts")
            profile_path = out/"complete-original-field-profile.json"
            profile = read_small(profile_path, 300000)
            rows, piv = profile["originalSourceRows"], profile["leadingOriginalOutputColumns"]
            free = profile["freeOriginalColumns"]
            need(profile["binding"] == binding and profile["rank"] == rank
                 and len(rows) == len(piv) == rank
                 and rows == sorted(set(rows))
                 and all(0 <= j < NS for j in rows)
                 and len(set(piv)) == rank and all(0 <= j < NT for j in piv)
                 and free == sorted(set(range(NT))-set(piv))
                 and profile["sortedOriginalMinorDeterminant"] == stats["sortedOriginalMinorDeterminant"]
                 and 0 < profile["sortedOriginalMinorDeterminant"] < P,
                 "actual original row/column rank-minor profile")
            kernel = out/"complete-original-field-kernel.bin"
            expected_size = 8+4*4+64+4*k+NT*k
            need(kernel.stat().st_size == expected_size, "complete original field kernel binary size")
            with kernel.open("rb") as stream:
                head = stream.read(24)
                need(struct.unpack("<8s4I", head) == (b"R15NAK01",1,P,NT,k),
                     "original complete field kernel header")
                need(stream.read(64).decode("ascii") == binding,
                     "original complete field kernel binding")
            receipt["parameters"].update({
                "completeFieldRank": rank, "completeFieldCokernelDimension": k,
                "all6188OriginalRowsIncluded": True,
                "all4367OriginalPositiveTargetsIncluded": True,
                "completeFieldKernelVerifiedAgainstAllOriginalRows": True,
                "characteristicZeroRankLowerBound": rank,
                "characteristicZeroFullMacaulayRankProved": rank == NT,
                "fixedMeanEntireOriginalIdealEqualsMaximalIdealProved": rank == NT,
                "parameterOnlyNonzeroOriginalMinorExists": rank == NT,
                "rationalCokernelNotRecoveredWhenNonfull": rank != NT,
                "wholeFixedMeanClaimRequiresFullRank": True,
                "actualOriginalRankMinorDeterminant127": profile["sortedOriginalMinorDeterminant"],
                "actualMinorRowsSha256": sha(canon(rows)),
                "actualMinorColumnsSha256": sha(canon(sorted(piv))),
                "completeProfile": descriptor(profile_path),
                "completeFieldKernel": descriptor(kernel),
                "freeOriginalMonomialsPreview": [list(target[i]) for i in free[:64]],
                "freeOriginalMonomialsPreviewTruncated": k > 64,
            })
            receipt["status"] = "completed"
            exit_code = 0
    except Budget as exc:
        receipt["status"] = "budget-checkpoint"
        receipt["parameters"]["error"] = {"type": type(exc).__name__, "message": str(exc)}
        exit_code = 75
    except BaseException as exc:
        receipt["status"] = "failed"
        receipt["parameters"]["error"] = {"type": type(exc).__name__, "message": str(exc)}
        exit_code = 1
    finally:
        receipt["elapsedSeconds"] = time.monotonic()-started
        receipt["parameters"]["elapsedSecondsIncludesCompilation"] = receipt["elapsedSeconds"]
        desc = save_json(out/"original-nonrankone-complete-macaulay-rank-receipt.json", receipt)
        print(json.dumps({"status": receipt["status"], "exitCode": exit_code,
                          "binding": receipt.get("binding"), "receipt": desc,
                          "elapsedSeconds": receipt["elapsedSeconds"],
                          "parameters": receipt["parameters"]},
                         ensure_ascii=False, sort_keys=True), flush=True)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
