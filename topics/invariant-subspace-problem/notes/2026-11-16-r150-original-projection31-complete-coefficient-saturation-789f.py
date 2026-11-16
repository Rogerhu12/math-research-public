#!/usr/bin/env python3
"""Complete original P31 coefficient colon pages at t=s-2.

AI-assisted: GPT-6 Astra Pro / literature_audit, 2026-11-16.
The genuine formal source kernel, not a point/Toeplitz kernel, is used.
Finite prefixes are consumed only within their proved actual validity.
All matrices and checkpoints remain temporary.
"""
import argparse
import array
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
import struct
import sys
import time
import types
from flint import nmod_mat

FORMAT = "r150-original-projection31-complete-coefficient-saturation-v1"
P = 31
COEFFICIENT_DIGITS = 5
MOD = P**COEFFICIENT_DIGITS
ROWS, COLS, RANK = 155, 224, 142
DEADLINE = float("inf")
PINS = {
    "core": (34432, "727175cf485a8ba5b5146a4cc6e749962e109c9e42265a2dd45f58cecdf933fb"),
    "generator": (15328, "2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"),
    "schur": (37379, "dc17dc88a5f1415c648b6ba5bf3fab4f7fb810aef6cc1552a5b2ea4acacbdf79"),
    "primitive": (65159, "44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe"),
    "projection_receipt": (7828, "9acb3368250f9efeeed1b358036f3ee6620846ba48fb176f6b2011a94c00e2a4"),
    "gap_audit": (2013, "1ac4cfed2d998f11b9c382f814287d46f5a02e4be64e7b2db856839482a2b8f9"),
}
DECODED = (158741, "fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3")
CONSTRUCTION_PARENT = {
    "bytes": 20153,
    "sha256": "9261795904bf7181e4db84bac1cd4ec5bfaecc431af62755d8a1bd9f2e7d8c7f",
    "blob": "59dfb331f06d7ef1f84bf8c1aeca9a16848a1b10",
    "change": "same complete primitive/compression body, arithmetic modulus31^5 and explicit31-unit denominators",
}


def require(v, message):
    if not v:
        raise AssertionError(message)


def tick():
    if time.monotonic() >= DEADLINE:
        raise TimeoutError("Complete verified coefficient-page budget")


def canonical(x):
    return (json.dumps(x, sort_keys=True, ensure_ascii=True, separators=(",", ":"))+"\n").encode("ascii")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def identity(path, pin=None):
    b = Path(path).read_bytes()
    value = (len(b), sha(b))
    if pin is not None:
        require(value == pin, "Full source/input identity: "+str(path))
    return {"bytes": value[0], "sha256": value[1]}


