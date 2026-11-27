#!/usr/bin/env python3
"""First actual level-47 CM height, using R1097--R1099 exact local formulas."""
import hashlib
import json
import os
from pathlib import Path
import signal
import sys
import time
import traceback
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[3]
PRE = "topics/serre-uniformity/"
REQUEST = ROOT/(PRE+"notes/full-p47-first-global-CM-height-request.json")
START = time.monotonic()
SOURCE = None
REQUEST_HASH = None
STAGE = "preflight"
COMPLETED = {}

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def emit(kind,**data):
    print(json.dumps(dict(kind=kind,elapsed_seconds=time.monotonic()-START,**data),
                     sort_keys=True),flush=True)

def stop(signum,frame):
    raise TimeoutError("The declared mathematical reserve has been reached.")

def source_head():
    gd=ROOT/".git"
    source=(gd/"HEAD").read_text().strip()
    if source.startswith("ref: "):
        ref=source[5:]
        if not ref.startswith("refs/") or ".." in ref.split("/"):
            raise RuntimeError("Unexpected checkout ref.")
        path=gd/ref
        if path.exists():
            source=path.read_text().strip()
        else:
            rows=[s.split(" ",1)[0] for s in (gd/"packed-refs").read_text().splitlines()
                  if s.endswith(" "+ref)]
            if len(rows)!=1:
                raise RuntimeError("Ambiguous actual checkout.")
            source=rows[0]
    if len(source)!=40 or source!=os.environ.get("GITHUB_SHA"):
        raise RuntimeError("Actual checkout/GITHUB_SHA mismatch.")
    return source

def exact_quotient(a,b,label):
    q,r=divmod(a,b)
    if r:
        raise ArithmeticError(label+" has a nonintegral contribution.")
    return q

