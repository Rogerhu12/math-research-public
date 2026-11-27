#!/usr/bin/env python3
"""Full original level-47 first height layer in a certified small odd Hecke basis."""
import hashlib
import importlib.util
import json
import math
import multiprocessing
import os
from pathlib import Path
import signal
import sys
import time
import traceback
from array import array

ROOT=Path(__file__).resolve().parents[3]
PRE="topics/serre-uniformity/"
REQUEST=ROOT/(PRE+"notes/full-p47-complete-global-CM-height-request.json")
START=time.monotonic()
SOURCE=None
REQUEST_HASH=None
STAGE="preflight"
COMPLETED={}
SMALL_SPF=None
SMALL_BOUND=0
BAD_VERTICAL={}
COEFFICIENT_PRIME=4513

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def emit(kind,**data):
    print(json.dumps(dict(kind=kind,elapsed_seconds=time.monotonic()-START,**data),
                     sort_keys=True),flush=True)

def stop(signum,frame):
    raise TimeoutError("The declared mathematical reserve has been reached.")

def import_source(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def exact_quotient(a,b,label):
    result,remainder=divmod(a,b)
    if remainder:
        raise ArithmeticError(label+" is not integral.")
    return result

class StreamHash:
    """Exactly SHA256 of the compact JSON list, without retaining its elements."""
    def __init__(self):
        self.hash=hashlib.sha256(b"[")
        self.count=0
    def add(self,row):
        if self.count:
            self.hash.update(b",")
        self.hash.update(json.dumps(row,separators=(",",":")).encode())
        self.count+=1
    def finish(self):
        result=self.hash.copy()
        result.update(b"]")
        return result.hexdigest()

class StreamNorms:
    def __init__(self):
        from sage.all import ZZ
        self.ZZ=ZZ
        self.cache={}
        self.fermat_cache={}
        self.small_factorizations=0
        self.large_factorizations=0

    def data(self,n):
        if n<=0:
            raise ValueError("Positive norm required.")
        cached=self.cache.get(n)
        if cached is not None:
            return cached
        factors=[]
        if n<=SMALL_BOUND:
            remaining=n
            while remaining>1:
                p=int(SMALL_SPF[remaining]) or remaining
                exponent=0
                while remaining%p==0:
                    remaining//=p
                    exponent+=1
                factors.append((p,exponent))
            self.small_factorizations+=1
        else:
            factors=[(int(p),int(e)) for p,e in
                     self.ZZ(n).factor(algorithm="pari",proof=True)]
            self.large_factorizations+=1
        product=1
        split=4
        inert=[]
        for p,e in factors:
            product*=p**e
            if p%4==1:
                split*=e+1
            elif p%4==3 and e%2:
                inert.append((p,e))
        if product!=n:
            raise ArithmeticError("Exact factorization product mismatch.")
        value=(split if not inert else 0,tuple(inert),split)
        if len(self.cache)>=65536:
            self.cache.clear()
        self.cache[n]=value
        return value

    def r2(self,n):
        return 1 if n==0 else self.data(n)[0]

    def fq(self,ell):
        if ell==COEFFICIENT_PRIME:
            raise ArithmeticError("Coefficient prime appeared in the non-q sum.")
        cached=self.fermat_cache.get(ell)
        if cached is not None:
            return cached
        q=COEFFICIENT_PRIME
        value=exact_quotient(pow(ell,q-1,q*q)-1,q,"Fermat quotient")%q
        if len(self.fermat_cache)>=65536:
            self.fermat_cache.clear()
        self.fermat_cache[ell]=value
        return value

    def odd_good_weighted(self,m):
        """Sum G_ell(m)*Fermat_q(ell) modulo q, retaining all norm terms."""
        q=COEFFICIENT_PRIME
        value=0
        unweighted=0
        trace=StreamHash()
        for s in range(1,(8*m-1)//2209+1):
            if s%4==0:
                continue
            large=8*m-2209*s
            rs,inert_s,split_s=self.data(s)
            if rs:
                _,inert_b,split_b=self.data(large)
                if len(inert_b)==1:
                    ell,e=inert_b[0]
                    if ell not in (47,q):
                        term=exact_quotient(rs*split_b*(e+1),16,"odd first branch")
                        value=(value+term*self.fq(ell))%q
                        unweighted+=term
                        trace.add([s,0,ell,term])
            if len(inert_s)==1:
                ell,e=inert_s[0]
                if ell not in (47,q):
                    ra=self.r2(large)
                    if ra:
                        term=exact_quotient(ra*split_s*(e+1),16,"odd second branch")
                        value=(value+term*self.fq(ell))%q
                        unweighted+=term
                        trace.add([s,1,ell,term])
        return value,{"m":m,"contributions":trace.count,
                      "unweighted_sum":unweighted,"sha256":trace.finish()}

    def dyadic(self,m):
        numerator=0
        trace=StreamHash()
        for s in range(m//2209+1):
            term=self.r2(s)*self.r2(m-2209*s)
            numerator+=term
            if term:
                trace.add([s,0,term])
        for s in range(2,(4*m-1)//2209+1,4):
            term=self.r2(s)*self.r2(4*m-2209*s)
            numerator+=term
            if term:
                trace.add([s,1,term])
        return exact_quotient(numerator,4,"dyadic total"),trace.finish()

    def bad_horizontal(self,m):
        value=0
        trace=StreamHash()
        for t in range(1,(8*m-1)//(47**3)+1):
            if t%4==0:
                continue
            numerator=self.r2(t)*self.r2(8*m-(47**3)*t)
            if not numerator:
                continue
            v=0
            remaining=t
            while remaining%47==0:
                v+=1
                remaining//=47
            term=exact_quotient(numerator*(2+v),16,"bad47 horizontal")
            value+=term
            trace.add([t,term])
        return value,trace.finish()

def make_small_sieve(bound):
    """Zero entries beyond 1 are prime; others contain the smallest prime factor."""
    from sage.all import prime_range
    if bound<1 or bound>=2**32:
        raise ArithmeticError("Unexpected certified finite sieve range.")
    table=array("I",[0])*(bound+1)
    if table.itemsize!=4:
        raise RuntimeError("The exact sieve requires 32-bit unsigned entries.")
    for pp in prime_range(math.isqrt(bound)+1):
        p=int(pp)
        for multiple in range(p*p,bound+1,p):
            if table[multiple]==0:
                table[multiple]=p
    return table

def initialize_worker():
    signal.setitimer(signal.ITIMER_REAL,0)

def height_worker(n):
    start=time.monotonic()
    q=COEFFICIENT_PRIME
    if n%2==0 or n%47==0 or n>=q:
        raise ArithmeticError("Index outside the proved original odd-height scope.")
    norms=StreamNorms()
    coefficients=[q*q+3*q+1,-2*(q+1),1]
    odd=0
    dyadic=0
    horizontal=0
    local_work=[]
    for c,m in zip(coefficients,[n,n*q,n*q*q]):
        go,go_meta=norms.odd_good_weighted(m)
        g2,g2_hash=norms.dyadic(m)
        h47,h47_hash=norms.bad_horizontal(m)
        odd=(odd+c*go)%q
        dyadic+=c*g2
        horizontal+=c*h47
        local_work.append({"m":m,"odd":go_meta,"G2":g2,"G2_sha256":g2_hash,
                           "H47":h47,"H47_sha256":h47_hash})
    parts={"odd_good":23**2*odd%q,
           "dyadic":23**2*dyadic*norms.fq(2)%q,
           "bad47":(23**2*horizontal+23*BAD_VERTICAL[n])*norms.fq(47)%q}
    gamma=sum(parts.values())%q
    return {"n":n,"Gamma_mod4513":gamma,"parts":parts,
            "norm_work_sha256":digest(local_work),
            "norm_term_counts":[row["odd"]["contributions"] for row in local_work],
            "elapsed_seconds":time.monotonic()-start}

def matrix_rows(M):
    return [[int(c) for c in row] for row in M.rows()]

def consume_bad47_source(indices,req):
    from sage.all import BrandtModule,ZZ,vector,identity_matrix,diagonal_matrix
    q=COEFFICIENT_PRIME
    module=BrandtModule(47)
    if module.dimension()!=5:
        raise ArithmeticError("Wrong original bad47 source.")
    weights=[int(w) for w in module.monodromy_weights()]
    if weights!=req["original_Brandt"]["weights"]:
        raise ArithmeticError("The original Brandt basis changed.")
    i4=weights.index(2)
    M2=module.hecke_matrix(2,algorithm="brandt").change_ring(ZZ)
    Hq=module.hecke_matrix(q,algorithm="brandt").change_ring(ZZ)
    for name,M in [("T2_sha256",M2),("Tq_sha256",Hq)]:
        if digest(matrix_rows(M))!=req["original_Brandt"][name]:
            raise ArithmeticError("Original Brandt hash mismatch: "+name)
    e4=vector(ZZ,[int(i==i4) for i in range(5)])
    v16=vector(ZZ,(e4*M2-e4)/2)
    if list(v16).index(1)!=req["original_Brandt"]["E16_basis_index"]:
        raise ArithmeticError("Original E16 labeling mismatch.")
    I=identity_matrix(ZZ,5)
    W=diagonal_matrix(ZZ,weights)
    move=(q+1)*I-Hq
    moved=v16*move*move
    outputs={}
    rows=[]
    for n in indices:
        Hn=module.hecke_matrix(n,algorithm="brandt").change_ring(ZZ)
        degree=int(sum(ZZ(n).divisors()))
        if any(sum(row)!=degree for row in Hn.rows()):
            raise ArithmeticError("A full Hn row lost noncyclic kernel multiplicity.")
        if Hn*W!=W*Hn.transpose() or Hn*Hq!=Hq*Hn:
            raise ArithmeticError("Actual Hn Brandt convention failed.")
        outputs[n]=int((moved*Hn)[i4])
        rows.append([n,outputs[n],digest(matrix_rows(Hn))])
    return outputs,{"basis_dimension":5,"input_hashes":req["original_Brandt"],
                    "all_selected_entries_sha256":digest(rows)}

def recover_height_algebra(basis,values,source_request):
    from sage.all import matrix,vector,PolynomialRing
    P=basis["polynomial"]
    field=P.base_ring()
    PR=P.parent()
    d=int(P.degree())
    C=basis["coordinate_matrix"]
    indices=basis["indices"]
    if d!=73 or C.nrows()!=73 or C.ncols()!=73:
        raise ArithmeticError("Incomplete original integral height basis.")
    g=vector(field,[values[n] for n in indices])
    moments=C.solve_right(g)
    if C*moments!=g:
        raise ArithmeticError("Actual Hecke-height coordinate solve failed.")
    # Newton's identities compute Tr(h^r), including Tr(1)=73.
    traces=[field(d)]
    for k in range(1,2*d-1):
        if k<=d:
            traces.append(-sum((P[d-j]*traces[k-j] for j in range(1,k)),
                               field(0))-field(k)*P[d-k])
        else:
            traces.append(-sum((P[d-j]*traces[k-j] for j in range(1,d+1)),
                               field(0)))
    Gram=matrix(field,[[traces[i+j] for j in range(d)] for i in range(d)])
    if Gram.det()!=field(2650) or Gram.det()!=P.discriminant():
        raise ArithmeticError("The actual etale trace Gram lost its original unit.")
    coeff=Gram.solve_right(moments)
    kappa=PR(list(coeff))
    if Gram*coeff!=moments:
        raise ArithmeticError("The actual trace-dual height solve failed.")
    resolvent=PR([sum((moments[j]*P[i+j+1] for j in range(d-i)),field(0))
                  for i in range(d)])
    kappa_resolvent=(resolvent*P.derivative().inverse_mod(P))%P
    if kappa_resolvent!=kappa:
        raise ArithmeticError("Independent resolvent trace-dual normalization failed.")
    p2=basis["hecke_polynomials"][2]
    p3=basis["hecke_polynomials"][3]
    p5=basis["hecke_polynomials"][5]
    a=((p2-1)/field(2))%P
    if a.gcd(P).degree()!=0:
        raise ArithmeticError("The paid CM moving unit changed.")
    w=(kappa*a.inverse_mod(P))%P
    height_norm=P.resultant(w)
    determinant=Gram.det()*height_norm
    factors=sorted([f.monic() for f,e in P.factor()],
                   key=lambda f:(int(f.degree()),tuple(int(c) for c in f.list())))
    if sum(int(f.degree()) for f in factors)!=73:
        raise ArithmeticError("Incomplete residue-factor collection.")
    blocks=[]
    normalized=[]
    old_rows={int(r["H2_eigenvalue"]):r
              for r in source_request["original_CM_linear_rows"]}
    H2pol=(p2+2*p3+4*p5)%P
    for f in factors:
        residue=kappa%f
        norm=f.resultant(residue)
        row={"degree":int(f.degree()),"factor_sha256":digest([int(c) for c in f.list()]),
             "kappa_norm":int(norm),"kappa_nonzero":bool(residue),
             "kappa_residue_sha256":digest([int(c) for c in residue.list()])}
        blocks.append(row)
        if f.degree()==1:
            root=-f[0]
            h2=int(H2pol(root))
            if h2 not in old_rows:
                raise ArithmeticError("A linear height block lacks the paid original CM log.")
            old=old_rows[h2]
            lam=field(old["q_inverse_log_Bq_u1728"])
            if not lam:
                raise ArithmeticError("The paid original CM first log is no longer a unit.")
            mu=w(root)/(lam*lam)
            normalized.append({"Hodd_eigenvalue":int(root),"H2_eigenvalue":h2,
                "kappa":int(kappa(root)),"CM_moving_a":int(a(root)),
                "CM_first_log":int(lam),"normalized_height_mu":int(mu),
                "eigenform_coordinates_sha256":old["eigenform_coordinates_sha256"]})
    if len(normalized)!=16 or {x["H2_eigenvalue"] for x in normalized}!=set(old_rows):
        raise ArithmeticError("The sixteen original normalized linear blocks were not all paid.")
    gcd_degree=int(kappa.gcd(P).degree())
    all_units=all(row["kappa_nonzero"] for row in blocks)
    if all_units!=(gcd_degree==0) or all_units!=bool(determinant):
        raise ArithmeticError("Equivalent full-height unit tests disagree.")
    return {
        "dimension":73,"basis_indices":indices,
        "height_values_sha256":digest([[n,values[n]] for n in indices]),
        "Hodd_height_moments_sha256":digest([int(c) for c in moments]),
        "trace_Gram_sha256":digest(matrix_rows(Gram)),
        "kappa_coefficients_sha256":digest([int(c) for c in coeff]),
        "resolvent_numerator_sha256":digest([int(c) for c in resolvent.list()]),
        "trace_and_resolvent_agree":True,
        "kappa_gcd_degree":gcd_degree,"all_28_blocks_are_units":all_units,
        "normalized_full_height_determinant_mod4513":int(determinant),
        "full_height_multiplier_norm":int(height_norm),
        "blocks":blocks,"normalized_linear_heights":sorted(normalized,key=lambda x:x["H2_eigenvalue"]),
        "scope":"Full original first height layer in the actual MW lattice; no disk uniqueness claim."}

def main():
    global SOURCE,REQUEST_HASH,STAGE,SMALL_SPF,SMALL_BOUND,BAD_VERTICAL
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get(
            "GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise RuntimeError("Only this public repository's Actions may execute mathematics.")
    raw=REQUEST.read_bytes()
    REQUEST_HASH=hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH!=os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("Request pin mismatch.")
    req=json.loads(raw)
    if (req["execution_id"]!="full-p47-complete-global-CM-height-v1" or
        req["prime"]!=47 or req["coefficient_prime"]!=4513 or
        req["workers"]!=4 or req["total_seconds"]!=18000 or
        req["reserve_seconds"]!=120 or req["sage_version"]!="10.6"):
        raise RuntimeError("Unexpected finite complete-height request.")
    for name,wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=wanted:
            raise RuntimeError("Source pin mismatch: "+name)
    first=import_source("first_height_source",PRE+"scripts/full_p47_first_global_CM_height.py")
    SOURCE=first.source_head()
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,17880-(time.monotonic()-START)))
    emit("preflight",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,workers=4,
         consumed_first_height_run=req["consumed_first_height_run"])
    from sage.all import proof
    from sage.env import SAGE_VERSION
    if SAGE_VERSION!="10.6":
        raise RuntimeError("Wrong pinned Sage version.")
    proof.all(True)
    STAGE="consume_actual_small_odd_basis"
    module=import_source("small_odd_source",PRE+"scripts/full_p47_small_odd_Hecke_basis.py")
    # Rebuild only the certified indices; never reopen the greedy basis search.
    basis=module.build_basis(req["basis_request"],indices=req["basis_indices"],
                             expected_certificate=req["basis_certificate"])
    indices=basis["indices"]
    if indices!=req["basis_indices"] or len(indices)!=73 or 1 not in indices:
        raise ArithmeticError("Incomplete certified original odd basis.")
    COMPLETED["basis"]=basis["certificate"]
    emit("original_basis_consumed",certificate=basis["certificate"])
    STAGE="consume_original_bad47_source"
    BAD_VERTICAL,bad_meta=consume_bad47_source(indices,req)
    COMPLETED["bad47_source"]=bad_meta
    emit("bad47_source_consumed",certificate=bad_meta)
    prior={int(n):int(v) for n,v in req["certified_prior_heights"].items()}
    if prior!={1:818}:
        raise RuntimeError("Unexpected old-height input.")
    values=dict(prior)
    COMPLETED["height_values"]=dict(values)
    todo=sorted([n for n in indices if n not in prior],reverse=True)
    STAGE="new_all_selected_norm_heights"
    SMALL_BOUND=(8*max(todo)*4513**2-1)//2209
    SMALL_SPF=make_small_sieve(SMALL_BOUND)
    emit("new_norm_work_started",new_index_count=len(todo),small_factor_bound=SMALL_BOUND,
         indices_sha256=digest(todo),sieve_bytes=(SMALL_BOUND+1)*4)
    pool=multiprocessing.get_context("fork").Pool(4,initializer=initialize_worker)
    try:
        for result in pool.imap_unordered(height_worker,todo,chunksize=1):
            n=result["n"]
            if n in values:
                raise ArithmeticError("A certified index was computed twice.")
            values[n]=result["Gamma_mod4513"]
            COMPLETED["height_values"]=dict(values)
            emit("new_height_value",**result,completed_new_indices=len(values)-1)
        pool.close()
        pool.join()
    except BaseException:
        pool.terminate()
        pool.join()
        raise
    if set(values)!=set(indices):
        raise ArithmeticError("Not all certified height indices completed.")
    STAGE="new_full_height_trace_dual"
    source_request=json.loads((ROOT/req["original_CM_request_path"]).read_text())
    algebra=recover_height_algebra(basis,values,source_request)
    COMPLETED["height_algebra"]=algebra
    emit("new_full_height_certificate",**algebra)
    signal.setitimer(signal.ITIMER_REAL,0)
    STAGE="completed"
    emit("receipt",status="complete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,completed=COMPLETED,result_sha256=digest(COMPLETED),
         scope="Complete first height layer. Degenerate blocks are valid output; the Serre main goal is not declared complete.")

if __name__=="__main__":
    try:
        main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("receipt",status="incomplete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
             request_sha256=REQUEST_HASH,stage=STAGE,completed=COMPLETED,
             exception_type=type(exc).__name__,message=str(exc))
        traceback.print_exc()
        sys.exit(1)
