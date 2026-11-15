#!/usr/bin/env python3
"""Original R150 co-moving jets and exact normal-degree blocks.

Pure helper: no mathematical computation occurs on import.
The parent driver supplies the pinned original first generator module.
All target coordinates are ordinary polynomial coefficients, not divided powers.
The normal-degree5 block is retained; no high-source surjectivity is assumed.
"""
from itertools import combinations_with_replacement
from math import comb

def require(ok,msg):
    if not ok:
        raise AssertionError(msg)

def target_columns(normal_degree):
    r=normal_degree
    require(0<=r<=5,"Normal target degree")
    mons=list(combinations_with_replacement(range(2,11),r))
    return [(a,b,mon) for d in range(0 if r else 1,6-r)
            for a in range(d+1) for b in [d-a] for mon in mons]

def source_rows(normal_degree):
    r=normal_degree
    require(0<=r<=3,"Normal source degree")
    mons=list(combinations_with_replacement(range(2,11),r))
    return [(i,a,d-a,mon) for i in range(17) for d in range(4-r)
            for a in range(d+1) for mon in mons]

def original_coefficients(m,chart,max_order=6):
    """Return all exact original F_0..F_max, pure/linear/quadratic parts.

    chart='infinity' uses exact reversal of K followed by natural u=1/s.
    chart='zero' uses the original K and the original finite parameter s.
    Independent pure geometric convolution checks every original equation.
    """
    require(chart in ("zero","infinity") and 0<=max_order<=10,
            "Original chart / Taylor order")
    N=max_order
    K=m.fmpq_mat(m.ORIGINAL_K if chart=="zero" else
                 [[m.ORIGINAL_K[5-i][5-j] for j in range(6)] for i in range(6)])
    J2=m.polynomial_power_kernel(K,2)
    J3=m.polynomial_power_kernel(K,3)
    J3inv=J3.inv()
    require(J3inv*J3==m.fmpq_mat([[int(i==j) for j in range(16)] for i in range(16)]),
            "Original J3 inverse")
    p=[[K[i,k] if k<6 else m.ZERO for i in range(6)] for k in range(N+1)]
    y=[[m.ONE if i==k else m.ZERO for i in range(6)] for k in range(N+1)]
    maps=[]
    for k in range(N+1):
        B=m.fmpq_mat([[p[k][i-j] if 0<=i-j<6 else m.ZERO
                      for j in range(11)] for i in range(16)])
        maps.append(J3inv*B*J2)
    physical={"J2":m.matrix_hash(J2),"J3":m.matrix_hash(J3)}
    for k,M in enumerate(maps):
        physical["L_y"+str(k)]=m.matrix_hash(M)

    def moment(j):
        return [m.sequence(j+k,comb(j+k,k)) for k in range(N+1)]
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
    g={2:24,3:-8,4:-2} if chart=="zero" else {2:-2,3:-8,4:24}
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
    require(all(not x for k in range(min(2,N+1)) for x in pure[k]),
            "F0/F1 pure vanish in the original co-moving chart")
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
    coeff={"chart":chart,"maxOrder":N,"pure":pure,"linear":linear,
           "quadratic":quadratic,"physical":physical}
    for k in range(N+1):
        P=block(m,coeff,k,0,1)
        physical["P"+str(k)]=m.matrix_hash(P)
    return coeff

def sparse_row_terms(coeff,order,row,target_degree,index):
    """Complete A_order^T row on the selected normal-degree target sector."""
    eq,a,b,normal=row
    r=len(normal);t=target_degree
    if t==r:
        value=coeff["pure"][order][eq]
        key=(a,b+2,normal)
        if value and key in index:
            yield index[key],value
    elif t==r+1:
        for j in range(2,11):
            mon=tuple(sorted(normal+(j,)))
            for mode,(da,db) in enumerate(((0,0),(1,0),(0,1))):
                value=coeff["linear"][j][mode][order][eq]
                key=(a+da,b+db,mon)
                if value and key in index:
                    yield index[key],value
    elif t==r+2:
        for pair,q in coeff["quadratic"].items():
            value=q[order][eq]
            key=(a,b,tuple(sorted(normal+pair)))
            if value and key in index:
                yield index[key],value

def block(m,coeff,order,source_degree,target_degree):
    rows=source_rows(source_degree);cols=target_columns(target_degree)
    ix={v:j for j,v in enumerate(cols)}
    M=m.fmpq_mat(len(rows),len(cols))
    for r,row in enumerate(rows):
        for c,v in sparse_row_terms(coeff,order,row,target_degree,ix):
            M[r,c]+=v
    return M

def apply(m,coeff,order,source_degree,sections,ncols):
    """Apply an original coefficient using only present target sectors."""
    rows=source_rows(source_degree)
    out=m.fmpq_mat(len(rows),ncols)
    for t,X in sections.items():
        if t<source_degree or t>source_degree+2:
            continue
        cols=target_columns(t);ix={v:j for j,v in enumerate(cols)}
        require(X.nrows()==len(cols) and X.ncols()==ncols,
                "Actual cochain normal sector dimension")
        # Native exact multiplication; release each original block afterwards.
        M=block(m,coeff,order,source_degree,t)
        out+=M*X
        del M
    return out

def apply_sparse(m,coeff,order,source_degree,sections,ncols):
    """Original-row exact multiplication without storing a large block."""
    rows=source_rows(source_degree)
    out=m.fmpq_mat(len(rows),ncols)
    for t,X in sections.items():
        if t<source_degree or t>source_degree+2:
            continue
        cols=target_columns(t);ix={v:j for j,v in enumerate(cols)}
        require(X.nrows()==len(cols) and X.ncols()==ncols,
                "Actual cochain normal sector dimension")
        for r,row in enumerate(rows):
            for c,v in sparse_row_terms(coeff,order,row,t,ix):
                for j in range(ncols):
                    if X[c,j]:
                        out[r,j]+=v*X[c,j]
    return out

def join_vertical(m,blocks):
    require(blocks and len({x.ncols() for x in blocks})==1,
            "Vertical block column sizes")
    M=m.fmpq_mat(sum(x.nrows() for x in blocks),blocks[0].ncols())
    row=0
    for X in blocks:
        for i in range(X.nrows()):
            for j in range(X.ncols()):
                M[row+i,j]=X[i,j]
        row+=X.nrows()
    return M

def canonical_kernel(m,reduced,rank):
    """Complete nullspace from an ACTUAL RREF, with full free-coordinate I."""
    piv=m.pivot_columns(reduced,rank)
    pset=set(piv)
    free=[j for j in range(reduced.ncols()) if j not in pset]
    K=m.fmpq_mat(reduced.ncols(),len(free))
    for j,f in enumerate(free):
        K[f,j]=1
        for i,p in enumerate(piv):
            K[p,j]=-reduced[i,f]
    return K,piv,free

def actual_leading_image(m,K,row_start,row_count):
    C=m.submatrix(K,range(row_start,row_start+row_count),range(K.ncols()))
    R,r=C.rref()
    choice=m.pivot_columns(R,r)
    selected=m.submatrix(K,range(K.nrows()),choice)
    leading=m.submatrix(C,range(C.nrows()),choice)
    return selected,leading,r

def dimensions():
    return {"sourceSectors":[len(source_rows(r)) for r in range(4)],
            "targetSectors":[len(target_columns(r)) for r in range(6)]}
