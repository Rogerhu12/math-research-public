#!/usr/bin/env python3
"""Read-only independent binary/Toeplitz/colon replay of completed P31 pages.

AI-assisted: GPT-6 Astra Pro / literature_audit, 2026-11-16.
Does not import the producer, its core, or its Schur helper.
All replay matrices and result arrays remain temporary.
"""
import argparse
import array
import gzip
import hashlib
import json
from pathlib import Path
import struct
import sys
import time
from flint import nmod_mat

P, MOD, NR, NC, RANK = 31, 31**5, 155, 224, 142
RAW_PIN = (26562, "7e1a65781f45f53a77dbac77c73f155979db71988b6fad9043116f51c25b12be")
MANIFEST_PIN = (34722, "709ae4705596a71519ebc3800b1a6f03cf296523f90463815ab72a89504fdb23")
BINDING = "7699b41009fc57c84b54055757d05e72a3aa1295082e289436c6856235daed71"


def require(ok, why):
    if not ok:
        raise AssertionError(why)


def canonical(x):
    return (json.dumps(x, sort_keys=True, ensure_ascii=True, separators=(",", ":"))+"\n").encode("ascii")


def digest(b):
    return hashlib.sha256(b).hexdigest()


def read_checked(path, pin):
    b = Path(path).read_bytes()
    require((len(b), digest(b)) == pin, "Complete actual byte identity")
    return b


def mat(nr, nc, values, modulus):
    return nmod_mat(nr, nc, [int(v) % modulus for v in values], modulus)


def change(M, modulus):
    return mat(M.nrows(), M.ncols(), (M[i, j] for i in range(M.nrows()) for j in range(M.ncols())), modulus)


def zero(M):
    return all(not M[i, j] for i in range(M.nrows()) for j in range(M.ncols()))


def product(A, B, degree, modulus):
    aa, bb = [change(M, modulus) for M in A], [change(M, modulus) for M in B]
    nonzero_a, nonzero_b = [not zero(M) for M in aa], [not zero(M) for M in bb]
    ans = []
    for k in range(degree+1):
        M = mat(aa[0].nrows(), bb[0].ncols(), [0]*(aa[0].nrows()*bb[0].ncols()), modulus)
        for j in range(max(0, k-len(bb)+1), min(k, len(aa)-1)+1):
            if nonzero_a[j] and nonzero_b[k-j]:
                M += aa[j]*bb[k-j]
        ans.append(M)
    return ans


def phase(root, manifest, name):
    record = manifest["phases"][name]
    require(record["verified"] and Path(record["file"]).name == record["file"], "Verified immutable phase path")
    blob = read_checked(root/record["file"], (record["bytes"], record["sha256"]))
    data = gzip.decompress(blob)
    require(len(data) <= 16*1024*1024 and len(data) == record["decodedBytes"]
            and digest(data) == record["payloadSha256"], "Full immutable decoded phase identity")
    require(data[:8] == b"R15PC31A", "Independent phase magic")
    hlen, = struct.unpack_from("<I", data, 8)
    require(hlen <= 131072 and 12+hlen <= len(data), "Complete bounded phase header")
    head = json.loads(data[12:12+hlen])
    require(head["binding"] == BINDING and head["phase"] == name
            and head["metadata"] == record["metadata"], "Header binding and metadata")
    off, groups, moduli = 12+hlen, {}, {}
    for group in head["groups"]:
        nr, nc, count, modulus = (group[k] for k in ("rows", "cols", "length", "modulus"))
        require(nr in (155, 224) and nc == 224 and 1 <= count <= 25
                and modulus in [31**j for j in range(1, 6)], "Actual matrix sizes and residue rings")
        matrices = []
        for _ in range(count):
            size = 4*nr*nc
            require(off+size <= len(data), "No truncated coefficient block")
            values = array.array("I")
            values.frombytes(data[off:off+size])
            if sys.byteorder != "little":
                values.byteswap()
            require(all(v < modulus for v in values), "All exact canonical residues")
            matrices.append(mat(nr, nc, values, modulus))
            off += size
        require(group["name"] not in groups, "No duplicate phase group")
        groups[group["name"]], moduli[group["name"]] = matrices, modulus
    require(off == len(data), "Complete phase EOF")
    return groups, moduli, head["metadata"]


