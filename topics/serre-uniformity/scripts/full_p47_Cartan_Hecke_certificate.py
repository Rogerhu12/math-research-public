#!/usr/bin/env python3
"""Original full-p47 Cartan trace algebra and integral auxiliary Hecke factors."""
import hashlib
import json
import os
from pathlib import Path
import signal
import sys
import time
import traceback

ROOT = Path(__file__).resolve().parents[3]
REQUEST = ROOT / "topics/serre-uniformity/notes/full-p47-Cartan-Hecke-request.json"
START = time.monotonic()
STAGE = "preflight"

def emit(kind, **data):
    print(json.dumps(dict(kind=kind, elapsed_seconds=time.monotonic()-START, **data),
                     sort_keys=True, ensure_ascii=False), flush=True)

def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True,
                          separators=(",", ":")).encode()).hexdigest()

def stop(signum, frame):
    raise TimeoutError("Mathematical budget; unfinished conclusions unresolved.")

def source_head():
    gd = ROOT / ".git"
    source = (gd / "HEAD").read_text().strip()
    if source.startswith("ref: "):
        ref = source[5:]
        if not ref.startswith("refs/") or ".." in ref.split("/"):
            raise RuntimeError("Unexpected ref.")
        p = gd / ref
        if p.exists():
            source = p.read_text().strip()
        else:
            rows = [s.split(" ", 1)[0] for s in (gd/"packed-refs").read_text().splitlines()
                    if s.endswith(" "+ref)]
            if len(rows) != 1:
                raise RuntimeError("Ambiguous actual checkout.")
            source = rows[0]
    if len(source) != 40 or source != os.environ.get("GITHUB_SHA"):
        raise RuntimeError("Actual checkout/GITHUB_SHA mismatch.")
    return source

