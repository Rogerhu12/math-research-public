#!/usr/bin/env python3
"""Original pencil reconstruction, rank-four trace, and full singularity gates.

Author: Astra-ISP-789f / normal_annihilator, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Rebuild the same four mean matrices from the literal original potential and
matched Bell coordinate map. All inverses are fixed coefficient-field units.
The legal127 place is used for complete polynomial coefficient certificates;
no mean, moment, or pencil parameter point replaces a source identity.
All mathematical arrays stay in temporary phases and execution logs.
"""
import argparse,functools,gzip,hashlib,importlib.util,itertools,json,os
from pathlib import Path
import resource,signal,sys,time
from flint import fmpq,nmod_mat,nmod_mpoly_ctx
sys.set_int_max_str_digits(0)

FORMAT="r150-original-pencil-trace-and-complete-singularity-gates-v1"
P=127
ROOT=100
HELPER_SHA="31df769fb0fd3a41eb7606f500aae8b46952219c24927bd3265ed3dc34d7fe10"
FIELD_SHA="da80b727c47a050f3e268f00d1d6598336866a41b354d6aecb5edbb1ca1e730d"
MATCHED=[52565262336,6080833024,-43931504,3725]
HP=[2,1,0,3,4,5]
HU=[6,7,8,9,10]
KEEP_PAIRS=[(1,4),(2,3),(2,4),(3,4)]
CANON_POS=[(0,0),(0,1),(0,2),(0,3)]

def need(b,s):
    if not b:raise ValueError(s)
def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(",",":")).encode("ascii")
def sha(x):return hashlib.sha256(x).hexdigest()
def identity(p):
    b=Path(p).read_bytes()
    return {"bytes":len(b),"sha256":sha(b)}
def save_json(p,x):
    b=json.dumps(x,sort_keys=True,indent=2).encode("ascii")
    q=p.with_name(p.name+".tmp");q.write_bytes(b);os.replace(q,p)
    return {"path":p.name,"bytes":len(b),"sha256":sha(b)}
def save_gz(p,x):
    b=canonical(x);z=gzip.compress(b,compresslevel=1,mtime=0)
    q=p.with_name(p.name+".tmp");q.write_bytes(z);os.replace(q,p)
    return {"path":p.name,"bytes":len(z),"sha256":sha(z),
            "logicalBytes":len(b),"logicalSha256":sha(b)}
def load_gz(p,d,binding):
    z=p.read_bytes()
    need(len(z)==d["bytes"] and sha(z)==d["sha256"],"entire saved phase bytes")
    b=gzip.decompress(z)
    need(len(b)==d["logicalBytes"] and sha(b)==d["logicalSha256"],"entire saved logical phase")
    x=json.loads(b);need(x["binding"]==binding,"same mathematical phase binding")
    return x["data"]
def module(path,name,expected):
    need(identity(path)["sha256"]==expected,"exact source helper "+name)
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m
def mons(n,d):
    out=[]
    for ii in itertools.combinations_with_replacement(range(n),d):
        e=[0]*n
        for j in ii:e[j]+=1
        out.append(tuple(e))
    return sorted(out)
def basis_through(n,d):
    return [e for k in range(d+1) for e in mons(n,k)]
def packed(poly):
    return [[list(map(int,e)),int(c)] for e,c in sorted(poly.to_dict().items())]
def table(A):
    return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def mat(rows):return nmod_mat(rows,P)
def eye(n):return nmod_mat([[int(i==j) for j in range(n)] for i in range(n)],P)
def zeros(n,m):return nmod_mat(n,m,[0]*(n*m),P)
def inverse(A,label):
    need(A.nrows()==A.ncols(),label+" square original unit")
    d=int(A.det());need(d!=0,label+" nonzero original coefficient determinant")
    V=A.inv();I=eye(A.nrows())
    need(A*V==I and V*A==I,label+" complete left and right inverse products")
    return V,d
def rational_residue(x):
    q=fmpq(x);den=int(q.denom())%P
    need(den!=0,"every original rational coefficient has unit127 denominator")
    return int(q.numer())%P*pow(den,-1,P)%P
def field_residue(coeff):
    return sum(rational_residue(c)*pow(ROOT,i,P) for i,c in enumerate(coeff))%P