def toeplitz_rank(B, order):
    coefficient = [change(M, P) for M in B[:order]]
    T = nmod_mat(NR*order, NC*order, [0]*(NR*NC*order*order), P)
    for i in range(order):
        for j in range(i+1):
            A = coefficient[i-j]
            for a in range(NR):
                for b in range(NC):
                    if A[a, b]:
                        T[NR*i+a, NC*j+b] = A[a, b]
    return T.rank()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--checkpoints", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    raw = json.loads(read_checked(args.receipt, RAW_PIN))
    manifest = json.loads(read_checked(args.checkpoints/"checkpoint-manifest.json", MANIFEST_PIN))
    require(raw["status"] == "completed" and raw["exitCode"] == 0
            and raw["binding"] == manifest["binding"] == BINDING
            and digest(canonical(raw["parameters"]["bindingInput"])) == BINDING,
            "Actual completed source semantic binding")
    require(set(manifest["phases"]) == {f"{name}-{a}" for name in ("state", "field") for a in range(5)},
            "All five complete states and source bases, no omitted page")
    initial, _, _ = phase(args.checkpoints, manifest, "state-0")
    B0 = initial["B"]
    records = []
    actual_original_products = 0
    actual_colon_coordinates = 0
    for a in range(5):
        state, moduli, metadata = phase(args.checkpoints, manifest, "state-"+str(a))
        field, fmoduli, fs = phase(args.checkpoints, manifest, "field-"+str(a))
        B, Z, V = state["B"], state["Z"], field["V"]
        require(moduli == {"B": P**(5-a), "Z": MOD} and fmoduli == {"V": P}, "Full actual coefficient moduli")
        require(len(B) == len(Z) == 25-4*a and len(V) == 21-4*a,
                "Actual recorded precision24,20,16,12,8 and basis20,16,12,8,4")
        require(int(V[0].det()) != 0, "Complete source transformation constant is a field unit")
        ranks = [toeplitz_rank(B, n) for n in (4, 5)]
        require(ranks[1]-ranks[0] == RANK, "Complete original rank142 from independent Toeplitz increment")
        parameter_length = 5*RANK-ranks[1]
        require(parameter_length == fs["positiveParameterLength"], "Independent complete parameter length")
        genuine = product(B0, Z, len(B)-1, MOD)
        for k, M in enumerate(genuine):
            expected = mat(NR, NC, (P**a*int(B[k][i, j]) for i in range(NR) for j in range(NC)), MOD)
            require(M == expected, "Independent whole source provenance at modulus p5")
        actual_original_products += len(B)*NR*NC
        kernel_product = product(B, V, len(V)-1, P**(5-a))
        require(all(int(M[i, j]) % P == 0 for M in kernel_product for i in range(NR) for j in range(RANK, NC)),
                "Every current complete kernel entry actually divisible by31")
        if a < 4:
            successor, _, _ = phase(args.checkpoints, manifest, "state-"+str(a+1))
            Bn, Zn = successor["B"], successor["Z"]
            source_product = product(Z, V, len(V)-1, MOD)
            for k, M in enumerate(kernel_product):
                expected = mat(NR, NC, (int(M[i, j]) if j < RANK else int(M[i, j])//P
                                       for i in range(NR) for j in range(NC)), P**(4-a))
                require(expected == Bn[k], "Independent complete constant-width colon identity")
                expected_source = mat(NC, NC, (int(source_product[k][i, j])*(P if j < RANK else 1)
                                               for i in range(NC) for j in range(NC)), MOD)
                require(expected_source == Zn[k], "Independent complete column-source update")
            actual_colon_coordinates += len(V)*(NR+NC)*NC
        records.append({"page": a, "inputDegree": len(B)-1, "basisDegree": len(V)-1,
                        "toeplitzRanksAtOrders4And5": ranks,
                        "completeParameterTorsionLength": parameter_length,
                        "constantUnitDeterminant": int(V[0].det())})
    lengths = [r["completeParameterTorsionLength"] for r in records]
    require(lengths == [22, 22, 19, 18, 17], "Actual independent completed length sequence")
    exponents = [e for e in range(1, 5) for _ in range(lengths[e-1]-lengths[e])]
    require(exponents == [2, 2, 2, 3, 4] and sum(exponents) == 13, "Independent coefficient lengths and no whole-W gap")
    result = {"format": "r150-original-projection31-colon-independent-replay-v1", "status": "completed",
              "producerNotImported": True, "coreAndSchurHelperNotImported": True,
              "source": {"bytes": Path(__file__).stat().st_size, "sha256": digest(Path(__file__).read_bytes())},
              "parentRaw": {"bytes": RAW_PIN[0], "sha256": RAW_PIN[1]},
              "parentManifest": {"bytes": MANIFEST_PIN[0], "sha256": MANIFEST_PIN[1]},
              "parentBinding": BINDING, "allTenImmutableFullByteAndPayloadHashesVerified": True,
              "allOriginalProvenanceCoordinates": actual_original_products,
              "allColonAndSourceUpdateCoordinates": actual_colon_coordinates,
              "pages": records, "projectedCoefficientExponents": exponents,
              "projectedCoefficientLength": sum(exponents), "remainingWholeWOverMExactLength": 0,
              "elapsedSeconds": time.monotonic()-started}
    args.out.write_bytes(canonical(result))
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
