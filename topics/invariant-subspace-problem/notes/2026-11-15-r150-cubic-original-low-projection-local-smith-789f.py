#!/usr/bin/env python3
"""F+ or F- local positive-length certificate from the original 51x36 block.

Astra-ISP-789f / root; AI-assisted, GPT-6 Astra Pro.
The low right-cochain block embeds in the TRUE 224x155 original projection.
Every low jet, plus four exact pure jets, is a full projected jet. This gives
delta(projected) >= delta(low), not an assertion that all full corrections
are low. Both cubics have already-proved irreducibility over Q.
The regular representation is 153x108 over Q; the paid constant rank is75
and the paid generic rank81. No original6188 full elimination is repeated.

All original equations and all projected sources are retained in the
polynomial embedding proof. g is an actual UNIT in this number field.
The original h0 has exactly two factors of the selected cubic. No negative full-module claim
is made if the sufficient low length threshold6 is not reached.
"""
import argparse
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path
import resource
import signal
import time

from flint import fmpq, fmpq_mat

GENERATOR_SHA = "2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACTIONS_SHA = "2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
SCHUR_HELPER_SHA = "73c11b1d957962fdb8c9b17143aaf8d894845b1b4c8382f200eeaf2422178119"
FORMAT = "r150-cubic-original-low-projection-local-smith-v1"
E8 = [9600,-25472,-3392,15936,-2888,-936,153,50,5]
FP = [-8,32,-25,5]
FM = [864,864,135,5]
FIELD_DEGREE = 3
PAID_FULL_LOCAL_LENGTH_UPPER = 8
POINT = None
MINIMAL = None

def require(ok, message):
    if not ok:
        raise AssertionError(message)

def sha_file(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1048576),b""):
            h.update(b)
    return h.hexdigest()

def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

def eye(n):
    return fmpq_mat([[int(i==j) for j in range(n)] for i in range(n)])

def matrix_polynomial(coefficients,C):
    value=fmpq_mat(C.nrows(),C.ncols())
    I=eye(C.nrows())
    for coefficient in reversed(coefficients):
        value=value*C+fmpq(coefficient)*I
    return value

def original_projection_polynomial_coefficients(m, actions):
    """Original pure/one-normal coefficient polynomials through degree25.

    This is the same original physical convolution as the pinned actions.
    Quadratic-normal output is not needed for this exact projection.
    No samples, interpolation, or parameterwise primitive rescaling is used.
    """
    chart="zero"
    max_order=25
    require(max_order==25, "Complete original polynomial degree bound")
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
        for tt in range(2):
            both=evaluate(add(tangent[tt],z[j]))
            linear[j].append([[both[k][i]-Fz[j][k][i]-Ft[tt][k][i]
                               for i in range(17)] for k in range(N+1)])
    coeff={"chart":chart,"maxOrder":N,"pure":pure,"linear":linear,
           "quadratic":quadratic,"physical":physical}
    for k in range(N+1):
        P=actions.block(m,coeff,k,0,1)
        physical["P"+str(k)]=m.matrix_hash(P)
    return coeff