def atomic(path, x):
    path = Path(path)
    data = canonical(x)
    tmp = path.with_name(path.name+".tmp-"+str(os.getpid()))
    with tmp.open("wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)
    return {"bytes": len(data), "sha256": sha(data)}


def module_at(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


class Ring:
    def __init__(self, modulus):
        self.modulus = modulus

    def mat(self, rows, cols, entries=None):
        data = [0]*(rows*cols) if entries is None else [int(v) % self.modulus for v in entries]
        return nmod_mat(rows, cols, data, self.modulus)

    def eye(self, n):
        return self.mat(n, n, (int(i == j) for i in range(n) for j in range(n)))

    def sub(self, M, rows, cols):
        rows, cols = list(rows), list(cols)
        return self.mat(len(rows), len(cols), (M[i, j] for i in rows for j in cols))

    def cat(self, blocks):
        require(blocks and len({M.nrows() for M in blocks}) == 1, "True horizontal join")
        nr = blocks[0].nrows()
        return self.mat(nr, sum(M.ncols() for M in blocks),
                        (M[i, j] for i in range(nr) for M in blocks for j in range(M.ncols())))


def convert(M, ring):
    return ring.mat(M.nrows(), M.ncols(), (M[i, j] for i in range(M.nrows()) for j in range(M.ncols())))


def iszero(M):
    return all(not M[i, j] for i in range(M.nrows()) for j in range(M.ncols()))


def convolution(A, B, degree, ring):
    require(A and B and A[0].ncols() == B[0].nrows(), "Complete series product shape")
    za = [iszero(M) for M in A]
    zb = [iszero(M) for M in B]
    out = []
    for k in range(degree+1):
        tick()
        M = ring.mat(A[0].nrows(), B[0].ncols())
        for i in range(max(0, k-len(B)+1), min(k, len(A)-1)+1):
            if not za[i] and not zb[k-i]:
                M += A[i]*B[k-i]
        out.append(M)
    return out


def matrix_sha(M):
    h = hashlib.sha256()
    h.update(struct.pack("<II", M.nrows(), M.ncols()))
    for i in range(M.nrows()):
        h.update(struct.pack("<"+"I"*M.ncols(), *(int(M[i, j]) for j in range(M.ncols()))))
    return h.hexdigest()


class Cache:
    MAGIC = b"R15PC31A"
    MAX_DECODED = 16 << 20
    MAX_STORED = 17 << 20

    def __init__(self, root, binding):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.path = self.root/"checkpoint-manifest.json"
        self.binding = binding
        if self.path.exists():
            self.manifest = json.loads(self.path.read_bytes())
            require(self.manifest["format"] == FORMAT and self.manifest["binding"] == binding,
                    "Exact immutable coefficient checkpoint binding")
        else:
            self.manifest = {"format": FORMAT, "binding": binding, "phases": {}}
            atomic(self.path, self.manifest)

    def has(self, name):
        return name in self.manifest["phases"]

    def put(self, name, series, moduli, metadata):
        require(set(series) == set(moduli), "Checkpoint groups and moduli")
        shape = []
        for key in sorted(series):
            matrices = series[key]
            require(matrices and len(matrices) <= 25, "Actual bounded series prefix")
            nr, nc = matrices[0].nrows(), matrices[0].ncols()
            require(1 <= nr <= COLS and 1 <= nc <= COLS and moduli[key] in [P**j for j in range(1, 6)],
                    "Bounded complete matrix shape/modulus")
            require(all(M.nrows() == nr and M.ncols() == nc for M in matrices), "Constant series shape")
            shape.append({"name": key, "length": len(matrices), "rows": nr, "cols": nc, "modulus": moduli[key]})
        head = canonical({"format": FORMAT, "binding": self.binding, "phase": name,
                          "groups": shape, "metadata": metadata})
        require(len(head) <= 1 << 17, "Bounded small checkpoint metadata")
        payload = bytearray(self.MAGIC+struct.pack("<I", len(head))+head)
        for group in shape:
            for M in series[group["name"]]:
                tick()
                values = array.array("I", (int(M[i, j]) for i in range(M.nrows()) for j in range(M.ncols())))
                require(values.itemsize == 4 and all(v < group["modulus"] for v in values),
                        "Canonical uint32 coefficient residues")
                if sys.byteorder != "little":
                    values.byteswap()
                payload.extend(values.tobytes())
        require(len(payload) <= self.MAX_DECODED, "Full phase decoded size bound")
        ph = sha(payload)
        path = self.root/(name+"-"+ph+".bin.gz")
        if not path.exists():
            tmp = path.with_name(path.name+".tmp-"+str(os.getpid()))
            with tmp.open("wb") as raw:
                with gzip.GzipFile(filename="", fileobj=raw, mode="wb", compresslevel=1, mtime=0) as f:
                    f.write(payload)
                raw.flush()
                os.fsync(raw.fileno())
            os.replace(tmp, path)
        ident = identity(path)
        require(ident["bytes"] <= self.MAX_STORED, "Full phase stored size bound")
        record = dict(ident, file=path.name, decodedBytes=len(payload), payloadSha256=ph,
                      verified=True, temporaryOnly=True, metadata=metadata)
        self.manifest["phases"][name] = record
        atomic(self.path, self.manifest)
        return record

    def get(self, name):
        rec = self.manifest["phases"][name]
        require(rec["verified"] and Path(rec["file"]).name == rec["file"], "Verified local immutable phase")
        path = self.root/rec["file"]
        require(rec["bytes"] <= self.MAX_STORED and rec["decodedBytes"] <= self.MAX_DECODED,
                "Stored bounded phase sizes")
        identity(path, (rec["bytes"], rec["sha256"]))
        with gzip.open(path, "rb") as f:
            payload = f.read(self.MAX_DECODED+1)
        require(len(payload) == rec["decodedBytes"] and sha(payload) == rec["payloadSha256"],
                "Entire decoded phase identity")
        require(payload[:8] == self.MAGIC, "Independent coefficient checkpoint magic")
        nhead, = struct.unpack_from("<I", payload, 8)
        require(nhead <= 1 << 17 and 12+nhead <= len(payload), "Bounded complete checkpoint header")
        head = json.loads(payload[12:12+nhead])
        require(head["format"] == FORMAT and head["binding"] == self.binding
                and head["phase"] == name and head["metadata"] == rec["metadata"],
                "Full checkpoint semantic identity")
        off, out = 12+nhead, {}
        for group in head["groups"]:
            nr, nc, count, modulus = (group[x] for x in ("rows", "cols", "length", "modulus"))
            require(1 <= nr <= COLS and 1 <= nc <= COLS and 1 <= count <= 25
                    and modulus in [P**j for j in range(1, 6)], "Decoded phase dimensions")
            ring, matrices = Ring(modulus), []
            for _ in range(count):
                size = 4*nr*nc
                require(off+size <= len(payload), "Complete coefficient payload")
                values = array.array("I")
                values.frombytes(payload[off:off+size])
                if sys.byteorder != "little":
                    values.byteswap()
                require(all(v < modulus for v in values), "Decoded canonical residues")
                matrices.append(ring.mat(nr, nc, values))
                off += size
            require(group["name"] not in out, "Unique checkpoint group")
            out[group["name"]] = matrices
        require(off == len(payload), "Complete checkpoint EOF")
        return out, head["metadata"]


# The following construction body is the frozen whole-original polynomial
# builder, with its arithmetic modulus changed to p^5. It still verifies all
# 6188 sources and both compression directions before any colon operation.

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
    return trim([v % MOD for v in c])


def pscale(a, c):
    return trim([v * c % MOD for v in a])


def shift_add(a, b, scalar, shift):
    if not b or scalar % MOD == 0:
        return a
    return padd(a, [0] * shift + pscale(b, scalar))


def pmul(a, b):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % MOD
    return trim(out)


def reduce_poly(q):
    den = int(q.denom())
    require(den % 31, "Every original whole rational polynomial denominator is a31 unit")
    inv = pow(den % MOD, -1, MOD)
    return trim([int(v) * inv % MOD for v in q.numer().coeffs()])


def taylor(q, center, degree):
    return [sum(q[d] * math.comb(d, k) * pow(center, d-k, MOD)
                for d in range(k, len(q))) % MOD for k in range(degree+1)]


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
            and len(contents) == 17 and den % 31 and all(c % 31 for c in contents),
            "All18 original normalization constants are31 units")
    scales = [den * pow(c % MOD, -1, MOD) % MOD for c in contents]
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
            q = trim([int(v) % MOD for v in coeff])
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
        weights.append((q[0] if q else 0)*pow(scales[i], -1, MOD) % MOD)
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
        "coefficientPrime": 31, "arithmeticModulus": MOD, "center": args.center, "TaylorDegree": N,
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
        "wholeOriginalProjectedRowsReduction31Sha256": sha(canonical([{j: w for j, q in row.items() if (w := trim([v % 31 for v in q]))} for row in rows])),
        "sourceDictionaryLogicalSha256": sha(canonical(labels)),
        "targetDictionaryLogicalSha256": sha(canonical(targets)),
        "compressedTaylorCoefficientSha256": [e.mh(X) for X in series],
        "physicalOriginalConstruction": physical,
    }
    rec["parameters"]["originalConstruction"] = metadata
    return series, sparse_taylor