def main():
    global STAGE
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get(
            "GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("Only this public repository's Actions may execute.")
    raw = REQUEST.read_bytes()
    rh = hashlib.sha256(raw).hexdigest()
    if rh != os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("Request pin mismatch.")
    req = json.loads(raw)
    for name, wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != wanted:
            raise RuntimeError("Source pin mismatch: "+name)
    source = source_head()
    if req["prime"] != 47 or req["total_seconds"] != 600 or req["reserve_seconds"] != 30:
        raise RuntimeError("Unexpected request.")
    signal.signal(signal.SIGALRM, stop)
    signal.setitimer(signal.ITIMER_REAL, max(0.1, 570-(time.monotonic()-START)))
    emit("preflight", source=source, run=os.environ.get("GITHUB_RUN_ID"),
         attempt=os.environ.get("GITHUB_RUN_ATTEMPT"), request_sha256=rh,
         source_sha256=req["source_sha256"])
    from fractions import Fraction as Q
    p = 47
    inv2, inv3 = pow(2, -1, p), pow(3, -1, p)
    def angle(a):
        a %= p
        return min(a, (-a) % p)
    def chi(a):
        a %= p
        if not a:
            return 0
        s = pow(a, (p-1)//2, p)
        return 1 if s == 1 else -1
    angles = [a for a in range((p+1)//2) if a != 1]
    deg = {a: 24 if a == 0 else 48 for a in angles}
    STAGE = "original_fixed_cycles"
    cycle_rows = []
    traces = {}
    for C in angles:
        e4 = sum(deg[A] for A in angles if angle(2*A*A-1) == C)
        e3 = sum(deg[A] for A in angles if angle((3*A*A-1)*inv2) == C)
        nc = sum(angle(1+m*m*inv2) == C for m in range(1, p))
        if C == 0:
            expected = (48, 48, 0)
        else:
            expected = (24*(2+chi((1+C)*inv2)+chi((1-C)*inv2)),
                        24*(2+chi((1+2*C)*inv3)+chi((1-2*C)*inv3)),
                        2+chi(2*(C-1))+chi(-2*(C+1)))
        if (e4, e3, nc) != expected:
            raise ArithmeticError("Original fixed-cycle/closed-form disagreement.")
        tau = Q(deg[C])-Q(e4,4)-Q(e3,3)-Q(23*nc,2)
        if tau.denominator != 1:
            raise ArithmeticError("Nonintegral actual Hodge trace.")
        traces[C] = int(tau)
        cycle_rows.append([C, deg[C], e4, e3, nc, int(tau)])
    genus = Q(1)+Q(1081,12)-Q(25,4)-Q(1,3)-Q(23,2)
    if genus != 73 or 73+sum(traces.values()) != 0:
        raise ArithmeticError("Genus or full j-pull-push relation failed.")
    emit("fixed_cycles", genus=int(genus), rows=cycle_rows,
         source_trace_sha256=digest(cycle_rows))

    def comp(A, B, D):
        if A and B:
            return 2+chi(1+2*A*B*D-A*A-B*B-D*D)+chi(
                1-2*A*B*D-A*A-B*B-D*D)
        if A or B:
            return 1+chi(1-A*A-B*B-D*D)
        return (1+chi(1-D*D))//2

    # Independent finite-fiber realization: actual trace-zero matrices x^2=-I.
    # Counts every intermediate necklace, rather than rerunning the formula.
    STAGE = "original_fiber_composition"
    def canon(x):
        return min(x, tuple((-a) % p for a in x))
    points = set()
    for a in range(p):
        for b in range(1, p):
            c = (-1-a*a)*pow(b, -1, p) % p
            points.add(canon((a,b,c)))
    points = sorted(points)
    if len(points) != 1081:
        raise ArithmeticError("Incomplete original necklace fiber.")
    def Bform(x, y):
        a,b,c=x
        d,e,f=y
        return (-a*d-(b*f+c*e)*inv2) % p
    x0=canon((0,1,p-1))
    target={}
    fiber_degrees={}
    for z in points:
        D=angle(Bform(x0,z))
        target.setdefault(D,z)
        fiber_degrees[D]=fiber_degrees.get(D,0)+1
    if fiber_degrees != {1:1, **deg}:
        raise ArithmeticError("Original angle degrees failed.")
    for D,z in sorted(target.items()):
        actual={}
        for y in points:
            A=angle(Bform(x0,y))
            B=angle(Bform(y,z))
            if A != 1 and B != 1:
                actual[A,B]=actual.get((A,B),0)+1
        for A in angles:
            for B in angles:
                wanted = (deg[A] if A == B else 0) if D == 1 else comp(A,B,D)
                if actual.get((A,B),0) != wanted:
                    raise ArithmeticError("Actual finite-fiber composition mismatch.")
    comp_rows=[[[comp(A,B,D) for D in angles] for B in angles] for A in angles]
    emit("composition", original_necklaces=len(points),
         all_angle_pairs_and_target_angles_verified=True,
         composition_sha256=digest(comp_rows))

    STAGE="actual_Rosati_trace_pairing"
    labels=["I"]+angles
    size=len(labels)
    gram=[[0]*size for _ in range(size)]
    gram[0][0]=73
    for i,A in enumerate(angles,1):
        gram[0][i]=gram[i][0]=traces[A]
        for j,B in enumerate(angles,1):
            gram[i][j]=(73*deg[A] if A == B else 0)+sum(
                comp(A,B,D)*traces[D] for D in angles)
    if any(sum(row) != 0 for row in gram):
        raise ArithmeticError("Actual j-pull-push relation missing from trace kernel.")
    matrix=[[Q(a) for a in row] for row in gram]
    remaining=list(labels)
    pivots=[]
    while matrix:
        pos=next((i for i in range(len(matrix)) if matrix[i][i] != 0),None)
        if pos is None:
            if any(a != 0 for row in matrix for a in row):
                raise ArithmeticError("Trace form is not positive semidefinite.")
            break
        pivot=matrix[pos][pos]
        if pivot <= 0:
            raise ArithmeticError("Negative actual Rosati pivot.")
        pivots.append([remaining[pos],str(pivot)])
        keep=[i for i in range(len(matrix)) if i != pos]
        matrix=[[matrix[i][j]-matrix[i][pos]*matrix[pos][j]/pivot
                 for j in keep] for i in keep]
        remaining=[remaining[i] for i in keep]
    i0=labels.index(0)
    i2=labels.index(2)
    trZ=13*traces[0]+4*traces[2]
    trZ2=169*gram[i0][i0]+104*gram[i0][i2]+16*gram[i2][i2]
    if trZ != 0 or trZ2 < 0:
        raise ArithmeticError("Specified original trace-zero cycle failed.")
    emit("trace_certificate", labels=labels, rank=len(pivots),
         nullity=size-len(pivots), positive_semidefinite=True,
         gram_sha256=digest(gram), LDL_pivots_sha256=digest(pivots),
         original_Z_coefficients={"R0":13,"R2":4},
         trace_Z=trZ, trace_Z_squared=trZ2,
         nonzero_Jacobian_endomorphism=(trZ2>0))

    # New task: integral splitting of the COMPLETE original Hecke algebra.
    # Reconstruct the exact modular-symbol input; do not rerun L' certification.
    STAGE="exact_Hecke_input"
    from sage.all import (QQ, ZZ, GF, ModularSymbols, PolynomialRing,
                          identity_matrix, proof)
    from sage.env import SAGE_VERSION
    if SAGE_VERSION != req["sage_version"]:
        raise RuntimeError("Wrong Sage version.")
    proof.all(True)
    auxiliary=req["auxiliary_primes"]
    if any(not ZZ(ell).is_prime(proof=True) for ell in auxiliary):
        raise ArithmeticError("Auxiliary integer is not prime.")
    S=ModularSymbols(2209,2,sign=1,base_ring=QQ).cuspidal_subspace().new_subspace()
    factors=list(S.decomposition())
    if sum(int(F.dimension()) for F in factors) != 157:
        raise ArithmeticError("Incomplete new space.")
    plus=[]
    for F in factors:
        d=int(F.dimension())
        w=F.atkin_lehner_operator(2209).matrix()
        if w == identity_matrix(QQ,d):
            plus.append(F)
        elif w != -identity_matrix(QQ,d):
            raise ArithmeticError("Unexpected Fricke block.")
    if sorted(int(F.dimension()) for F in plus) != [16,24,33]:
        raise ArithmeticError("Wrong full positive space.")
    hecke=[{n:F.hecke_operator(n).matrix() for n in [2,3,5]} for F in plus]
    PR=PolynomialRing(ZZ,"X")
    local_results={}
    for t in req["hecke_t_candidates"]:
        STAGE="Hecke_integral_generator_t_%d" % t
        pieces=[]
        for operators in hecke:
            H=operators[2]+t*operators[3]+t*t*operators[5]
            pieces.append(PR(H.charpoly()))
        whole=PR.one()
        for P in pieces:
            whole*=P
        if whole.degree()!=73 or not whole.is_monic():
            raise ArithmeticError("Incomplete integral Hecke characteristic polynomial.")
        new=[]
        for ell in auxiliary:
            if ell in local_results:
                continue
            PRell=PolynomialRing(GF(ell),"X")
            Pbar=PRell(whole)
            if Pbar.gcd(Pbar.derivative()).degree()!=0:
                continue
            parts=[]
            for F,P in zip(plus,pieces):
                fact=list(PRell(P).factor())
                if any(int(e)!=1 for _,e in fact):
                    raise ArithmeticError("Nonreduced factor after squarefree test.")
                degrees=sorted(int(g.degree()) for g,_ in fact)
                roots=sorted(int(-g[0]/g[1]) for g,_ in fact if g.degree()==1)
                if sum(degrees)!=int(F.dimension()):
                    raise ArithmeticError("Incomplete auxiliary factorization.")
                parts.append({"newform_dimension":int(F.dimension()),
                              "factor_degrees":degrees,"linear_roots":roots})
            row={"prime":int(ell),"t":int(t),
                 "H":"T2+t*T3+t^2*T5","squarefree_full_degree73":True,
                 "rational_charpoly_sha256":digest([str(a) for a in whole.list()]),
                 "factors":parts,
                 "degree_one_blocks":sum(len(f["linear_roots"]) for f in parts)}
            local_results[ell]=row
            new.append(row)
        if new:
            emit("integral_Hecke_certificate", certificates=new)
        if len(local_results)==len(auxiliary):
            break
    unresolved=[ell for ell in auxiliary if ell not in local_results]
    STAGE="completed"
    signal.setitimer(signal.ITIMER_REAL,0)
    emit("receipt",status="complete",source=source,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=rh,trace_rank=len(pivots),trace_Z_squared=trZ2,
         hecke_certified_primes=sorted(local_results),unresolved_Hecke_primes=unresolved,
         scope="Actual angle endomorphisms and integral Hecke decomposition only; no MW saturation or disk uniqueness.")

if __name__ == "__main__":
    try:
        main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("receipt",status="incomplete",stage=STAGE,
             exception_type=type(exc).__name__,message=str(exc),
             scope="No conclusion for unfinished computations.")
        traceback.print_exc()
        sys.exit(1)