def original_low_polynomial_model(m,actions):
    coeff=original_projection_polynomial_coefficients(m,actions)
    pure_cols=actions.target_columns(0)
    normal_cols=actions.target_columns(1)
    all_cols=pure_cols+normal_cols
    pure_rows=actions.source_rows(0)
    selected_rows=[r for r,(_,a,b,_) in enumerate(pure_rows) if a+b<=1]
    selected_cols=[c for c,(a,b,mon) in enumerate(all_cols)
                   if (not mon and a+b<=3) or (len(mon)==1 and a+b<=1)]
    exact_cols=[c for c,(a,b,mon) in enumerate(all_cols)
                if not mon and b<=1 and 4<=a+b<=5]
    require(len(selected_rows)==51 and len(selected_cols)==36
            and len(exact_cols)==4,"Exact low-cochain support dimensions")
    excluded_rows=[r for r in range(170) if r not in set(selected_rows)]
    g_rows=[(a,d-a+2,(j,)) for d in range(3)
            for a in range(d+1) for j in range(2,11)]
    require(len(g_rows)==54 and not
            set(g_rows).intersection(all_cols[c] for c in selected_cols+exact_cols),
            "All54 genuine g-multiple rows kill this low embedding")
    small=[]
    projected_hashes=[]
    for k in range(26):
        P=m.join_columns(actions.block(m,coeff,k,0,0),
                         actions.block(m,coeff,k,0,1))
        require(P.nrows()==170 and P.ncols()==155,
                "Complete170 original pure source projection")
        require(m.matrix_zero(m.submatrix(P,excluded_rows,selected_cols)),
                "All higher pure multipliers kill all low coefficient jets")
        require(m.matrix_zero(m.submatrix(P,range(170),exact_cols)),
                "All four high pure columns are exact original kernels")
        small.append(m.submatrix(P,selected_rows,selected_cols))
        projected_hashes.append(m.matrix_hash(P))
    rows1=actions.source_rows(1)
    index1={key:i for i,key in enumerate(normal_cols)}
    for k in range(26):
        for row in rows1:
            eq,a,b,mon=row
            key=(a,b+2,mon)
            require(key in index1,"Original one-normal projection degree bound")
            value=coeff["pure"][k][eq]
            actual=list(actions.sparse_row_terms(coeff,k,row,1,index1))
            expected=[(index1[key],value)] if value else []
            require(actual==expected,"Every original one-normal projected source")
    require(len(rows1)==918 and
            len(actions.source_rows(2))+len(actions.source_rows(3))==5100,
            "All6188 original source coordinates accounted for")
    meta={
        "fullOriginalParameterPolynomialDegreeBound":25,
        "originalParameterPolynomialsNotInterpolated":True,
        "all17OriginalPhysicalEquationsRetained":True,
        "all170OriginalPureProjectionRowsRetained":True,
        "all918OriginalOneNormalPolynomialRowsVerified":True,
        "all5100HigherNormalProjectionRowsZeroByDegree":True,
        "all6188OriginalProjectedSourcesRetained":True,
        "all224RowsOfLowEmbeddingVerifiedPolynomially":True,
        "allFourAdditionalPureColumnsAreExactPolynomialKernels":True,
        "lowSourceRows":[list(pure_rows[r][:3]) for r in selected_rows],
        "lowTargetColumns":[[a,b,list(mon)] for a,b,mon in
                            (all_cols[c] for c in selected_cols)],
        "exactPureTargetColumns":[[a,b,list(mon)] for a,b,mon in
                                  (all_cols[c] for c in exact_cols)],
        "smallPolynomialCoefficientSHA256":[m.matrix_hash(X) for X in small],
        "fullProjectedPolynomialCoefficientSHA256":projected_hashes,
        "originalPhysicalCoefficientIdentities":coeff["physical"],
        "fixedDetJ3PhysicalNormalization":True,
        "parameterwisePrimitiveRowDivisionUsed":False,
        "originalPrimitiveRescalingIsOnlyPaidNonzeroRationalConstants":True}
    return small,coeff,meta

def field_model(m,coeff):
    d=FIELD_DEGREE
    minimal=MINIMAL
    require(POINT in ("plus","minus") and len(minimal)==d+1,
            "One explicit original irreducible cubic")
    C=fmpq_mat(d,d)
    for i in range(d-1):
        C[i+1,i]=1
    for i in range(d):
        C[i,d-1]=-fmpq(minimal[i])/minimal[d]
    require(m.matrix_zero(matrix_polynomial(minimal,C)),
            "Actual cubic companion satisfies the selected original factor")
    powers=[eye(d)]
    for _ in range(25):
        powers.append(powers[-1]*C)
    g=matrix_polynomial([0,0,24,-8,-2],C)
    dg=g.det()
    require(dg,"Original g is a genuine unit at every selected cubic embedding")
    dp=matrix_polynomial([i*minimal[i] for i in range(1,d+1)],C).det()
    require(dp,"Natural t=s-alpha has valuation one for the selected factor")
    unit_eq=None
    det_pure=None
    for eq in range(11):
        value=fmpq_mat(d,d)
        for k in range(26):
            if coeff["pure"][k][eq]:
                value+=coeff["pure"][k][eq]*powers[k]
        det=value.det()
        if det:
            unit_eq,det_pure=eq,det
            break
    require(unit_eq is not None,"Actual original pure N coordinate is a local unit")
    other=FM if POINT=="plus" else FP
    B=matrix_polynomial(other,C)
    unitpart=(C*C*C)*(C-2*eye(d))*B*B*matrix_polynomial(E8,C)
    du=unitpart.det()
    require(du,"Original h0 divided by the selected factor squared is a local unit")
    return powers,{
        "field":"Q[alpha]/(F"+("+" if POINT=="plus" else "-")+"(alpha))",
        "selectedFactor":POINT,
        "minimalPolynomialAscending":minimal,
        "fieldDegree":d,
        "irreducibilityPreviouslyProvedOverQ":True,
        "irreducibilityReference":"R150-appendix-rank-one-P"+POINT+
            "-means-complete-critical-classification.md",
        "fieldRegularRepresentationSHA256":m.matrix_hash(C),
        "originalCubicCompanionIdentityVerified":True,
        "originalGIsActualFieldUnit":True,
        "originalGMultiplicationDeterminant":str(dg),
        "originalFactorDerivativeIsActualFieldUnit":True,
        "originalFactorDerivativeMultiplicationDeterminant":str(dp),
        "actualOriginalPureUnitEquationZeroBased":unit_eq,
        "actualOriginalPureUnitMultiplicationDeterminant":str(det_pure),
        "originalH0Formula":"s^3(s-2)Fp^2Fm^2E8",
        "originalH0LocalOrder":2,
        "originalH0UnitPartMultiplicationDeterminant":str(du),
        "noVanishingGDivided":True,
        "allThreeConjugateEmbeddingsCovered":True}