class NormSums:
    def __init__(self):
        from sage.all import ZZ
        self.ZZ=ZZ
        self.cache={}
        self.factor_count=0

    def data(self,n):
        if n<=0:
            raise ValueError("Positive norm required.")
        if n not in self.cache:
            factors=tuple((int(p),int(e)) for p,e in
                          self.ZZ(n).factor(algorithm="pari",proof=True))
            product=1
            r_split=4
            inert=[]
            for p,e in factors:
                product*=p**e
                if p%4==1:
                    r_split*=e+1
                elif p%4==3 and e%2:
                    inert.append((p,e))
            if product!=n:
                raise ArithmeticError("Factorization product mismatch.")
            self.cache[n]=(r_split if not inert else 0,tuple(inert),r_split,factors)
            self.factor_count+=1
        return self.cache[n]

    def r2(self,n):
        if n==0:
            return 1
        return self.data(n)[0]

    def odd_good(self,m):
        """Both disjoint 2209 progressions; output excludes 2,47 and q=4513."""
        raw=defaultdict(int)
        contributions=[]
        bound=(8*m-1)//2209
        for s in range(1,bound+1):
            if s%4==0:
                continue
            large=8*m-2209*s
            rs,inert_s,split_s,_=self.data(s)
            # First branch A=2209*s, B=large.
            if rs:
                _,inert_b,split_b,_=self.data(large)
                if len(inert_b)==1:
                    ell,e=inert_b[0]
                    if ell not in (47,4513):
                        value=exact_quotient(rs*split_b*(e+1),16,"odd first branch")
                        raw[ell]+=value
                        contributions.append([s,0,ell,value])
            # Second branch A=large, B=2209*s.
            # Adding 47^2 changes no odd inert valuation; ell=47 is treated separately.
            if len(inert_s)==1:
                ell,e=inert_s[0]
                if ell not in (47,4513):
                    ra=self.r2(large)
                    if ra:
                        value=exact_quotient(ra*split_s*(e+1),16,"odd second branch")
                        raw[ell]+=value
                        contributions.append([s,1,ell,value])
        rows=[[ell,raw[ell]] for ell in sorted(raw) if raw[ell]]
        return dict(rows),{
            "m":m,"progression_limit":bound,
            "nonzero_norm_contributions":len(contributions),
            "local_prime_count":len(rows),
            "local_intersection_sum":sum(v for ell,v in rows),
            "largest_local_prime":max(raw,default=None),
            "local_rows_sha256":digest(rows),
            "norm_contributions_sha256":digest(contributions)}

    def dyadic(self,m):
        even_sum=0
        half_sum=0
        contributions=[]
        for s in range(m//2209+1):
            value=self.r2(s)*self.r2(m-2209*s)
            even_sum+=value
            if value:
                contributions.append([s,0,value])
        for s in range(2,(4*m-1)//2209+1,4):
            value=self.r2(s)*self.r2(4*m-2209*s)
            half_sum+=value
            if value:
                contributions.append([s,1,value])
        G=exact_quotient(even_sum+half_sum,4,"dyadic total")
        return G,{"m":m,"G2":G,"integer_lattice_numerator":even_sum,
                  "half_lattice_numerator":half_sum,
                  "norm_contributions_sha256":digest(contributions)}

    def bad_horizontal(self,m):
        total=0
        contributions=[]
        for t in range(1,(8*m-1)//(47**3)+1):
            if t%4==0:
                continue
            a=8*m-(47**3)*t
            numerator=self.r2(t)*self.r2(a)
            if not numerator:
                continue
            v=0
            reduced=t
            while reduced%47==0:
                v+=1
                reduced//=47
            value=exact_quotient(numerator*(2+v),16,"bad47 horizontal")
            total+=value
            contributions.append([t,value])
        return total,{"m":m,"H47":total,
                      "nonzero_norm_contributions":len(contributions),
                      "norm_contributions_sha256":digest(contributions)}

    def bad_brandt_entry(self,m):
        """Small-index independent normalization check; never run at q^2."""
        total=0
        for c in range(1,(8*m-1)//47+1):
            a=8*m-47*c
            if a%4:
                total+=exact_quotient(self.r2(a)*self.r2(c),16,
                                      "bad47 Brandt norm entry")
        return total

def integral_rows(M):
    return [[int(x) for x in row] for row in M.rows()]

def brandt_bad47(q,norms):
    from sage.all import BrandtModule, ZZ, vector, identity_matrix, diagonal_matrix
    B=BrandtModule(47)
    if B.dimension()!=5:
        raise ArithmeticError("Wrong original supersingular dimension.")
    weights=[int(w) for w in B.monodromy_weights()]
    if sorted(weights)!=[1,1,1,2,3]:
        raise ArithmeticError("Wrong original supersingular weights.")
    i4=weights.index(2)
    M2=B.hecke_matrix(2,algorithm="brandt").change_ring(ZZ)
    e4=vector(ZZ,[int(i==i4) for i in range(5)])
    v16=vector(ZZ,(e4*M2-e4)/2)
    entries=list(v16)
    if sorted(entries)!=[0,0,0,0,1] or entries[i4]!=0:
        raise ArithmeticError("The literal original T2 CM relation did not mark E16.")
    i16=entries.index(1)
    H=B.hecke_matrix(q,algorithm="brandt").change_ring(ZZ)
    W=diagonal_matrix(ZZ,weights)
    I=identity_matrix(ZZ,5)
    if any(sum(row)!=q+1 for row in H.rows()):
        raise ArithmeticError("Brandt row degree convention failed.")
    if H*W!=W*H.transpose() or H*M2!=M2*H:
        raise ArithmeticError("Brandt weighted self-adjointness/commutation failed.")
    Hq2=H*H-q*I
    if any(sum(row)!=q*q+q+1 for row in Hq2.rows()):
        raise ArithmeticError("The full noncyclic q^2 Hecke degree failed.")
    b1=int(v16[i4])
    bq=int((v16*H)[i4])
    bq2=int((v16*Hq2)[i4])
    norm_bq=norms.bad_brandt_entry(q)
    if norm_bq!=bq:
        raise ArithmeticError("Actual Brandt direction disagrees with the norm formula.")
    move=(q+1)*I-H
    moved=int((v16*move*move)[i4])
    if moved!=(q*q+3*q+1)*b1-2*(q+1)*bq+bq2:
        raise ArithmeticError("Full Bq square lost a noncyclic term.")
    return [b1,bq,bq2],{
        "basis_dimension":5,"weights":weights,
        "E4_basis_index":i4,"E16_basis_index":i16,
        "T2_sha256":digest(integral_rows(M2)),
        "Tq_sha256":digest(integral_rows(H)),
        "Tq2_sha256":digest(integral_rows(Hq2)),
        "b_1":b1,"b_q":bq,"b_q2":bq2,
        "b_q_norm_check":norm_bq,"Bq_squared_entry":moved}

def fermat_quotient(ell,q):
    if ell%q==0:
        raise ArithmeticError("The coefficient prime is not a non-q local term.")
    residue=pow(ell,q-1,q*q)
    return exact_quotient(residue-1,q,"Fermat quotient")%q

def main():
    global SOURCE, REQUEST_HASH, STAGE
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get(
            "GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise RuntimeError("Only this public repository's Actions may execute mathematics.")
    raw=REQUEST.read_bytes()
    REQUEST_HASH=hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH!=os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("Request pin mismatch.")
    req=json.loads(raw)
    if (req["execution_id"]!="full-p47-first-global-CM-height-v1" or
        req["prime"]!=47 or req["coefficient_prime"]!=4513 or
        req["hecke_indices"]!=[1] or req["total_seconds"]!=900 or
        req["reserve_seconds"]!=30 or req["sage_version"]!="10.6"):
        raise RuntimeError("Unexpected finite request.")
    for name,wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=wanted:
            raise RuntimeError("Source pin mismatch: "+name)
    SOURCE=source_head()
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,870-(time.monotonic()-START)))
    emit("preflight",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,source_sha256=req["source_sha256"])
    from sage.all import ZZ, proof
    from sage.env import SAGE_VERSION
    if SAGE_VERSION!="10.6":
        raise RuntimeError("Wrong Sage version.")
    proof.all(True)
    q=4513
    if not ZZ(q).is_prime(proof=True):
        raise ArithmeticError("Coefficient prime failed.")
    norms=NormSums()
    STAGE="new_bad47_Brandt"
    b,brand=brandt_bad47(q,norms)
    COMPLETED["bad47_Brandt"]=brand
    emit("new_bad47_Brandt_certificate",**brand)
    indices=[1,q,q*q]
    odd=[]
    dyadic=[]
    bad=[]
    local_records=[]
    for m in indices:
        STAGE="new_local_norm_sums_m_"+str(m)
        od,ro=norms.odd_good(m)
        g2,r2=norms.dyadic(m)
        h47,r47=norms.bad_horizontal(m)
        odd.append(od)
        dyadic.append(g2)
        bad.append(h47)
        record={"m":m,"odd_good":ro,"dyadic":r2,"bad47_horizontal":r47}
        local_records.append(record)
        COMPLETED["local_norm_sums"]=list(local_records)
        emit("new_local_norm_sum_certificate",**record)
    if (dyadic[0],bad[0],bad[1],b[0],odd[0])!=(1,0,0,0,{}):
        raise ArithmeticError("The proved base cases were not respected.")
    STAGE="new_first_global_height"
    coefficients=[q*q+3*q+1,-2*(q+1),1]
    local=defaultdict(int)
    for c,d in zip(coefficients,odd):
        for ell,g in d.items():
            local[ell]+=23**2*c*g
    local[2]=23**2*sum(c*g for c,g in zip(coefficients,dyadic))
    local[47]=23**2*sum(c*h for c,h in zip(coefficients,bad))+23*sum(
        c*t for c,t in zip(coefficients,b))
    rows=[]
    parts={"dyadic":0,"bad47":0,"odd_good":0}
    for ell in sorted(local):
        if local[ell]==0:
            continue
        fq=fermat_quotient(ell,q)
        value=(local[ell]%q)*fq%q
        rows.append([ell,local[ell],fq,value])
        category="dyadic" if ell==2 else "bad47" if ell==47 else "odd_good"
        parts[category]=(parts[category]+value)%q
    gamma=sum(parts.values())%q
    result={"prime":47,"coefficient_prime":q,"hecke_index":1,
            "definition":"q^(-1) h(Bq u4, Bq u16) mod q",
            "Gamma_1_mod4513":gamma,"Gamma_1_nonzero":bool(gamma),
            "local_contributions_mod4513":parts,
            "I2_exact":local[2],"I47_exact":local[47],
            "local_prime_count":len(rows),
            "largest_local_prime":max(local,default=None),
            "full_local_height_rows_sha256":digest(rows),
            "factorizations_performed":norms.factor_count,
            "q_local_divisible_by_q_squared_source":"R1094 and R1096",
            "all_73_block_units_claimed":False}
    COMPLETED["first_global_height"]=result
    emit("new_first_global_height_certificate",**result)
    signal.setitimer(signal.ITIMER_REAL,0)
    STAGE="completed"
    emit("receipt",status="complete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,completed=COMPLETED,result_sha256=digest(COMPLETED),
         scope="First actual original level-47 CM height. No full-height-matrix unit or rational-point classification claim.")

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
