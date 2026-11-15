#!/usr/bin/env python3
"""Exact constant-unit Schur kernel with actual full-row verification.

For B (constant, rank r) and new C:
 choose a genuine unit U=B[I,P]; solve U X=-C[I];
 form full S=C+B[:,P]X; compute ker S;
 ker[B,C] consists of (N_B a+E_P X z,z), z in ker S.
No new RHS is appended to a large rational RREF of B.
No complete inverse is formed: only actual RHS columns are solved, with
independent normalization, candidate checkpoints, and original-row checks.
All phases are temporary and use the caller's complete source binding.
"""
from math import gcd
from pathlib import Path
import time
from flint import nmod_mat

def req(ok,msg):
    if not ok: raise AssertionError(msg)

def eye(m,n):
    return m.fmpq_mat([[int(i==j) for j in range(n)] for i in range(n)])

def exact_zero(m,M):
    return m.matrix_zero(M)

def kernel_free_identity(m,K,free):
    req(K.ncols()==len(free),"Complete free-coordinate kernel size")
    for c,f in enumerate(free):
        for d,g in enumerate(free):
            req(K[g,c]==int(c==d),"Canonical free-coordinate identity")

def pick_unit_rows(m,B,P,rank):
    """Primitive rational row scaling only selects a unit, never changes B/C."""
    nr=B.nrows();A=nmod_mat(rank,nr,[0]*(rank*nr),31)
    scales=[]
    for i in range(nr):
        vals=[];den=1
        for j,p in enumerate(P):
            v=B[i,p]
            if v:
                num=int(v.numer());dv=int(v.denom())
                den=den//gcd(den,dv)*dv
                vals.append((j,num,dv))
        nums=[(j,num*(den//dv)) for j,num,dv in vals]
        content=0
        for _,v in nums: content=gcd(content,abs(v))
        content=content or 1
        for j,v in nums: A[j,i]=(v//content)%31
        scales.append((str(den),str(content)))
    R,r31=A.rref()
    if r31==rank:
        I=m.pivot_columns(R,r31)
        method="mod31-original-constant-rows-primitive-scaled"
    else:
        # This fallback only touches the fixed small-coefficient B, never C.
        T=m.submatrix(B,range(nr),P).transpose()
        Rq,rq=T.rref()
        req(rq==rank,"Exact constant selected-column rank")
        I=m.pivot_columns(Rq,rq)
        method="exact-rational-constant-transpose"
    req(len(I)==rank and len(set(I))==rank,"Complete unit-row indices")
    return I,{"method":method,"actualPrimitiveFieldRank":int(r31),
              "fieldPrime":31,"rowPrimitiveScales":scales,
              "actualRHSNotScaledOrChanged":True}

def constant_unit(d,m,j,a,binding,prefix,B,expected_rank,result):
    bsha=m.matrix_hash(B);nr,n=B.nrows(),B.ncols()
    old=d.load_matrix(m,a,binding,prefix+"-constant-kernel",result)
    if old is None:
        d.guard(a,prefix+" fixed constant kernel",3.0)
        R,r=B.rref()
        req(r==expected_rank,"Paid fixed constant rank changed")
        N,P,F=j.canonical_kernel(m,R,r)
        kernel_free_identity(m,N,F)
        req(exact_zero(m,B*N),"All fixed constant homogeneous rows")
        meta={"constantSHA256":bsha,"rank":r,"pivotColumns":P,"freeColumns":F,
              "allOriginalConstantKernelRowsVerified":True}
        d.save_matrix(m,a,binding,prefix+"-constant-kernel",N,meta,result,True)
        del R
    else:
        N,meta,verified=old
        req(verified and meta["constantSHA256"]==bsha
            and meta["rank"]==expected_rank,"Fixed constant kernel cache")
        r=meta["rank"];P=meta["pivotColumns"];F=meta["freeColumns"]
        kernel_free_identity(m,N,F)
    old=d.load_matrix(m,a,binding,prefix+"-unit",result)
    if old is None:
        d.guard(a,prefix+" genuine constant unit",3.0)
        I,profile=pick_unit_rows(m,B,P,r)
        U=m.submatrix(B,I,P)
        umeta={"constantSHA256":bsha,"rank":r,"rows":I,"columns":P,
               "profile":profile,"genuineRationalUnit":True,
               "constantKernelSHA256":m.matrix_hash(N)}
        d.save_matrix(m,a,binding,prefix+"-unit",U,umeta,result,True)
    else:
        U,umeta,verified=old
        req(verified and umeta["constantSHA256"]==bsha
            and umeta["constantKernelSHA256"]==m.matrix_hash(N)
            and umeta["columns"]==P and umeta["genuineRationalUnit"],
            "Actual original constant unit cache")
        I=umeta["rows"]
        req(U==m.submatrix(B,I,P),"Unit retained exact original coordinates")
    result["parameters"][prefix+"ConstantUnit"]={
        "rank":r,"shape":[nr,n],"constantSHA256":bsha,
        "unitSHA256":m.matrix_hash(U),"unitSelectionMethod":umeta["profile"]["method"],
        "primitiveFieldRank":umeta["profile"]["actualPrimitiveFieldRank"],
        "constantKernelSHA256":m.matrix_hash(N),
        "unitRowsSHA256":d.small_hash(I),"pivotColumnsSHA256":d.small_hash(P),
        "homogeneousKernelDimension":N.ncols(),
        "allHomogeneousKernelColumnsRetained":True,
    }
    return N,P,F,I,U,bsha

def rhs_progress(d,a,binding,prefix,bsha,csha,usha,states):
    """Small same-job progress survives a later native timeout."""
    out={"format":"r150-unit-rhs-columns-progress-v1","binding":binding,
         "prefix":prefix,"constantSHA256":bsha,"rhsSHA256":csha,
         "unitSHA256":usha,"temporaryOnly":True,
         "columns":states,"newNativeGroupsThisInvocation":getattr(a,"_new_unit_groups",0)}
    d.atomic_json(Path(a.checkpoint_dir)/(prefix+"-rhs-column-progress.json"),out)

def primitive_unit(d,m,a,binding,prefix,U,usha,result):
    old=d.load_matrix(m,a,binding,prefix+"-primitive-unit",result)
    r=U.nrows()
    if old is None:
        d.guard(a,prefix+" constant-only row normalization",2.0)
        A=m.fmpq_mat(r,r);scales=[];maxbits=0
        for i in range(r):
            vals=[];den=1
            for j in range(r):
                v=U[i,j]
                if v:
                    nn=int(v.numer());dd=int(v.denom())
                    den=den//gcd(den,dd)*dd;vals.append((j,nn,dd))
            ints=[(j,nn*(den//dd)) for j,nn,dd in vals]
            content=0
            for _,nn in ints: content=gcd(content,abs(nn))
            req(content>0,"A genuine unit cannot have a zero row")
            scale=m.fmpq(den,content);scales.append(scale)
            for j,nn in ints:
                val=nn//content;A[i,j]=val
                maxbits=max(maxbits,abs(val).bit_length())
                req(A[i,j]==scale*U[i,j],"Original constant row normalization")
        meta={"unitSHA256":usha,"rowScales":[str(x) for x in scales],
              "allOriginalConstantRowScalingsVerified":True,
              "originalRows":r,"maxPrimitiveCoefficientBits":maxbits,
              "RHSNotUsedToScaleUnit":True}
        d.save_matrix(m,a,binding,prefix+"-primitive-unit",A,meta,result,True)
    else:
        A,meta,verified=old
        req(verified and meta["unitSHA256"]==usha
            and meta["allOriginalConstantRowScalingsVerified"]
            and meta["RHSNotUsedToScaleUnit"]
            and [A.nrows(),A.ncols()]==[r,r],"Original primitive unit cache")
        scales=[m.fmpq(x) for x in meta["rowScales"]]
    req(len(scales)==r,"All actual constant row scales")
    result["parameters"][prefix+"PrimitiveUnit"]={
        "unitSHA256":usha,"primitiveUnitSHA256":m.matrix_hash(A),
        "shape":[r,r],"maxPrimitiveCoefficientBits":meta["maxPrimitiveCoefficientBits"],
        "RHSNotUsedToScaleUnit":True,"noCompleteInverseConstructed":True}
    return A,scales

def normalized_rhs(d,m,a,binding,prefix,c,CI,scales,asha,csha,usha,result):
    name=prefix+"-normalized-rhs-%04d"%c
    old=d.load_matrix(m,a,binding,name,result);r=CI.nrows()
    if old is None:
        d.guard(a,prefix+" exact RHS column normalization "+str(c),1.0)
        entries=[-scales[i]*CI[i,c] for i in range(r)]
        den=1;parts=[]
        for v in entries:
            nn=int(v.numer());dd=int(v.denom())
            den=den//gcd(den,dd)*dd;parts.append((nn,dd))
        nums=[nn*(den//dd) for nn,dd in parts]
        content=0
        for nn in nums: content=gcd(content,abs(nn))
        if content:
            rhs=m.fmpq_mat(r,1,[nn//content for nn in nums])
            scale=m.fmpq(content,den)
        else:
            rhs=m.fmpq_mat(r,1);scale=m.fmpq(1)
        req(all(scale*rhs[i,0]==entries[i] for i in range(r)),
            "Original independently scaled RHS column")
        meta={"column":c,"rhsSHA256":csha,"unitSHA256":usha,
              "primitiveUnitSHA256":asha,"originalSolutionScale":str(scale),
              "allOriginalColumnScalingRowsVerified":True,
              "maxPrimitiveRHSBits":max((abs(int(rhs[i,0])).bit_length()
                                         for i in range(r)),default=0),
              "solutionScaleNumeratorBits":abs(int(scale.numer())).bit_length(),
              "solutionScaleDenominatorBits":int(scale.denom()).bit_length(),
              "isZero":m.matrix_zero(rhs)}
        d.save_matrix(m,a,binding,name,rhs,meta,result,True)
    else:
        rhs,meta,verified=old
        req(verified and meta["column"]==c and meta["rhsSHA256"]==csha
            and meta["unitSHA256"]==usha and meta["primitiveUnitSHA256"]==asha
            and meta["allOriginalColumnScalingRowsVerified"]
            and [rhs.nrows(),rhs.ncols()]==[r,1],"Actual normalized RHS column")
        scale=m.fmpq(meta["originalSolutionScale"])
    return rhs,scale,meta

def solve_actual_rhs_columns(d,m,a,binding,prefix,U,C,I,bsha,csha,usha,result):
    """Solve only actual RHS, with per-column candidate and original-row checks."""
    r=U.nrows();k=C.ncols();CI=m.submatrix(C,I,range(k))
    result["parameters"][prefix+"ActualRHSSolvePolicy"]={
        "algorithm":a.unit_algorithm,"columnsPerNativeCall":a.unit_batch_columns,
        "maximumNewGroupsThisInvocation":a.max_new_unit_groups,
        "actualColumns":k,"actualOriginalRows":r,
        "unitRowScalingIndependentOfRHS":True,
        "independentRHSColumnScaleRestoredBeforeOriginalProduct":True,
        "noCompleteInverseConstructed":True}
    X=m.fmpq_mat(r,k);states={};pending=[];loaded={}
    for c in range(k):
        name=prefix+"-rhs-column-%04d"%c
        old=d.load_matrix(m,a,binding,name,result)
        if old is not None:
            col,meta,verified=old
            req(meta["column"]==c and meta["constantSHA256"]==bsha
                and meta["rhsSHA256"]==csha and meta["unitSHA256"]==usha
                and [col.nrows(),col.ncols()]==[r,1],
                "Actual original RHS solution column cache")
            if not verified:
                d.guard(a,prefix+" cached original RHS product "+str(c),0.0)
                req(m.matrix_zero(U*col+m.submatrix(CI,range(r),[c])),
                    "Cached actual original unit product failed")
                meta["allOriginalUnitRowsVerified"]=True
                d.save_matrix(m,a,binding,name,col,meta,result,True)
            for i in range(r): X[i,c]=col[i,0]
            states[str(c)]={"verified":True,"matrixSHA256":m.matrix_hash(col),
                            "originalColumn":c,"nativeSeconds":meta.get("nativeSeconds"),
                            "algorithm":meta.get("algorithm")}
            continue
        size=0;nonzero=False
        for i in range(r):
            v=CI[i,c]
            if v:
                nonzero=True
                size=max(size,abs(int(v.numer())).bit_length(),
                         int(v.denom()).bit_length())
        if not nonzero:
            col=m.fmpq_mat(r,1)
            meta={"column":c,"constantSHA256":bsha,"rhsSHA256":csha,
                  "unitSHA256":usha,"allOriginalUnitRowsVerified":True,
                  "originalUnitProductCoordinates":r,"algorithm":"exact-zero-RHS",
                  "nativeSeconds":0.0,"nativeSolveUsed":False}
            req(m.matrix_zero(m.submatrix(CI,range(r),[c])),"Actual zero RHS")
            d.save_matrix(m,a,binding,name,col,meta,result,True)
            states[str(c)]={"verified":True,"matrixSHA256":m.matrix_hash(col),
                            "originalColumn":c,"nativeSeconds":0.0,
                            "algorithm":"exact-zero-RHS"}
        else:
            pending.append((size,c))
    rhs_progress(d,a,binding,prefix,bsha,csha,usha,states)
    # Actual coordinate order is never changed; only execution order uses size.
    pending.sort()
    result["parameters"][prefix+"RemainingRHSExecutionOrder"]=[
        {"originalColumn":c,"actualInputMaxBits":bits} for bits,c in pending]
    if pending:
        A,scales=primitive_unit(d,m,a,binding,prefix,U,usha,result)
        asha=m.matrix_hash(A)
    pos=0
    while pos<len(pending):
        if getattr(a,"_new_unit_groups",0)>=a.max_new_unit_groups:
            rhs_progress(d,a,binding,prefix,bsha,csha,usha,states)
            raise d.SafeStop("Requested actual RHS group prefix verified; resume remaining columns")
        d.guard(a,prefix+" next actual RHS group",4.0)
        group=[c for _,c in pending[pos:pos+a.unit_batch_columns]]
        inputs=[];factors=[];imeta=[]
        for c in group:
            rhs,scale,meta=normalized_rhs(d,m,a,binding,prefix,c,CI,scales,
                                         asha,csha,usha,result)
            inputs.append(rhs);factors.append(scale);imeta.append(meta)
        rhs=inputs[0]
        for more in inputs[1:]: rhs=m.join_columns(rhs,more)
        started=time.monotonic()
        Y=A.solve(rhs,algorithm=a.unit_algorithm)
        elapsed=time.monotonic()-started
        a._new_unit_groups=getattr(a,"_new_unit_groups",0)+1
        candidates=[]
        # Save ALL returned columns before any independent original product.
        for t,c in enumerate(group):
            col=m.fmpq_mat(r,1,[factors[t]*Y[i,t] for i in range(r)])
            meta={"column":c,"constantSHA256":bsha,"rhsSHA256":csha,
                  "unitSHA256":usha,"primitiveUnitSHA256":asha,
                  "normalizedRHSSHA256":m.matrix_hash(inputs[t]),
                  "originalSolutionScale":str(factors[t]),
                  "nativeGroupColumns":group,"nativeSeconds":elapsed,
                  "algorithm":a.unit_algorithm,"nativeSolveUsed":True,
                  "originalUnitProductCoordinates":r,
                  "maxPrimitiveRHSBits":imeta[t]["maxPrimitiveRHSBits"],
                  "solutionScaleNumeratorBits":imeta[t]["solutionScaleNumeratorBits"],
                  "solutionScaleDenominatorBits":imeta[t]["solutionScaleDenominatorBits"]}
            name=prefix+"-rhs-column-%04d"%c
            d.save_matrix(m,a,binding,name,col,meta,result,False)
            candidates.append((c,col,meta))
            states[str(c)]={"verified":False,"matrixSHA256":m.matrix_hash(col),
                            "originalColumn":c,"nativeSeconds":elapsed,
                            "algorithm":a.unit_algorithm,
                            "maxPrimitiveRHSBits":imeta[t]["maxPrimitiveRHSBits"]}
        rhs_progress(d,a,binding,prefix,bsha,csha,usha,states)
        del Y,rhs,inputs
        for c,col,meta in candidates:
            d.guard(a,prefix+" all original unit rows for column "+str(c),0.0)
            req(m.matrix_zero(U*col+m.submatrix(CI,range(r),[c])),
                "All original unscaled unit RHS rows failed")
            meta["allOriginalUnitRowsVerified"]=True
            d.save_matrix(m,a,binding,prefix+"-rhs-column-%04d"%c,
                          col,meta,result,True)
            for i in range(r): X[i,c]=col[i,0]
            states[str(c)]["verified"]=True
            rhs_progress(d,a,binding,prefix,bsha,csha,usha,states)
        result["parameters"][prefix+"ActualRHSColumns"]=states
        del candidates
        pos+=len(group)
    result["parameters"][prefix+"ActualRHSColumns"]=states
    req(len(states)==k and all(v["verified"] for v in states.values()),
        "Every actual unit RHS column must be verified")
    return X


def complete_kernel(d,m,j,a,binding,prefix,B,C,expected_rank,result):
    nr,n=B.nrows(),B.ncols();k=C.ncols()
    req(C.nrows()==nr,"Constant-unit full RHS dimensions")
    bsha=m.matrix_hash(B);csha=m.matrix_hash(C)
    done=d.load_matrix(m,a,binding,prefix+"-kernel",result)
    if done is not None:
        K,meta,verified=done
        req(meta["constantSHA256"]==bsha and meta["rhsSHA256"]==csha,
            "Complete Schur kernel binding")
        kernel_free_identity(m,K,meta["freeIndices"])
        if not verified:
            d.guard(a,prefix+" final complete original product",0.0)
            lhs=B*m.submatrix(K,range(n),range(K.ncols()))
            lhs+=C*m.submatrix(K,range(n,n+k),range(K.ncols()))
            req(exact_zero(m,lhs),"All original complete Schur kernel rows")
            meta["allOriginalKernelRowsVerified"]=True
            d.save_matrix(m,a,binding,prefix+"-kernel",K,meta,result,True)
        result["parameters"][prefix+"CompleteSchurKernel"]={
            "rank":meta["rank"],"shape":[nr,n+k],"kernelDimension":K.ncols(),
            "kernelSHA256":m.matrix_hash(K),"allOriginalRowsVerified":True,
            "schurRank":meta["schurRank"],
            "constantRank":meta["constantRank"],
        }
        return K,meta

    N,P,F,I,U,bsha=constant_unit(d,m,j,a,binding,prefix,B,expected_rank,result)
    r=expected_rank;usha=m.matrix_hash(U)
    solved=d.load_matrix(m,a,binding,prefix+"-unit-rhs-solution",result)
    if solved is None:
        X=solve_actual_rhs_columns(d,m,a,binding,prefix,U,C,I,bsha,csha,usha,result)
        xmeta={"constantSHA256":bsha,"rhsSHA256":csha,"unitSHA256":usha,
               "unitRows":I,"pivotColumns":P,
               "fullOriginalUnitProductCoordinates":r*k,
               "allOriginalUnitRHSRowsVerified":True,
               "onlyActualRHSColumnsSolved":True,"noCompleteInverseConstructed":True}
        d.save_matrix(m,a,binding,prefix+"-unit-rhs-solution",X,xmeta,result,True)
    else:
        X,xmeta,xverified=solved
        req(xverified and xmeta["constantSHA256"]==bsha
            and xmeta["rhsSHA256"]==csha and xmeta["unitSHA256"]==usha
            and xmeta["unitRows"]==I and xmeta["pivotColumns"]==P
            and xmeta["allOriginalUnitRHSRowsVerified"],
            "Complete verified actual new unit RHS source")
    del U
    old=d.load_matrix(m,a,binding,prefix+"-full-schur",result)
    if old is None:
        d.guard(a,prefix+" full actual Schur rows",1.0)
        BP=m.submatrix(B,range(nr),P)
        S=C+BP*X
        req(exact_zero(m,m.submatrix(S,I,range(k))),"All retained original unit rows")
        smeta={"constantSHA256":bsha,"rhsSHA256":csha,
               "unitSolutionSHA256":m.matrix_hash(X),
               "unitRows":I,"allOriginalRowsRetained":True,
               "unitRowsActuallyZero":True}
        d.save_matrix(m,a,binding,prefix+"-full-schur",S,smeta,result,True)
        del BP
    else:
        S,smeta,sverified=old
        req(sverified and smeta["constantSHA256"]==bsha
            and smeta["rhsSHA256"]==csha
            and smeta["unitSolutionSHA256"]==m.matrix_hash(X)
            and smeta["unitRows"]==I and smeta["allOriginalRowsRetained"]
            and smeta["unitRowsActuallyZero"],"Full actual Schur source")
    old=d.load_matrix(m,a,binding,prefix+"-small-schur-kernel",result)
    if old is None:
        d.guard(a,prefix+" small Schur kernel",3.0)
        used=set(I)
        keep=[i for i in range(nr) if i not in used]
        SR=m.submatrix(S,keep,range(k))
        rr,rs=SR.rref()
        Z,ps,fs=j.canonical_kernel(m,rr,rs)
        kernel_free_identity(m,Z,fs)
        zmeta={"fullSchurSHA256":m.matrix_hash(S),"rank":rs,
               "pivotColumns":ps,"freeColumns":fs,
               "reducedShape":[nr-r,k]}
        d.save_matrix(m,a,binding,prefix+"-small-schur-kernel",Z,zmeta,result,False)
        zverified=False
        del SR,rr
    else:
        Z,zmeta,zverified=old
        req(zmeta["fullSchurSHA256"]==m.matrix_hash(S),
            "Actual small Schur kernel binding")
        rs=zmeta["rank"];fs=zmeta["freeColumns"]
        kernel_free_identity(m,Z,fs)
    if not zverified:
        d.guard(a,prefix+" full Schur kernel product",0.0)
        req(exact_zero(m,S*Z),"All original Schur rows failed")
        zmeta["allOriginalSchurKernelRowsVerified"]=True
        d.save_matrix(m,a,binding,prefix+"-small-schur-kernel",Z,zmeta,result,True)
    d.guard(a,prefix+" complete kernel reconstruction",0.0)
    K=m.fmpq_mat(n+k,N.ncols()+Z.ncols())
    for i in range(n):
        for c in range(N.ncols()): K[i,c]=N[i,c]
    XZ=X*Z
    for a0,p in enumerate(P):
        for c in range(Z.ncols()): K[p,N.ncols()+c]=XZ[a0,c]
    for i in range(k):
        for c in range(Z.ncols()): K[n+i,N.ncols()+c]=Z[i,c]
    free=F+[n+x for x in fs]
    kernel_free_identity(m,K,free)
    meta={"shape":[nr,n+k],"rank":r+rs,"constantRank":r,"schurRank":rs,
          "constantSHA256":bsha,"rhsSHA256":csha,"freeIndices":free,
          "fullSchurSHA256":m.matrix_hash(S),"smallSchurKernelSHA256":m.matrix_hash(Z),
          "constantKernelSHA256":m.matrix_hash(N),
          "noLargeRationalAugmentedRREF":True,
          "allHomogeneousColumnsAndAllNewRHSRetained":True}
    d.save_matrix(m,a,binding,prefix+"-kernel",K,meta,result,False)
    d.guard(a,prefix+" complete original kernel product",0.0)
    lhs=B*m.submatrix(K,range(n),range(K.ncols()))
    lhs+=C*m.submatrix(K,range(n,n+k),range(K.ncols()))
    req(exact_zero(m,lhs),"Complete original constant-unit Schur identity")
    meta["allOriginalKernelRowsVerified"]=True
    d.save_matrix(m,a,binding,prefix+"-kernel",K,meta,result,True)
    result["parameters"][prefix+"CompleteSchurKernel"]={
        "rank":r+rs,"shape":[nr,n+k],"kernelDimension":K.ncols(),
        "kernelSHA256":m.matrix_hash(K),"allOriginalRowsVerified":True,
        "schurRank":rs,"constantRank":r,
        "schurMatrixShape":[nr-r,k],"allHomogeneousColumnsRetained":True,
    }
    return K,meta
