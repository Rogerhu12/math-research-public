#!/usr/bin/env python3
"""Original R150 non-rank-one two-atom gradient and exact linear certificate.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

Reconstruct the literal six-mode K and J3.  Differentiate the exact Schur
polynomial R3 in all 6 original mean and 11 physical Hankel coordinates,
BEFORE restricting the mean and translating H by the fixed atomic H0.
An independent original N/Gamma contraction checks every coefficient.
No rank-one formula, finite-field kernel, or old normal form is imported.

The frozen point is y=e0+e5, H0=(e0^2+e5^2)/2.  If the actual 17x11
linear part has rank 11, construct an explicit affine 11x11 C(M) with
F_selected=C(M)M and det C(0)!=0.  Its adjugate is then an exact original
source certificate after the stated determinant localization.
If the rank is smaller, save the complete exact model and report that
the full-linear certificate was NOT obtained.  No larger elimination
is automatically started.
"""
import argparse
import gzip
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import resource
import signal
import sys
import time

from flint import fmpq, fmpq_mat

FORMAT = "r150-original-nonrankone-two-atom-gradient-v1"
Q0, Q1 = fmpq(0), fmpq(1)
DZ = (Q0,) * 7
KRAW = [
    [0, 0, 0, 0, 5, -1],
    [0, 0, 0, -32, 5, -1],
    [0, 0, 54, -4, 5, 0],
    [0, -32, -4, -8, 0, 0],
    [5, 5, 5, 0, 0, 0],
    [-1, -1, 0, 0, 0, 0],
]
PAID_J2_DET = -64701092257700249600
PAID_J3_DET = 23366320238786911411830138211362846399922176000
Y_FIXED = [1, 0, 0, 0, 0, 1]
H0_FIXED = [fmpq(1, 2)] + [Q0] * 9 + [fmpq(1, 2)]
V0_FIXED = [fmpq(1, 2)] + [Q0] * 14 + [fmpq(1, 2)]
MON2 = [()] + [(i,) for i in range(11)] + list(
    itertools.combinations_with_replacement(range(11), 2))
MONPOS2 = MON2[1:]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def atomic_json(path, value):
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True,
                     indent=2).encode("utf-8")
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_bytes(raw)
    os.replace(tmp, path)
    return {"path": path.name, "bytes": len(raw), "sha256": sha(raw)}


def exact_gzip(path, value):
    raw = canonical(value)
    compressed = gzip.compress(raw, compresslevel=1, mtime=0)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_bytes(compressed)
    os.replace(tmp, path)
    return {"path": path.name, "bytes": len(compressed),
            "sha256": sha(compressed), "logicalBytes": len(raw),
            "logicalSha256": sha(raw)}


def dconst(x):
    return (fmpq(x),) + (Q0,) * 6


def dadd(a, b):
    return tuple(a[i] + b[i] for i in range(7))


def dmul(a, b):
    return (a[0] * b[0],) + tuple(
        a[0] * b[i] + a[i] * b[0] for i in range(1, 7))


class Poly:
    """M polynomial with a six-direction first-order exact rational mean jet."""
    __slots__ = ("data",)

    def __init__(self, data=None):
        self.data = {tuple(k): tuple(v) for k, v in (data or {}).items()
                     if any(v)}
        require(all(tuple(sorted(k)) == k and len(k) <= 3
                    and all(0 <= j < 11 for j in k)
                    and len(v) == 7 for k, v in self.data.items()),
                "valid full M polynomial and six-direction coefficients")

    @staticmethod
    def scalar(x):
        if isinstance(x, Poly):
            return x
        return Poly({(): dconst(x)})

    @staticmethod
    def dual(value, direction):
        v = list(dconst(value))
        v[direction + 1] = Q1
        return Poly({(): tuple(v)})

    @staticmethod
    def variable(j, constant=0):
        return Poly({(): dconst(constant), (j,): dconst(1)})

    def __add__(self, other):
        other = Poly.scalar(other)
        out = dict(self.data)
        for k, v in other.data.items():
            out[k] = dadd(out.get(k, DZ), v)
            if not any(out[k]):
                del out[k]
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: tuple(-x for x in v) for k, v in self.data.items()})

    def __sub__(self, other):
        return self + (-Poly.scalar(other))

    def __rsub__(self, other):
        return Poly.scalar(other) - self

    def __mul__(self, other):
        other = Poly.scalar(other)
        out = {}
        for k, a in self.data.items():
            for l, b in other.data.items():
                key = tuple(sorted(k + l))
                require(len(key) <= 3, "no silent truncation of M degree")
                out[key] = dadd(out.get(key, DZ), dmul(a, b))
        return Poly(out)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        scalar = fmpq(scalar)
        require(bool(scalar), "nonzero rational scalar divisor")
        return self * (Q1 / scalar)

    def __pow__(self, n):
        require(isinstance(n, int) and n >= 0, "nonnegative polynomial power")
        out = Poly.scalar(1)
        for _ in range(n):
            out = out * self
        return out

    def component(self, i=0):
        return Poly({k: dconst(v[i]) for k, v in self.data.items()})

    def diff(self, j):
        out = {}
        for k, v in self.data.items():
            count = k.count(j)
            if count:
                key = list(k)
                key.remove(j)
                out[tuple(key)] = tuple(count * x for x in v)
        return Poly(out)

    def constant(self, component=0):
        return self.data.get((), DZ)[component]

    def base_coeff(self, key):
        return self.data.get(tuple(key), DZ)[0]

    def identical(self, other):
        return self.data == Poly.scalar(other).data

    def ordinary(self):
        require(all(not v[j] for v in self.data.values()
                    for j in range(1, 7)), "ordinary coefficient projection")
        return [[list(k), str(self.data[k][0])]
                for k in sorted(self.data, key=lambda t: (len(t), t))]


