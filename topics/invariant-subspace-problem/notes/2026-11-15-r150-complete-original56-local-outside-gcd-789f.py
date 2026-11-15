#!/usr/bin/env python3
"""R150: complete original56-row outside-gcd certificate in finite Q-algebras.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-15 UTC.
Consumes the paid original56x22 core and the three exact minor upper U.
First use Q[s]/(squarefree f), splitting f by exact gcd when needed.
A residual corank reaching the upper exponent closes that branch immediately.
Only unresolved branches lift the already selected profile to Q[s]/(f**e).
Every whole unit pivot, factor split, or full f-division is checkpointed.
No determinant, original core, or previous Hermite state is recomputed.
Official scalar API: https://python-flint.readthedocs.io/en/latest/fmpq_poly.html
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time
from flint import fmpq, fmpq_poly, fmpz_poly

FORMAT = "r150-complete-original56-local-outside-gcd-v1"
UPPER_SOURCE = {"bytes":29189,
 "sha256":"4ae559a6b1b5efdf3d88e1f59bc987895f0f6ab5ec8dd2d61d5a55db3ef9a1be"}
UPPER_BINDING = "5fc42d162e51b638ce06bbd67c2afd5755539a95a3bf5a650c4155df0ed6c8ef"
UPPER_RAW = {"bytes":8436,
 "sha256":"a18b3c1dd68890455a2b256adf1dfd9a9d690b60f81c99155be6e60a507dd145"}
UPPER_RECORD = {"file":"current-outside-gcd-upper.json.gz","bytes":12999,
 "sha256":"b6c26ab0cfae6a08dbdb02ebac570ef2fffaec953a0de4d9aef422b74815c3ab",
 "payloadSHA256":"e1722fa0f09424affa18c29e4275858619cf4c789a891937fc6c6d4355a867c1"}
UPPER_COEFFICIENT_SHA = "150089b4e115b8d975d4e4eb13492779a692a6af258094f852af22b7f34e652d"
CORE_SOURCE = {"bytes":34432,
 "sha256":"727175cf485a8ba5b5146a4cc6e749962e109c9e42265a2dd45f58cecdf933fb"}
CORE_BINDING = "ce358eac629541da0c9d35fd29c66424fa0d89ded97cfec93f324cf56e9d16ba"
CORE_PAYLOAD_SHA = "efdb8a0cff5626575fb1e667c5753cf82dc040d0a3598444d61f5452db1d67a5"
CORE_LOGICAL_SHA = "752d21d7ca74ee5235c05ade9048ef48f120891c567abfb5132a4b2b33b745c8"
FACTORS = [[0,1],[-2,1],[6,1],[-8,32,-25,5],
 [864,864,135,5],[9600,-25472,-3392,15936,-2888,-936,153,50,5]]
ZERO=fmpq_poly([])
ONE=fmpq_poly([1])
STOP=False
DEADLINE=float("inf")

class BudgetStop(Exception):
    pass

def require(v,message):
    if not v:
        raise AssertionError(message)

def tick():
    if STOP or time.monotonic()>=DEADLINE:
        raise BudgetStop("Whole prior transaction retained; pending work not committed")

def canonical(x):
    return json.dumps(x,sort_keys=True,ensure_ascii=True,separators=(",",":")).encode("ascii")

def digest(b):
    return hashlib.sha256(b).hexdigest()

def file_id(path):
    h=hashlib.sha256();n=0
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""):
            h.update(b);n+=len(b)
    return {"bytes":n,"sha256":h.hexdigest()}

def atomic_bytes(path,data):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".pending-"+str(os.getpid()))
    with tmp.open("wb") as f:
        f.write(data);f.flush();os.fsync(f.fileno())
    os.replace(tmp,path)

def atomic_json(path,obj):
    atomic_bytes(path,canonical(obj))

def save_gzip(path,obj):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=canonical(obj);tmp=path.with_name(path.name+".pending-"+str(os.getpid()))
    with tmp.open("wb") as h:
        with gzip.GzipFile(filename="",fileobj=h,mode="wb",compresslevel=1,mtime=0) as z:
            z.write(raw)
        h.flush();os.fsync(h.fileno())
    os.replace(tmp,path)
    return dict(file_id(path),file=path.name,payloadSHA256=digest(raw),temporaryOnly=True)

def load_gzip(path,pin):
    require(file_id(path)=={"bytes":pin["bytes"],"sha256":pin["sha256"]},
            "Whole temporary file bytes/SHA256")
    with gzip.open(path,"rb") as f:
        raw=f.read()
    require(digest(raw)==pin["payloadSHA256"],"Whole exact temporary payload SHA256")
    return json.loads(raw)

def encp(p):
    return {"n":[str(x) for x in p.numer().coeffs()],"d":str(p.denom())}

def decp(p):
    return fmpq_poly([int(x) for x in p["n"]],int(p["d"]))

def encm(M):
    return [[encp(x) for x in row] for row in M]

def decm(M):
    return [[decp(x) for x in row] for row in M]

def phash(p):
    return digest(canonical(encp(p)))

def mhash(M):
    return digest(canonical(encm(M)))

def monic(p):
    require(bool(p),"Nonzero polynomial to monic")
    return p/p.leading_coefficient()

def exactq(a,b):
    require(bool(b),"Nonzero exact polynomial divisor")
    q,r=divmod(a,b)
    require(not r and q*b==a,"Exact polynomial division and multiplication")
    return q

def pstats(p):
    return {"degree":int(p.degree()),"numeratorMaximumBits":int(p.numer().height_bits()),
            "denominatorBits":abs(int(p.denom())).bit_length(),"coefficientSHA256":phash(p)}

def squarefree_groups(U):
    U=monic(U)
    c=monic(U.gcd(U.derivative()))
    w=exactq(U,c);e=1;groups=[]
    while int(w.degree())>0:
        tick()
        y=monic(w.gcd(c));f=exactq(w,y)
        if int(f.degree())>0:
            f=monic(f)
            require(int(f.gcd(f.derivative()).degree())==0,"Every support branch squarefree")
            groups.append((f,e))
        w=y;c=exactq(c,y);e+=1
    require(int(c.degree())==0,"Characteristic-zero squarefree decomposition exhausted")
    prod=ONE
    for i,(f,e) in enumerate(groups):
        prod=prod*f**e
        require(all(int(f.gcd(g).degree())==0 for g,_ in groups[:i]),
                "Initial squarefree groups pairwise coprime")
    require(prod==U,"Complete squarefree product equals the actual upper U")
    return groups

def reduced_matrix(A,modulus):
    out=[];n=0
    for row in A:
        tick();rr=[]
        for x in row:
            q,r=divmod(x,modulus)
            require(q*modulus+r==x,"Every original polynomial quotient/remainder identity")
            rr.append(r);n+=1
        out.append(rr)
    return out,n

def pivot_or_split(A,f):
    candidates=[]
    for i,row in enumerate(A):
        for j,x in enumerate(row):
            if x:
                candidates.append((int(x.degree()),int(x.numer().height_bits()),i,j))
    candidates.sort()
    split=None
    for number,(_,_,i,j) in enumerate(candidates):
        if number%8==0:
            tick()
        x=A[i][j]
        if int(x.degree())==0:
            return ("unit",i,j)
        g=monic(x.gcd(f))
        if int(g.degree())==0:
            return ("unit",i,j)
        if int(g.degree())<int(f.degree()) and split is None:
            split=g
    if split is not None:
        return ("split",split,None)
    require(all(not divmod(x,f)[1] for row in A for x in row),
            "No unit or split means every retained entry is divisible by the whole f")
    return ("divisible",None,None)

def unit_transaction(A,f,precision,row,column,rows,columns,hook=tick):
    hook()
    require(A and A[0] and 0<=row<len(A) and 0<=column<len(A[0]),
            "Actual unit-pivot coordinates")
    modulus=f**precision
    B=[list(x) for x in A]
    rr=list(rows);cc=list(columns)
    B[0],B[row]=B[row],B[0];rr[0],rr[row]=rr[row],rr[0]
    for r in B:
        r[0],r[column]=r[column],r[0]
    cc[0],cc[column]=cc[column],cc[0]
    p=B[0][0]
    g,a,b=p.xgcd(modulus)
    require(a*p+b*modulus==g and int(g.degree())==0 and bool(g),
            "Exact extended-gcd unit identity")
    inv=(a/g[0])%modulus
    require((p*inv)%modulus==ONE,"Actual unit inverse in the full finite ring")
    normalized=[(inv*x)%modulus for x in B[0]]
    require(normalized[0]==ONE,"Normalized unit row")
    out=[];checks=0
    for i in range(1,len(B)):
        hook();newrow=[]
        for j in range(1,len(B[0])):
            z=(B[i][j]-B[i][0]*normalized[j])%modulus
            require((p*z-(p*B[i][j]-B[i][0]*B[0][j]))%modulus==ZERO,
                    "Every full retained-row Schur coordinate product")
            newrow.append(z);checks+=1
        out.append(newrow)
    event={"kind":"unit","factor":encp(f),"precision":precision,
           "position":[row,column],"originalRow":rr[0],"originalColumn":cc[0],
           "pivot":encp(p),"inverse":encp(inv),"unitInverseVerified":True,
           "allRetainedRowsVerified":True,"coordinateProducts":checks,
           "beforeSHA256":mhash(A),"afterSHA256":mhash(out)}
    return out,rr[1:],cc[1:],event

def factor_division(A,f,precision):
    require(precision>1,"A further exact f-digit is actually available")
    B=[];count=0
    for row in A:
        tick();rr=[]
        for x in row:
            rr.append(exactq(x,f));count+=1
        B.append(rr)
    require(all(int(x.degree())<int(f.degree())*(precision-1)
                for row in B for x in row if x),"Reduced precision after exact whole-block division")
    return B,count

def branch_summary(b):
    return {"id":b["id"],"factor":pstats(decp(b["factor"])),
            "upperExponent":b["upperExponent"],"mode":b["mode"],
            "precision":b["precision"],"paidValuation":b["paidValuation"],
            "remainingRows":len(b["rows"]),"remainingColumns":len(b["columns"]),
            "profilePivots":len(b["profilePivots"]),"replayedPivots":b.get("replayedPivots",0),
            "operationCount":len(b["operations"])}

def state_summary(state):
    pending=[branch_summary(b) for b in state["pending"]]
    closed=[{k:v for k,v in b.items() if k!="factor"} for b in state["closed"]]
    return {"generation":state["generation"],"completed":not state["pending"],
            "pendingBranchCount":len(pending),"closedBranchCount":len(closed),
            "pendingBranches":pending[:16],"closedBranches":closed[:16],
            "allBranchSummarySHA256":digest(canonical({"pending":pending,"closed":closed})),
            "branchListsTruncated":len(pending)>16 or len(closed)>16,
            "unitPivots":state["unitPivots"],"splitCount":state["splitCount"],
            "wholeFactorDivisions":state["wholeFactorDivisions"],
            "verifiedSchurCoordinates":state["verifiedSchurCoordinates"],
            "verifiedOriginalReductionCoordinates":state["verifiedOriginalReductionCoordinates"]}

def initial_state(A,groups):
    pending=[];checks=0
    for i,(f,e) in enumerate(groups):
        M,n=reduced_matrix(A,f);checks+=n
        pending.append({"id":str(i),"factor":encp(f),"upperExponent":e,
            "mode":"profile","precision":1,"paidValuation":0,"matrix":encm(M),
            "rows":list(range(len(A))),"columns":list(range(len(A[0]))),
            "profilePivots":[],"operations":[],"replayedPivots":0})
    return {"generation":0,"pending":pending,"closed":[],"unitPivots":0,
            "splitCount":0,"wholeFactorDivisions":0,"verifiedSchurCoordinates":0,
            "verifiedOriginalReductionCoordinates":checks}

def close_branch(state,b,exponent,reason):
    require(0<=exponent<=b["upperExponent"],"Closed exact exponent is inside the proved upper")
    closed={"id":b["id"],"factor":b["factor"],"factorStatistics":pstats(decp(b["factor"])),
            "upperExponent":b["upperExponent"],"exactExponent":exponent,
            "reason":reason,"profileCorank":b.get("profileCorank"),
            "operationCount":len(b["operations"]),
            "operationSHA256":digest(canonical(b["operations"])),
            "allRetainedRowsVerified":True}
    ns=dict(state);ns["pending"]=state["pending"][1:]
    ns["closed"]=state["closed"]+[closed];ns["generation"]=state["generation"]+1
    return ns,{"event":"closed-support-branch","id":b["id"],"exactExponent":exponent,
               "factorDegree":int(decp(b["factor"]).degree()),"reason":reason},b["operations"]

def advance(state,A):
    tick()
    b=state["pending"][0];f=decp(b["factor"]);M=decm(b["matrix"])
    n=len(b["columns"]);e=b["upperExponent"];mode=b["mode"];precision=b["precision"]
    if n==0:
        return close_branch(state,b,b["paidValuation"],"all-original-columns-exited")
    nb=dict(b);ns=dict(state);event=None;closed_ops=None
    if mode=="replay":
        k=b["replayedPivots"]
        if k<len(b["profilePivots"]):
            row,column=b["profilePivots"][k]
            N,rr,cc,op=unit_transaction(M,f,precision,row,column,b["rows"],b["columns"])
            nb.update(matrix=encm(N),rows=rr,columns=cc,replayedPivots=k+1,
                      operations=b["operations"]+[dict(op,mode="higher-precision-profile-replay")])
            ns["unitPivots"]+=1;ns["verifiedSchurCoordinates"]+=op["coordinateProducts"]
            event={"event":"replayed-profile-at-new-precision","id":b["id"],
                   "completedPivots":k+1,"precision":precision}
        else:
            require(all(not divmod(x,f)[1] for row in M for x in row),
                    "Lifted complete residue-field Schur is divisible by f on every row")
            lower=b["paidValuation"]+n
            require(lower<=e,"Local lower valuation cannot exceed actual minor upper")
            if lower==e:
                nb["profileCorank"]=n
                return close_branch(state,nb,e,"full-row-lower-bound-meets-minor-upper")
            N,count=factor_division(M,f,precision)
            op={"kind":"factor-division","factor":encp(f),"precisionBefore":precision,
                "precisionAfter":precision-1,"remainingColumns":n,"valuationAdded":n,
                "exactCoordinateProducts":count,"beforeSHA256":mhash(M),"afterSHA256":mhash(N)}
            nb.update(matrix=encm(N),mode="precision",precision=precision-1,
                      paidValuation=lower,operations=b["operations"]+[op])
            ns["wholeFactorDivisions"]+=1
            event={"event":"complete-whole-f-division","id":b["id"],
                   "paidValuation":lower,"precision":precision-1,"coordinateProducts":count}
    else:
        kind,x,y=pivot_or_split(M,f)
        if kind=="unit":
            N,rr,cc,op=unit_transaction(M,f,precision,x,y,b["rows"],b["columns"])
            nb.update(matrix=encm(N),rows=rr,columns=cc,
                      operations=b["operations"]+[dict(op,mode=mode)])
            if mode=="profile":
                nb["profilePivots"]=b["profilePivots"]+[[x,y]]
            ns["unitPivots"]+=1;ns["verifiedSchurCoordinates"]+=op["coordinateProducts"]
            event={"event":"complete-full-row-unit-Schur","id":b["id"],"mode":mode,
                   "remainingRows":len(rr),"remainingColumns":len(cc),"precision":precision}
        elif kind=="split":
            g=monic(x);h=monic(exactq(f,g))
            require(g*h==f and int(g.gcd(h).degree())==0,
                    "Exact coprime factor split, with no lost support")
            children=[];reduction_checks=0
            for suffix,ff in (("a",g),("b",h)):
                N,count=reduced_matrix(M,ff**precision);reduction_checks+=count
                child=dict(b);child.update(id=b["id"]+suffix,factor=encp(ff),matrix=encm(N),
                    operations=b["operations"]+[{"kind":"coprime-support-split",
                        "parentFactor":encp(f),"newFactor":encp(ff),"precision":precision,
                        "originalFullRowCoordinates":count}])
                children.append(child)
            ns["pending"]=children+state["pending"][1:];ns["generation"]=state["generation"]+1
            ns["splitCount"]+=1
            ns["verifiedOriginalReductionCoordinates"]+=reduction_checks
            event={"event":"exact-coprime-support-split","parent":b["id"],
                   "degrees":[int(g.degree()),int(h.degree())],"precision":precision}
            return ns,event,closed_ops
        else:
            if mode=="profile":
                require(all(not z for row in M for z in row),
                        "Complete first-precision residual is exactly zero")
                lower=n
                require(lower<=e,"Original all-row residue corank cannot exceed minor upper exponent")
                nb["profileCorank"]=n
                if lower==e:
                    return close_branch(state,nb,e,"residue-corank-meets-minor-upper")
                require(0<lower<e,"Only genuinely unresolved positive branch needs more precision")
                N,count=reduced_matrix(A,f**e)
                nb.update(mode="replay",precision=e,paidValuation=0,matrix=encm(N),
                          rows=list(range(len(A))),columns=list(range(len(A[0]))),
                          replayedPivots=0,
                          operations=b["operations"]+[{"kind":"higher-precision-preparation",
                              "factor":encp(f),"precision":e,"originalFullRowCoordinates":count,
                              "profileRank":len(A[0])-n,"profileCorank":n}])
                ns["verifiedOriginalReductionCoordinates"]+=count
                event={"event":"higher-precision-only-for-unresolved-branch","id":b["id"],
                       "profileCorank":n,"upperExponent":e,"newPrecision":e}
            else:
                lower=b["paidValuation"]+n
                require(lower<=e,"Full-row local lower valuation cannot exceed minor upper")
                if lower==e:
                    return close_branch(state,b,e,"full-row-lower-bound-meets-minor-upper")
                N,count=factor_division(M,f,precision)
                op={"kind":"factor-division","factor":encp(f),"precisionBefore":precision,
                    "precisionAfter":precision-1,"remainingColumns":n,"valuationAdded":n,
                    "exactCoordinateProducts":count,"beforeSHA256":mhash(M),"afterSHA256":mhash(N)}
                nb.update(matrix=encm(N),precision=precision-1,paidValuation=lower,
                          operations=b["operations"]+[op])
                ns["wholeFactorDivisions"]+=1
                event={"event":"complete-whole-f-division","id":b["id"],
                       "paidValuation":lower,"precision":precision-1,"coordinateProducts":count}
    ns["pending"]=[nb]+state["pending"][1:];ns["generation"]=state["generation"]+1
    return ns,event,closed_ops

def finish_polynomials(state,U):
    require(not state["pending"],"Every original support branch completed")
    omega=ONE;cover=ONE;factors=[]
    for b in state["closed"]:
        f=decp(b["factor"])
        require(all(int(f.gcd(g).degree())==0 for g in factors),"Closed support branches disjoint")
        factors.append(f)
        cover=cover*f**b["upperExponent"];omega=omega*f**b["exactExponent"]
    require(cover==monic(U),"All upper support and multiplicities accounted for")
    quotient=exactq(monic(U),omega)
    return monic(omega),quotient

def tiny_verification():
    x=fmpq_poly([0,1]);f=x*x-1
    A=[[x-1,ZERO],[ZERO,f],[ZERO,ZERO]]
    U=f*f
    state=initial_state(A,squarefree_groups(U));iterations=0
    while state["pending"]:
        state,_,_=advance(state,A);iterations+=1
        require(iterations<40,"Bounded tiny exact support test")
    omega,_=finish_polynomials(state,U)
    independent=ZERO
    for i,j in ((0,1),(0,2),(1,2)):
        minor=A[i][0]*A[j][1]-A[i][1]*A[j][0]
        independent=minor if not independent else independent.gcd(minor)
    require(omega==monic(independent),"Independent all-three-minors exact gcd")
    require(state["splitCount"]>=1 and state["wholeFactorDivisions"]>=1,
            "Tiny test exercises coprime splitting and unresolved higher precision")
    M=[[ONE,x],[x,ONE],[x+1,x*x]]
    before=mhash(M);count=[0]
    def stop_pending():
        count[0]+=1
        if count[0]==2:
            raise BudgetStop("intentional tiny pending stop")
    interrupted=False
    try:
        unit_transaction(M,f,2,0,0,[0,1,2],[0,1],hook=stop_pending)
    except BudgetStop:
        interrupted=True
    require(interrupted and mhash(M)==before,"Pending unit transaction leaves original matrix unchanged")
    return {"independentAllMinorGcdVerified":True,"coprimeSplitVerified":True,
            "higherPrecisionDivisionVerified":True,"pendingPivotInputUnchanged":True}

class Checkpoints:
    def __init__(self,root,binding):
        self.root=Path(root);self.root.mkdir(parents=True,exist_ok=True)
        self.binding=binding;self.pointer=self.root/"checkpoint-pointer.json"
    def load(self):
        if not self.pointer.exists():
            return None
        pp=json.loads(self.pointer.read_text())
        require(pp["format"]==FORMAT and pp["binding"]==self.binding,
                "Exact continuation source and immutable input binding")
        obj=load_gzip(self.root/pp["record"]["file"],pp["record"])
        require(obj["format"]==FORMAT and obj["binding"]==self.binding,
                "Whole checkpoint semantic identity")
        state=obj["state"]
        require(state["generation"]==pp["generation"],"Completed checkpoint generation")
        return state
    def save(self,state):
        slot=state["generation"]%2
        rec=save_gzip(self.root/("state-slot-"+str(slot)+".json.gz"),
                     {"format":FORMAT,"binding":self.binding,"state":state})
        pointer={"format":FORMAT,"binding":self.binding,"generation":state["generation"],
                 "slot":slot,"record":rec,"summary":state_summary(state)}
        atomic_json(self.pointer,pointer)
        return pointer
    def save_closed_operations(self,branch_id,ops):
        return save_gzip(self.root/("closed-operations-"+branch_id+".json.gz"),
            {"format":FORMAT,"binding":self.binding,"branch":branch_id,"operations":ops})

def load_inputs(args):
    require(file_id(args.upper_source)==UPPER_SOURCE,"Actual frozen determinant source")
    spec=importlib.util.spec_from_file_location("paid_three_minor_upper",args.upper_source)
    d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
    d.tick=tick
    _,original,A,scales,coremeta=d.load_core(args.core_source,args.parent_checkpoints)
    require(d.CORE_BINDING==CORE_BINDING and d.CORE_PAYLOAD_SHA==CORE_PAYLOAD_SHA
            and d.CORE_LOGICAL_SHA==CORE_LOGICAL_SHA and d.FACTORS==FACTORS,
            "Same original56 row core and localization")
    A=[[fmpq_poly(x) for x in row] for row in A]
    root=Path(args.upper_out);raw=root/"three-minor-upper-receipt.json"
    require(file_id(raw)==UPPER_RAW,"Complete actual three-minor raw receipt")
    paid=json.loads(raw.read_text())
    require(paid["binding"]==UPPER_BINDING and paid["status"]=="completed"
            and paid["parameters"]["completedMinorCount"]==3
            and paid["parameters"]["allCompletedMinorExactDivisionsVerified"] is True,
            "All three genuine original maximal-minor upper certificates completed")
    saved=load_gzip(root/UPPER_RECORD["file"],UPPER_RECORD)
    require(saved["format"]==d.FORMAT and saved["binding"]==UPPER_BINDING
            and saved["completedMinorNumbers"]==[0,1,2],
            "Exact same complete upper polynomial source")
    coeff=saved["primitivePositiveGcd"]
    require(digest(canonical(coeff))==UPPER_COEFFICIENT_SHA,
            "Actual primitive upper coefficient array SHA256")
    integer=fmpz_poly([int(c) for c in coeff]);U=monic(fmpq_poly(integer))
    require(int(U.degree())==120 and saved["statistics"]["degree"]==120,
            "Actual degree120 upper, without an equality presumption")
    require(all(int(U.gcd(fmpq_poly(f)).degree())==0 for f in FACTORS),
            "All upper support is outside the six already inverted factors")
    return A,U,{"paidCore":coremeta,"originalRowConstantScalesSHA256":digest(canonical(scales)),
        "full56NormalizedMatrixSHA256":mhash(A),"upperStatistics":pstats(U),
        "upperStored":UPPER_RECORD,"upperCoefficientSHA256":UPPER_COEFFICIENT_SHA,
        "allOriginal56RowsPresent":True,"originalRowCount":56,"originalColumnCount":22}

def main():
    global STOP,DEADLINE
    p=argparse.ArgumentParser()
    p.add_argument("--upper-source",required=True)
    p.add_argument("--core-source",required=True)
    p.add_argument("--parent-checkpoints",required=True)
    p.add_argument("--upper-out",required=True)
    p.add_argument("--out",required=True)
    p.add_argument("--remaining-seconds",type=float,default=180)
    p.add_argument("--memory-mib",type=int,default=2048)
    args=p.parse_args()
    require(0<args.remaining_seconds<=1200 and 512<=args.memory_mib<=8192,
            "Explicit shared mathematical time and memory budget")
    resource.setrlimit(resource.RLIMIT_AS,(args.memory_mib*1024**2,args.memory_mib*1024**2))
    sys.set_int_max_str_digits(0)
    began=time.monotonic();DEADLINE=began+max(.01,args.remaining_seconds-min(12,args.remaining_seconds/8))
    def request_stop(signum,frame):
        global STOP
        STOP=True
    signal.signal(signal.SIGTERM,request_stop)
    signal.signal(signal.SIGALRM,request_stop)
    signal.setitimer(signal.ITIMER_REAL,args.remaining_seconds)
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    identity={"format":FORMAT,"source":file_id(__file__),"upperSource":UPPER_SOURCE,
        "upperBinding":UPPER_BINDING,"upperRaw":UPPER_RAW,"upperRecord":UPPER_RECORD,
        "upperCoefficientSHA256":UPPER_COEFFICIENT_SHA,"coreSource":CORE_SOURCE,
        "coreBinding":CORE_BINDING,"corePayloadSHA256":CORE_PAYLOAD_SHA,
        "coreLogicalSHA256":CORE_LOGICAL_SHA,"knownFactors":FACTORS,
        "algorithm":"all56 rows; squarefree-unit Schur; exact support splits; upper-clamped finite precision"}
    binding=digest(canonical(identity))
    rec={"format":FORMAT,"binding":binding,"status":"started","events":[],
         "parameters":{"author":"Astra-ISP-789f / normal_annihilator",
            "aiAssisted":"GPT-6 Astra Pro","identity":identity,
            "remainingSeconds":args.remaining_seconds,"memoryMiB":args.memory_mib,
            "allLargeArraysTemporaryOnly":True,"oldDeterminantsNotRecomputed":True,
            "oldHermiteStateNotRead":True,"originalCoreNotRecomputed":True,
            "newNineTargetGlobalMembershipClaim":False}}
    cp=Checkpoints(out/"checkpoints",binding);state=None;result_record=None
    try:
        rec["parameters"]["tinyExactVerification"]=tiny_verification()
        A,U,meta=load_inputs(args);rec["parameters"]["inputs"]=meta
        groups=squarefree_groups(U)
        rec["parameters"]["squarefreeGroups"]=[dict(pstats(f),upperExponent=e) for f,e in groups]
        rec["parameters"]["actualUpperIsSquareOfSquarefreeDegree60"]=(len(groups)==1
            and groups[0][1]==2 and int(groups[0][0].degree())==60)
        state=cp.load()
        if state is None:
            state=initial_state(A,groups);cp.save(state)
            rec["parameters"]["resumed"]=False
        else:
            rec["parameters"]["resumed"]=True
            rec["parameters"]["startingGeneration"]=state["generation"]
        while state["pending"]:
            tick()
            newstate,event,closed_ops=advance(state,A)
            if closed_ops is not None:
                rr=cp.save_closed_operations(event["id"],closed_ops)
                newstate["closed"][-1]["operationCertificate"]=rr
            pointer=cp.save(newstate)
            state=newstate
            rec["events"]=(rec["events"]+[event])[-64:]
            rec["parameters"]["completedTransactionsThisCall"]=rec["parameters"].get("completedTransactionsThisCall",0)+1
            rec["parameters"]["lastWholeCheckpoint"]=pointer
        omega,quotient=finish_polynomials(state,U)
        require(all(int(omega.gcd(fmpq_poly(f)).degree())==0 for f in FACTORS),
                "Final exact gcd remains outside precisely the paid localization")
        obj={"format":FORMAT,"binding":binding,"monicExactOutsideGcd":encp(omega),
             "monicUpper":encp(U),"exactUpperQuotient":encp(quotient),
             "allOriginal56RowsCertified":True,"allSupportBranchesClosed":True,
             "exactGcdEqualsUpper":omega==U,"closedBranches":state["closed"],
             "completeStateSummary":state_summary(state)}
        result_record=save_gzip(out/"complete-original56-outside-gcd.json.gz",obj)
        rec["parameters"].update(
            completeOriginalOutsideGcdComputed=True,allOriginal56RowsCertified=True,
            allSupportBranchesClosed=True,exactGcdEqualsUpper=omega==U,
            exactOutsideGcdStatistics=pstats(omega),
            exactOutsideGcdPrimitiveCoefficientSHA256=digest(canonical(
                [str(x) for x in omega.numer().coeffs()])),
            originalOutsideDivisorOneProved=int(omega.degree())==0,
            actualCompleteCertificate=result_record,
            finalStateSummary=state_summary(state))
        rec["status"]="completed"
        rec["outcome"]="complete-original56-row-outside-maximal-minor-gcd"
    except BudgetStop as e:
        rec["status"]="budget-checkpoint";rec["message"]=str(e)
    except BaseException as e:
        rec["status"]="failed";rec["error"]={"type":type(e).__name__,"message":str(e)}
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        rec["elapsedSeconds"]=time.monotonic()-began
        rec["parameters"].setdefault("completeOriginalOutsideGcdComputed",False)
        rec["parameters"].setdefault("originalOutsideDivisorOneProved",False)
        if cp.pointer.exists():
            pp=json.loads(cp.pointer.read_text())
            rec["parameters"]["lastWholeCheckpoint"]=pp
        data=canonical(rec)
        require(len(data)<90000,"Only a small exact execution receipt may be published")
        atomic_bytes(out/"complete-original56-outside-gcd-receipt.json",data)
        print(data.decode("ascii"),flush=True)
    return 1 if rec["status"]=="failed" else (75 if rec["status"]=="budget-checkpoint" else 0)

if __name__=="__main__":
    raise SystemExit(main())