def reconstruct_original(fd,m):
    # prepare() independently verifies the full original N/Gamma gradients,
    # both J3 inverse products, weighted Euler, and every original denominator.
    original=fd.prepare(m)
    need(original["matchedCubic"]==MATCHED,"unchanged original matched cubic")
    need(original["all17OriginalGradientPolynomialsVerified"] and
         original["all512OriginalJ3InverseProductsVerified"],
         "whole original physical matrix identities before reconstruction")
    need(sum(c*pow(ROOT,i,P) for i,c in enumerate(MATCHED))%P==0 and
         sum(i*c*pow(ROOT,i-1,P) for i,c in enumerate(MATCHED) if i)%P==49,
         "same simple unramified127 place")
    L=[[0]*6 for _ in range(11)]
    for k,row in enumerate(original["BellFieldComponents"]):
        for e,c in row:
            yd=sum(e[:6]);hd=sum(e[6:])
            if hd:
                need(hd==1 and yd==1,"all original Bell H terms are y-linear")
                hi=next(i for i,v in enumerate(e[6:]) if v)
                yi=next(i for i,v in enumerate(e[:6]) if v)
                L[hi][yi]=(L[hi][yi]+rational_residue(c)*pow(ROOT,k,P))%P
    MP=mat([[L[j][i] for j in HP] for i in range(6)])
    MPinv,detMP=inverse(MP,"original six Hankel Bell columns")
    MU=mat([[L[j][i] for j in HU] for i in range(6)])
    X=-(MPinv*MU)
    N=[[0]*5 for _ in range(11)]
    for i,j in enumerate(HP):N[j]=[int(X[i,k]) for k in range(5)]
    for i,j in enumerate(HU):N[j][i]=1
    MN=mat([[L[j][i] for j in range(11)] for i in range(6)])*mat(N)
    need(MN==zeros(6,5),"all30 original Bell constant kernel products")
    need([N[j] for j in HU]==table(eye(5)),"the same five original free Hankel coordinates")
    ctx=nmod_mpoly_ctx.get(tuple("u%d"%i for i in range(5)),P,"lex")
    u=ctx.gens();zero=ctx.constant(0)
    HH=[sum((N[j][i]*u[i] for i in range(5)),zero) for j in range(11)]
    @functools.lru_cache(None)
    def hmon(e):
        v=ctx.constant(1)
        for j,k in enumerate(e):
            if k:v*=HH[j]**k
        return v
    def top(row,mean):
        ans=zero
        for e,c in row:
            if sum(e[6:])!=2:continue
            need(tuple(e[:6])==mean or sum(e[:6])==sum(mean),
                 "homogeneous original top normal degree")
            if tuple(e[:6])==mean:ans+=rational_residue(c)*hmon(tuple(e[6:]))
        need(all(sum(e)==2 for e in ans.to_dict()),"complete quadratic top after original substitution")
        return ans
    Q=[top(row,(0,)*6) for row in original["originalSeventeenGradients"][:11]]
    Y=[]
    for i in range(6):
        for j in range(6):
            mean=tuple(int(a==j) for a in range(6))
            Y.append(top(original["originalSeventeenGradients"][11+i],mean))
    mm=mons(5,2);kept=[]
    for i,j in KEEP_PAIRS:
        e=[0]*5;e[i]+=1;e[j]+=1;kept.append(mm.index(tuple(e)))
    eliminated=[j for j in range(15) if j not in kept]
    qmat=mat([[int(q.to_dict().get(e,0)) for e in mm] for q in Q])
    U=mat([[int(qmat[i,j]) for j in eliminated] for i in range(11)])
    Ui,detU=inverse(U,"complete eleven original Hankel quadratic sources")
    ymat=mat([[int(q.to_dict().get(e,0)) for e in mm] for q in Y])
    alpha=mat([[int(ymat[i,j]) for j in eliminated] for i in range(36)])
    transport=alpha*Ui
    NF=ymat-transport*qmat
    need(all(int(NF[i,j])==0 for i in range(36) for j in eliminated),
         "all396 eliminated original mean quadratic coordinates vanish")
    need(NF+transport*qmat==ymat,"all540 original mean-quadratic source identities")
    T=[[[int(NF[6*i+j,k]) for j in range(6)] for i in range(6)] for k in kept]
    need(all(T[k][i][j]==T[k][j][i] for k in range(4) for i in range(6) for j in range(6)),
         "four original mean matrices remain symmetric")
    dets=[int(mat(t).det()) for t in T]
    need(dets==[106,93,100,92],"same four previously verified original tensor determinants")
    C=mat([[T[k][i][j] for k in range(4)] for i,j in CANON_POS])
    Ci,detC=inverse(C,"unchanged four original upper-triangle pencil coordinates")
    Tp=[[[sum(T[k][i][j]*int(Ci[k,l]) for k in range(4))%P
            for j in range(6)] for i in range(6)] for l in range(4)]
    need([[Tp[k][i][j] for k in range(4)] for i,j in CANON_POS]==table(eye(4)),
         "all16 canonical original pencil coordinates")
    need(all(sum(Tp[l][i][j]*int(C[l,k]) for l in range(4))%P==T[k][i][j]
             for k in range(4) for i in range(6) for j in range(6)),
         "all144 canonical pencil coordinates return to the original tensor")
    return {"matchedCubic":MATCHED,"prime":P,"coefficientRoot":ROOT,
        "originalPhysicalModelLogicalSha256":sha(canonical(original)),
        "originalSeventeenLogicalSha256":sha(canonical(original["originalSeventeenGradients"])),
        "originalBellLogicalSha256":sha(canonical(original["BellFieldComponents"])),
        "allOriginalPhysicalCoefficientIdentitiesVerified":True,
        "allOriginalRationalDenominators127Units":True,
        "originalHankelPivotOrder":HP,"originalHankelFreeOrder":HU,
        "originalBellCoefficientMatrix":L,"originalBellUnit":table(MP),
        "originalBellUnitInverse":table(MPinv),"originalBellUnitDeterminant127":detMP,
        "originalFiveColumnHankelInclusion":N,
        "allQuadraticMonomials":mm,"keptOriginalQuadraticPositions":kept,
        "keptOriginalQuadraticMonomials":[mm[j] for j in kept],
        "eliminatedOriginalQuadraticPositions":eliminated,
        "allElevenOriginalQuadraticRows":table(qmat),
        "quadraticSourceUnit":table(U),"quadraticSourceInverse":table(Ui),
        "quadraticSourceUnitDeterminant127":detU,
        "all36OriginalMeanQuadraticRows":table(ymat),
        "completeOriginalMeanSourceTransport":table(transport),
        "allFourOriginalMeanMatrices":T,"originalMatrixDeterminants127":dets,
        "canonicalUpperTrianglePositions":CANON_POS,"canonicalUnit":table(C),
        "canonicalInverse":table(Ci),"canonicalUnitDeterminant127":detC,
        "allFourCanonicalMatrices":Tp,
        "coefficientDVRDefinition":"localization of Z_(127)[d]/monic(MATCHED) at (127,d-100)",
        "coefficientDVRSourceDefinition":{
            "originalModel":"literal helper K,J3,full R3 and matched Bell",
            "N":"H_U=I5; H_P=-M_P^{-1}M_U; constant original Bell inverse",
            "Q":"degree-two u part of all eleven original dH gradients at H=N u",
            "Y":"y_j*u^2 coefficients of all six original dy gradients at H=N u",
            "T":"unique remainder of Y modulo Q on the four fixed retained monomials",
            "Tp":"T times inverse of the four fixed upper-triangle coordinate rows"},
        "allConstantInversesHaveNonzero127Residue":True,
        "fullParameterSubstitutionOrPointSamplingUsed":False,
        "newExpandedCharacteristicZeroTensorArrayClaimed":False}