def complete_source_basis(B, schur):
    """Complete formal kernel by true rank142; finite maps retain actual validity."""
    field = Ring(P)
    A = [convert(M, field) for M in B]
    N = len(A)-1
    r0 = schur.rank(A[0])
    require(0 < r0 <= RANK, "Actual complete-field constant rank")
    residual, lift, first = schur.unit_schur(A, schur.DF, r0)
    constant = [field.mat(COLS, r0) for _ in range(N+1)]
    for j, source in enumerate(first["unitColumns"]):
        constant[0][source, j] = 1
    active_groups = [{"exponent": 0, "width": r0, "valid": N, "map": constant}]
    profiles = [{"exponent": 0, **first}]
    covered, order, valid = r0, 0, N
    while covered < RANK:
        tick()
        require(residual and order <= 4, "Complete parameter rank142 must exit within paid maximum4")
        r = schur.rank(residual[0])
        if not r:
            residual = residual[1:]
            order += 1
            continue
        require(1 <= order <= 4 and covered+r <= RANK and valid >= order,
                "Actual positive source exits in true precision")
        reduced, rr = residual[0].rref()
        pc = schur.pivots(reduced, rr)
        active = [field.sub(M, range(COLS), pc) for M in lift]
        next_residual, transform, prof = schur.unit_schur(residual, schur.DF, r)
        active_groups.append({"exponent": order, "width": r, "valid": valid, "map": active})
        covered += r
        profiles.append({"exponent": order, **prof})
        nextvalid = min(valid, len(transform)-1)
        lift = schur.convolution(lift, transform, nextvalid, schur.DF)
        residual, valid = next_residual, nextvalid
    require(covered == RANK and lift[0].ncols() == COLS-RANK and all(iszero(M) for M in residual),
            "Full formal source kernel: all142 directions, remaining82 and generic-zero residual")
    actual_valid = min([valid]+[g["valid"] for g in active_groups])
    require(actual_valid >= N-4 and actual_valid >= 0, "Actual finite-prefix loss at most4")
    V = [field.cat([g["map"][k] for g in active_groups]+[lift[k]]) for k in range(actual_valid+1)]
    require(V[0].nrows() == COLS and V[0].ncols() == COLS, "Full224 source basis shape")
    determinant = int(V[0].det())
    require(determinant % P and V[0]*V[0].inv() == field.eye(COLS), "True constant source basis is a31 unit")
    product = convolution(A, V, actual_valid, field)
    for M in product:
        require(iszero(field.sub(M, range(ROWS), range(RANK, COLS))),
                "All155 by82 kernel products at every actual coefficient")
    offset, positive = 0, []
    for group in active_groups:
        e, width = group["exponent"], group["width"]
        require(e <= actual_valid, "Original full positive exit contained in true verified prefix")
        for k in range(e):
            require(iszero(field.sub(product[k], range(ROWS), range(offset, offset+width))),
                    "All complete-current-image products before source exit zero")
        lead = field.sub(product[e], range(ROWS), range(offset, offset+width))
        require(schur.rank(lead) == width, "Actual source exit leading rank")
        if e:
            positive.extend([e]*width)
        offset += width
    require(offset == RANK, "All142 active source directions retained")
    summary = {
        "constantRank": r0, "genericRank": covered,
        "sourceKernelRank": COLS-RANK, "targetFreeRank": ROWS-RANK,
        "positiveParameterExponents": positive, "positiveParameterLength": sum(positive),
        "maximumParameterExponent": max(positive, default=0),
        "inputTaylorDegree": N, "actualSourceBasisValidDegree": actual_valid,
        "constantSourceBasisDeterminantMod31": determinant,
        "allUnitSchurRowsAndOriginalCurrentProductsVerified": True,
        "completeFormalKernelByGenericRank142": True,
        "missingTaylorTailNotFilledWithZero": True,
        "sourceBasisCoefficientSha256": [matrix_sha(M) for M in V],
        "unitProfiles": profiles,
    }
    return V, summary