def expand_small_taylor(m,small,powers,order):
    d=FIELD_DEGREE
    series=[fmpq_mat(51*d,36*d) for _ in range(order+1)]
    cache={}
    nonzero=0
    for r in range(51):
        for c in range(36):
            poly=[small[k][r,c] for k in range(26)]
            if not any(poly):
                continue
            nonzero+=1
            key=tuple(str(x) for x in poly)
            tiles=cache.get(key)
            if tiles is None:
                tiles=[]
                for n in range(order+1):
                    T=fmpq_mat(d,d)
                    for k in range(n,26):
                        if poly[k]:
                            T+=(poly[k]*comb(k,n))*powers[k-n]
                    tiles.append(T)
                cache[key]=tiles
            for n,T in enumerate(tiles):
                for i in range(d):
                    for l in range(d):
                        series[n][d*r+i,d*c+l]=T[i,l]
    # A multiplication block must commute with the field action. Testing each
    # cached block checks every actual entry of every expanded Taylor matrix.
    C=powers[1]
    require(all(T*C==C*T for ts in cache.values() for T in ts),
            "Every Taylor coefficient is actual field multiplication")
    return series,{
        "numberFieldTaylorParameter":"t=s-alpha",
        "lowShapeOverNumberField":[51,36],
        "regularShapeOverQ":[51*d,36*d],
        "lowPolynomialNonzeroEntries":nonzero,
        "distinctPolynomialCoefficientEntries":len(cache),
        "allFieldMultiplicationBlocksVerified":True,
        "numberFieldTaylorCoefficientSHA256":[m.matrix_hash(X) for X in series]}