def psum(values):
    out = Poly.scalar(0)
    for value in values:
        out = out + value
    return out


def mm(A, B):
    require(A and B and len(A[0]) == len(B), "matrix multiplication shape")
    return [[psum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def mv(A, b):
    return [psum(A[i][k] * b[k] for k in range(len(b)))
            for i in range(len(A))]


def dot(a, b):
    require(len(a) == len(b), "dot shape")
    return psum(x * y for x, y in zip(a, b))


def tr(A):
    require(len(A) == len(A[0]), "trace shape")
    return psum(A[i][i] for i in range(len(A)))


def conv(a, b):
    out = [Poly.scalar(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = out[i+j] + x*y
    return out


def power_kernel(power):
    base = {(i, j): KRAW[i][j] for i in range(6)
            for j in range(6) if KRAW[i][j]}
    out = {(0, 0): 1}
    for _ in range(power):
        nxt = {}
        for (i, j), a in out.items():
            for (k, l), b in base.items():
                key = (i+k, j+l)
                nxt[key] = nxt.get(key, 0) + a*b
        out = {k: v for k, v in nxt.items() if v}
    n = 5*power + 1
    return fmpq_mat([[out.get((i, j), 0) for j in range(n)]
                    for i in range(n)])


def matrix_values(A):
    return [[str(A[i, j]) for j in range(A.ncols())]
            for i in range(A.nrows())]


def matrix_hash(A):
    h = hashlib.sha256()
    h.update(("%d,%d\n" % (A.nrows(), A.ncols())).encode("ascii"))
    for i in range(A.nrows()):
        h.update(("\t".join(str(A[i, j]) for j in range(A.ncols()))
                  + "\n").encode("ascii"))
    return h.hexdigest()


def exact_row_basis(A):
    reduced, rank = A.transpose().rref()
    pivots = []
    for i in range(rank):
        j = next((j for j in range(reduced.ncols()) if reduced[i, j]), None)
        require(j is not None and reduced[i, j] == 1, "true RREF pivot")
        pivots.append(j)
    require(pivots == sorted(set(pivots)), "original row basis order")
    require(rank == A.rank(), "independent exact linear-rank check")
    return int(rank), pivots


def original_model():
    K = fmpq_mat(KRAW)
    require(K.det() == -25600, "literal original K determinant")
    require(all(sum(KRAW[i][j] for i in range(6) for j in range(6)
                    if i+j == k) == 0 for k in range(11)),
            "all original physical curve isotropy coefficients")
    J2, J3 = power_kernel(2), power_kernel(3)
    require(J2.det() == PAID_J2_DET and J3.det() == PAID_J3_DET,
            "original J2 and J3 integer determinants")
    Jinv = J3.inv()
    identity = fmpq_mat([[int(i == j) for j in range(16)] for i in range(16)])
    require(Jinv*J3 == identity and J3*Jinv == identity,
            "all 512 original J3 inverse coordinates")
    # H0 is held fixed in this six-direction differentiation.  In particular
    # this is NOT a derivative along the two-atom mean parametrization.
    y = [Poly.dual(Y_FIXED[i], i) for i in range(6)]
    h = [Poly.variable(i, H0_FIXED[i]) for i in range(11)]
    H = [[h[i+j] for j in range(6)] for i in range(6)]
    p = mv(KRAW, y)
    F = dot(y, p)/2
    KH = mm(KRAW, H)
    KH2 = mm(KH, KH)
    HKH = mm(H, KH)
    tau2, tau3 = tr(KH2), tr(mm(KH2, KH))
    b = dot(p, mv(H, p))
    c = dot(p, mv(HKH, p))
    G6 = F**3 - 6*F*b + 6*F*tau2 + 12*c - 8*tau3
    KHK = mm(KRAW, mm(H, KRAW))
    qpolar = [psum(KHK[i][j] for i in range(6) for j in range(6)
                   if i+j == k) for k in range(11)]
    d = conv(conv(p, p), p)
    e = conv(qpolar, p)
    ell = [d[i]-6*e[i] for i in range(16)]
    ell_inv = [psum(ell[j]*Jinv[i, j] for j in range(16))
               for i in range(16)]
    R = G6-dot(ell, ell_inv)/2
    equations = [R.diff(i).component(0) for i in range(11)] + [
        R.component(i+1) for i in range(6)]
    require(all(all(len(k) <= 2 for k in eq.data) for eq in equations),
            "all seventeen true derivatives are complete quadratics")
    require(R.constant() == 0 and all(not eq.constant() for eq in equations),
            "original two-atom point is a full critical point")

    # Independent original low-gradient contraction.  All now have ordinary
    # coefficients, with no automatic-differentiation directions.
    yc = [Poly.scalar(v) for v in Y_FIXED]
    pc = mv(KRAW, yc)
    Hc = [[entry.component(0) for entry in row] for row in H]
    Fc = F.component(0)
    bc, tauc = b.component(0), tau2.component(0)
    Hpc = mv(Hc, pc)
    HKHc = mm(Hc, mm(KRAW, Hc))
    KHKc = mm(KRAW, mm(Hc, KRAW))
    V = [(-v/4).component(0) for v in ell_inv]
    require(all(V[i].constant() == V0_FIXED[i] for i in range(16)),
            "all sixteen original atomic third-moment coordinates")
    Vp = [[psum(V[i+j+k]*pc[k] for k in range(6))
           for j in range(6)] for i in range(6)]
    N = [[Fc*yc[i]*yc[j]-2*Fc*Hc[i][j]
          -2*(yc[i]*Hpc[j]+Hpc[i]*yc[j])
          +4*Vp[i][j]+4*HKHc[i][j]
          for j in range(6)] for i in range(6)]
    KNK = mm(KRAW, mm(N, KRAW))
    polarN = [psum(KNK[i][j] for i in range(6) for j in range(6)
                   if i+j == k) for k in range(11)]
    termHKHp = mv(HKHc, pc)
    Vpp = [psum(V[i+j+k]*pc[j]*pc[k]
                 for j in range(6) for k in range(6)) for i in range(6)]
    VKHK = [psum(V[i+j+k]*KHKc[j][k]
                  for j in range(6) for k in range(6)) for i in range(6)]
    Gamma = [(Fc**2-2*bc+2*tauc)*yc[i]-4*Fc*Hpc[i]
             +8*termHKHp[i]+4*Vpp[i]-8*VKHK[i] for i in range(6)]
    original_derivatives = [-6*x for x in polarN] + [
        3*x for x in mv(KRAW, Gamma)]
    require(all(a.identical(b) for a, b in zip(equations, original_derivatives)),
            "all original N/Gamma and Schur derivative coefficients")
    for a, b in zip(equations, original_derivatives):
        require(all(a.base_coeff(k) == b.base_coeff(k) for k in MON2),
                "all 1326 complete original gradient coefficient checks")

    triples = list(itertools.combinations_with_replacement(range(6), 3))
    T3 = []
    for i, j, k in triples:
        multiplicity = math.factorial(3)
        for v in set((i, j, k)):
            multiplicity //= math.factorial((i, j, k).count(v))
        value = yc[i]*yc[j]*yc[k] - 2*(
            yc[i]*Hc[j][k]+yc[j]*Hc[i][k]+yc[k]*Hc[i][j]) + 4*V[i+j+k]
        T3.append(multiplicity*value)
    require(all(not z.constant() and all(len(k) <= 1 for k in z.data)
                for z in T3), "complete centered T3 is a true linear map")
    Tmap = fmpq_mat([[z.base_coeff((j,)) for j in range(11)] for z in T3])
    trank = int(Tmap.rank())
    require(trank == 11, "original reduced-two-atom T3 map is injective")
    linear = fmpq_mat([[eq.base_coeff((j,)) for j in range(11)]
                      for eq in equations])
    rank, rows = exact_row_basis(linear)
    record = {
        "literalK": KRAW, "mean": Y_FIXED,
        "H0": [str(x) for x in H0_FIXED],
        "V0": [str(x) for x in V0_FIXED],
        "polynomialMonomials": [list(k) for k in MON2],
        "equations": [eq.ordinary() for eq in equations],
        "sourceEquationOrder": ["dR3/dH%d" % j for j in range(11)]
                               + ["dR3/dy%d" % j for j in range(6)],
        "linearPart": matrix_values(linear), "linearRank": rank,
        "independentOriginalEquationRows": rows,
        "T3Monomials": [list(t) for t in triples],
        "T3LinearMap": matrix_values(Tmap),
        "T3LinearRank": trank,
        "J2Sha256": matrix_hash(J2), "J3Sha256": matrix_hash(J3),
        "J3InverseSha256": matrix_hash(Jinv),
        "completeEquationsSha256": sha(canonical([eq.ordinary() for eq in equations])),
        "linearPartSha256": matrix_hash(linear),
        "T3MapSha256": matrix_hash(Tmap),
    }
    primitive = []
    for eq in equations:
        coeff = [eq.base_coeff(k) for k in MONPOS2]
        den = 1
        for x in coeff:
            den = math.lcm(den, int(x.denom()))
        ints = [int(x.numer())*(den//int(x.denom())) for x in coeff]
        content = 0
        for v in ints:
            content = math.gcd(content, abs(v))
        if not content:
            primitive.append({"originalPerPrimitive": "1",
                              "coefficients": [0]*len(MONPOS2),
                              "isZeroOriginalEquation": True})
            continue
        sign = 1 if next(v for v in ints if v) > 0 else -1
        divisor = sign*content
        reduced = [v//divisor for v in ints]
        ratio = fmpq(divisor, den)
        require(all(ratio*v == x for v, x in zip(reduced, coeff)),
                "entire original primitive row transport")
        primitive.append({"originalPerPrimitive": str(ratio),
                          "coefficients": reduced,
                          "isZeroOriginalEquation": False})
    record["primitiveIntegerEquations"] = primitive
    record["allOriginalRowScales127Units"] = all(
        int(fmpq(row["originalPerPrimitive"]).numer()) % 127
        and int(fmpq(row["originalPerPrimitive"]).denom()) % 127
        for row in primitive)

    certificate = None
    if rank == 11:
        selected = [equations[i] for i in rows]
        C = [[Poly.scalar(0) for _ in range(11)] for _ in range(11)]
        for i, eq in enumerate(selected):
            for key, value in eq.data.items():
                require(len(key) in (1, 2), "true positive centered equation")
                first = key[0]
                tail = key[1:]
                C[i][first] = C[i][first] + Poly({tail: value})
        variables = [Poly.variable(j) for j in range(11)]
        require(all(dot(C[i], variables).identical(selected[i])
                    for i in range(11)),
                "all original affine-matrix times M source identities")
        C0 = fmpq_mat([[C[i][j].constant() for j in range(11)]
                       for i in range(11)])
        det0 = C0.det()
        require(det0 != 0 and C0 == fmpq_mat(
            [[linear[i, j] for j in range(11)] for i in rows]),
            "actual nonzero original linear minor")
        C0inv = C0.inv()
        I11 = fmpq_mat([[int(i == j) for j in range(11)] for i in range(11)])
        require(C0*C0inv == I11 and C0inv*C0 == I11,
                "all original minor inverse identities")
        certificate = {
            "selectedOriginalEquationRows": rows,
            "affineMatrixEntries": [[p.ordinary() for p in row] for row in C],
            "constantDeterminant": str(det0),
            "constantInverse": matrix_values(C0inv),
            "sourceIdentity": "F_selected(M)=C(M) M",
            "conclusion": "det(C(M))*M_j is in the original seventeen-gradient ideal",
            "localization": "invert det(C(M)); do not drop this determinant",
            "all11CompleteAffineSourceIdentitiesVerified": True,
            "all242ConstantMinorInverseCoordinatesVerified": True,
            "notAGlobalUnlocalizedJacobianPowerCertificate": True,
        }
        record["affineSourceCertificate"] = certificate
    flags = {
        "allLiteralKPhysicalCurveIdentitiesVerified": True,
        "all512J3InverseCoordinatesVerified": True,
        "all17OriginalGradientEquationsRetained": True,
        "all1326OriginalGradientCoefficientCoordinatesVerified": True,
        "all1309PrimitiveRowCoefficientCoordinatesVerified": True,
        "all17OriginalCriticalConstantTermsVerified": True,
        "all16OriginalAtomicThirdMomentsVerified": True,
        "all56CompleteCenteredThirdTensorCoordinatesVerified": True,
        "meanDifferentiatedBeforeSpecialization": True,
        "atomicH0HeldFixedInAllSixMeanDerivatives": True,
        "T3LinearMapShape": [56, 11], "T3LinearRank": trank,
        "originalLinearShape": [17, 11], "originalLinearRank": rank,
        "independentOriginalEquationRows": rows,
        "fullLinearCertificateObtained": certificate is not None,
        "allOriginalRowScales127Units": bool(record["allOriginalRowScales127Units"]),
        "largeMacaulayMatrixConstructed": False,
        "finiteFieldRankUsed": False,
        "rankOneModelImported": False,
    }
    if certificate:
        flags.update({
            "actualLinearMinorDeterminant": certificate["constantDeterminant"],
            "all11CompleteAffineSourceIdentitiesVerified": True,
            "all242ConstantMinorInverseCoordinatesVerified": True,
        })
    return record, flags


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    parser.add_argument("--seconds", type=float, default=30)
    parser.add_argument("--memory-mib", type=int, default=512)
    args = parser.parse_args()
    require(0 < args.seconds <= 180 and 256 <= args.memory_mib <= 2048,
            "bounded exact small-model budget")
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    resource.setrlimit(resource.RLIMIT_AS,
                       (args.memory_mib*1024**2, args.memory_mib*1024**2))
    started = time.monotonic()
    source_sha = sha(Path(__file__).read_bytes())
    binding = sha(canonical({
        "format": FORMAT, "sourceSha256": source_sha,
        "literalK": KRAW, "mean": Y_FIXED,
        "atomicH0": [str(x) for x in H0_FIXED],
        "sixOriginalMeanDirections": 6,
        "elevenOriginalHankelDirections": 11,
    }))
    rec = {
        "format": FORMAT, "status": "started", "binding": binding,
        "sourceSha256": source_sha,
        "parameters": {
            "arithmetic": "exact rational python-flint",
            "originalMean": Y_FIXED,
            "atomicPhysicalParameters": {
                "firstPoint": "0", "secondPoint": "infinity",
                "firstAmplitude": "1", "secondAmplitude": "1"},
            "seconds": args.seconds, "memoryMiB": args.memory_mib,
            "historicalLargeInputsNeeded": False,
            "noConclusionAssumesLinearRankEleven": True,
        },
    }

    def timeout(signum, frame):
        raise TimeoutError("bounded exact non-rank-one model budget")

    signal.signal(signal.SIGALRM, timeout)
    signal.setitimer(signal.ITIMER_REAL, args.seconds)
    code = 1
    try:
        model, flags = original_model()
        descriptor = exact_gzip(out/"complete-original-seventeen-quadratics.json.gz",
                                {"format": FORMAT+"-model",
                                 "binding": binding, "data": model})
        rec["parameters"].update(flags)
        rec["parameters"]["completeOriginalModel"] = descriptor
        rec["parameters"]["modelIdentitySha256"] = model["completeEquationsSha256"]
        rec["parameters"]["originalLinearSha256"] = model["linearPartSha256"]
        rec["parameters"]["T3LinearSha256"] = model["T3MapSha256"]
        rec["status"] = "completed"
        rec["parameters"]["outcome"] = (
            "original-determinant-localized-linear-source-certificate"
            if flags["fullLinearCertificateObtained"]
            else "complete-original-model-only-linear-rank-not-eleven")
        code = 0
    except BaseException as exc:
        rec["status"] = "budget-checkpoint" if isinstance(exc, TimeoutError) else "failed"
        rec["parameters"]["error"] = {"type": type(exc).__name__, "message": str(exc)}
        code = 75 if isinstance(exc, TimeoutError) else 1
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        rec["elapsedSeconds"] = time.monotonic()-started
        rec["parameters"]["elapsedSeconds"] = rec["elapsedSeconds"]
        desc = atomic_json(out/"original-nonrankone-two-atom-gradient-receipt.json", rec)
        print(json.dumps({"status": rec["status"], "exitCode": code,
                          "binding": binding, "receipt": desc,
                          "elapsedSeconds": rec["elapsedSeconds"],
                          "parameters": rec["parameters"]},
                         ensure_ascii=False, sort_keys=True), flush=True)
    return code


if __name__ == "__main__":
    sys.exit(main())
