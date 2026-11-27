#!/usr/bin/env python3
"""Actual full47 signed CM coordinates from weighted Jacobi coefficients.

Only the new four CM Hecke ratios and the consumed Bq coordinate are read.
R89's generic proof is consumed; none of its level41 data is reconstructed.
All mathematics is restricted to this public repository's GitHub Actions.
"""
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import signal
import tempfile
import time
import traceback

ROOT = Path(__file__).resolve().parents[3]
PRE = "topics/serre-uniformity/"
REQUEST = ROOT/(PRE+"notes/full-p47-signed-Jacobi-CM-coordinates-request.json")
GP_SOURCE = PRE+"scripts/full_p47_signed_Jacobi_CM_coordinates.gp"
HODGE_SOURCE = PRE+"scripts/full_p47_weight_one_Hodge_certificate.py"
HEIGHT_INPUT = PRE+"notes/full-p47-CM-height-move-request.json"
START = time.monotonic()
DEADLINE = None
STAGE = "preflight"
SOURCE = None
REQUEST_HASH = None
RECORDS = []


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                          separators=(",", ":")).encode()).hexdigest()


def emit(kind, **data):
    print(json.dumps(dict(kind=kind, elapsed_seconds=time.monotonic()-START,
                          **data), sort_keys=True), flush=True)


def check():
    if DEADLINE is not None and time.monotonic() >= DEADLINE:
        raise TimeoutError("The declared mathematical reserve has been reached.")


def stop(signum, frame):
    raise TimeoutError("The declared mathematical reserve has been reached.")


def source_head():
    gd = ROOT/".git"
    head = (gd/"HEAD").read_text().strip()
    if head.startswith("ref: "):
        ref = head[5:]
        if not ref.startswith("refs/") or ".." in ref.split("/"):
            raise RuntimeError("Unexpected checkout ref.")
        if (gd/ref).exists():
            head = (gd/ref).read_text().strip()
        else:
            rows = [line.split(" ",1)[0] for line in (gd/"packed-refs").read_text().splitlines()
                    if line.endswith(" "+ref)]
            if len(rows) != 1:
                raise RuntimeError("Ambiguous actual checkout.")
            head = rows[0]
    if len(head) != 40 or head != os.environ.get("GITHUB_SHA"):
        raise RuntimeError("Actual checkout/GITHUB_SHA mismatch.")
    return head


def read_request():
    global REQUEST_HASH
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Mathematics may execute only in this public repository's Actions.")
    raw = REQUEST.read_bytes()
    REQUEST_HASH = hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH != os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("Unpinned finite mathematical request.")
    req = json.loads(raw)
    if (req["execution_id"] != "full-p47-signed-Jacobi-CM-v1" or
            req["prime"] != 47 or req["coefficient_prime"] != 4513 or
            req["sage_version"] != "10.6" or req["total_seconds"] != 1800 or
            req["reserve_seconds"] != 60 or req["auxiliary_prime_bound"] != 199 or
            req["first_auxiliary"] != [-11,2027] or
            req["CM_discriminants"] != [-4,-3,-7,-8] or
            req["candidate_ids"] != [141,0,76,108] or req["random_seed"] != 0):
        raise RuntimeError("Unexpected full47 signed Jacobi scope.")
    for path, wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest() != wanted:
            raise RuntimeError("Source pin mismatch: "+path)
    return req


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT/path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def rows(M):
    return [[int(a) for a in row] for row in M.rows()]


