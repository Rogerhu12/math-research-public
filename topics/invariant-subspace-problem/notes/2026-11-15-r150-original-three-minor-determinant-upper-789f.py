#!/usr/bin/env python3
"""R150: at most three exact 22-row determinant upper certificates.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-15 UTC.
Only consumes the paid original 56 x 22 polynomial core. All arrays and
polynomial coefficients remain temporary. No row-module equality is claimed.
Official python-flint 0.9.0 scalar APIs:
https://python-flint.readthedocs.io/en/latest/fmpz_poly.html
https://python-flint.readthedocs.io/en/latest/fmpq_poly.html
https://python-flint.readthedocs.io/en/latest/fmpz_mat.html

A complete fraction-free pivot is a transaction. An interrupted pending pivot
does not replace the prior matrix or its two-slot checkpoint. All divisions
are exact in Z[s]. A field profile selects nonzero minors only; it never
certifies the characteristic-zero maximal-minor gcd.
"""
import argparse
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
import sys
import time

from flint import fmpq, fmpq_poly, fmpz_poly, fmpz_mat

FORMAT = "r150-three-original-minor-determinant-upper-v1"
CORE_SOURCE = {"bytes":34432,
 "sha256":"727175cf485a8ba5b5146a4cc6e749962e109c9e42265a2dd45f58cecdf933fb"}
CORE_BINDING = "ce358eac629541da0c9d35fd29c66424fa0d89ded97cfec93f324cf56e9d16ba"
CORE_STORED = {"bytes":1394807,
 "sha256":"8693870cd23a4693d840d2d27bc1e0676ff4b8253a2b9c85e7b3c267a8199a82"}
CORE_PAYLOAD_SHA = "efdb8a0cff5626575fb1e667c5753cf82dc040d0a3598444d61f5452db1d67a5"
CORE_LOGICAL_SHA = "752d21d7ca74ee5235c05ade9048ef48f120891c567abfb5132a4b2b33b745c8"
CORE_FILE = "polynomial-core-" + CORE_PAYLOAD_SHA + ".json.gz"
PROFILE_PRIME = 65521
PROFILE_POINTS = (4,3,5)
SEED = "R150-original56-three-minors-789f-v1"
FACTORS = [[0,1],[-2,1],[6,1],[-8,32,-25,5],
 [864,864,135,5],[9600,-25472,-3392,15936,-2888,-936,153,50,5]]
STOP = False
DEADLINE = float("inf")
ZERO = fmpz_poly([])
ONE = fmpz_poly([1])

class BudgetStop(Exception):
    pass

def require(value, message):
    if not value:
        raise AssertionError(message)

def tick():
    if STOP or time.monotonic() >= DEADLINE:
        raise BudgetStop("Reached a safe boundary; last complete pivot retained")

def canonical(obj):
    return json.dumps(obj, sort_keys=True, ensure_ascii=True,
                      separators=(",",":")).encode("ascii")

def digest(data):
    return hashlib.sha256(data).hexdigest()

def file_id(path):
    hh=hashlib.sha256(); nn=0
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""):
            hh.update(b); nn+=len(b)
    return {"bytes":nn,"sha256":hh.hexdigest()}

def atomic_bytes(path,data):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".pending-"+str(os.getpid()))
    with tmp.open("wb") as f:
        f.write(data);f.flush();os.fsync(f.fileno())
    os.replace(tmp,path)

def atomic_json(path,obj):
    atomic_bytes(path,canonical(obj))

def temporary_gzip(path,obj):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    data=canonical(obj)
    tmp=path.with_name(path.name+".pending-"+str(os.getpid()))
    with tmp.open("wb") as raw:
        with gzip.GzipFile(filename="",fileobj=raw,mode="wb",
                          compresslevel=1,mtime=0) as f:
            f.write(data)
        raw.flush();os.fsync(raw.fileno())
    os.replace(tmp,path)
    return dict(file_id(path),file=path.name,payloadSHA256=digest(data),
                temporaryOnly=True)

