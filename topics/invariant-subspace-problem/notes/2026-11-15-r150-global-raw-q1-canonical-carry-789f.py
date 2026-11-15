#!/usr/bin/env python3
"""Verify the same raw global q1 section against paid 20-jets; save its p carry.

No VQ/normal-form or mathematical search is run. Inputs are immutable byte streams.
R150QC31 output: magic; 7 little-endian u32 (p, evaluation modulus, carry modulus,
rows, targets, Taylor length, center); 64 ASCII semantic binding; seven u16 global
slot labels; seven u16 paid K labels; then 6188 records consisting of the exact
15-byte original row header (u32 raw,u8 equation,u64 multiplier,u16 delta) and
20*7 u8 carry coefficients in [jet][target] order.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
import math
import mmap
import os
from pathlib import Path
import struct
import sys
import time

import numpy as np

P = 31
MOD = P * P
NR = 6188
NT = 7
L = 20
RAW_COST = 177
PAID_Q1_SHA256 = "4b02069c7654c942cfa6e180bec630b32b4121bf66e941443cef74b6a1cae5d2"
ROW_HEADER = struct.Struct("<IBQH")
U16 = struct.Struct("<H")
U32 = struct.Struct("<I")
K_LABEL = struct.Struct("<IHHII")
OUTPUT_MAGIC = b"R150QC31"


class Failure(RuntimeError):
    pass


class Reader:
    def __init__(self, name: str):
        self.path = Path(name)
        with self.path.open("rb") as fh:
            if os.fstat(fh.fileno()).st_size == 0:
                raise Failure(f"empty input: {self.path}")
            self.data = mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ)
        self.pos = 0
        self.sha256 = hashlib.sha256(self.data).hexdigest()

    def take(self, n: int) -> bytes:
        if n < 0 or self.pos + n > len(self.data):
            raise Failure(f"truncated input at {self.pos}: {self.path}")
        out = self.data[self.pos:self.pos + n]
        self.pos += n
        return out

    def unpack(self, form: struct.Struct):
        if self.pos + form.size > len(self.data):
            raise Failure(f"truncated structured record: {self.path}")
        out = form.unpack_from(self.data, self.pos)
        self.pos += form.size
        return out

    def u16(self) -> int:
        return self.unpack(U16)[0]

    def u32(self) -> int:
        return self.unpack(U32)[0]

    def array(self, dtype: str, n: int):
        item = np.dtype(dtype).itemsize
        if n < 0 or self.pos + item * n > len(self.data):
            raise Failure(f"truncated coefficient array: {self.path}")
        out = np.frombuffer(self.data, dtype=dtype, count=n, offset=self.pos)
        self.pos += item * n
        return out

    def eof(self):
        if self.pos != len(self.data):
            raise Failure(f"trailing bytes in {self.path}: {len(self.data)-self.pos}")


def require(ok, text: str):
    if not bool(ok):
        raise Failure(text)


def dictionary():
    # Same C++ enumeration: degree 0..3; nondecreasing variable indices 0..10.
    powers = [8 ** i for i in range(11)]
    multipliers = []
    degrees = []
    for degree in range(4):
        for variables in itertools.combinations_with_replacement(range(11), degree):
            multipliers.append(sum(powers[i] for i in variables))
            degrees.append(degree)
    require(len(multipliers) == 364, "complete original 364 multipliers")
    headers = []
    for raw in range(1, NR + 1):
        equation = (raw - 1) % 17
        index = (raw - 1) // 17
        delta = 10 * (degrees[index] + 1) + (5 if equation >= 11 else 0)
        headers.append((raw, equation, multipliers[index], delta))
    return headers


def old_kernel(reader: Reader, headers, tick):
    require(reader.take(8) == b"R150KK31", "old K200 magic")
    require(tuple(reader.u32() for _ in range(4)) == (31, 6188, 200, 85),
            "same full old K200 dimensions")
    labels = []
    costs = []
    for j in range(200):
        graph, head, cost, source, raw = reader.unpack(K_LABEL)
        require(graph >= 1 and head >= 1035 and 1 <= source <= 2195
                and 1 <= raw <= 6188, "old K200 original source metadata")
        require(cost == (80 if j < 160 else 81 if j < 198 else 85),
                "same old K200 per-column source costs")
        labels.append(head)
        costs.append(cost)
    require(len(set(labels)) == 200, "old K200 unique source labels")
    nonzero = 0
    for index, header in enumerate(headers):
        require(reader.unpack(ROW_HEADER) == header, "old K200 complete row dictionary")
        delta = header[3]
        for j in range(200):
            n = reader.u16()
            require(n <= max(0, costs[j] - delta + 1),
                    "old K200 weighted polynomial bound")
            if n:
                a = reader.array("u1", n)
                require(int(a[-1]) != 0 and int(a.max()) <= 30,
                        "old K200 canonical nonzero polynomial tail")
                nonzero += int(np.count_nonzero(a))
        if index % 256 == 0:
            tick()
    reader.eof()
    return labels, costs, nonzero


def paid_jets(reader: Reader, headers, kernel_labels, tick):
    require(reader.take(8) == b"R150SP31", "paid twenty-jet source magic")
    scope = tuple(reader.u32() for _ in range(8))
    require(scope == (31, 6188, 197, 20, 140, 2, 6188, 177),
            "paid original q1 twenty-jet exact completed scope")
    binding_bytes = reader.take(64)
    try:
        binding = binding_bytes.decode("ascii")
    except UnicodeDecodeError as exc:
        raise Failure("paid q1 binding encoding") from exc
    require(len(binding) == 64 and all(c in "0123456789abcdef" for c in binding),
            "paid q1 semantic SHA256")
    labels = [reader.u16() for _ in range(197)]
    require(labels == kernel_labels[1:198], "all paid labels exactly old K2..K198")

    # Physical records are unaligned 10-byte dictionaries followed by 5 planes.
    dtype = np.dtype([
        ("id", "<u4"), ("raw", "<u4"), ("delta", "<u2"),
        ("words", "<u4", (5, 20, 7))
    ], align=False)
    require(dtype.itemsize == 2810, "packed row byte count")
    require(len(reader.data) - reader.pos == NR * dtype.itemsize,
            "full paid packed length and no trailing bytes")
    rows = np.ndarray((NR,), dtype=dtype, buffer=reader.data, offset=reader.pos)
    raw = np.arange(1, NR + 1, dtype=np.uint32)
    deltas = np.asarray([h[3] for h in headers], dtype=np.uint16)
    require(np.array_equal(rows["id"], raw) and np.array_equal(rows["raw"], raw)
            and np.array_equal(rows["delta"], deltas), "all paid original row dictionaries")
    words = rows["words"]
    require(not np.any(words[:, :, :, -1] >> 5),
            "all paid 197-target padding bits are zero")
    # A bit set in all five planes would encode 31, not an F31 coefficient.
    require(not np.any(np.bitwise_and.reduce(words, axis=1)),
            "all 197*20*6188 paid field coefficients are canonical")
    selected = np.zeros((NR, L, NT), dtype=np.uint8)
    shifts = np.arange(NT, dtype=np.uint32)
    for plane in range(5):
        selected |= (((words[:, plane, :, 0, None] >> shifts) & 1)
                     .astype(np.uint8) << plane)
    reader.pos = len(reader.data)
    reader.eof()
    tick()
    return selected, labels[:NT], binding


def global_q1(reader: Reader, headers, tick):
    require(reader.take(8) == b"R150PS31", "global raw q1 primitive source magic")
    prime, modulus, rows, targets, bound = (reader.u32() for _ in range(5))
    require((prime, modulus, rows, targets) == (31, 31, NR, 9),
            "global raw q1 exact prime/modulus/original rows/nine slots")
    require(10 <= bound <= 1348, "declared global source bound")
    labels = [reader.u16() for _ in range(9)]
    require(labels == list(range(2, 11)), "global original nine target labels")
    # q1 itself has the paid cost177; a larger allocation bound is not a new cost.
    max_length = RAW_COST - min(h[3] for h in headers) + 1
    coefficients = np.zeros((NR, NT, max_length), dtype=np.uint8)
    costs = [-1] * 9
    nonzero = 0
    for index, header in enumerate(headers):
        require(reader.unpack(ROW_HEADER) == header,
                "global full 6188 original row dictionary")
        delta = header[3]
        for j in range(9):
            n = reader.u16()
            require(n <= max(0, bound - delta + 1), "global declared weighted bound")
            if j >= NT:
                require(n == 0, "unused global raw q1 slots8/9 must be exactly zero")
            else:
                require(n <= max(0, RAW_COST - delta + 1),
                        "global raw q1 actual cost must not exceed177")
            a = reader.array("<u2", n)
            if n:
                require(int(a[-1]) != 0 and int(a.max()) <= 30,
                        "global canonical s coefficients and polynomial tail")
                coefficients[index, j, :n] = a
                costs[j] = max(costs[j], delta + n - 1)
                nonzero += int(np.count_nonzero(a))
        if index % 256 == 0:
            tick()
    reader.eof()
    return coefficients, labels[:NT], bound, costs, nonzero


def taylor_powers(maximum: int):
    # P[d,k] is [t^k](2+t)^d modulo961. No field reduction before division by31.
    values = np.zeros((maximum + 1, L), dtype=np.int64)
    values[0, 0] = 1
    for degree in range(1, maximum + 1):
        values[degree] = (2 * values[degree - 1]) % MOD
        values[degree, 1:] = (values[degree, 1:] + values[degree - 1, :-1]) % MOD
    return values


def atomic_json(path: Path, value):
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8") as fh:
        json.dump(value, fh, ensure_ascii=False, sort_keys=True, indent=2)
        fh.write("\n")
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(temporary, path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--global-source", required=True)
    parser.add_argument("--paid-jets", required=True)
    parser.add_argument("--old-kernel", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--remaining-seconds", type=float)
    args = parser.parse_args()
    started = time.monotonic()
    if args.remaining_seconds is not None:
        require(math.isfinite(args.remaining_seconds) and args.remaining_seconds > 0,
                "one shared positive remaining-seconds budget")

    def tick():
        if args.remaining_seconds is not None:
            if time.monotonic() - started >= args.remaining_seconds:
                raise TimeoutError("shared budget exhausted before a completed carry certificate")

    inputs = {
        "globalSource": Reader(args.global_source),
        "paidJets": Reader(args.paid_jets),
        "oldKernel": Reader(args.old_kernel)
    }
    require(inputs["paidJets"].sha256 == PAID_Q1_SHA256,
            "paid twenty-jet q1 input must match the completed second-stage source SHA256")
    tick()
    headers = dictionary()
    kernel_labels, kernel_costs, old_nonzero = old_kernel(inputs["oldKernel"], headers, tick)
    paid, paid_labels, paid_binding = paid_jets(
        inputs["paidJets"], headers, kernel_labels, tick)
    coefficients, global_labels, bound, costs, new_nonzero = global_q1(
        inputs["globalSource"], headers, tick)
    require(paid_labels == kernel_labels[1:8], "selected paid K2..K8 source labels")

    powers = taylor_powers(coefficients.shape[2] - 1)
    carry = np.empty((NR, L, NT), dtype=np.uint8)
    evaluations_sha = hashlib.sha256()
    coordinates = 0
    for start in range(0, NR, 256):
        stop = min(start + 256, NR)
        flat = coefficients[start:stop].reshape(-1, coefficients.shape[2]).astype(np.int64)
        evaluated = (flat @ powers) % MOD
        evaluated = evaluated.reshape(stop - start, NT, L).transpose(0, 2, 1)
        old = paid[start:stop].astype(np.int64)
        mismatch = (evaluated % P) != old
        if np.any(mismatch):
            offset, degree, target = map(int, np.argwhere(mismatch)[0])
            raise Failure(
                "raw q1 field mismatch: "
                f"originalRow={start+offset+1}, TaylorDegree={degree}, "
                f"globalSlotLabel={global_labels[target]}, "
                f"paidKLabel={paid_labels[target]}, "
                f"globalEvaluationMod31={int(evaluated[offset, degree, target] % P)}, "
                f"paidCanonicalTField={int(old[offset, degree, target])}")
        difference = evaluated - old
        require(not np.any(difference % P) and int(difference.min()) >= 0
                and int(difference.max()) <= 930,
                "every canonical s/t carry is an exact multiple of31")
        current = (difference // P).astype(np.uint8)
        require(np.array_equal(old + P * current.astype(np.int64), evaluated),
                "full canonical q1s=q1t+31c reconstruction modulo961")
        carry[start:stop] = current
        evaluations_sha.update(np.ascontiguousarray(evaluated, dtype="<u2").tobytes())
        coordinates += (stop - start) * L * NT
        tick()

    input_hashes = {name: r.sha256 for name, r in inputs.items()}
    script_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    semantic = {
        "format": "r150-raw-q1-canonical-carry-v1",
        "scriptSHA256": script_sha,
        "inputSHA256": input_hashes,
        "prime": P, "evaluationModulus": MOD, "carryModulus": P,
        "rows": NR, "TaylorCenter": 2, "TaylorPrecision": L,
        "globalSlotLabels": global_labels, "paidKernelLabels": paid_labels,
        "sourceMap": "global slots1..7 = old K2..K8; slots8/9 exactly zero"
    }
    binding = hashlib.sha256(json.dumps(
        semantic, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
    output_dir = Path(args.out)
    output_dir.mkdir(parents=True, exist_ok=True)
    binary = output_dir / "q1-s-to-t-carry.bin"
    receipt_path = output_dir / "q1-s-to-t-carry-receipt.json"
    if receipt_path.exists():
        previous = json.loads(receipt_path.read_text(encoding="utf-8"))
        require(previous.get("bindingSHA256") == binding,
                "existing output directory belongs to different source bytes")

    temporary = binary.with_name(binary.name + ".tmp")
    header_sha = hashlib.sha256()
    with temporary.open("wb") as out:
        out.write(OUTPUT_MAGIC)
        out.write(struct.pack("<7I", P, MOD, P, NR, NT, L, 2))
        out.write(binding.encode("ascii"))
        out.write(struct.pack("<7H", *global_labels))
        out.write(struct.pack("<7H", *paid_labels))
        for index, header in enumerate(headers):
            raw = ROW_HEADER.pack(*header)
            header_sha.update(raw)
            out.write(raw)
            out.write(carry[index].tobytes(order="C"))
        out.flush()
        os.fsync(out.fileno())
    expected = 8 + 7 * 4 + 64 + 4 * NT + NR * (ROW_HEADER.size + L * NT)
    require(temporary.stat().st_size == expected, "complete carry output exact byte length")
    tick()
    os.replace(temporary, binary)
    output_sha = hashlib.sha256(binary.read_bytes()).hexdigest()
    receipt = {
        **semantic,
        "status": "completed",
        "bindingSHA256": binding,
        "paidJetBindingSHA256": paid_binding,
        "declaredGlobalBound": bound,
        "actualGlobalSourceCosts": costs,
        "allOriginalRowsVerified": True,
        "allFieldJetsMatch": True,
        "integerCarryIdentityVerified": True,
        "allOriginal6188RowsVerified": True,
        "all197PaidTargetLabelsAndPaddingVerified": True,
        "allPaidFieldCoefficientsCanonical": True,
        "allInputTailBytesVerified": True,
        "allSevenRawSectionsEqualPaidModulo31": True,
        "canonicalSTCarryIdentityModulo961Verified": True,
        "q2Transport": "q2_local := q2_local - c; after whole P use P*c",
        "globalSlots8And9ExactlyZero": True,
        "verifiedCarryCoordinates": coordinates,
        "nonzeroCarryCoordinates": int(np.count_nonzero(carry)),
        "oldKernelNonzeroCoefficientsRead": old_nonzero,
        "globalQ1NonzeroCoefficientsRead": new_nonzero,
        "evaluationModulo961SHA256": evaluations_sha.hexdigest(),
        "originalRowDictionarySHA256": header_sha.hexdigest(),
        "output": {
            "file": binary.name, "magic": OUTPUT_MAGIC.decode(),
            "SHA256": output_sha, "bytes": expected,
            "shape": [NR, L, NT], "coefficientType": "uint8",
            "recordDictionaryBytes": ROW_HEADER.size,
            "coefficientOrder": "row then Taylor degree then selected source"
        },
        "newVQOrMathematicalSearchExecuted": False,
        "globalOriginal17IdentityClaimed": False,
        "elapsedSeconds": time.monotonic() - started,
        "inputPathsAuditOnly": {name: str(r.path) for name, r in inputs.items()}
    }
    atomic_json(receipt_path, receipt)
    print(json.dumps(receipt,
                     ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except TimeoutError as exc:
        print(json.dumps({"status": "deadline-no-complete-certificate", "error": str(exc)}),
              file=sys.stderr)
        sys.exit(75)
    except Exception as exc:
        print(json.dumps({"status": "failed", "error": str(exc)}), file=sys.stderr)
        sys.exit(1)
