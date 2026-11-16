#!/usr/bin/env python3
"""Exact E low-commutator coordinates in the original twenty cubic sources.

Author: Astra-ISP-789f / normal_annihilator, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

This reconstructs the ORIGINAL fixed coefficient matrices, without expanding
new twelve-parameter polynomials.  The paid cubic border sources have support
in original columns 0..34, so their projection to columns 35..54 is zero.
Only the projected 20 by 50 exact E system is newly materialized and checked.
Full 55-coordinate and parameter-source identities follow by the separately
proved kernel/canonical-source lemma, not by claiming unperformed products.
No Bell unit, high-commutator deletion, or finite-field coefficient lift is used.
"""
from __future__ import annotations
import argparse, gc, gzip, hashlib, importlib.util, itertools, json, os
import resource, signal, sys, time, zlib
from pathlib import Path
from flint import fmpq, fmpq_poly, fmpq_mat, nmod_mat

sys.set_int_max_str_digits(0)
FORMAT = "r150-original-low-commutator-twenty-exact-constants-v1"
PRIME, ROOT = 127, 100
MATCHED = [52565262336, 6080833024, -43931504, 3725]
MODEL_SHA = "da80b727c47a050f3e268f00d1d6598336866a41b354d6aecb5edbb1ca1e730d"
HELPER_SHA = "31df769fb0fd3a41eb7606f500aae8b46952219c24927bd3265ed3dc34d7fe10"
PAID_MODEL_SHA = "4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4"
PAID_MODEL_BINDING = "7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4"
PAID_MANIFEST = {"bytes": 30466, "sha256": "9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2"}
PAID_BASE = {"bytes": 776254, "sha256": "5cbba4f798ab95fe24538f35d23d4b3a2f0d6197ee3ed33f3149b7371b0d222c",
             "logicalBytes": 4442756, "logicalSha256": "f07c273c934e671f5e1069954771286c14e5d10ab7c4652d998a02f71beb7d05"}
HP, HU = [2, 1, 0, 3, 4, 5], [6, 7, 8, 9, 10]
KEEP = [(1, 4), (2, 3), (2, 4), (3, 4)]
LOW_IDS = [10*j+k for j in range(4) for k in range(1, 6)]

class Budget(Exception): pass

def need(ok, message):
    if not ok: raise ValueError(message)

