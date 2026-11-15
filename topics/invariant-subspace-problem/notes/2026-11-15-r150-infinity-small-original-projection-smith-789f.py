#!/usr/bin/env python3
"""Exact original natural-infinity 224 by 155 projection Smith calculation.

Read the ACTUAL paid fifth cochains and test their support entry by entry.
Rebuild original pure/one-normal source rows.  Keep the 54 actual eq8 rows,
including their u^2 factor; eliminate the other 864 rows only by regular
multiples of those actual rows.  Compute Q and F31 series Schur complements,
retaining original 155-coordinate lifts.  Every Q lift is checked on all 6188
original source rows, with absent high-normal terms checked from the source
dictionaries.  Completeness requires 14 positive directions to exit, plus
the paid exact 13-dimensional generic kernel, not a guessed truncation.
All recomputable arrays remain in the temporary job directory.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import signal
import time

from flint import fmpq, fmpq_mat, nmod_mat

FORMAT="r150-infinity-small-original-projection-smith-v1"
CHECKPOINT_FORMAT="r150-infinity-small-projection-temporary-v1"
P=31
PINS={
 "generator":(15328,"2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"),
 "jet_actions":(10050,"2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"),
 "fifth_receipt":(22769,"17361fc2f385bbc1ffe8b843d185d0c3acd2998276579d08e5d76e8233eaf036"),
 "q13_receipt":(52012,"2057846f5adb75ed84f20a144f4cb2da436f9b1db5674612ac376f9b4b503248"),
 "field_full_receipt":(43322,"14f396c3969ea90694d06e6f26fe75299bf2e678381b491ddb6cb78b93826815"),
}
FIFTH_BINDING="ccacc20f5bf3e678c4b3fcab2090e25b84c72abb35440c9b0c8473fa007a8576"
FIFTH_MANIFEST=(2991,"911bfc575782bd81aa69bf98e47efab546bb0d4dd164370d943aaaebda1b5e34")
FIFTH_PACK=(171510,"0a7912065c0b03edfa8b1b0aea086729ddcc2ebfbe8fc890e6e06671c0bb01b2")
FIFTH_MATRIX="91416a4981ee7ec4331f9ab52aaa4dc01e4f8b84e16a11e48c407528b1a6f710"
FULL_FIELD_SPECTRUM=[1,1,1,1,3,4,4,4,5,6,7,8,10,11]
RANGES={
 "lambda0Normal0":(0,20),"lambda0Normal1":(20,155),
 "lambda1Normal0":(155,175),"lambda1Normal1":(175,310),
 "lambda2Normal0":(310,330),"lambda2Normal1":(330,465),
 "lambda2Normal2":(465,915),"lambda3Normal1":(915,1050),
 "lambda3Normal2":(1050,1500),"lambda4Normal1":(1500,1635),
 "lambda4Normal2":(1635,2085),"lambda4Normal3":(2085,3075),
 "lambda5Normal1":(3075,3210),"lambda5Normal2":(3210,3660),
 "lambda5Normal3":(3660,4650),
}
STOP=False
DEADLINE=0.0
OUT=None
REC=None

def require(ok,message):
    if not ok:
        raise ValueError(message)

def stop_requested(signum,frame):
    global STOP
    STOP=True

def check(label="next complete operation"):
    if STOP or time.monotonic()>=DEADLINE:
        raise TimeoutError("Saved complete temporary phases; stop before "+label)

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):
            h.update(b)
    return h.hexdigest()

def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")

def write_json(path,x):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    tmp.write_text(json.dumps(x,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    os.replace(tmp,path)

def small_event(event,**kw):
    REC["events"].append(dict(event=event,elapsedSeconds=time.monotonic()-REC["_start"],**kw))
    flush_receipt()

def flush_receipt():
    if OUT is None or REC is None:
        return
    x={k:v for k,v in REC.items() if not k.startswith("_")}
    x["elapsedSeconds"]=time.monotonic()-REC["_start"]
    write_json(OUT/"small-original-projection-smith-receipt.json",x)

def pinned_file(path,pin,label):
    path=Path(path)
    require(path.is_file() and path.stat().st_size==pin[0],label+" byte count")
    digest=sha(path)
    require(digest==pin[1],label+" SHA256")
    return {"bytes":pin[0],"sha256":digest}

def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def result_at(path):
    x=json.loads(Path(path).read_text())
    r=x.get("result",x)
    require(r.get("status")=="completed","Paid receipt incomplete: "+str(path))
    return r

def value(r,key):
    return r.get(key,r.get("parameters",{}).get(key))

def zero(M):
    return all(not M[i,j] for i in range(M.nrows()) for j in range(M.ncols()))

def mh(M):
    h=hashlib.sha256()
    h.update(("%d,%d\n"%(M.nrows(),M.ncols())).encode("ascii"))
    for i in range(M.nrows()):
        h.update(("\t".join(str(M[i,j]) for j in range(M.ncols()))+"\n").encode("ascii"))
    return h.hexdigest()

class Domain:
    def __init__(self,name):
        self.name=name
        require(name in ("Q","F31"),"Arithmetic domain")
    def mat(self,r,c,data=None):
        if self.name=="Q":
            return fmpq_mat(r,c) if data is None else fmpq_mat(r,c,list(data))
        return nmod_mat(r,c,[0]*(r*c) if data is None else [int(x)%P for x in data],P)
    def parse(self,x):
        return fmpq(x) if self.name=="Q" else int(x)%P
    def eye(self,n):
        return self.mat(n,n,[int(i==j) for i in range(n) for j in range(n)])
    def sub(self,M,rows,cols):
        rows=list(rows);cols=list(cols)
        return self.mat(len(rows),len(cols),[M[i,j] for i in rows for j in cols])
    def cat(self,blocks):
        require(bool(blocks) and len({M.nrows() for M in blocks})==1,"Horizontal join")
        nr=blocks[0].nrows()
        return self.mat(nr,sum(M.ncols() for M in blocks),
                        [M[i,j] for i in range(nr) for M in blocks for j in range(M.ncols())])
    def vcat(self,blocks):
        require(bool(blocks) and len({M.ncols() for M in blocks})==1,"Vertical join")
        return self.mat(sum(M.nrows() for M in blocks),blocks[0].ncols(),
                        [M[i,j] for M in blocks for i in range(M.nrows()) for j in range(M.ncols())])

DQ=Domain("Q")
DF=Domain("F31")

def pivots(R,rank):
    cols=[]
    for i in range(rank):
        p=next((j for j in range(R.ncols()) if R[i,j]),None)
        require(p is not None and R[i,p]==1,"Actual normalized RREF pivot")
        cols.append(p)
    require(cols==sorted(set(cols)),"RREF pivot order")
    return cols

def rank(M):
    return M.rref()[1]

def enc(x):
    if hasattr(x,"nrows") and hasattr(x,"ncols"):
        return {"_exactMatrix":True,"shape":[x.nrows(),x.ncols()],
                "rows":[[str(x[i,j]) for j in range(x.ncols())] for i in range(x.nrows())]}
    if isinstance(x,dict):
        return {k:enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):
        return [enc(v) for v in x]
    return x

def dec(x,d):
    if isinstance(x,dict) and x.get("_exactMatrix") is True:
        r,c=x["shape"];rows=x["rows"]
        require(len(rows)==r and all(len(v)==c for v in rows),"Stored full matrix dimensions")
        return d.mat(r,c,[d.parse(v) for row in rows for v in row])
    if isinstance(x,dict):
        return {k:dec(v,d) for k,v in x.items()}
    if isinstance(x,list):
        return [dec(v,d) for v in x]
    return x

class Store:
    def __init__(self,path,binding):
        self.path=Path(path);self.path.mkdir(parents=True,exist_ok=True)
        self.binding=binding;self.manpath=self.path/"small-projection-checkpoints.json"
        if self.manpath.exists():
            self.man=json.loads(self.manpath.read_text())
            require(self.man.get("format")==CHECKPOINT_FORMAT and
                    self.man.get("binding")==binding and self.man.get("temporaryOnly") is True,
                    "Temporary checkpoint semantic binding")
        else:
            self.man={"format":CHECKPOINT_FORMAT,"binding":binding,"temporaryOnly":True,"phases":{}}
    def save(self,name,data,d):
        payload={"format":CHECKPOINT_FORMAT,"binding":self.binding,"phase":name,
                 "domain":d.name,"complete":True,"data":enc(data)}
        tmp=self.path/(name+".tmp.json.gz")
        with gzip.open(tmp,"wt",encoding="utf-8",compresslevel=1) as f:
            json.dump(payload,f,sort_keys=True,separators=(",",":"))
        digest=sha(tmp);dest=self.path/(name+"-"+digest+".json.gz")
        os.replace(tmp,dest)
        item={"file":dest.name,"bytes":dest.stat().st_size,"sha256":digest}
        self.man["phases"][name]=item
        write_json(self.manpath,self.man)
        REC["parameters"]["temporaryPhaseFiles"]=self.man["phases"]
        REC["parameters"]["temporaryManifestSHA256"]=sha(self.manpath)
        flush_receipt()
        return item
    def load(self,name,d):
        item=self.man["phases"].get(name)
        if item is None:
            return None
        path=self.path/item["file"]
        require(path.resolve().parent==self.path.resolve(),"Checkpoint filename")
        pinned_file(path,(item["bytes"],item["sha256"]),"Temporary "+name)
        with gzip.open(path,"rt",encoding="utf-8") as f:
            obj=json.load(f)
        require(obj.get("format")==CHECKPOINT_FORMAT and obj.get("binding")==self.binding and
                obj.get("phase")==name and obj.get("domain")==d.name and obj.get("complete") is True,
                "Complete temporary phase identity")
        REC["parameters"].setdefault("resumedPhases",[]).append(name)
        return dec(obj["data"],d)

def coefficient_encode(c):
    return {
        "chart":c["chart"],"maxOrder":c["maxOrder"],"physical":c["physical"],
        "pure":[[str(x) for x in row] for row in c["pure"]],
        "linear":{str(j):[[[str(x) for x in row] for row in mode] for mode in modes]
                  for j,modes in c["linear"].items()},
        "quadratic":[[a,b,[[str(x) for x in row] for row in q]]
                     for (a,b),q in sorted(c["quadratic"].items())],
    }

def coefficient_decode(c):
    return {
        "chart":c["chart"],"maxOrder":c["maxOrder"],"physical":c["physical"],
        "pure":[[fmpq(x) for x in row] for row in c["pure"]],
        "linear":{int(j):[[[fmpq(x) for x in row] for row in mode] for mode in modes]
                  for j,modes in c["linear"].items()},
        "quadratic":{(a,b):[[fmpq(x) for x in row] for row in q]
                     for a,b,q in c["quadratic"]},
    }

def poly_product(a,b):
    out=[fmpq(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def read_paid_fifth(a,m):
    p=Path(a.fifth_checkpoint_dir)
    manpath=p/"fifth-joint-high-low-checkpoint.json"
    pinned_file(manpath,FIFTH_MANIFEST,"Paid fifth manifest")
    man=json.loads(manpath.read_text())
    require(man.get("format")=="r150-infinity-fifth-shifted-incoming-temporary-v1" and
            man.get("binding")==FIFTH_BINDING and man.get("temporaryOnly") is True,
            "Actual fifth manifest semantic identity")
    entry=man["phases"]["actual-fifth-cochains-verified"]
    require((entry["bytes"],entry["sha256"])==FIFTH_PACK,"Paid actual fifth pack pin")
    file=p/entry["file"]
    require(file.resolve().parent==p.resolve(),"Paid fifth pack path")
    pinned_file(file,FIFTH_PACK,"Paid actual fifth cochains")
    with gzip.open(file,"rt",encoding="utf-8") as f:
        obj=json.load(f)
    require(obj.get("complete") is True and obj.get("phase")=="actual-fifth-cochains-verified"
            and obj.get("binding")==FIFTH_BINDING and obj.get("shape")==[4650,18],
            "Paid actual fifth full cochain payload")
    rows=obj["matrix"]
    require(len(rows)==4650 and all(len(r)==18 for r in rows),"Paid full fifth entries")
    M=fmpq_mat([[fmpq(x) for x in row] for row in rows])
    require(mh(M)==FIFTH_MATRIX==obj["matrixSHA256"],"Paid fifth canonical arithmetic matrix")
    meta=obj["metadata"]
    require(meta.get("fullOriginalVerificationComplete") is True and
            meta.get("allSixOrdersAll6188OriginalSourceRowsVerified") is True,
            "Paid original fifth product scope")
    actual=result_at(a.fifth_receipt)
    ranges=value(actual,"newCochainRanges")
    sections={}
    zero_entries=0
    for name,(lo,hi) in RANGES.items():
        require((ranges[name]["start"],ranges[name]["stop"])==(lo,hi),"Paid range "+name)
        X=DQ.sub(M,range(lo,hi),range(18))
        require(mh(X)==ranges[name]["matrixSHA256"],"Paid block hash "+name)
        sections[name]=X
        if name not in ("lambda0Normal0","lambda0Normal1") and not name.endswith("Normal1"):
            require(zero(X),"Actual entries outside pure/one-normal support: "+name)
            zero_entries+=X.nrows()*X.ncols()
    leading=DQ.vcat([sections["lambda0Normal0"],sections["lambda0Normal1"]])
    require(rank(leading)==18,"Actual pure/one-normal fifth leading rank18")
    L=[]
    for k in range(6):
        pure=sections.get("lambda%dNormal0"%k,DQ.mat(20,18))
        one=sections["lambda%dNormal1"%k]
        L.append(DQ.vcat([pure,one]))
    info={
        "actualFifthCochainSHA256":FIFTH_MATRIX,
        "allPaidHigherNormalEntriesExactlyZero":True,
        "allPaidPositiveOrderPureEntriesExactlyZero":True,
        "paidZeroEntriesActuallyTested":zero_entries,
        "actualFifthPureAndOneNormalLeadingRank":18,
        "actualFifthCanonicalSourcePackSHA256":FIFTH_PACK[1],
    }
    REC["parameters"].update(info)
    small_event("actual-fifth-support-read-and-verified",leadingRank=18,zeroEntries=zero_entries)
    return L

def build_projection(a,m,j,store):
    old=store.load("original-projection-coefficients",DQ)
    if old is not None:
        return coefficient_decode(old["coefficients"]),old["P"],old["metadata"]
    check("original natural coefficient generation")
    c=j.original_coefficients(m,"infinity",a.degree)
    N=a.degree
    source0=j.source_rows(0);source1=j.source_rows(1)
    targets0=j.target_columns(0);targets1=j.target_columns(1)
    require([len(j.source_rows(r)) for r in range(4)]==[170,918,2295,2805],
            "Original6188 source partition")
    require([len(j.target_columns(r)) for r in range(6)]==[20,135,450,990,1485,1287],
            "Original4367 output partition")
    require(len(set(source0+source1))==1088,"Original distinct source records")
    chosen=[i for i,row in enumerate(source1) if row[0]==8]
    require(len(chosen)==54,"Actual54 eq8 one-normal source rows")
    group={(a0,b,mon):i for i,(eq,a0,b,mon) in enumerate(source1) if eq==8}
    require(len(group)==54,"Actual eq8 source group dictionary")
    ix0={v:i for i,v in enumerate(targets0)}
    ix1={v:i for i,v in enumerate(targets1)}
    K=[[fmpq(m.ORIGINAL_K[5-i][5-jj]) for jj in range(6)] for i in range(6)]
    fullpure=[[fmpq(0)]*17 for _ in range(15)]
    for t,g in {2:-2,3:-8,4:24}.items():
        for aa in range(6):
            for bb in range(6):
                for ii in range(6):
                    for jj in range(6):
                        fullpure[t+aa+bb][ii+jj]+=4*g*K[ii][aa]*K[jj][bb]
    require(all(c["pure"][k]==fullpure[k] if k<15 else
                c["pure"][k]==[fmpq(0)]*17 for k in range(N+1)),
            "All17 actual pure coefficients match whole natural geometric polynomials")
    require(all(not fullpure[k][eq] for k in (0,1) for eq in range(17)),
            "Whole original pure equations divisible by u^2")
    require(fullpure[2][8]==-8,"Actual eq8 F8/u^2 constant -8")
    denominator=[fullpure[k][8] for k in range(2,15)]
    numerators=[[fullpure[k][eq] for k in range(2,15)] for eq in range(17)]
    ratios=[]
    for eq in range(17):
        check("regular original-row ratio")
        rr=[]
        for k in range(max(0,N-1)):
            s=numerators[eq][k] if k<len(numerators[eq]) else fmpq(0)
            for v in range(1,min(k,len(denominator)-1)+1):
                s-=denominator[v]*rr[k-v]
            rr.append(s/denominator[0])
        for k in range(N+1):
            z=sum((fullpure[i][8]*rr[k-i] for i in range(2,min(k,14)+1)
                   if k-i<len(rr)),fmpq(0))
            require(z==c["pure"][k][eq],"Regular row ratio complete prefix")
        # This records the whole rational ratio q_eq/q_8, without inverting u.
        A=poly_product(numerators[eq],[fullpure[k][8] for k in range(15)])
        B=poly_product(denominator,[fullpure[k][eq] for k in range(15)])
        require(A==B,"Whole pure-polynomial row-multiple identity")
        ratios.append(rr)
    PM=[]
    for k in range(N+1):
        check("original projection coefficient "+str(k))
        top=DQ.cat([j.block(m,c,k,0,0),j.block(m,c,k,0,1)])
        bottom=DQ.mat(54,155)
        for r,si in enumerate(chosen):
            eq,aa,bb,mon=source1[si]
            for col,v in j.sparse_row_terms(c,k,source1[si],1,ix1):
                bottom[r,20+col]+=v
            require(bottom[r,20+ix1[(aa,bb+2,mon)]]==c["pure"][k][8],
                    "Actual selected original row retains F8")
        PM.append(DQ.vcat([top,bottom]))
        # All 918 projected one-normal rows are checked with their original keys.
        for row in source1:
            eq,aa,bb,mon=row
            terms0=list(j.sparse_row_terms(c,k,row,0,ix0))
            terms1=list(j.sparse_row_terms(c,k,row,1,ix1))
            expected=[] if not c["pure"][k][eq] else [(ix1[(aa,bb+2,mon)],c["pure"][k][eq])]
            require(not terms0 and terms1==expected,"All actual918 projected original rows")
            require((aa,bb,mon) in group,"Every eliminated row has its actual eq8 row")
        # The remaining 5100 source rows have no term in any retained target.
        for sd in (2,3):
            for row in j.source_rows(sd):
                require(not list(j.sparse_row_terms(c,k,row,0,ix0)) and
                        not list(j.sparse_row_terms(c,k,row,1,ix1)),
                        "Actual original high-normal source has no projected term")
    require(rank(PM[0])==128,"Actual constant projection rank128")
    metadata={
        "projectionShape":[224,155],"allOriginalSourceRows":6188,
        "pureSourceRows":170,"oneNormalSourceRows":918,
        "retainedActualEq8Rows":54,"regularlyEliminatedActualRows":864,
        "identicallyZeroProjectedHighSourceRows":5100,
        "actualConstantRank":128,"pureDenominatorUnitConstant":"-8",
        "actualF8Valuation":2,"wholePureNumeratorCoefficients":[[str(x) for x in r] for r in numerators],
        "wholePureDenominatorCoefficients":[str(x) for x in denominator],
        "all17WholePureGeometricPolynomialsVerified":True,
        "all918ActualOriginalProjectedRowsVerified":True,
        "all5100HigherNormalOriginalSourceRowsExactlyZero":True,
        "regularOriginalRowOperationsRetainU2Factor":True,
        "actualRetainedEq8SourceIndicesWithinOneNormal":chosen,
        "originalCoefficientOrder":N,
        "originalProjectionCoefficientSHA256":[mh(X) for X in PM],
        "originalPhysicalCoefficientHashes":c["physical"],
    }
    store.save("original-projection-coefficients",
               {"coefficients":coefficient_encode(c),"P":PM,"metadata":metadata},DQ)
    small_event("original-224-by-155-projection-complete",constantRank=128,degree=N)
    return c,PM,metadata

def fq_parts(x):
    s=str(x)
    a,b=s.split("/",1) if "/" in s else (s,"1")
    return int(a),int(b)

def reduce_field(M):
    data=[]
    for i in range(M.nrows()):
        for j in range(M.ncols()):
            n,d=fq_parts(M[i,j])
            require(d%P,"Original rational coefficient has nonunit31 denominator")
            data.append((n%P)*pow(d%P,-1,P)%P)
    return DF.mat(M.nrows(),M.ncols(),data)

def convolution(A,B,N,d):
    require(A and B and A[0].ncols()==B[0].nrows(),"Series multiplication shape")
    anz=[not zero(X) for X in A];bnz=[not zero(X) for X in B]
    out=[]
    for k in range(N+1):
        check("complete series product coefficient")
        X=d.mat(A[0].nrows(),B[0].ncols())
        for i in range(max(0,k-len(B)+1),min(k,len(A)-1)+1):
            if anz[i] and bnz[k-i]:
                X+=A[i]*B[k-i]
        out.append(X)
    return out

def unit_schur(A,d,r):
    """All rows are retained; no pivot-row solution is mistaken for full solve."""
    N=len(A)-1;nr=A[0].nrows();nc=A[0].ncols()
    R,rr=A[0].rref();require(rr==r and 0<r<=min(nr,nc),"Actual unit rank")
    pc=pivots(R,r)
    Cp=d.sub(A[0],range(nr),pc)
    Rt,rt=Cp.transpose().rref()
    require(rt==r,"Actual independent unit columns")
    pr=pivots(Rt,r)
    rs=[i for i in range(nr) if i not in set(pr)]
    cs=[i for i in range(nc) if i not in set(pc)]
    U=[d.sub(X,pr,pc) for X in A]
    B=[d.sub(X,pr,cs) for X in A]
    C=[d.sub(X,rs,pc) for X in A]
    D=[d.sub(X,rs,cs) for X in A]
    inv=U[0].inv()
    require(inv*U[0]==d.eye(r) and U[0]*inv==d.eye(r),"Actual two-sided constant-unit inverse")
    Q=[]
    unz=[not zero(X) for X in U]
    for k in range(N+1):
        check("complete unit-series coefficient")
        rhs=B[k]
        for i in range(1,k+1):
            if unz[i]:
                rhs=rhs-U[i]*Q[k-i]
        Q.append(inv*rhs)
    unitcheck=convolution(U,Q,N,d)
    require(all(unitcheck[k]==B[k] for k in range(N+1)),
            "All original selected unit-row series products")
    CQ=convolution(C,Q,N,d)
    S=[D[k]-CQ[k] for k in range(N+1)]
    require(zero(S[0]),"Complete residual constant vanishes after actual rank elimination")
    T=[]
    for k in range(N+1):
        X=d.mat(nc,len(cs))
        if k==0:
            for v,j in enumerate(cs):
                X[j,v]=1
        for i,j in enumerate(pc):
            for v in range(len(cs)):
                X[j,v]=-Q[k][i,v]
        T.append(X)
    direct=convolution(A,T,N,d)
    for k in range(N+1):
        require(zero(d.sub(direct[k],pr,range(len(cs)))) and
                d.sub(direct[k],rs,range(len(cs)))==S[k],
                "All retained original rows of unit Schur identity")
    profile={"rank":r,"unitRows":pr,"unitColumns":pc,
             "allUnitAndResidualRowsVerified":True,
             "unitOriginalProductCoordinates":(N+1)*nr*len(cs),
             "constantInverseSHA256":mh(inv)}
    return S,T,profile

def smith(Pseries,d,store,N):
    name=d.name+"-smith-state"
    state=store.load(name,d)
    if state is None:
        require(rank(Pseries[0])==128,"Actual projection constant rank in "+d.name)
        S,T,prof=unit_schur(Pseries,d,128)
        require(len(T)==N+1 and T[0].nrows()==155 and T[0].ncols()==27,
                "Original155 constant-kernel lift")
        require(zero(Pseries[0]*T[0]) and rank(T[0])==27,
                "Complete27 original constant heads")
        state={"level":0,"series":S,"map":T,"positive":[],"steps":[],
               "constantUnit":prof,"complete":False}
        store.save(name,state,d)
    require(len(state["map"])==N+1,"Stored full original map precision")
    while sum(g["map"][0].ncols() for g in state["positive"])<14:
        check(d.name+" next actual Smith layer")
        A=state["series"];level=state["level"]
        if not A:
            break
        r=rank(A[0])
        if r==0:
            state["series"]=A[1:]
            state["level"]=level+1
            state["steps"].append({"order":level,"rank":0,"remainingColumns":A[0].ncols()})
            store.save(name,state,d)
            continue
        require(level>=1,"No forgotten constant units")
        paid=sum(g["map"][0].ncols() for g in state["positive"])
        require(paid+r<=14,"Projection exceeds paid generic rank142")
        R,rr=A[0].rref();pc=pivots(R,rr)
        active=[d.sub(X,range(155),pc) for X in state["map"]]
        S,T,profile=unit_schur(A,d,r)
        newmap=convolution(state["map"],T,N,d)
        state["positive"].append({"exponent":level,"map":active})
        state["map"]=newmap
        state["series"]=S
        state["steps"].append({"order":level,"rank":r,"remainingColumns":S[0].ncols(),
                               "unitProfile":profile})
        store.save(name,state,d)
        small_event("actual-projection-Smith-units",domain=d.name,order=level,
                    rank=r,positiveDirections=paid+r)
    count=sum(g["map"][0].ncols() for g in state["positive"])
    if count==14:
        require(state["map"][0].ncols()==13 and all(zero(X) for X in state["series"]),
                "Paid generic rank plus complete residual13")
        state["complete"]=True
        store.save(name,state,d)
    heads=d.cat([g["map"][0] for g in state["positive"]]+[state["map"][0]])
    require(heads.ncols()==27 and rank(heads)==27,"All active/free original constant heads independent")
    exponents=[g["exponent"] for g in state["positive"] for _ in range(g["map"][0].ncols())]
    info={"domain":d.name,"constantRank":128,"knownGenericRank":142,"freeRank":13,
          "positiveIndices":exponents,"positiveDirections":count,
          "positiveLength":sum(exponents),"maxPositiveIndex":max(exponents,default=0),
          "complete":state["complete"],"availableTaylorDegree":N,
          "remainingConstantHeads":state["map"][0].ncols(),
          "remainingPositiveIndicesAtLeast":0 if state["complete"] else state["level"],
          "all27ActiveAndFreeHeadsIndependent":True,"headMatrixSHA256":mh(heads),
          "steps":[{"order":v["order"],"rank":v["rank"],
                    "remainingColumns":v["remainingColumns"]} for v in state["steps"]]}
    REC["parameters"][d.name+"ProjectionSmith"]=info
    flush_receipt()
    return state,info

def original_product(m,j,c,Top,oneindex,L,k):
    """Actual all1088 nontrivial original rows; other5100 rows were checked empty."""
    width=L[0].ncols()
    upper=DQ.mat(170,width)
    for i in range(k+1):
        if i<len(Top) and k-i<len(L):
            upper+=Top[i]*L[k-i]
    lower=DQ.mat(918,width)
    rows=j.source_rows(1)
    for rr,(eq,aa,bb,mon) in enumerate(rows):
        col=20+oneindex[(aa,bb+2,mon)]
        for i in range(min(k,len(c["pure"])-1)+1):
            if k-i>=len(L):
                continue
            v=c["pure"][i][eq]
            if v:
                for z in range(width):
                    if L[k-i][col,z]:
                        lower[rr,z]+=v*L[k-i][col,z]
    return upper,lower

def verify_original(m,j,c,PM,state,N,paid_fifth):
    check("original6188 verification")
    Top=[DQ.sub(X,range(170),range(155)) for X in PM]
    oneindex={v:i for i,v in enumerate(j.target_columns(1))}
    coordinates=0
    for k in range(6):
        check("actual paid fifth original product")
        A,B=original_product(m,j,c,Top,oneindex,paid_fifth,k)
        require(zero(A) and zero(B),"Paid actual18 fifth cochains on newly rebuilt original coefficients")
        coordinates+=6188*18
    REC["parameters"]["paidFifthOriginalProductCoordinatesRechecked"]=coordinates
    REC["parameters"]["allActualFifthCoefficientsRecheckedOnOriginal6188Sources"]=True
    coordinates=0
    active_info=[]
    eq8=[i for i,row in enumerate(j.source_rows(1)) if row[0]==8]
    for g in state["positive"]:
        e=g["exponent"];L=g["map"];r=L[0].ncols()
        for k in range(e):
            check("actual positive Smith lift original product")
            A,B=original_product(m,j,c,Top,oneindex,L,k)
            require(zero(A) and zero(B),"Actual original6188 positive Smith lift")
            coordinates+=6188*r
        A,B=original_product(m,j,c,Top,oneindex,L,e)
        leading=DQ.vcat([A,DQ.sub(B,eq8,range(r))])
        require(rank(leading)==r,"Original leading obstruction has its actual unit rank")
        active_info.append({"exponent":e,"columns":r,
                            "originalLeadingProductSHA256":mh(leading),
                            "originalHeadSHA256":mh(L[0])})
    L=state["map"]
    cutoff=N+1 if state["complete"] else min(state["level"],N+1)
    for k in range(cutoff):
        check("remaining original free-jet product")
        A,B=original_product(m,j,c,Top,oneindex,L,k)
        require(zero(A) and zero(B),"All original6188 remaining source products")
        coordinates+=6188*L[0].ncols()
    REC["parameters"].update({
        "allOriginal6188PositiveAndRemainingJetProductsZero":True,
        "newOriginalSourceProductCoordinates":coordinates,
        "positiveOriginalLifts":active_info,
        "remainingOriginalJetCount":L[0].ncols(),
        "remainingOriginalJetVerifiedThroughOrder":cutoff-1,
        "original155TargetCoordinatesRetained":True,
        "allSourceNormalDegreesZeroThroughThreeRetained":True,
        "noHigherNormalSurjectivityAssumed":True,
        "finiteFreeJetsNotClaimedAsWholeRationalKernel":True,
    })
    return coordinates

def main():
    global DEADLINE,OUT,REC
    ap=argparse.ArgumentParser()
    ap.add_argument("--generator",required=True)
    ap.add_argument("--jet-actions",required=True)
    ap.add_argument("--fifth-checkpoint-dir",required=True)
    ap.add_argument("--fifth-receipt",required=True)
    ap.add_argument("--q13-receipt",required=True)
    ap.add_argument("--field-full-receipt",required=True)
    ap.add_argument("--degree",type=int,default=11)
    ap.add_argument("--out",required=True)
    ap.add_argument("--remaining-seconds",type=float,default=180)
    ap.add_argument("--memory-mib",type=int,default=2048)
    a=ap.parse_args()
    require(5<=a.degree<=17 and 0<a.remaining_seconds<=600,"Finite degree/budget")
    require(512<=a.memory_mib<=4096,"Memory bound")
    started=time.monotonic();reserve=min(8.0,a.remaining_seconds/10)
    DEADLINE=started+a.remaining_seconds-reserve
    OUT=Path(a.out);OUT.mkdir(parents=True,exist_ok=True)
    signal.signal(signal.SIGTERM,stop_requested);signal.signal(signal.SIGINT,stop_requested)
    soft,hard=resource.getrlimit(resource.RLIMIT_AS)
    cap=a.memory_mib*1024*1024
    if hard!=resource.RLIM_INFINITY:
        cap=min(cap,hard)
    resource.setrlimit(resource.RLIMIT_AS,(cap,hard))
    REC={"format":FORMAT,"status":"running","outcome":"pending-original-input-verification",
         "scriptSHA256":sha(__file__),"arithmetic":"exact Q and F31 original finite jets",
         "parameters":{"sharedMathematicalSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
            "TaylorDegree":a.degree,"largeDataUploadedOrCommitted":False,
            "largeRecomputableDataPersisted":False,"temporaryOnly":True,
            "characteristicZeroHigherQuotient26NotClaimed":True,
            "selectedMinorLeading31UnitNotClaimed":True},
         "events":[],"_start":started}
    exitcode=1
    try:
        inputs={}
        for key,pin in PINS.items():
            inputs[key]=pinned_file(getattr(a,key),pin,key)
        q13=result_at(a.q13_receipt)
        for key in ("primitiveFormalKernelProved","all155NormalizedCoefficientsRegular",
                    "all80444CoMovingOriginalSourceProductsZero",
                    "all4367OriginalOutputCoordinatesTransported",
                    "sameOriginalNaturalUAndReversedPhysicalKernelVerified",
                    "samePaidOriginalFree13IdentityVerified",
                    "sourceAndOutputChangesArePolynomialUnits"):
            require(value(q13,key) is True,"Paid generic original13 scope: "+key)
        require(value(q13,"primitiveFormalKernelRank")==13 and
                value(q13,"coefficientwise31UnitRepresentationVerified") is True,
                "Paid generic13 normalized31-integral kernel")
        scales=q13["parameters"]["actual17ConstantRowScales"]
        require(len(scales)==17,"Paid full17 original constant row scales")
        scale_residues=[]
        for s in scales:
            n,d=fq_parts(fmpq(s))
            require(n%P and d%P,"Same original row scale is a31 unit")
            scale_residues.append((n%P)*pow(d%P,-1,P)%P)
        REC["parameters"]["all17OriginalRowScalesActually31Units"]=True
        REC["parameters"]["actualOriginalRowScalesModulo31"]=scale_residues
        fifth=result_at(a.fifth_receipt)
        require(value(fifth,"fullFirstFiveRanks")==[4,0,1,3,1] and
                value(fifth,"allSixOrdersAll6188OriginalSourceRowsVerified") is True,
                "Paid fifth actual full original scope")
        field=result_at(a.field_full_receipt)
        # Paid full spectrum is pinned in bytes; the small projection is recomputed.
        require(value(field,"status")=="completed" and
                value(field,"fullConstantRankModulo31")==4340 and
                value(field,"fullGenericRankModulo31")==4354 and
                value(field,"fullInfinityTorsionLengthModulo31")==66 and
                value(field,"fullInfinityMaximumPositiveExponentModulo31")==11 and
                value(field,"fullOriginalFreeCokernelRank")==13 and
                field["parameters"]["smallSeriesSmith"]["paidExponents"]==FULL_FIELD_SPECTRUM and
                field["parameters"]["smallSeriesSmith"]["complete"] is True,
                "Paid full field original spectrum and free-rank identity")
        named={"source":sha(__file__),"inputs":inputs,"degree":a.degree,
               "fifthManifestSHA256":FIFTH_MANIFEST[1],"fifthPackSHA256":FIFTH_PACK[1],
               "format":FORMAT,"naturalParameter":"u=1/s","chart":"original infinity"}
        binding=hashlib.sha256(canonical(named)).hexdigest()
        REC["parameters"]["semanticBinding"]=binding
        REC["parameters"]["inputFiles"]=inputs
        REC["parameters"]["sameOriginalQ13PrimitiveKernelRead"]=True
        m=module_at("r150_small_original_first",a.generator)
        j=module_at("r150_small_original_actions",a.jet_actions)
        L5=read_paid_fifth(a,m)
        store=Store(OUT/"temporary",binding)
        c,PM,meta=build_projection(a,m,j,store)
        REC["parameters"]["originalProjection"]=meta
        check("actual small field projection")
        PF=[reduce_field(X) for X in PM]
        fstate,finfo=smith(PF,DF,store,a.degree)
        require(finfo["complete"],"Small field projection requires greater Taylor degree")
        REC["parameters"]["allActualProjectionCoefficients31Integral"]=True
        REC["parameters"]["fieldProjectionEqualsPaidFullSpectrum"]=(finfo["positiveIndices"]==FULL_FIELD_SPECTRUM)
        qstate,qinfo=smith(PM,DQ,store,a.degree)
        verify_original(m,j,c,PM,qstate,a.degree,L5)
        require(qinfo["positiveLength"]<=66,"Projection Q torsion cannot exceed paid full-field upper66")
        REC["parameters"]["QGenericProjectionRank142Verified"]=bool(qinfo["complete"])
        REC["parameters"]["paidGeneric13ProvidesUpperRank142"]=True
        REC["parameters"]["projectionIsActualOriginalCokernelQuotient"]=True
        REC["parameters"]["projectionAndFullHaveEqualGenericFreeRank13"]=True
        REC["parameters"]["QProjectionSpectrumEqualsActualFieldProjection"]=(qinfo["complete"] and
                                  qinfo["positiveIndices"]==finfo["positiveIndices"])
        REC["parameters"]["QProjectionSpectrumEqualsPaidFullField"]=(qinfo["complete"] and
                                  qinfo["positiveIndices"]==FULL_FIELD_SPECTRUM)
        if qinfo["complete"]:
            REC["status"]="completed"
            REC["outcome"]="complete-characteristic-zero-original-projection-smith"
            REC["characteristicZeroProjectionLength"]=qinfo["positiveLength"]
            REC["characteristicZeroProjectionPositiveIndices"]=qinfo["positiveIndices"]
            REC["characteristicZeroProjectionFreeRank"]=13
            if qinfo["positiveLength"]==66:
                # Actual original cokernel surjection with equal free rank and
                # equal torsion length is an isomorphism on torsion; this is
                # stronger than comparing two unrelated totals.
                REC["fullOriginalCharacteristicZeroTorsionLength"]=66
                REC["fullOriginalCharacteristicZeroPositiveIndices"]=qinfo["positiveIndices"]
                REC["fullOriginalCharacteristicZeroSpectrumProved"]=True
                REC["parameters"]["fullToProjectionTorsionIsomorphismBySurjectionAndEqualLength"]=True
                REC["parameters"]["fullQAndF31AllSmithIndicesActuallyEqual"]=(qinfo["positiveIndices"]==FULL_FIELD_SPECTRUM)
                REC["outcome"]="complete-projection-and-full-characteristic-zero-smith"
            else:
                REC["fullOriginalCharacteristicZeroSpectrumProved"]=False
                REC["parameters"]["fullOriginalCharacteristicZeroLengthLowerBound"]=max(54,qinfo["positiveLength"])
                REC["parameters"]["fullOriginalCharacteristicZeroLengthUpperBound"]=66
            exitcode=0
        else:
            REC["status"]="completed-prefix"
            REC["outcome"]="original-projection-needs-higher-Taylor-precision"
            REC["fullOriginalCharacteristicZeroSpectrumProved"]=False
            exitcode=75
    except TimeoutError as e:
        REC["status"]="checkpointed-time-budget-or-signal"
        REC["outcome"]="complete-temporary-phases-retained"
        REC["parameters"]["stoppingReason"]=str(e)
        exitcode=75
    except Exception as e:
        REC["status"]="failed"
        REC["outcome"]="original-projection-check-failed"
        REC["parameters"]["exceptionType"]=type(e).__name__
        REC["parameters"]["exception"]=str(e)
        exitcode=1
    finally:
        flush_receipt()
        print(json.dumps({"status":REC["status"],"outcome":REC["outcome"],
                          "receipt":str(OUT/"small-original-projection-smith-receipt.json"),
                          "elapsedSeconds":time.monotonic()-started},sort_keys=True))
    return exitcode

if __name__=="__main__":
    raise SystemExit(main())