def read_gzip(path,record):
    require(file_id(path)=={"bytes":record["bytes"],"sha256":record["sha256"]},
            "Temporary file bytes and SHA256")
    with gzip.open(path,"rb") as f:
        raw=f.read()
    require(digest(raw)==record["payloadSHA256"],"Temporary exact payload SHA256")
    return json.loads(raw)

def zp(p):
    return [str(c) for c in p.coeffs()]

def uzp(v):
    return fmpz_poly([int(c) for c in v])

def zm(A):
    return [[zp(p) for p in row] for row in A]

def uzm(A):
    return [[uzp(p) for p in row] for row in A]

def mh(A):
    return digest(canonical(zm(A)))

def polynomial_stats(p):
    return {"degree":int(p.degree()),"coefficientCount":len(p.coeffs()),
            "maximumCoefficientBits":int(p.height_bits()),
            "coefficientSHA256":digest(canonical(zp(p)))}

def matrix_stats(A):
    arr=[p for row in A for p in row if p]
    return {"shape":[len(A),len(A[0]) if A else 0],
            "nonzeroPolynomials":len(arr),
            "maximumDegree":max([int(p.degree()) for p in arr],default=-1),
            "maximumCoefficientBits":max([int(p.height_bits()) for p in arr],default=0),
            "logicalSHA256":mh(A)}

def exact_divide(a,b):
    require(bool(b),"Nonzero Bareiss divisor")
    q,r=divmod(a,b)
    require(not r,"Every Bareiss polynomial division has exactly zero remainder")
    require(q*b==a,"Exact quotient multiplication")
    return q

def primitive_positive(p):
    require(bool(p),"Primitive part of nonzero polynomial")
    q=exact_divide(p,fmpz_poly([int(p.content())]))
    if int(q.leading_coefficient())<0:
        q=-q
    return q

def strip_known(p):
    q=primitive_positive(p); vv=[]
    for fc in FACTORS:
        f=fmpz_poly(fc); e=0
        while q and int(q.degree())>=int(f.degree()):
            tick()
            z,r=divmod(q,f)
            if r:
                break
            require(z*f==q,"Known-support exact quotient multiplication")
            q=z;e+=1
        vv.append(e)
    q=primitive_positive(q)
    require(all(int(q.gcd(fmpz_poly(f)).degree())==0 for f in FACTORS),
            "Candidate coprime to every known support factor")
    return q,vv

def polynomial_eval_mod(p,x,prime):
    v=0
    for c in reversed(p.coeffs()):
        v=(v*x+int(c))%prime
    return v

def integer_eval(p,x):
    v=0
    for c in reversed(p.coeffs()):
        v=v*x+int(c)
    return v

def row_basis(rows,order,prime):
    basis={};chosen=[]
    for i in order:
        v=[int(a)%prime for a in rows[i]]
        for k in sorted(basis):
            q=v[k]
            if q:
                v=[(a-q*b)%prime for a,b in zip(v,basis[k])]
        pivot=next((j for j,a in enumerate(v) if a),None)
        if pivot is not None:
            inv=pow(v[pivot],-1,prime)
            basis[pivot]=[(a*inv)%prime for a in v]
            chosen.append(i)
            if len(chosen)==22:
                break
    return chosen

def det_mod(M,prime):
    A=[[int(a)%prime for a in row] for row in M]
    n=len(A);out=1
    for j in range(n):
        k=next((i for i in range(j,n) if A[i][j]),None)
        if k is None:
            return 0
        if k!=j:
            A[k],A[j]=A[j],A[k];out=-out
        v=A[j][j];out=out*v%prime;iv=pow(v,-1,prime)
        for i in range(j+1,n):
            q=A[i][j]*iv%prime
            if q:
                for k in range(j+1,n):
                    A[i][k]=(A[i][k]-q*A[j][k])%prime
                A[i][j]=0
    return out%prime