def source_check(B0, B, Z, page):
    require(len(B) == len(Z), "Same true source/product prefix")
    N, full = len(B)-1, Ring(MOD)
    original = convolution(B0, Z, N, full)
    for k in range(N+1):
        tick()
        expected = full.mat(ROWS, COLS, (P**page*int(B[k][i, j]) for i in range(ROWS) for j in range(COLS)))
        require(original[k] == expected, "All original projected-source products p^a B_a = B0 Z_a modp5")
    return {"allOriginalSourceProductsVerified": True,
            "coefficientCount": N+1, "scalarCoordinateCount": (N+1)*ROWS*COLS,
            "modulus": MOD, "page": page,
            "allOriginal6188SourcesCoveredByVerifiedTwoSidedCompression": True,
            "globalPolynomialIdentityClaimed": False,
            "formalIdentityRestrictedToActualValidPrefix": True,
            "sourceCoefficientSha256": [matrix_sha(M) for M in Z],
            "originalProductCoefficientSha256": [matrix_sha(M) for M in original]}


def colon_step(B, Z, V, page):
    require(page < 4, "No coefficient division beyond paid exponent4")
    N = len(V)-1
    current_modulus, next_modulus = P**(COEFFICIENT_DIGITS-page), P**(COEFFICIENT_DIGITS-page-1)
    current, full, next_ring = Ring(current_modulus), Ring(MOD), Ring(next_modulus)
    W = convolution(B, [convert(M, current) for M in V], N, current)
    next_B = []
    divisions = 0
    for M in W:
        data = []
        for i in range(ROWS):
            for j in range(COLS):
                v = int(M[i, j])
                if j >= RANK:
                    require(v % P == 0, "Every true kernel-product coefficient divisible by31")
                    v //= P
                    divisions += 1
                data.append(v % next_modulus)
        next_B.append(next_ring.mat(ROWS, COLS, data))
    source_product = convolution(Z, [convert(M, full) for M in V], N, full)
    next_Z = [full.mat(COLS, COLS,
                      (int(M[i, j])*(P if j < RANK else 1) for i in range(COLS) for j in range(COLS)))
              for M in source_product]
    return next_B, next_Z, {
        "allKernelEntriesDividedOnlyAfterExactDivisibility": True,
        "dividedKernelScalarCoordinates": divisions,
        "sameWidth224": True, "activeDirectionsRetained": RANK,
        "allFormalKernelDirectionsRetained": COLS-RANK,
        "newCoefficientModulus": next_modulus, "actualTaylorDegree": N,
        "noZeroCompletionOfMissingTaylorTail": True,
    }


