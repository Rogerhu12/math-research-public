#!/usr/bin/env sage-python
"""Exact original coefficient-field kernels and leading rows using the fixed packed prime backend."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the named public research Actions.")

import numpy as np
from sage.all import GF, matrix, vector


def prime_rref(p, values):
    """Import one original prime row at a time to bound conversion temporaries."""
    if values.ndim!=2 or not values.shape[0] or not values.shape[1]:
        raise ValueError("Expected a nonempty original constant-field matrix")
    k=GF(p)
    M=matrix(k,int(values.shape[0]),int(values.shape[1]),0,
             sparse=False,implementation="linbox-float")
    if type(M).__name__!="Matrix_modn_dense_float":
        raise RuntimeError("The pinned Sage dense prime-field backend changed")
    for i,row in enumerate(values):
        M.set_row(i,vector(k,row.tolist()))
    M.echelonize(algorithm="linbox_noefd")
    pivots=tuple(int(c) for c in M.pivots())
    return M,pivots


def prime_rows(field, rows):
    """Regular representation with paired original input and output coordinates."""
    f,r,n=rows.shape
    if f!=field.f:
        raise ValueError("The original coefficient planes do not agree")
    if f==1:
        return np.ascontiguousarray(rows[0],dtype=np.uint8)
    M=np.empty((2*r,2*n),dtype=np.uint8)
    M[0::2,0::2]=rows[0]
    M[0::2,1::2]=rows[1]
    M[1::2,0::2]=(field.a*rows[1].astype(np.int64))%field.p
    M[1::2,1::2]=(rows[0].astype(np.int64)+field.b*rows[1].astype(np.int64))%field.p
    return M


def paired_pivots(field,pivots,n):
    """For a k-stable row space, every next coordinate has k-rank zero or one."""
    inds=set(pivots)
    chosen=[]
    for j in range(n):
        bits=[field.f*j+b in inds for b in range(field.f)]
        if any(bits) and not all(bits):
            raise ArithmeticError("A claimed original-field rank split an actual scalar-coordinate pair")
        if all(bits):
            chosen.append(j)
    if len(chosen)*field.f!=len(pivots):
        raise ArithmeticError("A prime pivot is outside the full original coordinate list")
    return chosen


def left_kernel(field,A):
    f,u,v=A.shape
    prime=prime_rows(field,A)
    eq,piv=prime_rref(field.p,np.ascontiguousarray(prime.T))
    del prime
    cols=paired_pivots(field,piv,u)
    used=set(cols)
    free=[j for j in range(u) if j not in used]
    if u-len(free)!=len(cols):
        raise ArithmeticError("Original rank/nullity coordinates overlap")
    K=np.zeros((f,len(free),u),dtype=np.uint8)
    for row,j in enumerate(free):
        K[0,row,j]=1
    # Set each free original coordinate once to 1, leaving its alpha-component 0.
    # The alpha multiples span the other free prime rows. Check the full original
    # annihilation in small slabs after recovering *all* original pivots.
    free_prime=[f*j for j in free]
    for r,p in enumerate(piv):
        if int(eq[r,p])!=1:
            raise ArithmeticError("The pinned native echelon form did not normalize a pivot")
        packed=np.asarray(eq.row(r).list(),dtype=np.int64)
        K[p%f,:,p//f]=(-packed[free_prime])%field.p
    for r in range(0,len(free),32):
        if np.any(field.product(K[:,r:r+32,:],A)):
            raise ArithmeticError("The complete returned original kernel failed direct multiplication")
    return K,dict(prime_rows=f*v,prime_columns=f*u,full_prime_rank=len(piv),
                  original_rank=len(cols),full_original_nullity=len(free),
                  every_prime_pivot_pair_checked=True,every_original_kernel_row_verified=True,
                  native_echelon_algorithm="linbox_noefd")


def independent_leading_rows(field,K,info,n,m):
    """Paired rows span the original G_m, fields components are consecutive."""
    f,r,cols=K.shape
    if len(info)!=cols:
        raise ValueError("Wrong packed graded-coordinate labels")
    # info[c]=(coordinate,power,weight). Higher degree then higher index leads.
    order=sorted(range(cols),key=lambda c:(info[c][2], info[c][0]),reverse=True)
    sorted_K=np.take(K,order,axis=2)
    prime=prime_rows(field,sorted_K)
    del sorted_K
    echelon,piv=prime_rref(field.p,prime)
    del prime
    pivcols=paired_pivots(field,piv,cols)
    if len(pivcols)!=r:
        raise ArithmeticError("The complete packed paired G rows are not independent")
    pos={value:i for i,value in enumerate(piv)}
    smallest={}
    for c in pivcols:
        j,a,rho=info[order[c]]
        if j not in smallest or rho<smallest[j][0]:
            smallest[j]=(rho,c)
    if len(smallest)!=n:
        raise ArithmeticError("The full filtered graph does not have the required number of leading coordinates")
    selected=[]
    for j in sorted(smallest):
        rho,c=smallest[j]
        q=pos[f*c]
        raw=np.asarray(echelon.row(q).list(),dtype=np.uint8)
        if raw[f*c]!=1 or np.any(raw[:f*c]) or np.any(raw[f*c+1:f*c+f]):
            raise ArithmeticError("A selected original graded pivot is not the specified monic coefficient")
        unsorted=np.empty((f,cols),dtype=np.uint8)
        unsorted[:,order]=raw.reshape(cols,f).T
        selected.append((rho,j,unsorted))
    if any(rho>m for rho,j,row in selected):
        raise ArithmeticError("A selected graded row exceeds the complete original window")
    return selected,dict(full_original_echelon_rank=len(pivcols),
                         true_distinct_leading_coordinates=[j for rho,j,row in selected],
                         actual_original_row_weights=[rho for rho,j,row in selected])