def pencil_polynomials(T):
    ctx=nmod_mpoly_ctx.get(("mu0","mu1","mu2","mu3"),P,"lex")
    mu=ctx.gens();zero=ctx.constant(0);one=ctx.constant(1)
    A=[[sum((T[k][i][j]*mu[k] for k in range(4)),zero)
        for j in range(6)] for i in range(6)]
    @functools.lru_cache(None)
    def minor(rows,cols):
        if not rows:return one
        ans=zero
        for j,c in enumerate(cols):
            term=A[rows[0]][c]*minor(rows[1:],cols[:j]+cols[j+1:])
            ans=ans-term if j%2 else ans+term
        return ans
    labels=list(itertools.combinations_with_replacement(range(6),2))
    cof=[]
    for i,j in labels:
        v=minor(tuple(a for a in range(6) if a!=i),tuple(a for a in range(6) if a!=j))
        if (i+j)%2:v=-v
        need(all(sum(e)==5 for e in v.to_dict()),"every original symmetric cofactor is homogeneous five")
        cof.append(v)
    whole=minor(tuple(range(6)),tuple(range(6)))
    # This is a dictionary check on the complete coefficients, not a point
    # certificate. The old line is retained only as an extra ordering check.
    line=[0]*7
    for e,c in whole.to_dict().items():
        if e[1]==0:line[int(e[3])]=(line[int(e[3])]+int(c)*pow(7,int(e[2]),P))%P
    need(line[-1]==40,"same complete original sextic leading line coefficient")
    need([(x*pow(40,-1,P))%P for x in line]==[126,57,111,116,92,45,1],
         "same seven original sextic line coefficients")
    return ctx,A,minor,labels,cof,whole