def positive_divisors(n):
    out = []
    for a in range(1, math.isqrt(n)+1):
        if n % a == 0:
            out.append(a)
            if a*a != n:
                out.append(n//a)
    return out


def enumerate_rows(matrices, auxiliary, root):
    """Complete RSST weight2 signed intersection sums, including Q and -Q."""
    level = 2209
    ell = -auxiliary
    if (root*root-auxiliary) % (4*level):
        raise ArithmeticError("An auxiliary root is not admissible.")
    chi = [0 if a == 0 else (1 if pow(a,(ell-1)//2,ell)==1 else -1)
           for a in range(ell)]
    linear = []
    for a,b,c,d in matrices:
        if a*d-b*c != 1:
            raise ArithmeticError("A path matrix changed orientation.")
        linear.append((d*d,-d*c,c*c,-2*d*b,d*a+b*c,-2*c*a))
    output = []
    for D in (-4,-3,-7,-8):
        check()
        delta = D*level
        r = 0 if D % 2 == 0 else level
        if (r*r-delta) % (4*level):
            raise ArithmeticError("The actual antipodal CM label is inadmissible.")
        target = r*root % (2*level)
        discr = delta*auxiliary
        bound = math.isqrt(discr)
        if bound*bound == discr:
            raise ArithmeticError("A nonsquare RSST hypothesis failed.")
        values = [0]*len(matrices)
        total = hits = 0
        for b in range(-bound,bound+1):
            if (discr-b*b) % 4:
                continue
            n = (discr-b*b)//4
            if n <= 0:
                continue
            if b % 64 == 0:
                check()
            for a in positive_divisors(n):
                c = -n//a
                total += 1
                character = chi[a % ell] if a % ell else chi[c % ell]
                if not character:
                    continue
                for j,(l1,l2,l3,l4,l5,l6) in enumerate(linear):
                    A = l1*a+l2*b+l3*c
                    if A % level:
                        continue
                    B = (l4*a+l5*b+l6*c) % (2*level)
                    # Both indicators are required even for r=-r (0 or N).
                    multiplicity = int(B==target)+int(B==(-target)%(2*level))
                    values[j] -= character*multiplicity
                    hits += multiplicity
        output.append(dict(fundamental_discriminant=D,delta=delta,r=r,
                           product_discriminant=discr,positive_a_forms=total,
                           signed_hits=hits,nonzero_paths=sum(a!=0 for a in values),
                           values_sha256=digest(values),values=values))
    return output


def main():
    global DEADLINE,STAGE,SOURCE
    req = read_request()
    SOURCE = source_head()
    DEADLINE = START+req["total_seconds"]-req["reserve_seconds"]
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.001,DEADLINE-time.monotonic()))
    emit("started",source_commit=SOURCE,request_sha256=REQUEST_HASH,
         total_seconds=req["total_seconds"],reserve_seconds=req["reserve_seconds"],
         new_scope="Four actual weighted CM Hecke coordinates; consumed old Bq only.")
    from sage.all import (QQ,ZZ,GF,PolynomialRing,matrix,vector,identity_matrix,
                          zero_matrix,prime_range,pari,proof,set_random_seed)
    from sage.env import SAGE_VERSION
    if SAGE_VERSION != req["sage_version"]:
        raise RuntimeError("Wrong Sage version.")
    proof.all(True)
    set_random_seed(0)
    q=4513
    k=GF(q)
    PR=PolynomialRing(k,"X")
    I=identity_matrix(k,73)

    STAGE="actual_modular_symbol_input"
    pari.allocatemem(536870912,4294967296)
    with tempfile.TemporaryDirectory(prefix="serre-jacobi47-") as tmp:
        pari.read(str(ROOT/GP_SOURCE))
        pari("p47j_setup("+json.dumps(tmp)+")")
        packet=json.loads((Path(tmp)/"input.json").read_text())

    def decode(name):
        den,data=packet[name]
        if int(den)%q==0:
            raise ArithmeticError("A GP lattice denominator is not q-integral: "+name)
        return matrix(QQ,data)/QQ(den)

    def reduce(M):
        if M.denominator()%q==0:
            raise ArithmeticError("A needed exact rational matrix is not q-integral.")
        return matrix(k,M)

    E=decode("E")
    Pqq=decode("P")
    P=reduce(Pqq)
    full={n:reduce(decode("T%d"%n)) for n in (2,3,5)}
    ops={n:reduce(decode("A%d"%n)) for n in (2,3,5)}
    Aq=decode("Aq")
    oldpoly=PolynomialRing(ZZ,"X")(Aq.charpoly())
    if digest([str(a) for a in oldpoly.list()]) != req["consumed_Tq_integer_charpoly_sha256"]:
        raise ArithmeticError("The consumed full T4513 characteristic polynomial changed.")
    ops[4513]=reduce(Aq)
    Bq=I-ops[4513]
    if int(Bq.det()) != req["consumed_Bq_determinant_mod_q"]:
        raise ArithmeticError("The consumed Bq unit certificate changed.")
    H=ops[3]+ops[5]
    cp=PR(H.charpoly())
    if (digest([int(a) for a in cp.list()]) != req["Hodd_characteristic_polynomial_sha256"] or
            cp.degree()!=73 or cp.gcd(cp.derivative()).degree()!=0):
        raise ArithmeticError("Wrong or nonetale original Hodd algebra.")
    factors=list(cp.factor())
    if len(factors)!=28 or any(int(e)!=1 for f,e in factors):
        raise ArithmeticError("The complete 28 original blocks were not retained.")
    Ek=reduce(E)
    piv=list(Ek.transpose().pivots())
    if (len(piv)!=189 or P.nrows()!=189 or P.ncols()!=73 or P.rank()!=73 or
            E.nrows()!=packet["free_path_count"] or E.ncols()!=189):
        raise ArithmeticError("Actual cohomology lattice ranks failed.")
    Einv=E.matrix_from_rows(piv).inverse()
    reduce(Einv)  # Verify exact integral solving at q before any projected ratio.

    def evaluate(poly,A):
        out=zero_matrix(k,A.nrows())
        one=identity_matrix(k,A.nrows())
        for coefficient in reversed(poly.list()):
            out=out*A+coefficient*one
        return out

    STAGE="actual_integral_new_projection"
    projection=None
    chosen_separator=None
    for coefficients in req["separating_Hecke_coefficients"]:
        check()
        Sfull=sum((k(a)*full[n] for a,n in zip(coefficients,(2,3,5))),
                  zero_matrix(k,189))
        Snew=sum((k(a)*ops[n] for a,n in zip(coefficients,(2,3,5))),
                 zero_matrix(k,73))
        cnew=PR(Snew.charpoly())
        cfull=PR(Sfull.charpoly())
        complement,remainder=cfull.quo_rem(cnew)
        if remainder:
            raise ArithmeticError("The actual Hecke restriction failed on characteristic polynomials.")
        if cnew.gcd(complement).degree()!=0:
            continue
        Q=evaluate(cnew,Sfull).column_space().basis_matrix().transpose()
        if Q.ncols()!=116:
            raise ArithmeticError("Wrong actual complementary cohomology dimension.")
        basis=P.augment(Q)
        if basis.rank()!=189:
            raise ArithmeticError("The actual new/complement decomposition is singular.")
        projection=basis.inverse().matrix_from_rows(list(range(73)))
        if projection*P!=I or any(projection*full[n]!=ops[n]*projection for n in (2,3,5)):
            raise ArithmeticError("The actual projection does not commute with Hecke.")
        chosen_separator=list(map(int,coefficients))
        break
    if projection is None:
        raise ArithmeticError("Declared Hecke separators did not give a q-integral new projection.")
    emit("actual_input_consumed",pari_version=packet["pari_version"],
         full_dimension=189,new_dimension=157,plus_dimension=73,
         path_count=packet["path_count"],free_path_count=packet["free_path_count"],
         elliptic_zero_path_count=packet["path_count"]-packet["free_path_count"],
         separating_Hecke_coefficients=chosen_separator,
         path_matrices_sha256=digest(packet["paths"]),
         Hodd_characteristic_polynomial_sha256=req["Hodd_characteristic_polynomial_sha256"],
         consumed_Tq_integer_charpoly_sha256=req["consumed_Tq_integer_charpoly_sha256"],
         consumed_Bq_determinant_mod_q=int(Bq.det()))

    auxiliaries=[(-11,2027)]
    for ell in prime_range(3,req["auxiliary_prime_bound"]+1):
        ell=int(ell)
        if ell in (11,47) or ell%4!=3 or pow((-ell)%47,23,47)!=1:
            continue
        roots=[r for r in range(2*2209) if (r*r+ell)%(4*2209)==0]
        if not roots:
            raise ArithmeticError("A split auxiliary has no admissible integral root.")
        auxiliaries.append((-ell,min(roots)))
    used=[]
    projected=[]
    stack=None
    targets=None
    for auxiliary,root in auxiliaries:
        STAGE="RSST_auxiliary_%d"%(-auxiliary)
        result=enumerate_rows(packet["paths"],auxiliary,root)
        free=packet["free_path_count"]
        if any(any(row["values"][free:]) for row in result):
            raise ArithmeticError("A complete signed sum fails an elliptic path relation.")
        J=matrix(QQ,[[row["values"][j] for row in result] for j in range(free)])
        W=Einv*J.matrix_from_rows(piv)
        if E*W!=J:
            raise ArithmeticError("A signed functional fails an exact relative cohomology relation.")
        V=projection*reduce(W)
        reference=V.column(0)
        columns=[]
        v=reference
        for j in range(73):
            columns.append(v)
            v=H*v
        Krylov=matrix(k,columns).transpose()
        stack=Krylov if stack is None else stack.stack(Krylov)
        targets=V if targets is None else targets.stack(V)
        rank=int(stack.rank())
        if stack.augment(targets).rank()!=rank:
            raise ArithmeticError("Actual projected CM columns violate their q-integral Hecke relation.")
        stats=[{key:value for key,value in row.items() if key!="values"} for row in result]
        used.append(dict(auxiliary_discriminant=auxiliary,auxiliary_root=root,
                         projected_columns_sha256=digest(rows(V)),integer_path_sums=stats,
                         common_reference_rank=rank))
        projected.append(V)
        emit("completed_auxiliary",**used[-1])
        if rank==73:
            break
    if stack is None or stack.rank()!=73:
        raise ArithmeticError("The declared auxiliary set did not cover every original Hecke block.")

    reference_pivot_rows=list(stack.transpose().pivots())
    reference_minor=stack.matrix_from_rows(reference_pivot_rows)
    reference_determinant=int(reference_minor.det())
    if len(reference_pivot_rows)!=73 or not reference_determinant:
        raise ArithmeticError("The complete reference lacks its certified unit minor.")
    STAGE="new_complete_signed_coordinates"
    coefficients=stack.solve_right(targets)
    if stack*coefficients!=targets:
        raise ArithmeticError("The complete stacked Jacobi equation failed.")
    reference_polynomial=PR(list(coefficients.column(0)))
    if reference_polynomial!=PR.one():
        raise ArithmeticError("The actual Gaussian reference ratio is not one.")
    operator_polynomials={}
    for n,op in [(2,ops[2]),(3,ops[3]),(5,ops[5]),("Bq",Bq)]:
        right=vector(k,[a for V in projected for a in op*V.column(0)])
        solution=stack.solve_right(right)
        poly=PR(list(solution))
        if stack*solution!=right or evaluate(poly,H)!=op:
            raise ArithmeticError("A full Hecke polynomial reconstruction failed: "+str(n))
        operator_polynomials[n]=poly
    if (operator_polynomials[3]+operator_polynomials[5])%cp!=PR.gen():
        raise ArithmeticError("The actual H=T3+T5 convention changed.")
    bp=operator_polynomials["Bq"]
    if bp.gcd(cp)!=PR.one() or int(cp.resultant(bp))!=551:
        raise ArithmeticError("The Bq Hecke coordinate is not the consumed full unit.")
    binv=bp.inverse_mod(cp)

    STAGE="same_original_Hodge_coordinate_bridge"
    old=json.loads((ROOT/HEIGHT_INPUT).read_text())
    hodge=module("jacobi47_original_hodge",HODGE_SOURCE)
    source=hodge.build_source(descriptors=old["Hodge_descriptors"],
                              expected_certificate=old["Hodge_certificate"])
    bridge=hodge.hecke_bridge(source)
    Hodge=bridge["operators"][3]+bridge["operators"][5]
    if digest(rows(Hodge))!=req["Hodd_matrix_sha256"]:
        raise ArithmeticError("The consumed actual Hodge row matrix changed.")
    for n in (2,3,5):
        if (digest(rows(bridge["operators"][n]))!=old["original_Hecke_hashes"][str(n)] or
                evaluate(operator_polynomials[n],Hodge)!=bridge["operators"][n]):
            raise ArithmeticError("The signed coordinates do not use the actual original Hodge Hecke action.")
    if digest([int(a) for a in Hodge.charpoly().list()])!=req["Hodd_characteristic_polynomial_sha256"]:
        raise ArithmeticError("The actual Hodge polynomial changed.")
    check()
    bp_coefficients=[int(bp[j]) for j in range(73)]
    certificate=dict(
        method="R1119 signed weighted Jacobi coefficients on actual new Fricke-plus space",
        coefficient_prime=4513,prime=47,dimension=73,
        coordinate_convention="ascending powers of actual Hodd=T3+T5; Hecke polynomials",
        Hodd_characteristic_polynomial_sha256=req["Hodd_characteristic_polynomial_sha256"],
        Hodd_matrix_sha256=req["Hodd_matrix_sha256"],
        actual_Hodge_row_checks=[2,3,5],common_reference_rank=73,
        reference_pivot_rows=reference_pivot_rows,reference_minor_determinant=reference_determinant,
        reference_discriminant=-4,reference_pair=[-4*2209,0],
        auxiliaries=used,separating_Hecke_coefficients=chosen_separator,
        Bq_coefficients=bp_coefficients,Bq_coefficients_sha256=digest(bp_coefficients),
        Bq_determinant_mod_q=551,
        consumed_Tq_integer_charpoly_sha256=req["consumed_Tq_integer_charpoly_sha256"],
        exact_rational_path_relations=True,all_needed_denominators_q_units=True,
        path_count=packet["path_count"],free_path_count=packet["free_path_count"],
        pari_version=packet["pari_version"])
    for j,(D,identifier,units) in enumerate(zip((-4,-3,-7,-8),(141,0,76,108),(2,3,1,1))):
        ratio=(k(units)/k(2)*PR(list(coefficients.column(j))))%cp
        coordinate=(ratio*binv)%cp
        rlist=[int(ratio[z]) for z in range(73)]
        clist=[int(coordinate[z]) for z in range(73)]
        if (coordinate*bp-ratio)%cp:
            raise ArithmeticError("An actual CM coordinate lost its Bq normalization.")
        for V in projected:
            if evaluate(ratio,H)*V.column(0)!=(k(units)/k(2))*V.column(j):
                raise ArithmeticError("A weighted actual CM ratio fails a full reference block.")
        row=dict(candidate_id=identifier,fundamental_discriminant=D,
                 exact_divisor="23*y_%d-C_infty"%identifier,
                 weighted_Jacobi_pair=[D*2209,0 if D%2==0 else 2209],
                 source_coarse_weight=1,reverse_incidence_multiplicity=units,
                 ratio_to_u4_coefficients=rlist,ratio_to_u4_sha256=digest(rlist),
                 coordinate_relative_Bq_u4_coefficients=clist,
                 coordinate_relative_Bq_u4_sha256=digest(clist),
                 Hodd_characteristic_polynomial_sha256=req["Hodd_characteristic_polynomial_sha256"],
                 Bq_coefficients_sha256=certificate["Bq_coefficients_sha256"],
                 method="R1119",coefficient_prime=4513,dimension=73)
        RECORDS.append(row)
    # All four cases have passed the full common source, projection and Hodge bridge.
    for row in RECORDS:
        emit("actual_CM_Hecke_coordinate",**row)
    emit("complete",status="success",source_commit=SOURCE,request_sha256=REQUEST_HASH,
         completed_case_ids=[141,0,76,108],records_sha256=digest(RECORDS),
         certificate=certificate,certificate_sha256=digest(certificate),
         storage="No raw matrices, path arrays, artifacts or temporary data uploaded.")


if __name__=="__main__":
    try:
        main()
    except BaseException as exc:
        emit("failed",status="failed",stage=STAGE,source_commit=SOURCE,
             request_sha256=REQUEST_HASH,completed_records_sha256=digest(RECORDS),
             exception_type=type(exc).__name__,exception=str(exc))
        traceback.print_exc()
        raise