def completed_result(summaries, H, baseline):
    lengths = [r["positiveParameterLength"] for r in summaries]
    require(lengths[0] == baseline+len(H), "Original complete field length and five true coefficient directions")
    require(all(a >= b >= baseline for a, b in zip(lengths, lengths[1:])), "Actual colon-image monotonicity")
    require(lengths[-1] == baseline, "Actual coefficient saturation fully reached within exponent4")
    while len(lengths) < max(H)+1:
        lengths.append(baseline)
    multiplicities = [lengths[e-1]-lengths[e] for e in range(1, max(H)+1)]
    exponents = [e for e, m in enumerate(multiplicities, 1) for _ in range(m)]
    require(len(exponents) == len(H) and all(a <= b for a, b in zip(exponents, H)),
            "Complete five-summand quotient obeys exact ambient invariant-factor bound")
    length = sum(exponents)
    gap = sum(H)-length
    require(0 <= gap <= 8, "Remaining whole-W gap obeys paid complete bound")
    return {
        "complete": True, "coefficientPrime": P, "residueCenter": 2,
        "fullProjectedGenericRank": RANK, "initialSourceCount": COLS,
        "fullOriginalSourceCount": 6188,
        "actualParameterTorsionLengths": [r["positiveParameterLength"] for r in summaries],
        "unchangedFreePlusQuotientDefectLength": baseline,
        "quotientDefectLengthOneRetained": True,
        "projectedCoefficientTorsionExponents": exponents,
        "projectedCoefficientTorsionLength": length,
        "wholeWOverMExactLength": gap,
        "wholeWEqualsM": gap == 0,
        "remainingEmbeddedGapNotIdentifiedIfNonzero": gap != 0,
        "completeFormalSourceKernelsAtEveryPage": True,
        "allOriginalFinitePrefixSourceProductsVerified": True,
        "noFullAEliminationOrHistorical210Replay": True,
    }