def sign_entry(which,i,j):
    b=hashlib.sha256((SEED+"|"+which+"|"+str(i)+"|"+str(j)).encode("ascii")).digest()[0]
    return 1 if b&1 else -1

def fixed_unimodular_mix():
    # T = U L, with both factors triangular and diagonal exactly one.
    L=[[int(i==j) if i<=j else sign_entry("L",i,j) for j in range(56)]
       for i in range(56)]
    U=[[int(i==j) if i>=j else sign_entry("U",i,j) for j in range(56)]
       for i in range(56)]
    return [[sum(U[i][k]*L[k][j] for k in range(56)) for j in range(56)]
            for i in range(56)]

def integer_row_combinations(C,A):
    out=[]
    for cc in C:
        tick()
        row=[]
        for j in range(22):
            v=ZERO
            for k,c in enumerate(cc):
                if c and A[k][j]:
                    v=v+c*A[k][j]
            row.append(v)
        out.append(row)
    return out

def select_candidates(A):
    require(all(PROFILE_PRIME%d for d in range(2,math.isqrt(PROFILE_PRIME)+1)),
            "Fixed profile modulus is prime")
    T=fixed_unimodular_mix(); trials=[]
    for point in PROFILE_POINTS:
        tick()
        ev=[[polynomial_eval_mod(p,point,PROFILE_PRIME) for p in row] for row in A]
        asc=row_basis(ev,range(56),PROFILE_PRIME)
        trials.append({"point":point,"rank":len(asc)})
        if len(asc)==22:
            break
    else:
        return None,{"prime":PROFILE_PRIME,"trials":trials,"complete":False}
    desc=row_basis(ev,range(55,-1,-1),PROFILE_PRIME)
    tev=[[sum(T[i][k]*ev[k][j] for k in range(56))%PROFILE_PRIME
          for j in range(22)] for i in range(56)]
    mix=row_basis(tev,range(56),PROFILE_PRIME)
    require(len(desc)==len(mix)==22,"All prescribed row orders find a full basis")
    selectors=[]
    for number,(kind,ids) in enumerate((("original-ascending",asc),
                                        ("original-descending",desc),
                                        ("fixed-constant-UL",mix))):
        C=([[int(i==j) for j in range(56)] for i in ids]
           if number<2 else [T[i][:] for i in ids])
        EE=[[sum(C[i][k]*ev[k][j] for k in range(56))%PROFILE_PRIME
             for j in range(22)] for i in range(22)]
        dv=det_mod(EE,PROFILE_PRIME)
        require(dv!=0,"Selected square polynomial determinant is nonzero")
        selectors.append({"number":number,"kind":kind,"selectedRows":ids,
                          "rowCombination":C,"rowCombinationSHA256":digest(canonical(C)),
                          "profilePoint":point,"profilePrime":PROFILE_PRIME,
                          "determinantAtProfile":dv})
    return selectors,{"prime":PROFILE_PRIME,"point":point,"trials":trials,
                     "complete":True,"constantMixSeed":SEED,
                     "constantMix":"U L, unit triangular integer factors"}

def pivot_transaction(A,previous,rows,cols,sign,k,check=tick):
    n=len(A)
    choices=[(int(A[i][j].degree()),int(A[i][j].height_bits()),i,j)
             for i in range(k,n) for j in range(k,n) if A[i][j]]
    if not choices:
        return None
    _,_,ri,cj=min(choices)
    B=[r[:] for r in A];rp=rows[:];cp=cols[:];sg=sign
    if ri!=k:
        B[k],B[ri]=B[ri],B[k];rp[k],rp[ri]=rp[ri],rp[k];sg=-sg
    if cj!=k:
        for r in B:
            r[k],r[cj]=r[cj],r[k]
        cp[k],cp[cj]=cp[cj],cp[k];sg=-sg
    piv=B[k][k];divisions=0
    for i in range(k+1,n):
        multiplier=B[i][k]
        for j in range(k+1,n):
            check()
            numerator=piv*B[i][j]-multiplier*B[k][j]
            B[i][j]=exact_divide(numerator,previous)
            divisions+=1
        B[i][k]=ZERO
    check()
    return B,piv,rp,cp,sg,divisions,{"rowSwap":[k,ri],"columnSwap":[k,cj],
                                    "pivotDegree":int(piv.degree()),
                                    "pivotCoefficientBits":int(piv.height_bits())}

