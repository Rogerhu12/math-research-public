#!/usr/bin/env python3
"""New original p47 principal cycles and complete cusp fixed-cycle action."""
import hashlib
import json
import os
from pathlib import Path
import signal
import sys
import time
import traceback

ROOT = Path(__file__).resolve().parents[3]
REQUEST = ROOT / "topics/serre-uniformity/notes/full-p47-principal-fixed-action-request.json"
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
    if req["execution_id"] != "full-p47-principal-fixed-action-v1":
        raise RuntimeError("Wrong execution ID.")
    if (req["prime"], req["auxiliary_prime"], req["total_seconds"],
            req["reserve_seconds"]) != (47, 4513, 120, 10):
        raise RuntimeError("Unexpected request.")
    signal.signal(signal.SIGALRM, stop)
    signal.setitimer(signal.ITIMER_REAL, max(0.1, 110-(time.monotonic()-START)))
    emit("preflight", source=source, run=os.environ.get("GITHUB_RUN_ID"),
         attempt=os.environ.get("GITHUB_RUN_ATTEMPT"), request_sha256=rh,
         source_sha256=req["source_sha256"])
    from sage.all import (QQ, ZZ, GF, matrix, vector, identity_matrix,
                          PolynomialRing, proof)
    from sage.env import SAGE_VERSION
    if SAGE_VERSION != req["sage_version"]:
        raise RuntimeError("Wrong Sage version.")
    proof.all(True)
    p, ell = 47, 4513
    inv2 = pow(2, -1, p)
    inverses = {a: pow(a, -1, p) for a in range(1,p)}
    def angle(a):
        a %= p
        return min(a, (-a) % p)
    def chi(a):
        a %= p
        if not a:
            return 0
        return 1 if pow(a, (p-1)//2, p) == 1 else -1
    angles = [a for a in range((p+1)//2) if a != 1]
    indices = {a:i for i,a in enumerate(angles)}
    deg = {a:24 if a == 0 else 48 for a in angles}
    size = len(angles)
    def canon(y):
        return min(y, tuple((-a) % p for a in y))

    # New input: the eleven actual split regular conjugacy classes.
    # Normalize the first nonzero projective matrix entry to one.
    STAGE = "actual_split_class_cycles"
    targets = {r: {} for r in range(1,12)}
    class_sizes = {r:0 for r in range(1,12)}
    invariant_to_r = {}
    for r in range(1,12):
        a = pow(5,r,p)
        inv = (a+1)**2*inverses[a] % p
        if inv in invariant_to_r:
            raise ArithmeticError("Repeated projective class invariant.")
        invariant_to_r[inv] = r
    projective_size = 0
    def consume(a,b,c,d):
        nonlocal projective_size
        det = (a*d-b*c) % p
        if not det:
            return
        projective_size += 1
        di = inverses[det]
        r = invariant_to_r.get((a+d)**2*di % p)
        if r is None:
            return
        # x0=(0,1;-1,0), y=g*x0*g^{-1}.
        y = ((-b*d-a*c)*di % p, (a*a+b*b)*di % p,
             (-c*c-d*d)*di % p)
        if (y[0]*y[0]+y[1]*y[2]) % p != p-1:
            raise ArithmeticError("Conjugation changed the original x^2=-I.")
        y = canon(y)
        targets[r][y] = targets[r].get(y,0)+1
        class_sizes[r] += 1
    for b in range(p):
        for c in range(p):
            for d in range(p):
                consume(1,b,c,d)
    for c in range(1,p):
        for d in range(p):
            consume(0,1,c,d)
    if projective_size != p*(p*p-1) or set(class_sizes.values()) != {2256}:
        raise ArithmeticError("Incomplete PGL or split conjugacy class.")
    class_vectors = {}
    for r in range(1,12):
        per_angle = {}
        per_target = {}
        for y,n in targets[r].items():
            C = angle((y[1]-y[2])*inv2)
            if C == 1:
                raise ArithmeticError("Split regular class acquired a diagonal.")
            per_angle[C] = per_angle.get(C,0)+n
            per_target.setdefault(C,[]).append(n)
        coefficients = []
        for C in angles:
            quotient,remainder = divmod(per_angle.get(C,0),deg[C])
            if remainder:
                raise ArithmeticError("Nonintegral orbital coefficient.")
            if quotient:
                if len(per_target[C]) != deg[C] or set(per_target[C]) != {quotient}:
                    raise ArithmeticError("Class count not constant on the full original angle.")
            elif C in per_target:
                raise ArithmeticError("Zero orbital coefficient has actual targets.")
            coefficients.append(quotient)
        if sum(a*deg[C] for C,a in zip(angles,coefficients)) != 2256:
            raise ArithmeticError("Actual correspondence degree mismatch.")
        class_vectors[r] = vector(QQ,coefficients)
    Z = class_vectors[1]-class_vectors[2]
    # These ten differences span the principal trace-zero source.
    family_r = list(range(2,12))
    family = [class_vectors[r]-class_vectors[1] for r in family_r]
    emit("new_class_cycles", projective_group_size=projective_size,
         class_count=11, each_class_size=2256,
         no_diagonal=True, targetwise_orbital_multiplicities_checked=True,
         angles=angles, original_Zps_coefficients=[int(x) for x in Z],
         class_coefficient_sha256=digest(
             [[r,[int(x) for x in class_vectors[r]]] for r in range(1,12)]))

    # Consume certified R1081 algebra by its exact composition/source hashes.
    # Do not repeat its full finite-fiber verification, LDL or Hecke computation.
    STAGE = "consume_certified_angle_algebra"
    def comp(A,B,D):
        if A and B:
            return 2+chi(1+2*A*B*D-A*A-B*B-D*D)+chi(
                1-2*A*B*D-A*A-B*B-D*D)
        if A or B:
            return 1+chi(1-A*A-B*B-D*D)
        return (1+chi(1-D*D))//2
    comp_rows = [[[comp(A,B,D) for D in angles] for B in angles] for A in angles]
    if digest(comp_rows) != req["certified_composition_sha256"]:
        raise ArithmeticError("Certified R1081 composition input hash mismatch.")
    cycle_rows, traces = [], []
    for C in angles:
        e4 = sum(deg[A] for A in angles if angle(2*A*A-1) == C)
        e3 = sum(deg[A] for A in angles if angle((3*A*A-1)*inv2) == C)
        nc = sum(angle(1+m*m*inv2) == C for m in range(1,p))
        tau = QQ(deg[C])-QQ(e4)/4-QQ(e3)/3-QQ(23*nc)/2
        if tau.denominator() != 1:
            raise ArithmeticError("Nonintegral certified trace input.")
        traces.append(tau)
        cycle_rows.append([C,deg[C],e4,e3,nc,int(tau)])
    if digest(cycle_rows) != req["certified_trace_sha256"]:
        raise ArithmeticError("Certified R1081 trace input hash mismatch.")
    traces = vector(QQ,traces)
    # In the actual Jacobian quotient I=-sum_C R_C.
    multiplication = []
    for i,A in enumerate(angles):
        columns = []
        for j,B in enumerate(angles):
            diagonal = deg[A] if A == B else 0
            columns.append(vector(QQ,[comp_rows[i][j][k]-diagonal for k in range(size)]))
        multiplication.append(matrix(QQ,columns).transpose())
    one = vector(QQ,[-1]*size)
    identity = identity_matrix(QQ,size)
    def mul_matrix(v):
        result = matrix(QQ,size,size,0)
        for c,M in zip(v,multiplication):
            if c:
                result += c*M
        return result
    if mul_matrix(one) != identity:
        raise ArithmeticError("Actual j-pull-push quotient has wrong identity.")
    degrees = vector(QQ,[deg[C] for C in angles])
    if any(degrees.dot_product(v) != 0 or traces.dot_product(v) != 0 for v in family+[Z]):
        raise ArithmeticError("Original principal family lost degree/trace zero.")
    if matrix(QQ,family).rank() != 10:
        raise ArithmeticError("Incomplete principal trace-zero family.")
    MZ = mul_matrix(Z)
    if MZ.rank() != 11:
        raise ArithmeticError("Original principal multiplier has wrong rank.")
    PR = PolynomialRing(QQ,"X")
    X = PR.gen()
    PZ = PR(MZ.charpoly())
    QZ, remainder = PZ.quo_rem(X**12)
    if remainder or QZ.degree() != 11 or not QZ.is_irreducible():
        raise ArithmeticError("Unexpected actual principal minimal polynomial.")
    if abs(QZ[0]) != 23*47**11:
        raise ArithmeticError("Original principal norm disagrees with cyclotomic proof.")
    def polynomial_matrix(poly,M):
        out = matrix(QQ,size,size,0)
        for coefficient in reversed(poly.list()):
            out = out*M+coefficient*identity
        return out
    Pc = polynomial_matrix(QZ,MZ)/QZ[0]
    if Pc*Pc != Pc or Pc.rank() != 12 or MZ*Pc != 0:
        raise ArithmeticError("Actual cusp projector failed.")
    if any(ZZ(x.denominator()) % ell == 0 for x in Pc.list()):
        raise ArithmeticError("Cusp projector is not integral at the chosen auxiliary prime.")

    def fixed_transform(v,which):
        answer = []
        for A in angles:
            C = angle(2*A*A-1) if which == 4 else angle((3*A*A-1)*inv2)
            answer.append(0 if C == 1 else v[indices[C]])
        return vector(QQ,answer)
    w4,w3 = fixed_transform(Z,4),fixed_transform(Z,3)
    projected4,projected3 = Pc*w4,Pc*w3
    family4 = [fixed_transform(v,4) for v in family]
    family3 = [fixed_transform(v,3) for v in family]
    p4,p3 = [Pc*v for v in family4],[Pc*v for v in family3]
    joint = matrix(QQ,[list(a)+list(b) for a,b in zip(p4,p3)])
    emit("actual_cusp_fixed_action", principal_multiplier_rank=int(MZ.rank()),
         principal_minimal_polynomial_degree=int(QZ.degree()),
         principal_norm_abs=str(abs(QZ[0])),
         original_Zps_F4_cusp_nonzero=any(x != 0 for x in projected4),
         original_Zps_F3_cusp_nonzero=any(x != 0 for x in projected3),
         family_trace_zero_dimension=10,
         family_F4_cusp_rank=int(matrix(QQ,p4).rank()),
         family_F3_cusp_rank=int(matrix(QQ,p3).rank()),
         family_joint_cusp_rank=int(joint.rank()),
         principal_minimal_polynomial_sha256=digest([str(x) for x in QZ.list()]),
         cusp_projector_sha256=digest([[str(x) for x in row] for row in Pc.rows()]),
         projected_Zps_F4_sha256=digest([str(x) for x in projected4]),
         projected_Zps_F3_sha256=digest([str(x) for x in projected3]),
         projected_family_sha256=digest([[str(x) for x in row] for row in joint.rows()]))

    # New concrete target: all twelve cusp characters mod4513, with the actual
    # two CM coefficient rows for the ten original integral correspondences.
    STAGE = "all_actual_cusp_characters_mod4513"
    k = GF(ell)
    PRk = PolynomialRing(k,"X")
    Ik = identity_matrix(k,size)
    Pck = matrix(k,Pc)
    def over_k(M):
        return matrix(k,M)
    generator = None
    for t in req["generator_t_candidates"]:
        G = multiplication[indices[0]]+t*multiplication[indices[2]]+t*t*multiplication[indices[3]]
        pbar = PRk(G.charpoly())
        if pbar.gcd(pbar.derivative()).degree() == 0:
            generator = (t,G,pbar)
            break
    if generator is None:
        raise ArithmeticError("No separating angle generator in the declared finite candidates.")
    t,G,pbar = generator
    factorQ = list(PR(G.charpoly()).factor())
    if sorted(int(f.degree()) for f,e in factorQ) != [4,8,11] or any(e != 1 for f,e in factorQ):
        raise ArithmeticError("Unexpected rational angle fields.")
    factor_k = list(pbar.factor())
    if any(e != 1 for f,e in factor_k):
        raise ArithmeticError("Nonreduced auxiliary angle algebra.")
    roots = sorted(int(-f[0]/f[1]) for f,e in factor_k if f.degree() == 1)
    if len(roots) != 12 or sorted(int(f.degree()) for f,e in factor_k) != [1]*12+[11]:
        raise ArithmeticError("Incomplete original cusp character coverage.")
    GK = over_k(G)
    w4M,w3M = over_k(mul_matrix(w4)),over_k(mul_matrix(w3))
    f4M = [over_k(mul_matrix(v)) for v in family4]
    f3M = [over_k(mul_matrix(v)) for v in family3]
    character_rows = []
    for root in roots:
        line = (GK-k(root)*Ik).right_kernel()
        if line.dimension() != 1:
            raise ArithmeticError("Angle character eigenspace is not one dimensional.")
        v = line.basis()[0]
        if Pck*v != v:
            raise ArithmeticError("A purported linear character is not cusp type.")
        position = next(i for i,a in enumerate(v) if a)
        def eigenvalue(M):
            mv = M*v
            value = mv[position]/v[position]
            if mv != value*v:
                raise ArithmeticError("Fixed transform does not act by the same character.")
            return value
        a4,a3 = [eigenvalue(M) for M in f4M],[eigenvalue(M) for M in f3M]
        rank = matrix(k,[a4,a3]).rank()
        minor = None
        if rank == 2:
            for i in range(10):
                for j in range(i+1,10):
                    determinant = a4[i]*a3[j]-a4[j]*a3[i]
                    if determinant:
                        minor = {"class_exponents":[family_r[i],family_r[j]],
                                 "determinant":int(determinant)}
                        break
                if minor is not None:
                    break
        type_degrees = [int(f.degree()) for f,e in factorQ if PRk(f)(k(root)) == 0]
        if len(type_degrees) != 1 or type_degrees[0] not in (4,8):
            raise ArithmeticError("Ambiguous actual cusp character field.")
        character_rows.append({
            "generator_root":root, "rational_cusp_field_degree":type_degrees[0],
            "Zps_F4_scalar":int(eigenvalue(w4M)),
            "Zps_F3_scalar":int(eigenvalue(w3M)),
            "two_CM_coefficient_row_rank":int(rank), "rank_two_witness":minor})
    emit("actual_cusp_characters", prime=ell,
         angle_generator="R0+t*R2+t^2*R3", t=int(t),
         complete_characters=character_rows,
         all_twelve_CM_row_ranks_two=all(row["two_CM_coefficient_row_rank"] == 2
                                       for row in character_rows),
         rational_generator_polynomial_sha256=digest([str(a) for a in PR(G.charpoly()).list()]),
         character_rows_sha256=digest(character_rows))
    STAGE = "completed"
    signal.setitimer(signal.ITIMER_REAL,0)
    emit("receipt",status="complete",source=source,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=rh,budget_seconds=120,reserve_seconds=10,
         all_twelve_CM_row_ranks_two=all(row["two_CM_coefficient_row_rank"] == 2
                                       for row in character_rows),
         no_new_Hecke_or_Lprime_computation=True,
         scope="Original angle endomorphism coefficients only; no CM class/log/height nonvanishing inferred.")

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