def trace_algebra(prep):
    ctx,A,minor,labels,cof,whole=pencil_polynomials(prep["allFourCanonicalMatrices"])
    top=mons(3,5);low=basis_through(3,4)
    need(len(top)==21 and len(low)==35,"entire original degree-five border and low basis")
    lowpos={e:i for i,e in enumerate(low)};toppos={e:i for i,e in enumerate(top)}
    C=mat([[int(g.to_dict().get((0,)+e,0)) for g in cof] for e in top])
    Ci,detC=inverse(C,"all21 original highest cofactor coefficients")
    need(detC==103,"same paid original plane unit, not a replacement hyperplane")
    lower=zeros(35,21);affine=[]
    for j,g in enumerate(cof):
        d={}
        for e,c in g.to_dict().items():
            ee=tuple(map(int,e[1:]));d[ee]=(d.get(ee,0)+int(c))%P
        d={e:c for e,c in d.items() if c}
        need(all(sum(e)<=5 for e in d),"every original affine cofactor term retained")
        affine.append(d)
        for e,c in d.items():
            if sum(e)<=4:lower[lowpos[e],j]=c
    rules=-(lower*Ci)
    # m_alpha - rule_alpha = sum_i (C^{-1})_i,alpha cofactor_i.
    for a,e in enumerate(top):
        d={e:1}
        for k,mon in enumerate(low):
            c=int(rules[k,a])
            if c:d[mon]=(d.get(mon,0)-c)%P
        for i,g in enumerate(affine):
            c=int(Ci[i,a])
            for mon,z in g.items():d[mon]=(d.get(mon,0)-c*z)%P
        need(not any(d.values()),"all complete original cofactor border source identities")
    M=[]
    for axis in range(3):
        B=zeros(35,35)
        for j,e in enumerate(low):
            ee=list(e);ee[axis]+=1;ee=tuple(ee)
            if sum(ee)<=4:B[lowpos[ee],j]=1
            else:
                a=toppos[ee]
                for i in range(35):B[i,j]=rules[i,a]
        M.append(B)
    for i in range(3):
        for j in range(i):
            need(M[i]*M[j]==M[j]*M[i],"all3675 original multiplication commutator coordinates")
    cache={(0,0,0):eye(35)}
    def monmatrix(e):
        if e not in cache:
            k=next(i for i,v in enumerate(e) if v)
            prev=list(e);prev[k]-=1
            cache[e]=M[k]*monmatrix(tuple(prev))
        return cache[e]
    e0=zeros(35,1);e0[lowpos[(0,0,0)],0]=1
    for j,e in enumerate(low):
        v=zeros(35,1);v[j,0]=1
        need(monmatrix(e)*e0==v,"all1225 actual original monomial cyclic-basis products")
    for j,g in enumerate(affine):
        value=zeros(35,35)
        for e,c in g.items():value+=monmatrix(e)*int(c)
        need(value==zeros(35,35),"all25725 original cofactor multiplication-operator coordinates")
    bm=[monmatrix(e) for e in low];entries=[table(x) for x in bm]
    Tr=zeros(35,35)
    for i in range(35):
        for j in range(i+1):
            v=sum(entries[i][a][b]*entries[j][b][a] for a in range(35) for b in range(35))%P
            Tr[i,j]=v;Tr[j,i]=v
    trace_det=int(Tr.det());trace_rank=int(Tr.rank())
    trace_inv=None
    if trace_det:
        trace_inv,again=inverse(Tr,"complete original rank35 trace pairing")
        need(again==trace_det,"same actual full trace determinant")
    return {"prime":P,"coefficientRoot":ROOT,
        "all21OriginalCofactorLabels":[list(x) for x in labels],
        "all21OriginalHomogeneousCofactors":[packed(x) for x in cof],
        "all21OriginalAffineCofactors":[[[list(e),c] for e,c in sorted(x.items())] for x in affine],
        "all21DegreeFiveMonomials":top,"all35OriginalBasisMonomials":low,
        "originalHighestCoefficientUnit":table(C),"originalHighestCoefficientInverse":table(Ci),
        "originalHighestCoefficientUnitDeterminant127":detC,
        "all21BorderRules":table(rules),"allThreeOriginalMultiplicationMatrices":[table(x) for x in M],
        "all21OriginalCofactorSourceIdentitiesVerified":True,
        "all3675CommutatorCoordinatesVerified":True,
        "all1225MonomialCyclicBasisProductsVerified":True,
        "all25725OriginalCofactorOperatorCoordinatesVerified":True,
        "completeTracePairing":table(Tr),"tracePairingRank":trace_rank,
        "tracePairingDeterminant127":trace_det,
        "tracePairingInverse":table(trace_inv) if trace_inv is not None else None,
        "coefficientDVRFreenessProof":{
            "surjection":"the original unit21 border reduces every monomial to these35 over D",
            "characteristicZeroDimension":35,
            "reference":"results/R150-appendix-original-corank-two-pencil-exception-algebra-has-free-rank-thirty-five.md",
            "injectivity":"kernel is a submodule of D^35 and becomes0 over Frac(D)=E"},
        "sameDVRFree35Basis":True,
        "characteristicZeroEtaleProved":bool(trace_det),
        "geometricallyDistinctRankFourPointCount":35 if trace_det else None,
        "geometricRankFiveSmoothnessClaimed":False,
        "originalBellCriticalIdealEmptyClaimed":False}