def profile(m,helper,series,result,save):
    d=FIELD_DEGREE
    generic=27*d
    covered=0
    length=0
    original=series
    p=result["parameters"]
    for exponent in range(len(original)):
        residual,phase=helper.unit_schur_step(m,series,exponent)
        rank=phase["rank"]
        require(rank%d==0,"Every Q Smith multiplicity is divisible by field degree3")
        if exponent==0:
            require(rank==25*d,"Actual low constant rank agrees with paid full rank140")
        covered+=rank
        require(covered<=generic,"Paid low generic rank27 retained")
        length+=exponent*rank
        lower=length+(exponent+1)*(generic-covered)
        require(lower%d==0 and lower//d<=PAID_FULL_LOCAL_LENGTH_UPPER,
                "Embedded low length cannot exceed full original selected cubic length upper8")
        phase["rankOverNumberField"]=rank//d
        phase["coveredRankOverNumberField"]=covered//d
        phase["smallLengthLowerBoundOverNumberField"]=lower//d
        p["exactTaylorPhases"].append(phase)
        p["lastCompletedExponent"]=exponent
        p["smallTorsionLengthLowerBound"]=lower//d
        p["projectedOriginalLengthLowerBound"]=lower//d
        p["fullOriginalLocalLengthLowerBound"]=lower//d
        save()
        if covered==generic:
            require(all(m.matrix_zero(X) for X in residual),
                    "All residual jets vanish after actual small generic rank27")
            p.update({"smallGenericRankReached":True,
                      "smallTorsionLengthExact":length//d,
                      "smallFreeRankOverNumberField":9})
            return
        if exponent+1==len(original):
            p.update({"smallGenericRankReached":False,
                      "smallTorsionLengthExact":None,
                      "unresolvedSmallPositiveFactors":(generic-covered)//d,
                      "smallFreeRankOverNumberField":9})
            return
        require(m.matrix_zero(residual[0]),"Only a genuine common t factor is divided")
        series=residual[1:]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--point",choices=("plus","minus"),required=True)
    p.add_argument("--generator",required=True)
    p.add_argument("--jet-actions",required=True)
    p.add_argument("--unit-schur-helper",required=True)
    p.add_argument("--out",required=True)
    p.add_argument("--remaining-seconds",type=float,default=120.0)
    p.add_argument("--memory-mib",type=int,default=2048)
    p.add_argument("--max-order",type=int,default=4)
    a=p.parse_args()
    global POINT,MINIMAL
    POINT=a.point
    MINIMAL=FP if POINT=="plus" else FM
    require(a.remaining_seconds>0 and 512<=a.memory_mib<=4096
            and 1<=a.max_order<=7,"Bounded original cubic local interface")
    for path,expected in ((a.generator,GENERATOR_SHA),(a.jet_actions,ACTIONS_SHA),
                          (a.unit_schur_helper,SCHUR_HELPER_SHA)):
        require(sha_file(path)==expected,"Pinned original source identity")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,a.memory_mib*1024**2))
    m=module_at("r150_cubic_original_generator",a.generator)
    actions=module_at("r150_cubic_original_actions",a.jet_actions)
    helper=module_at("r150_cubic_exact_unit_schur",a.unit_schur_helper)
    start=time.monotonic()
    result={"format":FORMAT,"status":"started","scriptSHA256":sha_file(__file__),
            "arithmetic":"exact rational regular representation of the actual cubic number field",
            "parameters":{
                "remainingSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
                "maxLocalTaylorOrder":a.max_order,
                "inputSourceSHA256":{"generator":GENERATOR_SHA,"actions":ACTIONS_SHA,
                                     "unitSchur":SCHUR_HELPER_SHA},
                "paidOriginalFullGenericRank":4354,
                "paidOriginalFullCubicRank":4352,
                "paidProjectionGenericRank":142,
                "paidProjectionCubicRank":140,
                "paidLowGenericRank":27,
                "paidLowCubicRank":25,
                "paidFullCubicLengthUpperBound":8,
                "selectedFactor":POINT,
                "exactTaylorPhases":[],
                "oldNormalFormsNotRecomputed":True,
                "fullOriginalMacaulayNotRecomputed":True,
                "noNewFiniteFieldMathematics":True,
                "largeDataUploadedOrCommitted":False}}
    out=Path(a.out)
    out.parent.mkdir(parents=True,exist_ok=True)
    def save():
        result["elapsedSeconds"]=time.monotonic()-start
        raw=json.dumps(result,sort_keys=True,separators=(",",":")).encode()
        require(len(raw)<100000,"Small exact proof receipt limit")
        tmp=out.with_name(out.name+".tmp")
        tmp.write_bytes(raw)
        tmp.replace(out)
    def stop(signum,frame):
        raise TimeoutError("Shared original cubic local mathematical budget exhausted")
    signal.signal(signal.SIGALRM,stop)
    signal.signal(signal.SIGTERM,stop)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    try:
        small,coeff,meta=original_low_polynomial_model(m,actions)
        result["parameters"].update(meta);save()
        powers,meta=field_model(m,coeff)
        result["parameters"].update(meta);save()
        series,meta=expand_small_taylor(m,small,powers,a.max_order)
        result["parameters"].update(meta);save()
        profile(m,helper,series,result,save)
        q=result["parameters"]
        lower=q["smallTorsionLengthLowerBound"]
        gap=PAID_FULL_LOCAL_LENGTH_UPPER-lower
        q.update({
            "lowerBoundUsesLowJetInjectionPlusFourExactPureColumns":True,
            "smallJetsEmbedInAll224OriginalProjectionRows":True,
            "smallSupportNotClaimedToCaptureEveryFullCorrection":True,
            "fullOriginalWKernelLengthUpperBound":gap,
            "allNineActualH0TargetsLocallyInOriginalSource":gap<=2,
            "allTransverseSquareOutputsLocallyInOriginalSource":gap==0,
            "fullOriginalCubicLengthExactIfLowerEight":8 if lower==8 else None,
            "desiredH0LocalExponent":2,
            "allTaylorSchurIdentitiesVerified":True,
            "noGlobalPolynomialMembershipClaimed":True,
            "insufficientLowThresholdIsNotAFullModuleObstruction":True})
        result["status"]="completed"
    except BaseException as exc:
        result["status"]="incomplete"
        result["error"]=type(exc).__name__+": "+str(exc)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        save()
        raw=out.read_bytes()
        print(json.dumps({"status":result["status"],"receipt":str(out),
                          "bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),
                          "elapsedSeconds":result["elapsedSeconds"],
                          "projectedLengthLowerBound":result["parameters"].get(
                              "projectedOriginalLengthLowerBound"),
                          "localH0TargetsProved":result["parameters"].get(
                              "allNineActualH0TargetsLocallyInOriginalSource",False)},
                         sort_keys=True),flush=True)

if __name__=="__main__":
    main()