def tiny_exact_test():
    x=fmpz_poly([0,1])
    A=[[ZERO,x+2,ONE],[x-1,ZERO,2*x],[3*ONE,ONE,x*x+1]]
    expected=ZERO
    for pp in itertools.permutations(range(3)):
        inversions=sum(pp[i]>pp[j] for i in range(3) for j in range(i+1,3))
        v=ONE
        for i,j in enumerate(pp):
            v=v*A[i][j]
        expected=expected+(-1 if inversions%2 else 1)*v
    B=A;previous=ONE;rp=list(range(3));cp=rp[:];sg=1
    swaps=0
    for k in range(2):
        ans=pivot_transaction(B,previous,rp,cp,sg,k,check=lambda:None)
        require(ans is not None,"Nontrivial exact tiny minor")
        B,previous,rp,cp,sg,_,event=ans
        swaps+=int(event["rowSwap"][0]!=event["rowSwap"][1])
        swaps+=int(event["columnSwap"][0]!=event["columnSwap"][1])
    require(sg*B[-1][-1]==expected and swaps>0,
            "Independent six-term determinant and permutation signs")
    before=mh(A);counter=[0]
    def stop_pending():
        counter[0]+=1
        if counter[0]==2:
            raise BudgetStop("intentional tiny pending-pivot interruption")
    try:
        pivot_transaction(A,ONE,list(range(3)),list(range(3)),1,0,check=stop_pending)
        raise AssertionError("Tiny pending interruption must trigger")
    except BudgetStop:
        pass
    require(mh(A)==before,"Pending transaction did not mutate committed input")
    return {"independentThreeByThreeExpansionVerified":True,
            "nontrivialSwapsVerified":True,"pendingPivotInputUnchanged":True}

class Slots:
    def __init__(self,root,binding,number):
        self.root=Path(root);self.root.mkdir(parents=True,exist_ok=True)
        self.pointer=self.root/"state-pointer.json";self.binding=binding;self.number=number
    def load(self):
        if not self.pointer.exists():
            return None
        p=json.loads(self.pointer.read_text())
        require(p["binding"]==self.binding and p["number"]==self.number,
                "Two-slot checkpoint binding")
        obj=read_gzip(self.root/p["record"]["file"],p["record"])
        require(obj["binding"]==self.binding and obj["number"]==self.number,
                "Checkpoint payload binding")
        return obj["state"]
    def save(self,state):
        old=json.loads(self.pointer.read_text()) if self.pointer.exists() else None
        slot=1-int(old["slot"]) if old else 0
        obj={"format":FORMAT,"binding":self.binding,"number":self.number,"state":state}
        rec=temporary_gzip(self.root/("state-slot-"+str(slot)+".json.gz"),obj)
        summary={"nextPivot":state["nextPivot"],"completedPivots":state["nextPivot"],
                 "exactDivisions":state["exactDivisions"],"sign":state["sign"],
                 "determinantZero":state["determinantZero"],
                 "lastCompletePivot":state["events"][-1] if state["events"] else None}
        atomic_json(self.pointer,{"format":FORMAT,"binding":self.binding,
                                "number":self.number,"slot":slot,"record":rec,
                                "summary":summary})
    def record(self):
        return json.loads(self.pointer.read_text()) if self.pointer.exists() else None