def singularity_generators(prep):
    T=prep["allFourCanonicalMatrices"]
    ctx=nmod_mpoly_ctx.get(tuple("y%d"%i for i in range(6)),P,"lex")
    y=ctx.gens();zero=ctx.constant(0);one=ctx.constant(1)
    q=[sum((T[k][i][j]*y[i]*y[j] for i in range(6) for j in range(6)),zero) for k in range(4)]
    M=[[sum((T[k][i][j]*y[j] for j in range(6)),zero) for k in range(4)] for i in range(6)]
    @functools.lru_cache(None)
    def minor(rows,cols):
        if not rows:return one
        ans=zero
        for j,c in enumerate(cols):
            t=M[rows[0]][c]*minor(rows[1:],cols[:j]+cols[j+1:])
            ans=ans-t if j%2 else ans+t
        return ans
    rows=list(itertools.combinations(range(6),4))
    minors=[minor(rr,(0,1,2,3)) for rr in rows]
    labels=[{"kind":"original-quadratic","index":i,"degree":2} for i in range(4)]
    labels += [{"kind":"original-four-minor","rows":list(rr),"columns":[0,1,2,3],"degree":4} for rr in rows]
    polys=q+minors
    need(len(labels)==len(polys)==19,"all four original quadrics and all fifteen original minors")
    for lab,g in zip(labels,polys):
        need(all(sum(e)==lab["degree"] for e in g.to_dict()),"all original singularity generators homogeneous")
    return ctx,labels,polys