def canon(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")

def sha(b): return hashlib.sha256(b).hexdigest()

def identity(p):
    h = hashlib.sha256()
    with Path(p).open("rb") as f:
        for part in iter(lambda: f.read(1048576), b""): h.update(part)
    return {"path": Path(p).name, "bytes": Path(p).stat().st_size, "sha256": h.hexdigest()}

def exact(p, descriptor):
    d = identity(p)
    need(all(d[k] == descriptor[k] for k in ("bytes", "sha256")), "exact complete file " + Path(p).name)
    return d

def atomic(p, raw):
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_bytes(raw); os.replace(tmp, p)

def import_source(p, expected, name):
    need(identity(p)["sha256"] == expected, "exact original source " + name)
    sp = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    return m

def mons(n, degree):
    result = []
    for ii in itertools.combinations_with_replacement(range(n), degree):
        e = [0]*n
        for i in ii: e[i] += 1
        result.append(tuple(e))
    return result

M2, M3 = mons(5, 2), mons(5, 3)
M2_INDEX, M3_INDEX = {e:i for i,e in enumerate(M2)}, {e:i for i,e in enumerate(M3)}
KEEP_EXP = [tuple(int(k == i)+int(k == j) for k in range(5)) for i,j in KEEP]
KEEP_POS = [M2_INDEX[e] for e in KEEP_EXP]
ELIM = [i for i in range(15) if i not in KEEP_POS]
PAIRS = list(itertools.combinations(range(5), 2))
LABELS = [(i,j,k) for i,j in PAIRS for k in range(5)]
SELECTED = [a for a,(i,j,k) in enumerate(LABELS) if i == 0]

class EField:
    """Exact E values plus the same legal local-place arithmetic expression.

    A residue is NOT inferred from arbitrary canonical E-coordinate denominators.
    It is propagated from integral rational inputs and actual residue-unit
    inversions.  For a matrix solve it is fixed by the same residue-unit system,
    and the complete exact E product is independently verified afterwards.
    """
    def __init__(self):
        self.f = fmpq_poly([fmpq(x, MATCHED[-1]) for x in MATCHED])
        self.zero = (fmpq_poly(), 0)
        self.one = (fmpq_poly([1]), 1)
        self.d = (fmpq_poly([0,1]), ROOT)
        self.inversions = 0
    def rational(self, q):
        q = fmpq(q); den = int(q.denom()) % PRIME
        need(den != 0, "original rational input is integral at the specified place")
        return fmpq_poly([q]), int(q.numer()) % PRIME * pow(den, -1, PRIME) % PRIME
    def add(self, a, b): return a[0]+b[0], (a[1]+b[1]) % PRIME
    def neg(self, a): return -a[0], (-a[1]) % PRIME
    def sub(self, a, b): return a[0]-b[0], (a[1]-b[1]) % PRIME
    def mul(self, a, b): return (a[0]*b[0]) % self.f, a[1]*b[1] % PRIME
    def inverse(self, a):
        need(a[0] != 0 and a[1] != 0, "same exact E inverse with a residue-unit pivot")
        g,x,y = a[0].xgcd(self.f)
        need(g == fmpq_poly([1]), "genuine inverse in the original irreducible cubic field")
        v = (x % self.f, pow(a[1], -1, PRIME))
        need(self.mul(a, v) == self.one, "original E and place inverse product")
        self.inversions += 1
        return v
    def total(self, xs):
        s = self.zero
        for x in xs: s = self.add(s, x)
        return s
    def dot(self, a, b):
        need(len(a) == len(b), "complete exact E scalar product dimensions")
        return self.total(self.mul(x,y) for x,y in zip(a,b))
    def matrix(self, A, B):
        need(A and B and len(A[0]) == len(B), "complete exact E matrix dimensions")
        return [[self.total(self.mul(A[i][k], B[k][j]) for k in range(len(B)))
                 for j in range(len(B[0]))] for i in range(len(A))]
    def invert(self, A, label):
        n = len(A); need(n and all(len(row) == n for row in A), label+" square")
        R = [list(row)+[self.one if i == j else self.zero for j in range(n)] for i,row in enumerate(A)]
        pivots = []
        for j in range(n):
            k = next((k for k in range(j,n) if R[k][j][1]), None)
            need(k is not None, label+" exact legal residue-unit profile")
            R[j],R[k] = R[k],R[j]; pivots.append(k)
            inv = self.inverse(R[j][j]); R[j] = [self.mul(v,inv) for v in R[j]]
            for i in range(n):
                if i == j or not R[i][j][0]:
                    if not R[i][j][0]: need(R[i][j][1] == 0, "consistent exact zero at the legal place")
                    continue
                t = R[i][j]
                R[i] = [self.sub(a,self.mul(t,b)) for a,b in zip(R[i],R[j])]
        V = [row[n:] for row in R]
        for B,C in ((A,V),(V,A)):
            for i in range(n):
                for j in range(n):
                    need(self.total(self.mul(B[i][k],C[k][j]) for k in range(n)) ==
                         (self.one if i == j else self.zero), label+" both complete E inverse products")
        return V, pivots

def pack_e(v): return [str(v[0][i]) for i in range(3)] + [int(v[1])]
def unpack_e(v):
    need(isinstance(v,list) and len(v) == 4 and all(isinstance(x,str) for x in v[:3]) and
         type(v[3]) is int and 0 <= v[3] < PRIME, "canonical full exact E coordinate")
    return fmpq_poly([fmpq(x) for x in v[:3]]), v[3]
def pack_m(A): return [[pack_e(v) for v in row] for row in A]
def unpack_m(A): return [[unpack_e(v) for v in row] for row in A]
def bar_m(A): return [[v[1] for v in row] for row in A]

def rational_regular_matrix(F, A):
    n,m = len(A),len(A[0]); R = fmpq_mat(3*n,3*m)
    powers = [fmpq_poly([1]),fmpq_poly([0,1]),fmpq_poly([0,0,1])]
    for i in range(n):
        for j in range(m):
            for k,d in enumerate(powers):
                v = (A[i][j][0]*d) % F.f
                for a in range(3): R[3*i+a,3*j+k] = v[a]
    return R

def rational_columns(B):
    R = fmpq_mat(3*len(B),len(B[0]))
    for i,row in enumerate(B):
        for j,v in enumerate(row):
            for k in range(3): R[3*i+k,j] = v[0][k]
    return R

def read_paid_base(root):
    mp = root / "original-parameter-module-manifest.json"; exact(mp, PAID_MANIFEST)
    manifest = json.loads(mp.read_bytes())
    need(manifest["binding"] == PAID_MODEL_BINDING and len(manifest["seeds"]) == 116,
         "same full paid original parameter model")
    descriptor = manifest["phases"]["complete-original-ten-parameter-action127"]
    need(all(descriptor[k] == PAID_BASE[k] for k in PAID_BASE), "same original base mathematical descriptor")
    p = root / descriptor["path"]; exact(p,descriptor)
    raw = gzip.decompress(p.read_bytes())
    need(len(raw) == descriptor["logicalBytes"] and sha(raw) == descriptor["logicalSha256"], "whole paid base logical identity")
    obj = json.loads(raw)
    need(obj["binding"] == PAID_MODEL_BINDING and obj["format"] ==
         "r150-original-ten-generator-complete-parameter-seeds127-v2-phase", "same full model phase")
    b = obj["data"]
    need(b["prime"] == PRIME and b["coefficientRoot"] == ROOT and b["matchedCubic"] == MATCHED,
         "same original exact coefficient place")
    top = []
    for row in b["allElevenMomentGenerators"]:
        d = {}
        for ee,c in row:
            need(len(ee) == 17 and type(c) is int and 0 < c < PRIME, "all literal paid coefficient records")
            if sum(ee[12:]) == 2:
                need(not any(ee[:12]), "original quadratic top has fixed coefficients")
                e = tuple(ee[12:]); need(e in M2_INDEX and e not in d, "complete ordinary quadratic dictionary")
                d[e] = c
        top.append([d.get(e,0) for e in M2])
    needed = {k:b[k] for k in ("quadraticUnit","quadraticUnitInverse","quadraticUnitDeterminant127",
              "all55OriginalCubicLabels","all35OriginalCubicMonomials","selectedOriginalCubicColumns",
              "cubicUnit","cubicUnitInverse","cubicUnitDeterminant127")}
    needed["top"] = top
    return needed,{"manifest":identity(mp),"base":descriptor}

def build_constants(F, original, paid, tick):
    need(original["matchedCubic"] == MATCHED and original["all17OriginalGradientPolynomialsVerified"] and
         original["all512OriginalJ3InverseProductsVerified"] and original["allWeightedEulerCoefficientsVerified"],
         "all original physical source, J3 and Euler identities")
    need(original["matchedCubicIrreducibility"]["allRootValuesNonzero"], "paid original cubic irreducibility")
    L = [[F.zero for j in range(11)] for i in range(6)]
    dpowers = [F.one,F.d,F.mul(F.d,F.d)]
    for a,row in enumerate(original["BellFieldComponents"]):
        for ee,c in row:
            if not any(ee[6:]):
                need(sum(ee[:6]) == 3, "original pure mean Bell cubic")
                continue
            need(sum(ee[:6]) == 1 and sum(ee[6:]) == 1, "every original Bell Hankel coefficient is mean-linear")
            i = next(i for i,x in enumerate(ee[:6]) if x); j = next(j for j,x in enumerate(ee[6:]) if x)
            L[i][j] = F.add(L[i][j],F.mul(F.rational(c),dpowers[a]))
    LP = [[L[i][j] for j in HP] for i in range(6)]
    LI, bell_profile = F.invert(LP, "same original six Bell columns")
    Hw = [[F.zero]*6 for j in range(11)]; Hu = [[F.zero]*5 for j in range(11)]
    for k,j in enumerate(HP):
        Hw[j] = list(LI[k])
        Hu[j] = [F.neg(F.total(F.mul(LI[k][a],L[a][h]) for a in range(6))) for h in HU]
    for k,j in enumerate(HU): Hu[j][k] = F.one
    forward = [list(row) for row in L] + [[F.one if j == h else F.zero for j in range(11)] for h in HU]
    backward = [Hw[j]+Hu[j] for j in range(11)]
    for A,B in ((forward,backward),(backward,forward)):
        product = F.matrix(A,B)
        need(all(product[i][j] == (F.one if i == j else F.zero) for i in range(11) for j in range(11)),
             "all242 original linear Hankel coordinate inverse products")
    # At y=w=0 the weight-four Hankel derivatives are exactly quadratic in H.
    # Ordinary monomials, including their repeated-factor diagonal, are retained.
    pair_image = {}
    for i in range(11):
        for j in range(i,11):
            image = [F.zero]*15
            for a in range(5):
                for b in range(5):
                    e = tuple(int(k == a)+int(k == b) for k in range(5))
                    p = M2_INDEX[e]; image[p] = F.add(image[p],F.mul(Hu[i][a],Hu[j][b]))
            pair_image[i,j] = image
    raw_q = []
    for row in original["originalSeventeenGradients"][:11]:
        q = [F.zero]*15
        for ee,c in row:
            if any(ee[:6]): continue
            need(sum(ee[6:]) == 2, "all original mean-zero Hankel gradient terms are quadratic")
            ij = [i for i,k in enumerate(ee[6:]) for _ in range(k)]
            need(len(ij) == 2, "ordinary original quadratic source monomial")
            cc = F.rational(c)
            q = [F.add(x,F.mul(cc,y)) for x,y in zip(q,pair_image[tuple(ij)])]
        raw_q.append(q)
    Fq = [[F.total(F.mul(Hu[h][i],raw_q[h][j]) for h in range(11)) for j in range(15)] for i in range(5)]
    Wq = [[F.total(F.mul(Hw[h][i],raw_q[h][j]) for h in range(11)) for j in range(15)] for i in range(6)]
    squares = [M2_INDEX[tuple(2*int(i == j) for i in range(5))] for j in range(5)]
    Q = [[row[j] for j in squares] for row in Fq]; QI, square_profile = F.invert(Q,"same original five-square block")
    Gq = [list(row) for row in Fq]
    Wreduction = []
    for row in Wq:
        alpha = [row[j] for j in squares]
        lam = [F.total(F.mul(alpha[k],QI[k][g]) for k in range(5)) for g in range(5)]
        out = [F.sub(row[j],F.total(F.mul(lam[g],Fq[g][j]) for g in range(5))) for j in range(15)]
        need(all(out[j] == F.zero for j in squares), "all six original w-gradient square corrections")
        Gq.append(out); Wreduction.append(lam)
    need(bar_m(Gq) == paid["top"], "all165 original E quadratic coefficients specialize to the paid model")
    U = [[Gq[g][j] for g in range(11)] for j in ELIM]
    UI, quadratic_profile = F.invert(U,"same original eleven quadratic sources")
    need(bar_m(U) == paid["quadraticUnit"] and bar_m(UI) == paid["quadraticUnitInverse"],
         "full original quadratic unit and both source inverses at127")
    alpha = []; rho = []; qalpha = []
    for e in M2:
        rhs = [F.one if M2[j] == e else F.zero for j in ELIM]
        a = [F.dot(row,rhs) for row in UI]
        qa = [F.total(F.mul(Gq[g][j],a[g]) for g in range(11)) for j in range(15)]
        r = [F.sub(F.one if e == v else F.zero,qa[j]) for v,j in zip(KEEP_EXP,KEEP_POS)]
        need(all(qa[j] == F.sub(F.one if e == M2[j] else F.zero,
             r[KEEP_POS.index(j)] if j in KEEP_POS else F.zero) for j in range(15)),
             "all225 original complete quadratic normal-source coefficients")
        alpha.append(a); rho.append(r); qalpha.append(qa)
    labels = [(g,k) for g in range(11) for k in range(5)]
    C = []
    for e in M3:
        row = []
        for g,k in labels:
            if e[k]:
                t = list(e); t[k] -= 1; row.append(Gq[g][M2_INDEX[tuple(t)]])
            else: row.append(F.zero)
        C.append(row)
    need([list(x) for x in labels] == paid["all55OriginalCubicLabels"] and
         [list(x) for x in M3] == paid["all35OriginalCubicMonomials"] and
         paid["selectedOriginalCubicColumns"] == list(range(35)), "same complete original cubic row and source dictionaries")
    Cbar = nmod_mat(bar_m(C),PRIME); rr,rank = Cbar.rref()
    pivots = [next(j for j in range(55) if rr[i,j]) for i in range(rank)]
    need(rank == 35 and pivots == list(range(35)), "same actual complete original cubic residue-unit profile")
    Cunit = [[C[i][j] for j in range(35)] for i in range(35)]
    Cb = nmod_mat(bar_m(Cunit),PRIME); det = int(Cb.det()); CIb = Cb.inv()
    need(det == 32 and det == paid["cubicUnitDeterminant127"] and bar_m(Cunit) == paid["cubicUnit"],
         "same original cubic unit, all coefficients and determinant127")
    need([[int(CIb[i,j]) for j in range(35)] for i in range(35)] == paid["cubicUnitInverse"],
         "same original full cubic inverse at the legal place")
    need(Cb*CIb == nmod_mat([[int(i == j) for j in range(35)] for i in range(35)],PRIME) and
         CIb*Cb == nmod_mat([[int(i == j) for j in range(35)] for i in range(35)],PRIME),
         "all2450 original cubic residue inverse coordinates")
    tick()
    # R kills every paid X_{i,v}: each is the same unit inverse embedded in
    # original source columns 0..34.  No X coefficient is lifted from F127.
    projected = [[F.zero for _ in LABELS] for gk in range(20)]
    for column,(i,j,k) in enumerate(LABELS):
        ik = M2_INDEX[tuple(int(a == i)+int(a == k) for a in range(5))]
        jk = M2_INDEX[tuple(int(a == j)+int(a == k) for a in range(5))]
        z0 = [F.zero]*55
        for g in range(11):
            z0[5*g+j] = F.add(z0[5*g+j],alpha[ik][g])
            z0[5*g+i] = F.sub(z0[5*g+i],alpha[jk][g])
        for r in range(20): projected[r][column] = z0[35+r]
        # Check CZ=0 with the paid exact identities C X_{a,v}=u_a*v.
        # This is the literal symbolic substitution; new X arrays are absent.
        cz = [F.zero]*35
        for v,c in zip(M2,qalpha[ik]):
            e=list(v);e[j]+=1; r=M3_INDEX[tuple(e)];cz[r]=F.add(cz[r],c)
        for v,c in zip(M2,qalpha[jk]):
            e=list(v);e[i]+=1; r=M3_INDEX[tuple(e)];cz[r]=F.sub(cz[r],c)
        for a,v in enumerate(KEEP_EXP):
            e=list(v);e[j]+=1;r=M3_INDEX[tuple(e)];cz[r]=F.add(cz[r],rho[ik][a])
            e=list(v);e[i]+=1;r=M3_INDEX[tuple(e)];cz[r]=F.sub(cz[r],rho[jk][a])
        need(all(x == F.zero for x in cz), "all1750 exact symbolic cubic-kernel coordinates with paid border images")
    original_ids = [10*PAIRS.index((i,j))+1+k for i,j,k in LABELS]
    need([original_ids[j] for j in SELECTED] == LOW_IDS and len(SELECTED) == 20,
         "same twenty original low-commutator labels")
    Zstar = [[row[j] for j in SELECTED] for row in projected]
    Zb = nmod_mat(bar_m(Zstar),PRIME); zdet = int(Zb.det())
    need(zdet != 0, "actual original twenty-by-twenty projected source unit")
    return {"matchedCubic":MATCHED,"hankelPivotOrder":HP,"hankelFreeOrder":HU,
        "allFiftyLowLabels":[list(x) for x in LABELS],"allFiftyOriginalSeedIndices":original_ids,
        "selectedTwentyLowColumns":SELECTED,"selectedTwentyOriginalSeedIndices":LOW_IDS,
        "originalQuadraticMonomials":[list(x) for x in M2],"originalCubicMonomials":[list(x) for x in M3],
        "originalCubicSources":[list(x) for x in labels],"cubicUnitColumns":list(range(35)),"kernelProjectionColumns":list(range(35,55)),
        "originalBellLinearCoefficients":pack_m(L),"originalHankelWMap":pack_m(Hw),"originalHankelUMap":pack_m(Hu),
        "originalFiveSquareInverse":pack_m(QI),"originalSixWSourceCorrections":pack_m(Wreduction),
        "allElevenOriginalQuadraticTops":pack_m(Gq),"originalQuadraticUnit":pack_m(U),"originalQuadraticUnitInverse":pack_m(UI),
        "allFifteenQuadraticSourceColumns":pack_m(alpha),"allFifteenRetainedQuadraticColumns":pack_m(rho),
        "allOriginalCubicCoefficients":pack_m(C),"projectedFiftyOriginalLowSources":pack_m(projected),
        "selectedTwentyProjectedSourceUnit":pack_m(Zstar),"twentyUnitDeterminant127":zdet,
        "cubicUnitDeterminant127":det,"inverseProfiles":{"Bell":bell_profile,"squares":square_profile,"quadratic":quadratic_profile},
        "originalPhysicalLogicalSHA256":sha(canon(original)),"allOriginalModelGatesVerified":True,
        "all242LinearCoordinateInverseProductsVerified":True,"all225QuadraticSourceCoefficientsVerified":True,
        "all165QuadraticSpecializationsVerified":True,"all1925CubicSourceCoefficientsRetained":True,
        "all2450CubicResidueInverseCoordinatesVerified":True,"all1750SymbolicCubicKernelCoordinatesVerified":True,
        "sameOriginalSixteenCubicSourceSupportUsed":True,"newSixteenCubicSourceArraysMaterialized":False,
        "noTwelveParameterExpansion":True,"sourceMap":"Phi(z), sigma(z) from the exact canonical-source lemma"}

def main():
    ap=argparse.ArgumentParser()
    for name in ("model-source","helper","paid-model-source","paid-model-out","out"):
        ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--through",choices=("constants","final"),default="final")
    ap.add_argument("--seconds",type=float,default=300)
    ap.add_argument("--memory-mib",type=int,default=2048)
    a=ap.parse_args()
    need(0 < a.seconds <= 900 and 512 <= a.memory_mib <= 4096,"bounded exact constant-source consumer")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    started=time.monotonic();deadline=started+a.seconds;a.out.mkdir(parents=True,exist_ok=True)
    own=identity(Path(__file__))
    semantic={"format":FORMAT,"source":own,"matchedCubic":MATCHED,"prime":PRIME,"coefficientRoot":ROOT,
      "modelSourceSHA256":MODEL_SHA,"helperSHA256":HELPER_SHA,"paidModelSourceSHA256":PAID_MODEL_SHA,
      "paidModelBinding":PAID_MODEL_BINDING,"paidModelManifest":PAID_MANIFEST,"paidModelBase":PAID_BASE,
      "hankelPivots":HP,"hankelFree":HU,"keptQuadraticPaths":[list(x) for x in KEEP],
      "cubicUnitColumns":list(range(35)),"kernelProjectionColumns":list(range(35,55)),
      "twentyOriginalLowSeedIndices":LOW_IDS,"newArithmetic":"exact E projected20x50 system; no field coefficient lift"}
    binding=sha(canon(semantic));mp=a.out/"exact-low20-manifest.json"
    state={"format":FORMAT+"-manifest","binding":binding,"semantic":semantic,"phases":{}}
    if mp.exists():
        state=json.loads(mp.read_bytes())
        need(state["format"] == FORMAT+"-manifest" and state["binding"] == binding and state["semantic"] == semantic,
             "same exact complete-phase continuation")
    rec={"format":FORMAT,"binding":binding,"source":own,"status":"running",
         "parameters":{"through":a.through,"seconds":a.seconds,"memoryMiB":a.memory_mib,
           "fullParameterIdentitiesFromCanonicalSourceTheorem":True,"newHighCommutatorClaim":False,
           "unitIdealClaim":False,"newFull55CoordinateProductsClaimed":False}}
    code=1
    def tick():
        if time.monotonic()+8 >= deadline: raise Budget("whole exact E constant-source phase budget")
    def alarm(sig=None,frame=None): raise Budget("actual exact E constant-source budget")
    def flush(): atomic(mp,canon(state))
    def phase(name,data):
        raw=canon({"format":FORMAT+"-phase","binding":binding,"data":data})
        p=a.out/(name+".json.gz");atomic(p,gzip.compress(raw,compresslevel=1,mtime=0))
        d={**identity(p),"logicalBytes":len(raw),"logicalSha256":sha(raw)}
        state["phases"][name]=d;flush();return d
    def read(name):
        d=state["phases"][name];p=a.out/d["path"];exact(p,d);raw=gzip.decompress(p.read_bytes())
        need(len(raw)==d["logicalBytes"] and sha(raw)==d["logicalSha256"],"whole exact E phase logical identity")
        o=json.loads(raw);need(o["format"]==FORMAT+"-phase" and o["binding"]==binding,"same source phase")
        return o["data"]
    def event(name,**kw):
        rec["parameters"]["lastWholePhase"]=name
        print(json.dumps({"phase":name,"elapsedSeconds":time.monotonic()-started,
              "peakRssKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**kw},separators=(",",":")),flush=True)
    signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds)
    try:
        import flint
        need(tuple(sys.version_info[:3])==(3,12,14) and flint.__version__=="0.9.0","fixed exact arithmetic and gzip runtime")
        rec["parameters"]["runtime"]={"python":sys.version.split()[0],"pythonFlint":flint.__version__,"zlib":zlib.ZLIB_VERSION}
        fd=import_source(a.model_source,MODEL_SHA,"exact_low20_original_physical")
        helper=import_source(a.helper,HELPER_SHA,"exact_low20_original_field")
        need(identity(a.paid_model_source)["sha256"]==PAID_MODEL_SHA,"same paid complete field model source")
        paid,parent=read_paid_base(a.paid_model_out);rec["parameters"]["actualParents"]=parent
        F=EField()
        if "original-exact-constants" not in state["phases"]:
            tick();original=fd.prepare(helper);event("original-physical-model-rebuilt")
            constants=build_constants(F,original,paid,tick)
            phase("original-exact-constants",constants);event("original-exact-constants",twentyUnitDeterminant127=constants["twentyUnitDeterminant127"])
            del original;gc.collect()
        else:
            constants=read("original-exact-constants")
            need(constants["allOriginalModelGatesVerified"] and constants["all1750SymbolicCubicKernelCoordinatesVerified"] and
                 constants["selectedTwentyOriginalSeedIndices"]==LOW_IDS,"complete verified original constant phase")
            event("original-exact-constants-reused")
        if a.through=="constants":
            rec["status"]="completed-prefix";rec["parameters"]["outcome"]="all original constants and exact projected50 sources";code=0
            return code
        tick()
        Z=unpack_m(constants["projectedFiftyOriginalLowSources"])
        A=unpack_m(constants["selectedTwentyProjectedSourceUnit"])
        need(len(A)==20 and all(len(r)==20 for r in A) and len(Z)==20 and all(len(r)==50 for r in Z),"complete projected dimensions")
        if "complete-exact-low20-coordinates" in state["phases"]:
            complete=read("complete-exact-low20-coordinates")
            need(complete["all3000FaithfulRationalProductCoordinatesVerified"] and complete["all1000OriginalEProjectedProductsVerified"] and
                 complete["allTwentySelectedColumnsIdentityVerified"] and complete["allFiftyOriginalLowSourcesAccountedFor"],"complete exact coordinate certificate")
            event("complete-exact-low20-coordinates-reused")
        else:
            QA=rational_regular_matrix(F,A);QB=rational_columns(Z)
            Ab=nmod_mat(bar_m(A),PRIME);Bb=nmod_mat(bar_m(Z),PRIME)
            need(int(Ab.det())==constants["twentyUnitDeterminant127"]!=0,"same exact projected residue-unit minor")
            LB=Ab.inv()*Bb
            if "candidate-exact-low20-coordinates" not in state["phases"]:
                tick();event("exact-rational60-solve-start",rightHandSides=50)
                X=QA.solve(QB,algorithm="dixon")
                L=[[(fmpq_poly([X[3*i+k,j] for k in range(3)]),int(LB[i,j])) for j in range(50)] for i in range(20)]
                candidate={"coordinates":pack_m(L),"candidateOnly":True,"exactProductsVerified":False,
                  "method":"faithful original E regular representation, exact rational Dixon solve", "rationalRows":60,"rightHandSides":50}
                phase("candidate-exact-low20-coordinates",candidate);event("candidate-exact-low20-coordinates")
            else:
                candidate=read("candidate-exact-low20-coordinates")
                need(candidate["candidateOnly"] and not candidate["exactProductsVerified"],"honest unverified full candidate scope")
                L=unpack_m(candidate["coordinates"]);X=rational_columns(L)
                need(len(L)==20 and all(len(r)==50 for r in L) and bar_m(L)==[[int(LB[i,j]) for j in range(50)] for i in range(20)],"same candidate coordinate dictionary and place solution")
                event("candidate-exact-low20-coordinates-reused")
            tick()
            product=QA*X
            need(product==QB,"all3000 exact faithful coordinates of the full1000 original E projected products")
            need(Ab*LB==Bb,"all1000 same local-place projected products")
            for a,j in enumerate(SELECTED):
                for i in range(20): need(L[i][j]==(F.one if i==a else F.zero),"all400 exact selected-column identity coordinates")
            complete={"coordinates":pack_m(L),"allFiftyLowLabels":[list(x) for x in LABELS],
              "selectedTwentyLowColumns":SELECTED,"selectedTwentyOriginalSeedIndices":LOW_IDS,
              "twentyUnitDeterminant127":constants["twentyUnitDeterminant127"],
              "all3000FaithfulRationalProductCoordinatesVerified":True,"all1000OriginalEProjectedProductsVerified":True,
              "all1000LocalPlaceProjectedProductsVerified":True,"allTwentySelectedColumnsIdentityVerified":True,
              "allFiftyOriginalLowSourcesAccountedFor":True,"fieldCoefficientsLifted":False,
              "full55IdentityMethod":"both sides are in ker(C); original R is injective there; their exact R coordinates agree",
              "fullParameterAndOriginalSourceIdentityMethod":"the unique correction a(z)=-U^-1 elim(sum z_g ell_g) is E-linear",
              "actualNewFull55CoordinateProducts":0,"newTwelveParameterPolynomialProducts":0,
              "sameOriginalCubicBorderSourcesUsedSymbolically":True,"noMeanOrBellSourcesUsed":True,
              "ordinaryBModuleLowGenerators":20,"originalFullSeedBound":76,"completeTwoRoundColumnBound":670,
              "highCommutatorDeletionClaim":False,"unitIdealClaim":False}
            phase("complete-exact-low20-coordinates",complete);event("complete-exact-low20-coordinates",exactEProducts=1000)
        rec["status"]="completed";rec["parameters"]["outcome"]="exact E20 low-commutator coefficients with complete original source theorem"
        rec["parameters"]["all1000OriginalEProjectedProductsVerified"]=True
        rec["parameters"]["allFiftyOriginalLowSourcesAccountedFor"]=True
        rec["parameters"]["sameOriginalOrdinaryBModule76Seeds"]=True
        code=0;return code
    except Budget as e:
        rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=75;return code
    except BaseException as e:
        rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1;return code
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        rec["parameters"]["elapsedSeconds"]=time.monotonic()-started
        rec["parameters"]["peakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rec["parameters"]["exitCode"]=code
        rec["parameters"]["completePhases"]=state["phases"]
        if mp.exists(): rec["parameters"]["manifest"]=identity(mp)
        atomic(a.out/"exact-low20-receipt.json",canon(rec))
        print(json.dumps(rec,separators=(",",":")),flush=True)

if __name__=="__main__": raise SystemExit(main())
