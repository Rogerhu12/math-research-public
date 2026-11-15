#!/usr/bin/env python3
"""Original R150 co-moving s=2 coefficients through order3.

Author: Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro.
Pure helper; no mathematical computation on import.  This is the entire
previously verified original_at_two formula with only its order guard widened.
All four terms of g(2+t), the parameter-dependent y,p and every convolution
are retained.  Consumers must compare the full0..2 physical prefixes with
the previously verified receipt before using the new coefficient3.
"""
from math import comb

def require(ok,message):
    if not ok:raise AssertionError(message)

def original_at_two(m,jmod,max_order=3):
    """All17 exact original coefficients at s=2+t in co-moving moments."""
    require(1<=max_order<=3,"Original s=2 coefficients through at most order3")
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