def complete_macaulay(prep,degree):
    ctx,labels,polys=singularity_generators(prep)
    outputs=mons(6,degree);pos={e:i for i,e in enumerate(outputs)}
    columns=[]
    for i,lab in enumerate(labels):
        for mon in mons(6,degree-lab["degree"]):
            columns.append({"originalGenerator":i,"multiplier":mon})
    n=len(outputs);c=len(columns);A=zeros(n,c)
    nnz=0
    for j,col in enumerate(columns):
        g=polys[col["originalGenerator"]].to_dict();mon=col["multiplier"]
        for e,v in g.items():
            ee=tuple(int(e[i])+mon[i] for i in range(6))
            need(ee in pos,"no original homogeneous Macaulay output omitted")
            A[pos[ee],j]=int(v);nnz+=1
    raw=bytes(int(A[i,j]) for i in range(n) for j in range(c))
    whole_sha=sha(raw);del raw
    R,r=A.rref()
    piv=[]
    for i in range(r):
        j=next((j for j in range(c) if int(R[i,j])),None)
        need(j is not None and int(R[i,j])==1 and (not piv or j>piv[-1]),
             "entire ordered original-column rank profile")
        piv.append(j)
    need(all(not int(R[i,j]) for i in range(r,n) for j in range(c)),"all remaining RREF rows zero")
    del R
    result={"degree":degree,"prime":P,"coefficientRoot":ROOT,
        "all19OriginalGeneratorLabels":labels,
        "all19CompleteOriginalPolynomials":[packed(x) for x in polys],
        "allOutputMonomials":outputs,"allOriginalSourceColumns":columns,
        "shape":[n,c],"nonzeroCoordinates":nnz,"completeFieldMatrixRowMajorByteSHA256":whole_sha,
        "completeOriginalRank":int(r),"selectedOriginalColumns":piv,
        "fullCoefficientRank":r==n,
        "characteristicZeroOriginalIdealContainsAllDegreeMonomials":False}
    if r==n:
        U=mat([[int(A[i,j]) for j in piv] for i in range(n)])
        Ui,detU=inverse(U,"full original homogeneous Macaulay coefficient unit")
        # Each inverse column is a complete original labelled source for one
        # degree-D monomial. Both products include every output row.
        result.update({"selectedOriginalCoefficientUnit":table(U),
            "selectedOriginalCoefficientInverse":table(Ui),
            "selectedOriginalCoefficientDeterminant127":detU,
            "allOriginalCoefficientLeftAndRightInverseProductsVerified":True,
            "originalSourceProductCoordinateCount":2*n*n,
            "characteristicZeroOriginalIdealContainsAllDegreeMonomials":True,
            "characteristicZeroSourceDefinition":"adjugate of the same original E coefficient unit divided by its nonzero fixed E determinant",
            "allRankFiveSexticSingularitiesExcluded":True,
            "noMeanParameterInverted":True})
    else:
        result["meaning"]="This complete degree has insufficient field rank; no characteristic-zero nonmembership or existence is inferred."
    return result

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--helper",required=True);ap.add_argument("--field-driver",required=True)
    ap.add_argument("--out",required=True)
    ap.add_argument("--through",choices=("prepare","trace","complete"),default="complete")
    ap.add_argument("--through-degree",type=int,default=8)
    ap.add_argument("--seconds",type=float,default=180)
    ap.add_argument("--memory-mib",type=int,default=768)
    a=ap.parse_args()
    need(0<a.seconds<=900 and 256<=a.memory_mib<=4096 and 5<=a.through_degree<=8,
         "bounded complete original polynomial gates")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    start=time.monotonic();ss=identity(__file__)["sha256"]
    binding=sha(canonical({"format":FORMAT,"sourceSha256":ss,
        "helperSha256":HELPER_SHA,"fieldDriverSha256":FIELD_SHA,
        "prime":P,"coefficientRoot":ROOT,"matchedCubic":MATCHED,
        "originalHankelPivotOrder":HP,"originalHankelFreeOrder":HU,
        "keptQuadraticPairs":KEEP_PAIRS,"canonicalPositions":CANON_POS}))
    manifest_path=out/"original-pencil-trace-singularity-manifest.json"
    manifest={"format":FORMAT+"-manifest","binding":binding,"phases":{}}
    if manifest_path.exists():
        manifest=json.loads(manifest_path.read_text())
        need(manifest["format"]==FORMAT+"-manifest" and manifest["binding"]==binding,"same complete source checkpoint")
    rec={"format":FORMAT,"binding":binding,"sourceSha256":ss,"status":"started",
        "parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib,"through":a.through,
                      "throughDegree":a.through_degree,"prime":P,"coefficientRoot":ROOT}}
    def event(name):
        rec["parameters"]["lastCompletedPhase"]=name
        print(json.dumps({"phase":name,"elapsedSeconds":time.monotonic()-start,
            "maxResidentKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
    def phase(name,build):
        if name in manifest["phases"]:
            d=manifest["phases"][name]
            v=load_gz(out/d["path"],d,binding)
            event("reused-"+name);return v
        v=build()
        desc=save_gz(out/(name+".json.gz"),{"format":FORMAT+"-phase","binding":binding,"data":v})
        manifest["phases"][name]=desc;save_json(manifest_path,manifest);event(name)
        return v
    def timeout(sig,frame):
        raise TimeoutError("whole original pencil polynomial phase budget")
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds)
    code=1
    try:
        m=module(a.helper,"paid_original_physical_helper",HELPER_SHA)
        fd=module(a.field_driver,"paid_original_bell_model_driver",FIELD_SHA)
        prep=phase("complete-original-small-pencil-reconstruction",lambda:reconstruct_original(fd,m))
        rec["parameters"].update({"originalPhysicalModelLogicalSha256":prep["originalPhysicalModelLogicalSha256"],
            "allOriginalConstantUnitsVerified":True,
            "allFourOriginalTensorDeterminants127":prep["originalMatrixDeterminants127"],
            "originalMeanParameterSpecializationUsed":False})
        if a.through!="prepare":
            tr=phase("complete-original-rankfour-trace-algebra",lambda:trace_algebra(prep))
            rec["parameters"].update({"originalCofactorUnitDeterminant127":tr["originalHighestCoefficientUnitDeterminant127"],
                "tracePairingRank":tr["tracePairingRank"],"tracePairingDeterminant127":tr["tracePairingDeterminant127"],
                "sameDVRFree35Basis":True,"characteristicZeroEtaleProved":tr["characteristicZeroEtaleProved"],
                "all21CofactorSourceIdentitiesVerified":tr["all21OriginalCofactorSourceIdentitiesVerified"],
                "all3675MultiplicationCommutatorCoordinatesVerified":tr["all3675CommutatorCoordinatesVerified"],
                "all25725OriginalCofactorOperatorCoordinatesVerified":tr["all25725OriginalCofactorOperatorCoordinatesVerified"]})
            if a.through=="complete":
                grades=[]
                for d in range(5,a.through_degree+1):
                    v=phase("complete-original-quadratic-minor-degree-%02d"%d,lambda d=d:complete_macaulay(prep,d))
                    grades.append({"degree":d,"shape":v["shape"],"rank":v["completeOriginalRank"],
                        "full":v["fullCoefficientRank"]})
                    rec["parameters"]["completeHomogeneousDegrees"]=grades
                    if v["fullCoefficientRank"]:
                        rec["parameters"]["allRankFiveSexticSingularitiesExcluded"]=True
                        rec["parameters"]["originalHomogeneousSourceDegree"]=d
                        break
                else:
                    rec["parameters"]["allRankFiveSexticSingularitiesExcluded"]=False
        rec["parameters"]["originalBellCriticalIdealEmptyClaimed"]=False
        rec["status"]="completed";code=0
    except BaseException as e:
        isbudget=isinstance(e,TimeoutError)
        rec["status"]="budget-checkpoint" if isbudget else "failed"
        rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=75 if isbudget else 1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        rec["elapsedSeconds"]=time.monotonic()-start
        rec["maxResidentKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if manifest_path.exists():rec["parameters"]["manifest"]={"path":manifest_path.name,**identity(manifest_path)}
        rec["parameters"]["completePhaseDescriptors"]=manifest["phases"]
        desc=save_json(out/"original-pencil-trace-singularity-receipt.json",rec)
        print(json.dumps({"exitCode":code,"receipt":desc,**rec},sort_keys=True),flush=True)
    return code
if __name__=="__main__":sys.exit(main())