def determinant_candidate(B,selector,binding,root):
    root=Path(root);root.mkdir(parents=True,exist_ok=True)
    complete=root/"complete.json"
    if complete.exists():
        rec=json.loads(complete.read_text())
        require(rec["binding"]==binding and rec["selectorSHA256"]==digest(canonical(selector)),
                "Completed determinant candidate binding")
        obj=read_gzip(root/rec["record"]["file"],rec["record"])
        require(obj["binding"]==binding,"Completed determinant payload binding")
        return obj,rec
    slots=Slots(root,binding,selector["number"])
    state=slots.load()
    if state is None:
        state={"matrix":zm(B),"nextPivot":0,"previousPivot":zp(ONE),
               "rowPermutation":list(range(22)),"columnPermutation":list(range(22)),
               "sign":1,"exactDivisions":0,"events":[],
               "originalSquareSHA256":mh(B),"determinantZero":False}
        slots.save(state)
    require(state["originalSquareSHA256"]==mh(B),"Original selected square identity")
    A=uzm(state["matrix"]);previous=uzp(state["previousPivot"])
    rp=state["rowPermutation"];cp=state["columnPermutation"];sg=state["sign"]
    require(sorted(rp)==sorted(cp)==list(range(22)) and sg in (-1,1),
            "Retained permutations and determinant sign")
    for k in range(state["nextPivot"],21):
        tick()
        ans=pivot_transaction(A,previous,rp,cp,sg,k)
        if ans is None:
            state["determinantZero"]=True;state["nextPivot"]=21
            slots.save(state);break
        AA,pv,rr,cc,ss,count,event=ans
        # No committed object is changed until the entire pivot has completed.
        newstate={"matrix":zm(AA),"nextPivot":k+1,"previousPivot":zp(pv),
                  "rowPermutation":rr,"columnPermutation":cc,"sign":ss,
                  "exactDivisions":state["exactDivisions"]+count,
                  "events":state["events"]+[dict(event,pivot=k,
                             fullTrailingCoordinateDivisions=count)],
                  "originalSquareSHA256":state["originalSquareSHA256"],
                  "determinantZero":False}
        slots.save(newstate)
        state=newstate;A=AA;previous=pv;rp=rr;cp=cc;sg=ss
    det=ZERO if state["determinantZero"] else sg*A[21][21]
    require(bool(det),"Nonzero finite-field selected minor cannot have zero exact determinant")
    degree_bound=sum(max(int(p.degree()) for p in row) for row in B)
    require(int(det.degree())<=degree_bound,"Original row-degree determinant bound")
    checks=[]
    for point in (-1,3,4):
        tick()
        M=fmpz_mat([[integer_eval(p,point) for p in row] for row in B])
        expected=int(M.det());actual=integer_eval(det,point)
        require(expected==actual,"Independent original integer determinant specialization")
        checks.append({"point":point,"integerDeterminantSHA256":digest(str(expected).encode("ascii"))})
    require(polynomial_eval_mod(det,selector["profilePoint"],PROFILE_PRIME)
            ==selector["determinantAtProfile"],"Original profile determinant sign and scale")
    outside,known=strip_known(det)
    obj={"format":FORMAT,"binding":binding,"selector":selector,
         "originalSquareSHA256":mh(B),"signedOriginalDeterminant":zp(det),
         "outsidePrimitivePositive":zp(outside),"removedKnownValuations":known,
         "determinantIntegerContent":str(det.content()),
         "exactDivisions":state["exactDivisions"],"rowDegreeUpperBound":degree_bound,
         "signedDeterminantStatistics":polynomial_stats(det),
         "outsideStatistics":polynomial_stats(outside),
         "independentIntegerSpecializations":checks,
         "allBareissDivisionRemaindersZero":True,
         "allOriginalRowCombinationIdentitiesVerified":True,
         "originalRowCombinationPolynomialCoordinates":484,
         "onlyMaximalMinorGcdUpperCertificate":True}
    rec=temporary_gzip(root/"complete-determinant.json.gz",obj)
    pointer={"format":FORMAT,"binding":binding,"selectorSHA256":digest(canonical(selector)),
             "record":rec}
    atomic_json(complete,pointer)
    return obj,pointer