def main():
    global DEADLINE
    ap = argparse.ArgumentParser()
    for key in PINS:
        ap.add_argument("--"+key.replace("_", "-"), type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--seconds", type=float, default=600)
    ap.add_argument("--memory-mib", type=int, default=2048)
    args = ap.parse_args()
    args.center, args.degree = 2, 24
    require(1 <= args.seconds <= 1800 and 768 <= args.memory_mib <= 4096, "Explicit bounded coefficient task")
    args.out.mkdir(parents=True, exist_ok=True)
    resource.setrlimit(resource.RLIMIT_AS, (args.memory_mib << 20, args.memory_mib << 20))
    start = time.monotonic()
    DEADLINE = start+args.seconds
    rec = {"format": FORMAT, "status": "started", "exitCode": 1, "parameters": {}}
    cache = None
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError("Hard coefficient-page budget")))
    signal.setitimer(signal.ITIMER_REAL, args.seconds)
    try:
        inputs = {k: identity(getattr(args, k), pin) for k, pin in PINS.items()}
        parent = json.loads(args.projection_receipt.read_bytes())
        gap = json.loads(args.gap_audit.read_bytes())
        require(parent["status"] == "completed" and parent["exitCode"] == 0 and parent["binding"] ==
                "544b53829f50ec0ce0f5293c9bec19d55802a743da43041c454c011fda501eee",
                "Same complete original P31 root-two parent")
        require(gap["status"] == "completed" and gap["remainingWholeWOverMEmbedsInPtimesRootTwoTOverS"]
                and gap["remainingWholeWOverMRootOneZeroByKilledByP"], "Same proved whole-W gap input")
        H = gap["rootTwoTOverS"]["exponents"]
        require(H == [2, 2, 2, 3, 4], "Exact prior complete H2 relation-lattice type")
        old = parent["parameters"]["actualSmith"]
        require(old["complete"] and old["cumulativeGenericRank"] == RANK and old["maximumPositiveExponent"] == 4,
                "Paid full parameter rank and precision debt")
        baseline = old["positiveLength"]-len(H)
        require(baseline == 17, "Free-plus-defect baseline, without deleting J")
        binding_input = {"format": FORMAT, "source": identity(__file__), "inputs": inputs,
                         "constructionOrigin": CONSTRUCTION_PARENT, "prime": P, "center": 2,
                         "initialTaylorDegree": 24, "initialCoefficientDigits": 5,
                         "maximumCoefficientPages": 4, "fullSourceShape": [ROWS, COLS],
                         "genericRank": RANK, "unchangedFreePlusQuotientDefectLength": baseline}
        binding = sha(canonical(binding_input))
        rec["binding"] = binding
        rec["parameters"]["bindingInput"] = binding_input
        cache = Cache(args.out/"checkpoints", binding)
        schur = module_at(args.schur, "paid_unmodified_field_unit_arithmetic")
        schur.DEADLINE, schur.STOP = DEADLINE, False
        if not cache.has("state-0"):
            core = module_at(args.core, "paid_original_rational_polynomial_core")
            generator = module_at(args.generator, "paid_original_physical_generator")
            construction_ring = types.SimpleNamespace(DF=Ring(MOD), mh=schur.mh)
            Pseries, _ = construct(args, construction_ring, core, generator, rec)
            B0 = [M.transpose() for M in Pseries]
            original = rec["parameters"]["originalConstruction"]
            old_original = parent["parameters"]["originalConstruction"]
            require(original["sourceDictionaryLogicalSha256"] == old_original["sourceDictionaryLogicalSha256"]
                    and original["targetDictionaryLogicalSha256"] == old_original["targetDictionaryLogicalSha256"]
                    and original["wholeOriginalProjectedRowsReduction31Sha256"] == old_original["wholeOriginalProjectedRowsLogicalSha256"],
                    "Same whole original 6188/155 dictionaries and every polynomial row modulo31")
            require([schur.mh(convert(M, Ring(P))) for M in Pseries[:13]] ==
                    old_original["compressedTaylorCoefficientSha256"], "All paid13 original Taylor coefficients match elementwise by full logical SHA")
            Z0 = [Ring(MOD).eye(COLS)]+[Ring(MOD).mat(COLS, COLS) for _ in range(args.degree)]
            meta0 = {"page": 0, "TaylorDegree": args.degree, "coefficientModulus": MOD,
                     "allOriginalSourceProductsVerified": True, "originalConstruction": original}
            cache.put("state-0", {"B": B0, "Z": Z0}, {"B": MOD, "Z": MOD}, meta0)
        zero_state, zero_meta = cache.get("state-0")
        B0 = zero_state["B"]
        rec["parameters"]["originalConstruction"] = zero_meta["originalConstruction"]
        summaries = []
        for page in range(5):
            state, smeta = cache.get("state-"+str(page))
            B, Z = state["B"], state["Z"]
            require(smeta["page"] == page and smeta["TaylorDegree"] == len(B)-1
                    and smeta["coefficientModulus"] == P**(5-page)
                    and smeta["allOriginalSourceProductsVerified"], "Actual verified current page")
            fieldname = "field-"+str(page)
            if not cache.has(fieldname):
                V, summary = complete_source_basis(B, schur)
                if page == 0:
                    require(summary["constantRank"] == old["constantRank"] and
                            summary["positiveParameterExponents"] == old["positiveExponents"],
                            "Complete transposed field spectrum matches paid original result")
                require(baseline <= summary["positiveParameterLength"] <= old["positiveLength"],
                        "Actual projected parameter length bounds")
                cache.put(fieldname, {"V": V}, {"V": P}, summary)
            fstate, summary = cache.get(fieldname)
            summaries.append(summary)
            rec["parameters"]["completedFieldPages"] = summaries
            if summary["positiveParameterLength"] == baseline:
                rec["parameters"]["final"] = completed_result(summaries, H, baseline)
                rec.update(status="completed", exitCode=0)
                break
            require(page < 4, "Paid exponent4 requires complete saturation at page4")
            nextname = "state-"+str(page+1)
            if not cache.has(nextname):
                next_B, next_Z, division = colon_step(B, Z, fstate["V"], page)
                provenance = source_check(B0, next_B, next_Z, page+1)
                nextmeta = {"page": page+1, "TaylorDegree": len(next_B)-1,
                            "coefficientModulus": P**(4-page),
                            "allOriginalSourceProductsVerified": True,
                            "division": division, "originalSourceCheck": provenance}
                cache.put(nextname, {"B": next_B, "Z": next_Z},
                          {"B": P**(4-page), "Z": MOD}, nextmeta)
        require(rec["status"] == "completed", "Actual complete saturation result")
    except Exception as ex:
        budget = isinstance(ex, TimeoutError) or type(ex).__name__ == "BudgetStop"
        rec.update(status="budget-checkpoint" if budget else "failed", exitCode=75 if budget else 1)
        rec["parameters"]["error"] = {"type": type(ex).__name__, "message": str(ex)}
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        rec["elapsedSeconds"] = time.monotonic()-start
        rec["peakRssKiB"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if cache is not None:
            rec["parameters"]["checkpointManifest"] = dict(identity(cache.path), path=str(cache.path), temporaryOnly=True)
            rec["parameters"]["checkpointPhases"] = {name: {**{k: v for k, v in phase.items() if k != "metadata"}, "metadataSha256": sha(canonical(phase["metadata"]))} for name, phase in cache.manifest["phases"].items()}
        raw = args.out/"original-projection31-complete-coefficient-saturation-receipt.json"
        atomic(raw, rec)
        print(json.dumps(rec, sort_keys=True), flush=True)
    return rec["exitCode"]


if __name__ == "__main__":
    sys.exit(main())
