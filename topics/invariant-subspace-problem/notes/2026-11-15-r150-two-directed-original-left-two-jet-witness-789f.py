#!/usr/bin/env python3
"""Directed ORIGINAL s=2 left-two-jet / nine-square obstruction test.

Author: Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro.
The original equations are rebuilt at s=2+t, not transported from a zero jet.
The first pure coefficient is NONZERO and is retained in every source row.
Constant heads are the paid COMPLETE 22-dimensional original kernel.
New corrections are deliberately restricted: lambda1 normal degree<=2,
lambda2 normal degree<=3. A nonzero true pairing disproves local membership;
zero pairings DO NOT prove membership or complete higher-connection ranks.
All 6188 original source rows are verified for every accepted cochain.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from math import comb, gcd
from pathlib import Path
import os
import resource
import signal
import sys
import time

GEN_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACT_SHA="2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
UNIT_SHA="36356983e71ee1e67677da1a7a5f7aebf2987db282a5447a741b6a6af93084d5"
CONST_SHA="5d83b8784ea4e1d2b99f9ccd8881dcf6f2abe4241586219a3b459541c10d6272"

def require(ok,msg):
    if not ok: raise AssertionError(msg)
req=require
class SafeStop(Exception): pass

def canonical_bytes(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),
                      ensure_ascii=True).encode("ascii")
def small_hash(x):
    return hashlib.sha256(canonical_bytes(x)).hexdigest()
def file_sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod
def atomic_json(path,obj):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=canonical_bytes(obj)
    tmp=path.with_name(path.name+".tmp");tmp.write_bytes(raw);os.replace(tmp,path)
def guard(a,label,reserve=0):
    if time.monotonic()+reserve>=a._deadline:
        raise SafeStop("Shared time exhausted before "+label)
def manifest(a,binding):
    p=Path(a.checkpoint_dir)/"manifest.json"
    if p.exists():
        x=json.loads(p.read_bytes())
        require(x["binding"]==binding,"Portable original input binding")
        return x
    return {"format":"r150-two-directed-left-jet-cache-v1","binding":binding,
            "temporaryOnly":True,"phases":{}}
def phase_summary(name,item,result):
    result["parameters"].setdefault("checkpointPhases",{})[name]={
        k:item[k] for k in ("shape","matrixSHA256","fileSHA256","bytes","verified")}
def save_matrix(m,a,binding,name,M,meta,result,verified):
    guard(a,"save "+name,0)
    obj={"binding":binding,"phase":name,
         "shape":[M.nrows(),M.ncols()],"matrixSHA256":m.matrix_hash(M),
         "rows":[[str(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())],
         "metadata":meta,"verified":bool(verified)}
    raw=canonical_bytes(obj);payload=hashlib.sha256(raw).hexdigest()
    root=Path(a.checkpoint_dir);root.mkdir(parents=True,exist_ok=True)
    p=root/(name+"-"+payload+".json.gz")
    if not p.exists():
        tmp=p.with_name(p.name+".tmp")
        with tmp.open("wb") as f:
            with gzip.GzipFile(filename="",mode="wb",fileobj=f,mtime=0,
                               compresslevel=1) as z: z.write(raw)
        os.replace(tmp,p)
    item={"file":p.name,"shape":obj["shape"],"matrixSHA256":obj["matrixSHA256"],
          "payloadSHA256":payload,"fileSHA256":file_sha(p),
          "bytes":p.stat().st_size,"verified":bool(verified)}
    man=manifest(a,binding);man["phases"][name]=item
    atomic_json(root/"manifest.json",man);phase_summary(name,item,result)
def load_matrix(m,a,binding,name,result):
    man=manifest(a,binding);item=man["phases"].get(name)
    if item is None: return None
    p=Path(a.checkpoint_dir)/item["file"]
    require(p.stat().st_size==item["bytes"] and file_sha(p)==item["fileSHA256"],
            "Immutable phase bytes "+name)
    raw=gzip.decompress(p.read_bytes())
    require(hashlib.sha256(raw).hexdigest()==item["payloadSHA256"],
            "Canonical phase payload "+name)
    obj=json.loads(raw)
    require(obj["binding"]==binding and obj["phase"]==name
            and obj["shape"]==item["shape"],"Actual phase identity "+name)
    nr,nc=obj["shape"]
    M=m.fmpq_mat(nr,nc,[m.fmpq(v) for row in obj["rows"] for v in row])
    require(m.matrix_hash(M)==item["matrixSHA256"]==obj["matrixSHA256"],
            "Actual phase matrix "+name)
    phase_summary(name,item,result)
    return M,obj["metadata"],obj["verified"]

def original_at_two(m,jmod,max_order=2):
    """All17 exact original coefficients at s=2+t in co-moving moments."""
    require(max_order==2,"This directed witness uses coefficients 0,1,2 only")
    N=max_order
    K=m.fmpq_mat(m.ORIGINAL_K)
    J2=m.polynomial_power_kernel(K,2)
    J3=m.polynomial_power_kernel(K,3)
    J3inv=J3.inv()
    require(J3inv*J3==m.fmpq_mat([[int(i==j) for j in range(16)] for i in range(16)]),
            "Original J3 inverse")
    y=[[m.fmpq(comb(i,k)*2**(i-k)) if k<=i else m.ZERO
        for i in range(6)] for k in range(N+1)]
    p=[m.values(K*m.column(v)) for v in y]
    maps=[]
    for k in range(N+1):
        B=m.fmpq_mat([[p[k][i-j] if 0<=i-j<6 else m.ZERO
                      for j in range(11)] for i in range(16)])
        maps.append(J3inv*B*J2)
    physical={"J2":m.matrix_hash(J2),"J3":m.matrix_hash(J3)}
    for k,M in enumerate(maps):
        physical["L_y"+str(k)]=m.matrix_hash(M)

    def moment(j):
        return [[m.fmpq(comb(i,j)*comb(i-j,k)*2**(i-j-k))
                 if i>=j+k else m.ZERO for i in range(11)]
                for k in range(N+1)]
    def add(A,B):
        return [m.add_vectors(A[k],B[k]) for k in range(N+1)]
    def neg(A):
        return [m.scale_vector(A[k],-1) for k in range(N+1)]
    def lp(t,v):
        return m.fmpq_mat([[sum((t[i+j+k]*v[k] for k in range(6)),m.ZERO)
                            for j in range(6)] for i in range(6)])
    def contract(t,Q):
        return [sum((t[i+j+k]*Q[j,k] for j in range(6) for k in range(6)),m.ZERO)
                for i in range(6)]
    def evaluate(jets):
        require(len(jets)==N+1,"Original co-moving moment jet length")
        M=[m.hankel(v) for v in jets]
        KM=[K*X for X in M]
        KMK=[X*K for X in KM]
        tensors=[];quad=[];tau=[]
        for k in range(N+1):
            l=m.fmpq_mat(16,1);q=m.fmpq_mat(6,6)
            for r in range(k+1):
                l+=maps[r]*m.column(jets[k-r])
                q+=M[r]*K*M[k-r]
            tensors.append(m.values(l));quad.append(q)
            tau.append(sum((m.trace(KM[r]*KM[k-r]) for r in range(k+1)),m.ZERO))
        out=[]
        for k in range(N+1):
            NN=4*quad[k];gamma=[m.ZERO]*6
            for r in range(k+1):
                NN+=6*lp(tensors[r],p[k-r])
                gp=m.values(quad[r]*m.column(p[k-r]))
                gc=contract(tensors[r],KMK[k-r])
                gamma=[gamma[i]+2*tau[r]*y[k-r][i]+8*gp[i]-12*gc[i]
                       for i in range(6)]
            KNK=K*NN*K
            polar=[sum((KNK[i,j] for i in range(6) for j in range(6)
                        if i+j==d),m.ZERO) for d in range(11)]
            out.append(polar+gamma)
        return out

    tangent=[moment(0),moment(1)]
    Ft=[evaluate(t) for t in tangent]
    pure=[]
    # Exact g(2+t)=-64*t-72*t^2-24*t^3-2*t^4.
    g={1:-64,2:-72,3:-24,4:-2}
    for order in range(N+1):
        seed=[m.ZERO]*17
        for t,co in g.items():
            for a in range(order-t+1):
                b=order-t-a
                if a<6 and b<6:
                    for i in range(6):
                        for j in range(6):
                            seed[i+j]+=4*co*p[a][i]*p[b][j]
        pure.append(seed)
    for jets,d in ((tangent[0],0),(tangent[1],1),(neg(tangent[0]),0),
                   (neg(tangent[1]),-1),(add(tangent[0],tangent[1]),1)):
        values=evaluate(jets)
        require(all(values[k]==[m.fmpq(d*d)*x for x in pure[k]]
                    for k in range(N+1)),
                "All17 original pure coefficients / geometric convolution")
    require(all(not x for x in pure[0]),"Original F0 pure vanishes at s=2")
    require(any(pure[1]),"The original first pure coefficient must be retained")
    z={j:moment(j) for j in range(2,11)}
    Fz={j:evaluate(z[j]) for j in range(2,11)}
    linear={};quadratic={}
    for j in range(2,11):
        minus=evaluate(neg(z[j]))
        linear[j]=[[[(Fz[j][k][i]-minus[k][i])/2 for i in range(17)]
                    for k in range(N+1)]]
        quadratic[(j,j)]=[[(Fz[j][k][i]+minus[k][i])/2 for i in range(17)]
                            for k in range(N+1)]
        for tt in range(2):
            both=evaluate(add(tangent[tt],z[j]))
            linear[j].append([[both[k][i]-Fz[j][k][i]-Ft[tt][k][i]
                               for i in range(17)] for k in range(N+1)])
    for j in range(2,11):
        for l in range(j+1,11):
            both=evaluate(add(z[j],z[l]))
            quadratic[(j,l)]=[[both[k][i]-Fz[j][k][i]-Fz[l][k][i]
                               for i in range(17)] for k in range(N+1)]
    coeff={"chart":"two","maxOrder":N,"pure":pure,"linear":linear,
           "quadratic":quadratic,"physical":physical}
    for k in range(N+1):
        P=jmod.block(m,coeff,k,0,1)
        physical["P"+str(k)]=m.matrix_hash(P)
    return coeff

def sub(m,X,rows,cols=None):
    return m.submatrix(X,list(rows),list(range(X.ncols())) if cols is None else list(cols))
def vjoin(m,j,blocks):
    return j.join_vertical(m,blocks)
def hjoin(m,blocks):
    out=blocks[0]
    for B in blocks[1:]: out=m.join_columns(out,B)
    return out
def sections(m,j,X,last):
    out={};p=0
    for r in range(last+1):
        n=len(j.target_columns(r))
        out[r]=sub(m,X,range(p,p+n));p+=n
    require(p==X.nrows(),"Complete cochain sector ranges")
    return out
def append_zero_pure(m,X):
    out=m.fmpq_mat(20+X.nrows(),X.ncols())
    for i in range(X.nrows()):
        for c in range(X.ncols()): out[20+i,c]=X[i,c]
    return out
def embed_01_to_012(m,X):
    require(X.nrows()==155,"Original pure/one-normal section")
    out=m.fmpq_mat(605,X.ncols())
    for i in range(155):
        for c in range(X.ncols()): out[i,c]=X[i,c]
    return out
def apply_rows(m,j,coeff,k,sec,ncols,source_degrees):
    return vjoin(m,j,[j.apply(m,coeff,k,r,sec,ncols) for r in source_degrees])
def square_read(m,j,X,last):
    require(last>=2,"Squares require normal-two sector")
    sec=sections(m,j,X,last);keys=j.target_columns(2);ix={v:i for i,v in enumerate(keys)}
    return sub(m,sec[2],[ix[(0,0,(v,v))] for v in range(2,11)])
def first_nonzero(M):
    for i in range(M.nrows()):
        for k in range(M.ncols()):
            if M[i,k]: return {"target":i+2,"headColumn":k,"value":str(M[i,k])}
    return None
def verify_jets(m,j,coeff,cochains,lastdegrees,result,label):
    n=cochains[0].ncols()
    sec=[sections(m,j,X,d) for X,d in zip(cochains,lastdegrees)]
    count=0;hashes=[]
    for k in range(len(cochains)):
        guard(ARGS,label+" original coefficient "+str(k),0)
        R=m.fmpq_mat(6188,n)
        for t in range(k+1):
            R+=apply_rows(m,j,coeff,t,sec[k-t],n,range(4))
        require(m.matrix_zero(R),"All6188 original rows "+label+" order"+str(k))
        hashes.append(m.matrix_hash(R));count+=6188*n
    result["parameters"][label+"Verification"]={
        "orders":len(cochains),"heads":n,"all6188OriginalRowsVerified":True,
        "originalProductCoordinates":count,"zeroProductHashes":hashes}
def actual_constant_kernel(d,m,j,a,binding,prefix,B,result):
    old=load_matrix(m,a,binding,prefix+"-constant-kernel",result)
    bsha=m.matrix_hash(B)
    if old is not None:
        N,meta,v=old
        require(v and meta["constantSHA256"]==bsha,"Verified constant source")
        return meta["rank"]
    guard(a,prefix+" exact constant kernel",3)
    R,r=B.rref()
    N,P,F=j.canonical_kernel(m,R,r)
    require(m.matrix_zero(B*N),"All original constant homogeneous products")
    meta={"constantSHA256":bsha,"rank":r,"pivotColumns":P,"freeColumns":F,
          "allOriginalConstantKernelRowsVerified":True}
    save_matrix(m,a,binding,prefix+"-constant-kernel",N,meta,result,True)
    del R
    return r
def leading_basis(m,j,K,start,count):
    C=sub(m,K,range(start,start+count))
    rr,r=C.rref();piv=m.pivot_columns(rr,r)
    chosen=sub(m,K,range(K.nrows()),piv)
    return chosen,sub(m,C,range(count),piv),r
def cached_constant_heads(d,m,j,a,binding,coeff,result):
    done=load_matrix(m,a,binding,"constant-heads",result)
    if done is not None:
        L,meta,v=done
        require(v and meta["completeOriginalConstantDimension"]==22,
                "Paid complete constant head cache")
        return L
    P=j.block(m,coeff,0,0,1)
    Q,r,piv,free=m.nullspace(P)
    require(r==133 and Q.ncols()==2,"True original s=2 P0 rank133")
    L=m.fmpq_mat(155,22)
    for c in range(20): L[c,c]=1
    for i in range(135):
        for c in range(2): L[20+i,20+c]=Q[i,c]
    R=apply_rows(m,j,coeff,0,sections(m,j,L,1),22,range(4))
    require(m.matrix_zero(R),"All original constant heads")
    meta={"completeOriginalConstantDimension":22,"P0Rank":133,
          "P0SHA256":m.matrix_hash(P),"normalKernelSHA256":m.matrix_hash(Q),
          "all6188ConstantRowsVerified":True,
          "completenessUsesPaidFullOriginalRank4345":True,
          "constantReceiptSHA256":CONST_SHA}
    save_matrix(m,a,binding,"constant-heads",L,meta,result,True)
    return L
def transfer_constants(m,a,binding,oldprefix,newprefix,result):
    for suffix in ("constant-kernel","unit","primitive-unit"):
        old=load_matrix(m,a,binding,oldprefix+"-"+suffix,result)
        if old is not None:
            M,meta,verified=old
            require(verified,"Only verified constant phase inherited")
            save_matrix(m,a,binding,newprefix+"-"+suffix,M,meta,result,True)
def transfer_rhs_prefix(m,a,binding,oldprefix,newprefix,B,Cold,Cnew,result):
    require(Cold.nrows()==Cnew.nrows()
            and Cold==sub(m,Cnew,range(Cnew.nrows()),range(Cold.ncols())),
            "Inherited RHS columns equal in all original rows")
    us=load_matrix(m,a,binding,newprefix+"-unit",result)
    require(us is not None and us[2],"Inherited original unit")
    U,um,_=us;I=um["rows"]
    for c in range(Cold.ncols()):
        old=load_matrix(m,a,binding,oldprefix+"-rhs-column-%04d"%c,result)
        require(old is not None and old[2],"Inherited first original unit column")
        X,meta,_=old
        require(meta["constantSHA256"]==m.matrix_hash(B)
                and meta["rhsSHA256"]==m.matrix_hash(Cold)
                and meta["unitSHA256"]==m.matrix_hash(U),"Inherited source column binding")
        meta=dict(meta);meta["rhsSHA256"]=m.matrix_hash(Cnew)
        meta["allOriginalRHSColumnEntriesComparedBeforeInheritance"]=True
        save_matrix(m,a,binding,newprefix+"-rhs-column-%04d"%c,X,meta,result,True)
def solve_probe(d,m,j,u,a,binding,result):
    coeff=original_at_two(m,j,2)
    result["parameters"]["physicalCoefficientSHA256"]=coeff["physical"]
    result["parameters"]["originalPureCoefficient"]= {
        "order0Zero":all(not x for x in coeff["pure"][0]),
        "order1RetainedNonzero":any(coeff["pure"][1]),
        "gAtTwoAscending":[0,-64,-72,-24,-2]}
    L=cached_constant_heads(d,m,j,a,binding,coeff,result)
    B=vjoin(m,j,[hjoin(m,[j.block(m,coeff,0,r,t) for t in (1,2)])
                 for r in (0,1)])
    C=apply_rows(m,j,coeff,1,sections(m,j,L,1),22,(0,1))
    rB=actual_constant_kernel(d,m,j,a,binding,"first-low",B,result)
    require(rB==583,"Paid complete constant kernel forces normal1/2 rank583")
    K,km=u.complete_kernel(d,m,j,a,binding,"first-low",B,C,rB,result)
    K0,H,h=leading_basis(m,j,K,585,22)
    L0=L*H;L1=append_zero_pure(m,sub(m,K0,range(585)))
    verify_jets(m,j,coeff,[L0,L1],[1,2],result,"firstRestrictedFamily")
    read=square_read(m,j,L1,2)
    result["parameters"]["firstRestrictedFamily"]={
        "constantHeads":22,"leadingDimension":h,
        "headMapSHA256":m.matrix_hash(H),
        "lambda0SHA256":m.matrix_hash(L0),"lambda1SHA256":m.matrix_hash(L1),
        "normalDegreeBounds":[1,2],"allConstantFirstCorrectionsRetainedAsSecondStageParameters":True,
        "nineLambda1SquareReadShape":[9,h],"nineLambda1SquareReadSHA256":m.matrix_hash(read),
        "nineLambda1SquareReadAllZero":m.matrix_zero(read),
        "firstNonzeroSquareRead":first_nonzero(read),
        "notClaimedCompleteFirstHeadSpace":True}
    save_matrix(m,a,binding,"first-leading-map",H,{},result,True)
    save_matrix(m,a,binding,"first-lambda0",L0,{},result,True)
    save_matrix(m,a,binding,"first-lambda1",L1,{},result,True)
    if m.matrix_zero(read):
        result["parameters"]["directedConclusion"]={
            "scope":"all first jets with lambda1 normal degree at most two",
            "squareReadInvariantUnderAnySameHeadConstantCorrection":True,
            "noCandidateForTheSpecifiedSecondJetObstruction":True,
            "secondJetsNotConstructed":True,
            "localTargetMembershipNotProved":True,
            "fullHigherConnectionNotComputed":True}
        return
    if a.through=="first":
        raise SafeStop("First restricted family verified; nonzero reads require TRUE second lifts")
    h0lead=8*(-8+32*2-25*4+5*8)**2*(864+864*2+135*4+5*8)**2*sum(
        c*2**i for i,c in enumerate([9600,-25472,-3392,15936,-2888,-936,153,50,5]))
    require(h0lead==17886115659776,"Original h0/(s-2) value")
    F=[]
    for r in range(4):
        x=j.apply(m,coeff,1,r,sections(m,j,L1,2),h)
        x+=j.apply(m,coeff,2,r,sections(m,j,L0,1),h)
        F.append(x)
    require(m.matrix_zero(F[3]),"All2805 original highest-source forcing rows zero")
    BH=j.block(m,coeff,0,2,3)
    rh=actual_constant_kernel(d,m,j,a,binding,"second-high",BH,result)
    KH,hm=u.complete_kernel(d,m,j,a,binding,"second-high",BH,F[2],rh,result)
    Y=sub(m,KH,range(990));Z=sub(m,KH,range(990,990+h))
    CL=vjoin(m,j,[j.block(m,coeff,0,r,3)*Y+F[r]*Z for r in (0,1)])
    C2=hjoin(m,[C,CL])
    transfer_constants(m,a,binding,"first-low","second-low",result)
    transfer_rhs_prefix(m,a,binding,"first-low","second-low",B,C,C2,result)
    KL,lm=u.complete_kernel(d,m,j,a,binding,"second-low",B,C2,rB,result)
    ZL=sub(m,KL,range(607,607+KH.ncols()))
    actualHead=Z*ZL
    rr,headrank=actualHead.rref();choice=m.pivot_columns(rr,headrank)
    T=sub(m,KL,range(KL.nrows()),choice)
    TL=sub(m,T,range(607,607+KH.ncols()));Head=Z*TL
    C0=L0*Head
    C1=L1*Head+embed_01_to_012(m,L*sub(m,T,range(585,607)))
    C2low=append_zero_pure(m,sub(m,T,range(585)))
    C2high=Y*TL;C2all=vjoin(m,j,[C2low,C2high])
    verify_jets(m,j,coeff,[C0,C1,C2all],[1,2,3],result,"secondRestrictedFamily")
    R=square_read(m,j,C1,2);Rscaled=h0lead*R
    # All zero-leading cochains have lambda1 in the FULL constant kernel;
    # their square values vanish. Thus independent leading representatives suffice.
    require(m.matrix_zero(square_read(m,j,
        embed_01_to_012(m,L),2)),"All complete constant correction squares zero")
    for label,M in (("second-lambda0",C0),("second-lambda1",C1),
                    ("second-lambda2",C2all),("second-leading",Head)):
        save_matrix(m,a,binding,label,M,{},result,True)
    witness=first_nonzero(Rscaled)
    result["parameters"]["secondRestrictedFamily"]={
        "leadingDimension":headrank,"normalDegreeBounds":[1,2,3],
        "headMapSHA256":m.matrix_hash(Head),
        "fullHighHomogeneousKernelDimension":KH.ncols(),
        "allConstantFirstCorrectionParametersRetained":22,
        "lambda0SHA256":m.matrix_hash(C0),"lambda1SHA256":m.matrix_hash(C1),
        "lambda2SHA256":m.matrix_hash(C2all),
        "all6188OriginalSourcesRetained":True,"ordersVerified":[0,1,2],
        "trueH0LeadingCoefficient":str(h0lead),
        "h0TargetCoefficientAtOrder2Shape":[9,headrank],
        "h0TargetCoefficientAtOrder2SHA256":m.matrix_hash(Rscaled),
        "h0TargetCoefficientAtOrder2AllZero":witness is None,
        "firstNonzeroOriginalObstruction":witness}
    result["parameters"]["directedConclusion"]={
        "scope":"true original left two-jets with stated correction support bounds",
        "someOriginalH0TargetNotInQLocalImage":witness is not None,
        "nonzeroWouldAlsoExcludeSameSourceQPolynomialMembership":witness is not None,
        "zeroDoesNotProveLocalMembership":True,
        "noClaimOfCompleteSecondConnection":True,
        "noOrdinaryInvariantSubspaceProblemConclusion":True}

def compact_metadata(result):
    p=result["parameters"]
    for k in list(p):
        if k.endswith("ActualRHSColumns") and isinstance(p[k],dict):
            x=p[k];p[k]={"columnCount":len(x),"logicalJSONSHA256":small_hash(x),
                         "allVerified":all(v.get("verified") for v in x.values()),
                         "perColumnMetadataRemainsInTemporaryCheckpoints":True}

def main():
    global ARGS
    p=argparse.ArgumentParser()
    for key in ("generator","jet-actions","unit-schur-helper","constant-receipt",
                "checkpoint-dir","out"): p.add_argument("--"+key,required=True)
    p.add_argument("--through",choices=("first","final"),default="final")
    p.add_argument("--remaining-seconds",type=float,default=180)
    p.add_argument("--memory-mib",type=int,default=2048)
    p.add_argument("--max-new-unit-groups",type=int,default=128)
    a=p.parse_args();ARGS=a
    require(0<a.remaining_seconds<=600 and 512<=a.memory_mib<=8192,"Actual resource bounds")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    if hasattr(sys,"set_int_max_str_digits"): sys.set_int_max_str_digits(0)
    pins=[(a.generator,GEN_SHA),(a.jet_actions,ACT_SHA),
          (a.unit_schur_helper,UNIT_SHA),(a.constant_receipt,CONST_SHA)]
    for name,digest in pins: require(file_sha(name)==digest,"Pinned input "+name)
    old=json.loads(Path(a.constant_receipt).read_bytes())
    require(old["s"]==2 and old["characteristicZeroRank"]==4345
            and old["normalQuadraticIdealTruncationDimension"]==4212,
            "Paid original complete constant fiber")
    m=module_at("r150_two_original_generator",a.generator)
    j=module_at("r150_two_original_actions",a.jet_actions)
    u=module_at("r150_two_original_unit",a.unit_schur_helper)
    started=time.monotonic();a._deadline=started+a.remaining_seconds
    a.unit_algorithm="dixon";a.unit_batch_columns=1;a._new_unit_groups=0
    binding=small_hash({"selfSHA256":file_sha(__file__),"generator":GEN_SHA,
        "actions":ACT_SHA,"helper":UNIT_SHA,"constant":CONST_SHA,
        "mean":2,"coefficientOrders":[0,1,2],"normalBounds":[1,2,3],
        "all6188OriginalSources":True})
    result={"format":"r150-two-directed-original-left-two-jet-witness-v1",
        "status":"started","parameters":{"binding":binding,
        "selfSHA256":file_sha(__file__),"sharedSeconds":a.remaining_seconds,
        "memoryMiB":a.memory_mib,"through":a.through,
        "inputSHA256":{"generator":GEN_SHA,"jetActions":ACT_SHA,
                      "unitHelper":UNIT_SHA,"constantReceipt":CONST_SHA},
        "noLargeRecomputableDataUploaded":True,"allMatricesTemporary":True}}
    def alarm(_signum,_frame): raise SafeStop("Actual shared time budget exhausted")
    signal.signal(signal.SIGALRM,alarm)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    try:
        solve_probe(sys.modules[__name__],m,j,u,a,binding,result)
        result["status"]="completed"
    except SafeStop as e:
        result["status"]="prefix-completed";result["error"]=str(e)
    except BaseException as e:
        result["status"]="failed";result["error"]=type(e).__name__+": "+str(e)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        result["elapsedSeconds"]=time.monotonic()-started
        manpath=Path(a.checkpoint_dir)/"manifest.json"
        if manpath.exists():
            result["parameters"]["temporaryManifest"]={
                "bytes":manpath.stat().st_size,"sha256":file_sha(manpath),
                "binding":binding}
        compact_metadata(result);raw=canonical_bytes(result)
        require(len(raw)<90000,"Compact mathematical receipt must stay below90KB")
        atomic_json(a.out,result)
        print(json.dumps({"status":result["status"],"receipt":a.out,
            "bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),
            "elapsedSeconds":result["elapsedSeconds"]}),flush=True)

if __name__=="__main__": main()