def load_core(source,checkpoints):
    require(file_id(source)==CORE_SOURCE,"Frozen original core decoder source")
    spec=importlib.util.spec_from_file_location("paid_original_core_decoder",source)
    d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
    root=Path(checkpoints);manifest=json.loads((root/"checkpoint-manifest.json").read_text())
    require(manifest["format"]==d.FORMAT and manifest["binding"]==CORE_BINDING,
            "Paid original core manifest semantic binding")
    rec=manifest["phases"]["polynomial-core"]
    require(rec["file"]==CORE_FILE and rec["bytes"]==CORE_STORED["bytes"]
            and rec["sha256"]==CORE_STORED["sha256"]
            and rec["payloadSha256"]==CORE_PAYLOAD_SHA and rec["verified"] is True,
            "Exact paid core phase descriptor; old row state is not read")
    path=root/CORE_FILE
    require(file_id(path)==CORE_STORED,"Paid full core bytes and SHA256")
    with gzip.open(path,"rb") as f:
        raw=f.read()
    require(digest(raw)==CORE_PAYLOAD_SHA,"Paid core exact payload")
    obj=json.loads(raw)
    require(obj["binding"]==CORE_BINDING and obj["phase"]=="polynomial-core"
            and obj["verified"] is True,"Original complete core identity")
    payload=obj["payload"];A=d.decm(payload["core"])
    require(len(A)==56 and all(len(row)==22 for row in A)
            and d.phash(A)==CORE_LOGICAL_SHA,"All original56 x22 polynomial entries")
    require(payload["knownFactors"]==[d.encp(fmpq_poly(f)) for f in FACTORS],
            "Exactly the original six localization factors")
    integer=[];scales=[];coordinates=0
    for row in A:
        tick()
        den=1
        for p in row:
            den=math.lcm(den,int(p.denom()))
        zz=[p.numer()*(den//int(p.denom())) for p in row]
        cont=0
        for p in zz:
            cont=math.gcd(cont,int(p.content()))
        if cont==0:
            cont=1
        zz=[exact_divide(p,fmpz_poly([cont])) for p in zz]
        scale=fmpq(den,cont)
        require(all(fmpq_poly(q)==p*scale for p,q in zip(row,zz)),
                "Every original row scaled by a nonzero rational constant only")
        coordinates+=len(row);integer.append(zz);scales.append(str(scale))
    return d,A,integer,scales,{"parentBinding":CORE_BINDING,"phaseStored":CORE_STORED,
        "phasePayloadSHA256":CORE_PAYLOAD_SHA,"originalCoreLogicalSHA256":CORE_LOGICAL_SHA,
        "normalizationOriginalPolynomialCoordinates":coordinates,
        "originalIntegerCore":matrix_stats(integer),
        "constantRowScalesSHA256":digest(canonical(scales)),
        "parentManifestActualIdentity":file_id(root/"checkpoint-manifest.json")}

def update_gcd(completed,binding,out):
    if not completed:
        return None
    vv=[uzp(obj["outsidePrimitivePositive"]) for obj,_ in completed]
    gg=vv[0]
    for p in vv[1:]:
        tick();gg=primitive_positive(gg.gcd(p))
    require(all(not divmod(p,gg)[1] for p in vv),"Upper polynomial divides every completed minor")
    require(all(int(gg.gcd(fmpz_poly(f)).degree())==0 for f in FACTORS),
            "Final upper polynomial is outside exactly the known support")
    obj={"format":FORMAT,"binding":binding,"completedMinorNumbers":
         [x["selector"]["number"] for x,_ in completed],
         "primitivePositiveGcd":zp(gg),"monicGcd":str(fmpq_poly(gg)/gg.leading_coefficient()),
         "statistics":polynomial_stats(gg),
         "isOne":int(gg.degree())==0,
         "doesNotClaimEqualityUnlessOne":True}
    rec=temporary_gzip(Path(out)/"current-outside-gcd-upper.json.gz",obj)
    return {"degree":int(gg.degree()),"isOne":int(gg.degree())==0,"record":rec,
            "coefficientSHA256":digest(canonical(zp(gg))),
            "onlyDivisibilityUpperBoundUnlessOne":True,
            "originalOutsideDivisorDegreeUpperBound":min(157,int(gg.degree()))}

def main():
    global DEADLINE,STOP
    p=argparse.ArgumentParser()
    p.add_argument("--core-source",required=True)
    p.add_argument("--parent-checkpoints",required=True)
    p.add_argument("--out",required=True)
    p.add_argument("--remaining-seconds",type=float,default=180)
    p.add_argument("--memory-mib",type=int,default=2048)
    p.add_argument("--max-candidates",type=int,default=3)
    args=p.parse_args()
    require(0<args.remaining_seconds<=1200 and 512<=args.memory_mib<=8192,
            "Explicit mathematical time and memory bounds")
    require(1<=args.max_candidates<=3,"At most three frozen candidate definitions")
    resource.setrlimit(resource.RLIMIT_AS,(args.memory_mib*1024**2,args.memory_mib*1024**2))
    sys.set_int_max_str_digits(0)
    began=time.monotonic()
    DEADLINE=began+max(.01,args.remaining_seconds-min(12,args.remaining_seconds/8))
    def request_stop(sig,frame):
        global STOP
        STOP=True
    signal.signal(signal.SIGTERM,request_stop)
    signal.signal(signal.SIGALRM,request_stop)
    signal.setitimer(signal.ITIMER_REAL,args.remaining_seconds)
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    source=file_id(__file__)
    identity={"format":FORMAT,"source":source,"coreSource":CORE_SOURCE,
              "coreBinding":CORE_BINDING,"corePayloadSHA256":CORE_PAYLOAD_SHA,
              "coreLogicalSHA256":CORE_LOGICAL_SHA,"knownFactors":FACTORS,
              "profilePrime":PROFILE_PRIME,"profilePoints":list(PROFILE_POINTS),
              "constantMixSeed":SEED,"algorithm":"integer Bareiss complete-pivot transactions"}
    binding=digest(canonical(identity))
    rec={"format":FORMAT,"binding":binding,"status":"started","events":[],
         "parameters":{"author":"Astra-ISP-789f / normal_annihilator",
             "aiAssisted":"GPT-6 Astra Pro","identity":identity,
             "remainingSeconds":args.remaining_seconds,"memoryMiB":args.memory_mib,
             "maximumFrozenCandidatesThisCall":args.max_candidates,
             "coreNotRecomputed":True,"oldRowReductionStateNotRead":True,
             "largeArraysTemporaryOnly":True,"fieldProfileDoesNotProveFullGcd":True}}
    completed=[];current_number=None;gcd_summary=None
    try:
        rec["parameters"]["tinyExactVerification"]=tiny_exact_test()
        d,originalQ,A,scales,coremeta=load_core(args.core_source,args.parent_checkpoints)
        rec["parameters"]["paidCore"]=coremeta
        selectors,profile=select_candidates(A)
        rec["parameters"]["fixedSelectionProfile"]=profile
        if selectors is None:
            rec["status"]="profile-insufficient"
            rec["outcome"]="no-selected-nonzero-minor-at-three-fixed-profile-points"
        else:
            rec["parameters"]["candidateProfiles"]=[
                {k:v for k,v in selector.items() if k!="rowCombination"}
                for selector in selectors]
            prepared={"format":FORMAT,"binding":binding,"constantRowScales":scales,
                      "selectors":selectors,"originalIntegerCoreSHA256":mh(A)}
            rec["parameters"]["preparedRowSources"]=temporary_gzip(out/"prepared-row-sources.json.gz",prepared)
            for selector in selectors[:args.max_candidates]:
                tick();current_number=selector["number"]
                B=integer_row_combinations(selector["rowCombination"],A)
                # This is a direct construction from all original56 normalized
                # rows, with all coefficients saved. No symbolic field solve is used.
                require(len(B)==22 and all(len(row)==22 for row in B),
                        "Complete original constant row-combination square")
                rationalSources=[[fmpq_poly([fmpq(c)*fmpq(scales[k])])
                                   for k,c in enumerate(row)]
                                  for row in selector["rowCombination"]]
                originalProduct=d.mm(rationalSources,originalQ)
                require(originalProduct==[[fmpq_poly(v) for v in row] for row in B],
                        "All484 rational polynomial source products against original56 rows")
                tick()
                require(det_mod([[polynomial_eval_mod(p,selector["profilePoint"],PROFILE_PRIME)
                                   for p in row] for row in B],PROFILE_PRIME)
                        ==selector["determinantAtProfile"],
                        "All source row-combinations agree with the retained selector")
                bb=matrix_stats(B)
                obj,record=determinant_candidate(B,selector,binding,
                    out/("candidate-"+str(current_number)))
                completed.append((obj,record))
                rec["events"].append({"event":"complete-exact-determinant",
                    "number":current_number,"kind":selector["kind"],
                    "selectedRows":selector["selectedRows"],"originalSquare":bb,
                    "rowCombinationSHA256":selector["rowCombinationSHA256"],
                    "signedDeterminant":obj["signedDeterminantStatistics"],
                    "outsideDeterminant":obj["outsideStatistics"],
                    "removedKnownValuations":obj["removedKnownValuations"],
                    "exactDivisions":obj["exactDivisions"],"temporaryCertificate":record["record"]})
                gcd_summary=update_gcd(completed,binding,out)
                rec["parameters"]["currentOutsideGcdUpper"]=gcd_summary
                atomic_json(out/"three-minor-upper-receipt.json",rec)
                if gcd_summary["isOne"]:
                    break
            rec["status"]="completed"
            rec["outcome"]=("original-projection-outside-divisor-proved-one"
                if gcd_summary and gcd_summary["isOne"] else
                "nonzero-exact-minor-gcd-upper-certificate-only")
    except BudgetStop as e:
        rec["status"]="budget-checkpoint";rec["message"]=str(e)
    except BaseException as e:
        rec["status"]="failed";rec["error"]={"type":type(e).__name__,"message":str(e)}
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        rec["elapsedSeconds"]=time.monotonic()-began
        rec["parameters"]["completedMinorCount"]=len(completed)
        rec["parameters"]["currentCandidateNumber"]=current_number
        if current_number is not None:
            pointer=out/("candidate-"+str(current_number))/"state-pointer.json"
            if pointer.exists():
                rec["parameters"]["lastWholePivotCheckpoint"]=json.loads(pointer.read_text())
        rec["parameters"]["allCompletedMinorExactDivisionsVerified"]=bool(completed)
        rec["parameters"]["completeOutsideMaximalMinorGcdComputed"]=bool(gcd_summary and gcd_summary["isOne"])
        rec["parameters"]["originalOutsideDivisorOneProved"]=bool(gcd_summary and gcd_summary["isOne"])
        rec["parameters"]["noNonconstantCandidateDeclaredActualOmega"]=True
        rec["parameters"]["newOriginalNineTargetGlobalMembershipClaim"]=False
        data=canonical(rec);require(len(data)<80000,"Only small execution summary is publishable")
        atomic_bytes(out/"three-minor-upper-receipt.json",data)
        print(data.decode("ascii"),flush=True)
    return 1 if rec["status"]=="failed" else (75 if rec["status"]=="budget-checkpoint" else 0)

if __name__=="__main__":
    raise SystemExit(main())
