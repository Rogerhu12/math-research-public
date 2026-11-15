#!/usr/bin/env python3
"""Exact constant-unit Schur kernel with actual full-row verification.

For B (constant, rank r) and new C:
 choose a genuine unit U=B[I,P]; solve U X=-C[I];
 form full S=C+B[:,P]X; compute ker S;
 ker[B,C] consists of (N_B a+E_P X z,z), z in ker S.
No new RHS is appended to a large rational RREF of B.
All phases are temporary and use the caller's complete source binding.
"""
from math import gcd
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
        inverse=d.load_matrix(m,a,binding,prefix+"-constant-inverse",result)
        if inverse is None:
            d.guard(a,prefix+" constant-only inverse",4.0)
            V=U.inv()
            vmeta={"constantSHA256":bsha,"unitSHA256":usha,
                   "candidateUsedOnlyAfterActualRHSProduct":True}
            # No claim about V is needed before the actual U X=-C_I check.
            d.save_matrix(m,a,binding,prefix+"-constant-inverse",V,vmeta,result,False)
        else:
            V,vmeta,vverified=inverse
            req(vmeta["constantSHA256"]==bsha and vmeta["unitSHA256"]==usha
                and vmeta["candidateUsedOnlyAfterActualRHSProduct"],
                "Original constant inverse candidate identity")
        d.guard(a,prefix+" actual new unit RHS",0.0)
        CI=m.submatrix(C,I,range(k))
        X=-(V*CI)
        xmeta={"constantSHA256":bsha,"rhsSHA256":csha,"unitSHA256":usha,
               "unitRows":I,"pivotColumns":P,
               "fullOriginalUnitProductCoordinates":r*k}
        d.save_matrix(m,a,binding,prefix+"-unit-rhs-solution",X,xmeta,result,False)
        del V,CI
        xverified=False
    else:
        X,xmeta,xverified=solved
        req(xmeta["constantSHA256"]==bsha and xmeta["rhsSHA256"]==csha
            and xmeta["unitSHA256"]==usha and xmeta["unitRows"]==I
            and xmeta["pivotColumns"]==P,"Actual new unit RHS source")
    if not xverified:
        d.guard(a,prefix+" all actual unit RHS products",0.0)
        CI=m.submatrix(C,I,range(k))
        req(exact_zero(m,U*X+CI),"All original constant-unit RHS rows failed")
        xmeta["allOriginalUnitRHSRowsVerified"]=True
        d.save_matrix(m,a,binding,prefix+"-unit-rhs-solution",X,xmeta,result,True)
        del CI
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
