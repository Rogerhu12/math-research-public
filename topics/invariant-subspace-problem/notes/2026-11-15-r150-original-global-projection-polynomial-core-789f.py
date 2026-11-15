#!/usr/bin/env python3
"""Exact original R150 projection outside known support: polynomial 56 x 22 core.

Author: AI (ChatGPT / literature_audit), 2026-11-15 UTC.
No mathematical work on import.  No Taylor truncation, large Macaulay RREF,
finite-field rank, or unverified replacement of a true g-row by a unit.
All large objects are temporary immutable checkpoints, never publication data.
The optional row-module phase proves both inclusions before reporting its gcd.
python-flint 0.9.0 polynomial API:
https://python-flint.readthedocs.io/en/latest/fmpq_poly.html
https://python-flint.readthedocs.io/en/latest/fmpz_poly.html
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import resource
import signal
import sys
import time
from math import comb
from flint import fmpq, fmpq_poly

GENERATOR_SHA = "2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
FORMAT = "r150-original-global-projection-polynomial-core-v1"
Z = fmpq_poly([])
O = fmpq_poly([1])
X = fmpq_poly([0,1])
DEADLINE = float("inf")
BMON = [(0,0),(1,0),(0,1),(2,0),(1,1),(3,0),(2,1)]
PUREFREE = [(a,0) for a in range(1,6)] + [(a,1) for a in range(5)] + [(0,2),(1,2),(0,3)]
PUREKEEP = [(2,2),(1,3),(3,2),(2,3)]
FACTORS = [X, X-2, X+6, fmpq_poly([-8,32,-25,5]),
           fmpq_poly([864,864,135,5]),
           fmpq_poly([9600,-25472,-3392,15936,-2888,-936,153,50,5])]
DLINEAR = FACTORS[0]**8 * FACTORS[1]**2 * FACTORS[2]**2 * FACTORS[3]**3 * FACTORS[4]**3 * FACTORS[5]**2
G = -2 * X**2 * (X-2) * (X+6)

class BudgetStop(Exception):
    pass

def require(test, msg):
    if not test:
        raise AssertionError(msg)

def tick():
    if time.monotonic() >= DEADLINE:
        raise BudgetStop("Shared time budget reached at a checkpoint boundary")

def canonical(obj):
    return json.dumps(obj, sort_keys=True, ensure_ascii=True,
                      separators=(",",":")).encode("ascii")

def sha(data):
    return hashlib.sha256(data).hexdigest()

def file_id(path):
    path = Path(path)
    h = hashlib.sha256()
    size = 0
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1 << 20), b""):
            h.update(b)
            size += len(b)
    return {"bytes":size,"sha256":h.hexdigest()}

def atomic_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = canonical(obj)
    tmp = path.with_name(path.name+".tmp-"+str(os.getpid()))
    with tmp.open("wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)

def encp(p):
    return [str(x) for x in p.coeffs()]

def decp(p):
    return fmpq_poly([fmpq(x) for x in p])

def encm(A):
    return [[encp(p) for p in row] for row in A]

def decm(A):
    return [[decp(p) for p in row] for row in A]

def phash(A):
    return sha(canonical(encm(A)))

def pstats(A):
    flat = [p for row in A for p in row if p]
    return {"shape":[len(A),len(A[0]) if A else 0],
            "nonzeroEntries":len(flat),
            "maximumDegree":max([int(p.degree()) for p in flat],default=-1),
            "maximumNumeratorBits":max([int(p.numer().height_bits()) for p in flat],default=0),
            "maximumDenominatorBits":max([int(p.denom()).bit_length() for p in flat],default=0),
            "logicalSha256":phash(A)}

class Cache:
    def __init__(self, root, binding):
        self.root = Path(root)
        self.root.mkdir(parents=True,exist_ok=True)
        self.path = self.root/"checkpoint-manifest.json"
        self.binding = binding
        if self.path.exists():
            self.manifest = json.loads(self.path.read_text())
            require(self.manifest["format"]==FORMAT and self.manifest["binding"]==binding,
                    "Checkpoint semantic binding mismatch")
        else:
            self.manifest = {"format":FORMAT,"binding":binding,"phases":{}}
            atomic_json(self.path,self.manifest)

    def has(self,name):
        return name in self.manifest["phases"]

    def get(self,name):
        rec = self.manifest["phases"][name]
        path = self.root/rec["file"]
        require(file_id(path)=={"bytes":rec["bytes"],"sha256":rec["sha256"]},
                "Checkpoint file identity: "+name)
        with gzip.open(path,"rb") as f:
            data = f.read()
        require(sha(data)==rec["payloadSha256"],"Checkpoint payload identity: "+name)
        obj = json.loads(data)
        require(obj["binding"]==self.binding and obj["phase"]==name,
                "Checkpoint content binding: "+name)
        return obj["payload"]

    def put(self,name,payload,verified,summary=None):
        obj = {"format":FORMAT,"binding":self.binding,"phase":name,
               "verified":bool(verified),"payload":payload}
        data = canonical(obj)
        digest = sha(data)
        path = self.root/(name+"-"+digest+".json.gz")
        if not path.exists():
            tmp = path.with_name(path.name+".tmp-"+str(os.getpid()))
            with tmp.open("wb") as raw:
                with gzip.GzipFile(filename="",fileobj=raw,mode="wb",compresslevel=1,mtime=0) as f:
                    f.write(data)
                raw.flush()
                os.fsync(raw.fileno())
            os.replace(tmp,path)
        ident = file_id(path)
        rec = dict(ident,file=path.name,payloadSha256=digest,verified=bool(verified),
                   temporaryOnly=True)
        if summary is not None:
            rec["summary"] = summary
        self.manifest["phases"][name] = rec
        atomic_json(self.path,self.manifest)
        return rec

def zeros(n,m):
    return [[Z for _ in range(m)] for _ in range(n)]

def eye(n):
    return [[O if i==j else Z for j in range(n)] for i in range(n)]

def transpose(A):
    return [list(x) for x in zip(*A)]

def madd(A,B,scale=1):
    return [[x+scale*y for x,y in zip(a,b)] for a,b in zip(A,B)]

def mscale(A,q):
    return [[q*x for x in row] for row in A]

def mm(A,B):
    require(A and B and len(A[0])==len(B),"Polynomial multiplication dimensions")
    R = zeros(len(A),len(B[0]))
    for i,row in enumerate(A):
        for k,a in enumerate(row):
            if a:
                for j,b in enumerate(B[k]):
                    if b:
                        R[i][j] = R[i][j] + a*b
    return R

def mv(A,v):
    return [sum((a*b for a,b in zip(row,v)),Z) for row in A]

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),Z)

def sub(A,rows,cols):
    return [[A[i][j] for j in cols] for i in rows]

def zero(A):
    return all(not p for row in A for p in row)

def poly_exact(a,b,where):
    q,r = divmod(a,b)
    require(not r,"Non-exact polynomial division: "+where)
    return q

def qmatrix(M):
    return [[fmpq_poly([M[i,j]]) for j in range(M.ncols())] for i in range(M.nrows())]

def encode_coeff(pure,linear):
    return {"pure":[encp(p) for p in pure],
            "linear":[[[encp(p) for p in mode] for mode in entry] for entry in linear]}

def decode_coeff(d):
    return ([decp(p) for p in d["pure"]],
            [[[decp(p) for p in mode] for mode in entry] for entry in d["linear"]])

def original_polynomials(m):
    """The exact original seventeen equations, evaluated in Q[s], without jets."""
    Kq = m.fmpq_mat(m.ORIGINAL_K)
    J2q = m.polynomial_power_kernel(Kq,2)
    J3q = m.polynomial_power_kernel(Kq,3)
    J2iq,J3iq = J2q.inv(),J3q.inv()
    require(J2q*J2iq==m.fmpq_mat([[int(i==j) for j in range(11)] for i in range(11)]),
            "Original J2 inverse")
    require(J3q*J3iq==m.fmpq_mat([[int(i==j) for j in range(16)] for i in range(16)]),
            "Original J3 inverse")
    require(int(J2q.det())==-64701092257700249600,"Original J2 determinant")
    require(int(J3q.det())==23366320238786911411830138211362846399922176000,
            "Original J3 determinant")
    K,J2,J3i = qmatrix(Kq),qmatrix(J2q),qmatrix(J3iq)
    y = [X**i for i in range(6)]
    yp = [Z]+[i*X**(i-1) for i in range(1,6)]
    p = mv(K,y)
    require(not dot(y,p) and not dot(yp,p) and dot(yp,mv(K,yp))==G,
            "Original contact polynomial and tangent identities")

    def moment(j):
        return [comb(i,j)*X**(i-j) if i>=j else Z for i in range(11)]

    def evaluate(v):
        M = [[v[i+j] for j in range(6)] for i in range(6)]
        KM = mm(K,M)
        KMK = mm(KM,K)
        quad = mm(M,KM)
        pv = mv(J2,v)
        convolution = [sum((p[i-j]*pv[j] for j in range(11)
                            if 0<=i-j<6),Z) for i in range(16)]
        tensor = mv(J3i,convolution)
        contracted = [[sum((tensor[i+j+k]*p[k] for k in range(6)),Z)
                       for j in range(6)] for i in range(6)]
        NN = madd(mscale(quad,4),mscale(contracted,6))
        polar = mm(mm(K,NN),K)
        N = [sum((polar[i][j] for i in range(6) for j in range(6) if i+j==a),Z)
             for a in range(11)]
        square = mm(KM,KM)
        tau = sum((square[i][i] for i in range(6)),Z)
        qp = mv(quad,p)
        gamma = [2*tau*y[i]+8*qp[i]-
                 12*sum((tensor[i+j+k]*KMK[j][k] for j in range(6) for k in range(6)),Z)
                 for i in range(6)]
        return N+gamma

    Y,T = moment(0),moment(1)
    pure = [4*G*x for x in mv(J2,Y)] + [Z]*6
    for vec,d in ((Y,0),(T,1),([-x for x in Y],0),
                  ([-x for x in T],-1),([a+b for a,b in zip(Y,T)],1)):
        require(evaluate(vec)==[d*d*x for x in pure],
                "All17 exact pure-plane original equations")
    tan = [Y,T]
    Ft = [evaluate(v) for v in tan]
    linear=[]
    for j in range(2,11):
        tick()
        v=moment(j)
        Fv,Fneg=evaluate(v),evaluate([-x for x in v])
        modes=[[(a-b)/2 for a,b in zip(Fv,Fneg)]]
        for tt in range(2):
            Fsum=evaluate([a+b for a,b in zip(tan[tt],v)])
            modes.append([a-b-c for a,b,c in zip(Fsum,Fv,Ft[tt])])
        linear.append(modes)
    require(all(not linear[j][0][i] for j in range(9) for i in range(11,17)),
            "Gamma has no moment-linear terms")
    require(max(int(q.degree()) for q in pure+[
        p for ent in linear for mode in ent for p in mode])<=25,
        "Untruncated original polynomial degree")
    inverse_row = [J2iq[0,i]/4 for i in range(11)]
    require(sum((inverse_row[i]*pure[i] for i in range(11)),Z)==G,
            "True g-row is a constant combination of original N sources")
    return pure,linear,{"J2":m.matrix_hash(J2q),"J3":m.matrix_hash(J3q),
                        "detJ2":str(J2q.det()),"detJ3":str(J3q.det()),
                        "compressionOriginalWeights":[str(x) for x in inverse_row],
                        "all17PurePolynomialIdentities":True,
                        "allOriginalPolarizedLinearCoefficientsRetained":True,
                        "noTaylorTruncation":True}

def indices():
    pc=[(a,d-a) for d in range(1,6) for a in range(d+1)]
    nc=[(a,d-a,j) for d in range(5) for a in range(d+1) for j in range(2,11)]
    rows=[(i,a,d-a) for i in range(17) for d in range(4) for a in range(d+1)]
    return pc,nc,rows

def build_P(pure,linear):
    pc,nc,rows=indices()
    pi={k:i for i,k in enumerate(pc)}
    ni={k:20+i for i,k in enumerate(nc)}
    P=zeros(224,155)
    for r,(i,a,b) in enumerate(rows):
        P[r][pi[(a,b+2)]] = P[r][pi[(a,b+2)]] + pure[i]
        for j in range(2,11):
            for mode,(da,db) in enumerate(((0,0),(1,0),(0,1))):
                P[r][ni[(a+da,b+db,j)]] = P[r][ni[(a+da,b+db,j)]] + linear[j-2][mode][i]
    extra=[k for k in nc if k[1]>=2]
    require(len(extra)==54,"All54 single-normal sources")
    for i,key in enumerate(extra):
        P[170+i][ni[key]]=G
    # Every original source with one normal factor reads only the original
    # pure part.  Check its exact representation in the retained 54 g rows.
    checked=0
    for i in range(17):
        ratio=poly_exact(pure[i],G,"Original one-normal g compression")
        for degree in range(3):
            for a in range(degree+1):
                b=degree-a
                for j in range(2,11):
                    require((a,b+2,j) in extra and ratio*G==pure[i],
                            "Every original one-normal source represented")
                    checked+=1
    require(checked==918,"All918 actual one-normal source rows")
    # The equations have only moment-degrees1 and2, so the remaining
    # 2295+2805 sources have no pure/one-normal projection coordinates.
    require(17*45*3+17*165==5100,"All higher-normal sources retained as zero projection")
    return P,pc,nc,rows

def prefix_check(m,P,nc,rows):
    P0,P1,nc0,rows0,physical=m.make_projection_jets("zero")
    require(nc0==nc and rows0==rows,"Original first prefix coordinate order")
    for k,M in enumerate((P0,P1)):
        require(all(P[i][20+j][k]==M[i,j] for i in range(170) for j in range(135)),
                "All original P"+str(k)+" prefix coefficients")
    return {"P0":m.matrix_hash(P0),"P1":m.matrix_hash(P1),"physical":physical}

def transformed_remainder(P,pc,nc,rows):
    colidx={("n",)+key:20+i for i,key in enumerate(nc)}
    colidx.update({("p",)+key:i for i,key in enumerate(pc)})
    cols=[("n",a,b,j) for a,b in BMON for j in range(2,11)]
    cols += [("n",4,0,j) for j in range(2,11)]
    cols += [("n",3,1,j) for j in range(2,11)]
    cols += [("p",)+x for x in PUREKEEP]
    require(len(cols)==85 and len(set(cols))==85,"Retained85 coordinates")
    ix={key:i for i,key in enumerate(rows)}
    R=zeros(119,85)
    for block,(a,b) in enumerate(BMON):
        for k in range(11):
            for i in range(k,11):
                q=comb(i,k)*X**(i-k)
                old=P[ix[(i,a,b)]]
                for j,key in enumerate(cols):
                    if old[colidx[key]]:
                        R[17*block+k][j] = R[17*block+k][j] + q*old[colidx[key]]
        for k in range(11,17):
            R[17*block+k]=[P[ix[(k,a,b)]][colidx[key]] for key in cols]
    pr=[17*b+i for b in range(7) for i in range(2,11)]
    lr=[17*b+i for b in range(7) for i in [0,1]+list(range(11,17))]
    U=sub(R,pr,range(63));B=sub(R,pr,range(63,85))
    C=sub(R,lr,range(63));D=sub(R,lr,range(63,85))
    H=sub(U,range(9),range(9))
    require(not zero(H),"Original linear block nonzero")
    for a in range(7):
        require(sub(U,range(9*a,9*a+9),range(9*a,9*a+9))==H,
                "Seven identical original H blocks")
        for b in range(7):
            if a!=b and sum(BMON[b])!=sum(BMON[a])+1:
                require(zero(sub(U,range(9*a,9*a+9),range(9*b,9*b+9))),
                        "Exact adjacent-degree upper triangular U")
    return R,U,B,C,D,H,cols

def adjugate(H):
    """Fraction-free Gauss-Jordan over Q[s], with all exact divisions checked."""
    n=len(H)
    A=[row[:] + eye(n)[i] for i,row in enumerate(H)]
    previous=O
    for k in range(n):
        tick()
        choices=[i for i in range(k,n) if A[i][k]]
        require(choices,"H determinant nonzero")
        p=min(choices,key=lambda i:(int(A[i][k].degree()),i))
        if p!=k:
            A[k],A[p]=A[p],A[k]
        pivot=A[k][k]
        for i in range(n):
            if i==k:
                continue
            multiplier=A[i][k]
            for j in range(2*n):
                if j!=k:
                    A[i][j]=poly_exact(pivot*A[i][j]-multiplier*A[k][j],
                                      previous,"H fraction-free step")
            A[i][k]=Z
        previous=pivot
    raw=A[0][0]
    require(raw and sub(A,range(n),range(n))==mscale(eye(n),raw),
            "Fraction-free adjugate scalar diagonal")
    AR=sub(A,range(n),range(n,2*n))
    require(mm(H,AR)==mscale(eye(n),raw) and mm(AR,H)==mscale(eye(n),raw),
            "Original H adjugate both products")
    scale=poly_exact(raw,DLINEAR,"det(H) / actual Dlinear")
    require(scale.degree()==0 and scale[0],"Original determinant has exactly paid Dlinear")
    AD=mscale(AR,1/scale[0])
    require(mm(H,AD)==mscale(eye(n),DLINEAR) and mm(AD,H)==mscale(eye(n),DLINEAR),
            "Normalized H adjugate both products")
    return AD,raw,scale[0]

def free_graph(P,pc,nc,pure,linear,AD):
    ni={key:20+i for i,key in enumerate(nc)}
    pi={key:i for i,key in enumerate(pc)}
    def transformed(eqvec):
        return [sum((comb(i,k)*X**(i-k)*eqvec[i] for i in range(k,11)),Z)
                for k in range(2,11)]
    v=transformed(pure)
    r=[-x for x in mv(AD,v)]
    Nc=transpose([transformed(linear[j][1]) for j in range(9)])
    Nd=transpose([transformed(linear[j][2]) for j in range(9)])
    rc=[-x for x in mv(AD,mv(Nc,r))]
    rd=[-x for x in mv(AD,mv(Nd,r))]
    Q=zeros(155,13)
    for f,key in enumerate(PUREFREE):
        Q[pi[key]][f]=DLINEAR**2
    for j in range(2,11):
        Q[ni[(0,0,j)]][10]=DLINEAR*r[j-2]
        Q[ni[(1,0,j)]][11]=DLINEAR*r[j-2]
        Q[ni[(0,0,j)]][11]=rc[j-2]
        Q[ni[(0,1,j)]][12]=DLINEAR*r[j-2]
        Q[ni[(0,0,j)]][12]=rd[j-2]
    require(zero(mm(P,Q)),"All224 original rows / 13 actual polynomial free kernels")
    require(sub(Q,[pi[k] for k in PUREFREE],range(13))==mscale(eye(13),DLINEAR**2),
            "True free13 coordinate normalization over localized ring")
    return Q

def remove_known_factors(A):
    """Only exact divisions by known localized units; constants stay in Q units."""
    B=[row[:] for row in A]
    ops=[]
    while True:
        changed=False
        for axis in ("row","column"):
            count=len(B) if axis=="row" else len(B[0])
            for k in range(count):
                entries=B[k] if axis=="row" else [row[k] for row in B]
                if not any(entries):
                    continue
                for fno,f in enumerate(FACTORS):
                    power=0
                    while True:
                        quot=[divmod(p,f) for p in entries]
                        if any(r for q,r in quot):
                            break
                        entries=[q for q,r in quot]
                        power+=1
                    if power:
                        changed=True
                        ops.append({"axis":axis,"index":k,"knownFactor":fno,"power":power})
                if axis=="row":
                    B[k]=entries
                else:
                    for i,p in enumerate(entries):
                        B[i][k]=p
        tick()
        if not changed:
            break
    return B,ops

def core_phase(m,cache):
    if cache.has("polynomial-core"):
        return decm(cache.get("polynomial-core")["core"])
    if cache.has("original-polynomials"):
        cp=cache.get("original-polynomials")
        pure,linear=decode_coeff(cp["coefficients"])
    else:
        pure,linear,physical=original_polynomials(m)
        P,pc,nc,rows=build_P(pure,linear)
        prefix=prefix_check(m,P,nc,rows)
        cp={"coefficients":encode_coeff(pure,linear),"physical":physical,
            "firstPrefix":prefix,"originalProjection":pstats(P)}
        cache.put("original-polynomials",cp,True,
                  {"allOriginalPolynomials":True,"prefixChecked":True,
                   "all918OneNormalSourceRepresentationsVerified":True,
                   "all5100HigherNormalSourceProjectionsZeroByExactSupport":True,
                   "projection":pstats(P)})
    tick()
    P,pc,nc,rows=build_P(pure,linear)
    R,U,B,C,D,H,cols=transformed_remainder(P,pc,nc,rows)
    if cache.has("linear-adjugate"):
        ap=cache.get("linear-adjugate")
        AD=decm(ap["normalizedAdjugate"])
        require(mm(H,AD)==mscale(eye(9),DLINEAR),"Restored H adjugate")
    else:
        AD,hraw,scale=adjugate(H)
        ap={"normalizedAdjugate":encm(AD),"actualH":encm(H),
            "rawDeterminant":encp(hraw),"constantDeterminantFactor":str(scale)}
        cache.put("linear-adjugate",ap,True,
                  {"H":pstats(H),"normalizedAdjugate":pstats(AD),
                   "all162AdjugateCoordinatesVerified":True})
    tick()
    if not cache.has("free-thirteen-kernel"):
        Q=free_graph(P,pc,nc,pure,linear,AD)
        cache.put("free-thirteen-kernel",{"matrix":encm(Q)},True,
                  {"matrix":pstats(Q),"all2912OriginalProductsZero":True,
                   "freeNormalization":"Dlinear^2 I13"})
    nums={}
    for degree in range(3,-1,-1):
        name="triangular-degree-"+str(degree)
        if cache.has(name):
            obj=cache.get(name)
            for key,arr in obj["numerators"].items():
                nums[int(key)]=decm(arr)
            continue
        for a in range(7):
            if sum(BMON[a])!=degree:
                continue
            rhs=mscale(B[9*a:9*a+9],DLINEAR**(3-degree))
            for b in range(7):
                if sum(BMON[b])==degree+1:
                    rhs=madd(rhs,mm(sub(U,range(9*a,9*a+9),range(9*b,9*b+9)),nums[b]),-1)
            nums[a]=mm(AD,rhs)
            require(mm(H,nums[a])==mscale(rhs,DLINEAR),
                    "Each complete triangular block equation")
        cache.put(name,{"numerators":{str(a):encm(nums[a]) for a in nums
                                      if sum(BMON[a])==degree}},True,
                  {"degree":degree,"blockCount":sum(sum(b)==degree for b in BMON)})
        tick()
    N=[]
    for a in range(7):
        N+=mscale(nums[a],DLINEAR**sum(BMON[a]))
    require(mm(U,N)==mscale(B,DLINEAR**4),"All1386 original U N = Dlinear^4 B coordinates")
    full=madd(mscale(D,DLINEAR**4),mm(C,N),-1)
    graph=[[-p for p in row] for row in N]+mscale(eye(22),DLINEAR**4)
    product=mm(R,graph)
    pr=[17*b+i for b in range(7) for i in range(2,11)]
    lr=[17*b+i for b in range(7) for i in [0,1]+list(range(11,17))]
    require(zero(sub(product,pr,range(22))) and sub(product,lr,range(22))==full,
            "All2618 retained original graph products")
    cache.put("polynomial-uncancelled-core",
              {"core":encm(full),"graph":encm(graph),"retainedMatrix":encm(R),
               "retainedColumns":[list(k) for k in cols]},True,
              {"core":pstats(full),"allOriginal119GraphRowsVerified":True})
    reduced,ops=remove_known_factors(full)
    cache.put("polynomial-core",
              {"core":encm(reduced),"knownUnitDivisions":ops,
               "knownFactors":[encp(f) for f in FACTORS],
               "allOriginalSourceRowsRetainedBeforeUnitElimination":True},True,
              {"core":pstats(reduced),"knownUnitDivisionCount":len(ops),
               "knownUnitDivisionsSha256":sha(canonical(ops)),
               "separatedUnitColumns":120,"separatedFreeColumns":13,
               "separatedZeroRows":48,"previouslyProvedGenericRank":22,
               "newGcdNotYetComputed":True})
    return reduced

def primitive(row,provenance):
    denominator=1
    for p in row:
        denominator=math.lcm(denominator,int(p.denom()))
    integral=[p*denominator for p in row]
    content=0
    for p in integral:
        content=math.gcd(content,abs(int(p.numer().content())))
    if not content:
        return row,provenance
    lead=next(p for p in integral if p)
    scale=fmpq(denominator,content)
    if lead.leading_coefficient()<0:
        scale=-scale
    return [scale*p for p in row],[scale*p for p in provenance]

def leading(row):
    nz=[(int(p.degree()),j) for j,p in enumerate(row) if p]
    if not nz:
        return None
    degree,j=max(nz)
    return j,degree,row[j].leading_coefficient()

def module_phase(A,cache):
    """Exact row-module equality with original56 forward certificates and reverse division."""
    nr,nc=len(A),len(A[0])
    if cache.has("row-module-complete"):
        return cache.get("row-module-complete")
    if cache.has("row-module-state"):
        st=cache.get("row-module-state")
        basis=[None if v is None else [decp(p) for p in v] for v in st["basis"]]
        provenance=[None if v is None else [decp(p) for p in v] for v in st["provenance"]]
        current=[decp(p) for p in st["current"]]
        curprov=[decp(p) for p in st["currentProvenance"]]
        row=int(st["nextInputRow"]);ops=int(st["operations"])
    else:
        basis=[None]*nc;provenance=[None]*nc
        current=[];curprov=[];row=0;ops=0
    def save():
        payload={"basis":[None if v is None else [encp(p) for p in v] for v in basis],
                 "provenance":[None if v is None else [encp(p) for p in v] for v in provenance],
                 "current":[encp(p) for p in current],
                 "currentProvenance":[encp(p) for p in curprov],
                 "nextInputRow":row,"operations":ops}
        cache.put("row-module-state",payload,False,
                  {"processedOriginalRows":row,"basisRows":sum(v is not None for v in basis),
                   "operations":ops,"candidateOnly":True})
    try:
        while row<nr or current:
            tick()
            if not current:
                current,curprov=primitive(A[row][:],[O if j==row else Z for j in range(nr)])
                row+=1
            while any(current):
                pos,degree,lc=leading(current)
                if basis[pos] is None:
                    basis[pos],provenance[pos]=current,curprov
                    current=[];curprov=[]
                    break
                bd=int(basis[pos][pos].degree())
                if degree<bd:
                    current,basis[pos]=basis[pos],current
                    curprov,provenance[pos]=provenance[pos],curprov
                    pos,degree,lc=leading(current)
                    bd=int(basis[pos][pos].degree())
                q=(lc/basis[pos][pos].leading_coefficient())*X**(degree-bd)
                current=[x-q*y for x,y in zip(current,basis[pos])]
                curprov=[x-q*y for x,y in zip(curprov,provenance[pos])]
                current,curprov=primitive(current,curprov)
                ops+=1
                if ops%16==0:
                    save()
                    tick()
            if current and not any(current):
                current=[];curprov=[]
            save()
    except BudgetStop:
        # An asynchronous signal may interrupt between the row and its
        # provenance assignments.  Resume only the last atomic boundary;
        # never publish the possibly half-updated in-memory pair.
        raise
    require(all(v is not None for v in basis),"Full original generic core rank22")
    # A weak Popov basis has one leading position per row.  These forward
    # products and reverse reductions certify equality of the two polynomial modules.
    basisid=phash(basis)
    verified_forward=0
    if cache.has("module-forward-verification"):
        fv=cache.get("module-forward-verification")
        require(fv["basisSha256"]==basisid,"Forward verification basis identity")
        verified_forward=fv["verifiedRows"]
    for i in range(verified_forward,nc):
        require(mv(transpose(A),provenance[i])==basis[i],
                "Actual polynomial forward row-source identity "+str(i))
        cache.put("module-forward-verification",
                  {"verifiedRows":i+1,"basisSha256":basisid},True,
                  {"original56RowCombinationsVerified":i+1})
        tick()
    verified_reverse=0
    if cache.has("module-reverse-verification"):
        rv=cache.get("module-reverse-verification")
        require(rv["basisSha256"]==basisid,"Reverse verification basis identity")
        verified_reverse=rv["verifiedRows"]
    for i in range(verified_reverse,nr):
        r=A[i][:]
        while any(r):
            p,d,lc=leading(r)
            b=basis[p]
            require(d>=int(b[p].degree()),"Original row not in polynomial basis module")
            q=(lc/b[p].leading_coefficient())*X**(d-int(b[p].degree()))
            r=[x-q*y for x,y in zip(r,b)]
        cache.put("module-reverse-verification",
                  {"verifiedRows":i+1,"basisSha256":basisid},True,
                  {"originalRowsReducedExactlyToZero":i+1})
        tick()
    data={"basis":encm(basis),"provenance":encm(provenance),"rank":nc,
          "allForwardOriginalCombinationsVerified":True,
          "allOriginalRowsReduceToZero":True,"operations":ops}
    cache.put("row-module-complete",data,True,
              {"basis":pstats(basis),"all1232ForwardCoordinatesVerified":True,
               "all56OriginalRowsReduceToZero":True,"rank":nc,"operations":ops})
    return data

def determinant_phase(module,cache):
    if cache.has("complete-gcd"):
        return cache.get("complete-gcd")
    if cache.has("hermite-state"):
        st=cache.get("hermite-state")
        A=decm(st["matrix"]);row=int(st["pivot"])
    else:
        A=decm(module["basis"]);row=0
    n=len(A)
    for k in range(row,n):
        tick()
        choices=[i for i in range(k,n) if A[i][k]]
        require(choices,"Full polynomial row-module determinant")
        q=min(choices,key=lambda i:(int(A[i][k].degree()),i))
        if q!=k:
            A[k],A[q]=A[q],A[k]
        for i in range(k+1,n):
            while A[i][k]:
                div,rem=divmod(A[i][k],A[k][k])
                A[i]=[x-div*y for x,y in zip(A[i],A[k])]
                A[i],_=primitive(A[i],[])
                if rem:
                    A[i],A[k]=A[k],A[i]
                tick()
        require(all(not A[i][k] for i in range(k+1,n)),"Hermite exact column elimination")
        cache.put("hermite-state",{"matrix":encm(A),"pivot":k+1},False,
                  {"completedPivotColumns":k+1,"candidateOnly":True})
    determinant=O
    for i in range(n):
        determinant = determinant*A[i][i]
    require(determinant,"Nonzero complete determinant gcd")
    determinant = determinant/determinant.leading_coefficient()
    outside=determinant
    vals=[]
    for f in FACTORS:
        exponent=0
        while True:
            q,r=divmod(outside,f)
            if r:
                break
            outside=q
            exponent+=1
        vals.append(exponent)
    outside = outside/outside.leading_coefficient()
    data={"fullDeterminantGcdMonic":encp(determinant),
          "outsideKnownSupportGcdMonic":encp(outside),
          "removedKnownFactorValuations":vals,
          "exactFullRowModuleEqualityAlreadyVerified":True,
          "originalProjectionOutsideGcdDegree":int(outside.degree()),
          "doesNotProveAnyUnknownNineTargetFactorVanishes":True}
    cache.put("complete-gcd",data,True,
              {"fullGcdDegree":int(determinant.degree()),
               "outsideKnownSupportGcdDegree":int(outside.degree()),
               "gcdCoefficientSha256":sha(canonical(data)),
               "removedKnownFactorValuations":vals,
               "isTrueCharacteristicZeroCompleteProjectionGcdOutsideKnownSupport":True,
               "doesNotProveNineTargetGlobalMembership":True})
    return data

def main():
    global DEADLINE
    ap=argparse.ArgumentParser()
    ap.add_argument("--generator",required=True)
    ap.add_argument("--out",required=True)
    ap.add_argument("--through",choices=("core","module","gcd"),default="gcd")
    ap.add_argument("--remaining-seconds",type=float,default=300.0)
    ap.add_argument("--memory-mib",type=int,default=2048)
    args=ap.parse_args()
    require(args.remaining_seconds>0 and args.memory_mib>=512,"Resource parameters")
    resource.setrlimit(resource.RLIMIT_AS,(args.memory_mib*1024**2,args.memory_mib*1024**2))
    start=time.monotonic()
    DEADLINE=start+max(0.01,args.remaining_seconds-min(15,args.remaining_seconds/10))
    def alarm(sig,frame):
        raise BudgetStop("Shared real-time deadline")
    signal.signal(signal.SIGALRM,alarm)
    signal.setitimer(signal.ITIMER_REAL,args.remaining_seconds)
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    selfid=file_id(__file__)
    genid=file_id(args.generator)
    require(genid["sha256"]==GENERATOR_SHA,"Pinned original physical generator")
    binding=sha(canonical({"format":FORMAT,"script":selfid,"generator":genid,
                          "parameter":"original finite s","field":"Q",
                          "sourceDegreeLimit":3,"targetDegreeLimit":5,
                          "localizationFactors":[encp(f) for f in FACTORS]}))
    cache=Cache(out/"checkpoints",binding)
    receipt={"format":FORMAT,"status":"started","binding":binding,
             "parameters":{"inputFiles":{"generator":genid,"script":selfid},
                           "through":args.through,"remainingSeconds":args.remaining_seconds,
                           "memoryMiB":args.memory_mib,"originalSourceRows":6188,
                           "originalTargetRows":4367,"projectionShape":[224,155],
                           "coreShape":[56,22],
                           "currentlyPaidFullInfinityLengthLowerBound":63,
                           "currentlyPaidResidualMultiplierDegreeUpperBound":160,
                           "currentlyPaidResidualTimesReducedH0DegreeUpperBound":183,
                           "temporaryLargeCheckpointsOnly":True}}
    try:
        spec=importlib.util.spec_from_file_location("paid_original_physical_generator",args.generator)
        m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
        core=core_phase(m,cache)
        if args.through in ("module","gcd"):
            module=module_phase(core,cache)
            if args.through=="gcd":
                determinant_phase(module,cache)
        receipt["status"]="completed"
    except BudgetStop as e:
        receipt["status"]="budget-checkpoint"
        receipt["message"]=str(e)
    except BaseException as e:
        receipt["status"]="failed"
        receipt["error"]={"type":type(e).__name__,"message":str(e)}
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        receipt["elapsedSeconds"]=time.monotonic()-start
        # Read the atomically committed manifest, including when SIGALRM
        # interrupted the in-memory update immediately before/after replace.
        cache.manifest=json.loads(cache.path.read_text())
        require(cache.manifest["binding"]==binding,"Final actual manifest binding")
        receipt["parameters"]["checkpointManifest"]=file_id(cache.path)
        receipt["parameters"]["checkpointPhases"]=cache.manifest["phases"]
        receipt["parameters"]["allLargeArtifactsTemporaryOnly"]=True
        receipt["noNewNineTargetMembershipClaim"]=True
        payload=canonical(receipt)
        require(len(payload)<90000,"Small receipt must remain below publication budget")
        atomic_json(out/"original-global-projection-core-receipt.json",receipt)
        print(payload.decode("ascii"),flush=True)
    return 0 if receipt["status"] in ("completed","budget-checkpoint") else 1

if __name__=="__main__":
    raise SystemExit(main())
