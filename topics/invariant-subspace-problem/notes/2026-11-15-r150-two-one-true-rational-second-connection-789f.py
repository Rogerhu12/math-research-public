#!/usr/bin/env python3
"""Original s=2 true-Q second connection: fourteen projected heads plus one RHS.

Author: Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro.
The true original projection supplies all15 first heads and14 second heads.
Its canonical first cochain is reconstructed and matched to the paid complete
605x15 logical hash, including an actual zero normal-two block check.
Only one new second-leading quotient direction is tested.  The low constant
matrix retains B585, BOTH true H3 homogeneous columns and all7 first incoming
image directions.  Its rank592 is inherited only after original span identities.
A positive full6188-row certificate proves complete beta2_Q=0.  Failure of
the normal<=3 correction trial is NOT a full second-connection lower bound.
No old huge incompatible22-RHS solutions or complete inverse are reconstructed.
"""
import argparse
import hashlib
import importlib.util
import json
from math import gcd
from pathlib import Path
import resource
import signal
import sys
import time
from flint import nmod_mat

BASE_SHA="8f55c5b5f0db2a7dd9b0b042e00cd506fd6e38698b9dc264a602e3dc8ccb510b"
GEN_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACT_SHA="2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
UNIT_SHA="36356983e71ee1e67677da1a7a5f7aebf2987db282a5447a741b6a6af93084d5"
CONST_SHA="5d83b8784ea4e1d2b99f9ccd8881dcf6f2abe4241586219a3b459541c10d6272"
FIRST_SHA="2a75b4dba0b1e28902bc3a441ec7ce03a7e7fbdf46abfa5c138f4f7ab29b269a"
FULL_FIRST_SHA="aebdd169ec950f7eb4c17b7e9ac4dc30ecb205dfc6a2d9476af9d4d03ebc9d3a"
PROJECTION_SHA="693da6446a6f04cba2c343ea49d9d3466caad1aebd056e91db338163b20d3332"
H3_SHA="92d6c57531406e5892b06632aca6a8262cd238bec926c2b73532d7e05ed3bc8e"
TANGENT_SHA="66c05b0911d7b003e635ca0ed43f605f1a4de32003a9da3878f1ca46b51279ab"
PROFILE_PRIME=17

def require(ok,message):
    if not ok:raise AssertionError(message)
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj
    spec.loader.exec_module(obj);return obj
def columns(d,m,M,which):
    return d.sub(m,M,range(M.nrows()),which)
def identity(m,n):
    return m.fmpq_mat([[int(i==j) for j in range(n)] for i in range(n)])
def embed(m,M,rows):
    require(M.nrows()<=rows,"Embedding preserves the complete old coordinate prefix")
    Z=m.fmpq_mat(rows,M.ncols())
    for i in range(M.nrows()):
        for j in range(M.ncols()):Z[i,j]=M[i,j]
    return Z

def cached_matrix(d,m,a,binding,name,M,meta,result):
    old=d.load_matrix(m,a,binding,name,result)
    if old is None:
        d.save_matrix(m,a,binding,name,M,meta,result,True)
    else:
        X,xmeta,verified=old
        require(verified and X==M and xmeta==meta,"Identical verified phase "+name)
    return M

def exact_kernel(d,m,j,a,binding,name,M,expected_rank,result):
    old=d.load_matrix(m,a,binding,name,result);msha=m.matrix_hash(M)
    if old is None:
        d.guard(a,name+" exact small kernel",2)
        R,rank=M.rref()
        require(rank==expected_rank,"Paid small projected rank "+name)
        K,piv,free=j.canonical_kernel(m,R,rank);del R
        meta={"matrixSHA256":msha,"rank":rank,"pivotColumns":piv,
              "freeColumns":free,"allOriginalRowsRetained":True}
        d.save_matrix(m,a,binding,name,K,meta,result,False)
    else:
        K,meta,verified=old
        require(meta["matrixSHA256"]==msha and meta["rank"]==expected_rank,
                "Same small-kernel source "+name)
    require(m.matrix_zero(M*K),"All actual small-kernel rows "+name)
    for c,f in enumerate(meta["freeColumns"]):
        for e,g in enumerate(meta["freeColumns"]):
            require(K[g,c]==int(c==e),"Canonical original free identity "+name)
    meta["allOriginalKernelProductsVerified"]=True
    d.save_matrix(m,a,binding,name,K,meta,result,True)
    return K,meta

def reconstruct_projected_families(d,m,j,a,binding,coeff,L,paid,result):
    # This is the actual original projection: ALL170+918 low source rows.
    B1=d.vjoin(m,j,[j.block(m,coeff,0,r,1) for r in (0,1)])
    C=d.apply_rows(m,j,coeff,1,d.sections(m,j,L,1),22,(0,1))
    M1=m.join_columns(B1,C)
    K1,km1=exact_kernel(d,m,j,a,binding,"projected-first-kernel",M1,140,result)
    chosen,H,h=d.leading_basis(m,j,K1,135,22)
    require(h==15 and K1.ncols()==17,"Complete projected first leading and zero fiber")
    Y=columns(d,m,d.sub(m,chosen,range(135)),range(15))
    L0=L*H;L1=d.append_zero_pure(m,Y)
    L1old=embed(m,L1,605)
    old=paid["firstRestrictedFamily"]
    require(m.matrix_hash(H)==old["headMapSHA256"]
            and m.matrix_hash(L0)==old["lambda0SHA256"]
            and m.matrix_hash(L1old)==old["lambda1SHA256"],
            "Reconstructed canonical cochain matches ALL paid605x15 coefficients")
    normal2=d.sub(m,L1old,range(155,605))
    require(m.matrix_zero(normal2),"All6750 paid first normal-two entries are actually zero")
    d.verify_jets(m,j,coeff,[L0,L1],[1,1],result,"projectedCompleteFirst")
    head_piv=[p-135 for p in km1["pivotColumns"] if p>=135]
    head_free=[f-135 for f in km1["freeColumns"] if f>=135]
    require(len(head_piv)==7 and len(head_free)==15,
            "All seven first incoming image columns and fifteen free heads")
    EF=m.fmpq_mat(15,22)
    for i,f in enumerate(head_free):EF[i,f]=1
    require(EF*H==identity(m,15),"Same canonical15-head frame")
    Q=identity(m,22)-H*EF
    require(m.matrix_zero(d.sub(m,Q,head_free)),
            "All constant head ambiguity splits into projected kernel plus seven columns")
    C7=columns(d,m,C,head_piv)
    Q7=d.sub(m,Q,head_piv)
    require(C==-B1*Y*EF+C7*Q7,
            "Every original first incoming column retained by exact full-row identity")
    result["parameters"]["firstReconstruction"]={
        "leadingHeads":15,"completeFullFirstRankAlreadyPaid":7,
        "allOld605By15CoefficientsMatchedByLogicalSHA256":True,
        "all6750OldNormalTwoEntriesZero":True,
        "oldHeadMapSHA256":m.matrix_hash(H),
        "oldLambda0SHA256":m.matrix_hash(L0),
        "oldLambda1Full605SHA256":m.matrix_hash(L1old),
        "allFirstCochainsMayUsePureAndOneNormal":True,
        "all22ConstantCorrectionsRetainedModuloOriginalB1":True,
        "incomingColumns":head_piv,"incomingDecompositionSHA256":m.matrix_hash(Q7),
        "noOld583UnitOr22IncompatibleRHSSolveRepeated":True}
    for name,X in (("first-leading-map",H),
                   ("first-lambda0",L0),("first-lambda1",L1),
                   ("first-incoming-coordinates",Q7)):
        cached_matrix(d,m,a,binding,name,X,{},result)

    R2=d.apply_rows(m,j,coeff,2,d.sections(m,j,L0,1),15,(0,1))
    R2+=d.apply_rows(m,j,coeff,1,d.sections(m,j,L1,1),15,(0,1))
    RH=d.apply_rows(m,j,coeff,2,d.sections(m,j,L0,1),15,(2,3))
    RH+=d.apply_rows(m,j,coeff,1,d.sections(m,j,L1,1),15,(2,3))
    require(m.matrix_zero(RH),"All5100 second forcing high rows are actually zero")
    M2=d.hjoin(m,[B1,C,R2])
    K2,km2=exact_kernel(d,m,j,a,binding,"projected-second-kernel",M2,141,result)
    chosen2,Z,zrank=d.leading_basis(m,j,K2,157,15)
    require(zrank==14 and K2.ncols()==31,
            "All fourteen genuine projected second heads and seventeen zero heads")
    d2=d.sub(m,chosen2,range(135,157))
    P0=L0*Z;P1=L1*Z+L*d2
    P2=d.append_zero_pure(m,d.sub(m,chosen2,range(135)))
    d.verify_jets(m,j,coeff,[P0,P1,P2],[1,1,1],result,"projectedSecondFourteen")
    LF,lf_rank,_,_=m.nullspace(Z.transpose())
    require(lf_rank==14 and LF.ncols()==1,"Exactly one missing leading quotient")
    q=next(i for i in range(15) if LF[i,0])
    E=m.fmpq_mat(15,1);E[q,0]=1
    Frame=m.join_columns(Z,E)
    require(Frame.det(),"Fourteen actual heads plus selected quotient span all fifteen")
    for name,X in (("projected-second-leading",Z),("projected-second-lambda0",P0),
                   ("projected-second-lambda1",P1),("projected-second-lambda2",P2),
                   ("missing-second-leading",E),("second-leading-frame",Frame)):
        cached_matrix(d,m,a,binding,name,X,{},result)
    result["parameters"]["oneMissingSecondHead"]={
        "paidTrueProjectedSecondHeads":14,"completeFirstHeads":15,
        "chosenFirstHeadCoordinate":q,"leadingFrameSHA256":m.matrix_hash(Frame),
        "completeProjectedKernelDimension":31,"projectedZeroHeadDimension":17,
        "all5100OriginalHigherSecondForcingRowsZero":True,
        "noDivisionByGOrRowContent":True,
        "newSecondLeadingRightHandSides":1}
    return B1,C,C7,head_piv,L0,L1,R2,E,Frame,[P0,P1,P2]

def true_two_cubics(d,m,j,a,binding,coeff,L,hpaid,tpaid,result):
    LL=m.fmpq_mat([[coeff["linear"][v][0][0][i] for v in range(2,11)]
                  for i in range(17)])
    N,rank,piv,free=m.nullspace(LL)
    require(rank==8 and N.ncols()==1 and m.matrix_zero(LL*N),
            "Same original unique weak normal line")
    w=[N[i,0] for i in range(9)]
    keys=j.target_columns(3);require(len(keys)==990,"All cubic output slices")
    W0=m.fmpq_mat(990,1)
    for i,(c,b,mon) in enumerate(keys):
        if c==b==0:
            value=m.fmpq(1)
            for v in mon:value*=w[v-2]
            W0[i,0]=value
    ix={key:i for i,key in enumerate(j.target_columns(1))}
    candidates=[]
    for col in (20,21):
        require(all(not L[20+i,col] for i,key in enumerate(j.target_columns(1))
                    if key[0]+key[1]>1),"Complete normal constant heads have tangent degree<=1")
        v=[L[20+ix[(0,0,(k,))],col] for k in range(2,11)]
        cc=[L[20+ix[(1,0,(k,))],col] for k in range(2,11)]
        dd=[L[20+ix[(0,1,(k,))],col] for k in range(2,11)]
        if any(cc) or any(dd):candidates.append((col,v,cc,dd))
    require(candidates,"A real tangent-coupled constant normal head")
    col,v,cc,dd=candidates[0];p=next(i for i,x in enumerate(w) if x)
    aa=cc[p]/w[p];bb=dd[p]/w[p]
    require((aa or bb) and all(cc[i]==aa*w[i] and dd[i]==bb*w[i]
                              for i in range(9)),"True coupled constant direction")
    for eq in range(17):
        value=sum((coeff["linear"][k][0][0][eq]*v[k-2]
                   +aa*coeff["linear"][k][1][0][eq]*w[k-2]
                   +bb*coeff["linear"][k][2][0][eq]*w[k-2]
                   for k in range(2,11)),m.fmpq(0))
        require(not value,"All seventeen exact coupled weak equations")
    W1=m.fmpq_mat(990,1)
    for i,(c,b,mon) in enumerate(keys):
        inds=[k-2 for k in mon];product=m.fmpq(1)
        for k in inds:product*=w[k]
        if c==b==0:
            value=m.fmpq(0)
            for pos in range(3):
                term=v[inds[pos]]
                for other in range(3):
                    if other!=pos:term*=w[inds[other]]
                value+=term
            W1[i,0]=value
        elif (c,b)==(1,0):W1[i,0]=aa*product
        elif (c,b)==(0,1):W1[i,0]=bb*product
    W=m.join_columns(W0,W1)
    expected=hpaid["rationalUpperCertificate"]["candidateSHA256"]
    require([m.matrix_hash(W0),m.matrix_hash(W1)]==expected,
            "Both original cubic vectors match paid complete H3 kernel")
    high=d.apply_rows(m,j,coeff,0,{3:W},2,(2,3))
    require(m.matrix_zero(high),"Both cubics verify ALL10200 original high products")
    Ch=d.apply_rows(m,j,coeff,0,{3:W},2,(0,1))
    tp=tpaid["tangentCubic"]
    require(m.matrix_hash(columns(d,m,Ch,[0]))==tp["paidLowCubicColumnSHA256"]
            and m.matrix_hash(columns(d,m,Ch,[1]))==tp["newLowColumnSHA256"],
            "Both actual low cubic feedback columns match paid original columns")
    for name,X in (("full-cubic-high-kernel",W),("full-cubic-low-return",Ch)):
        cached_matrix(d,m,a,binding,name,X,{},result)
    result["parameters"]["completeHighHomogeneous"]={
        "shape":[2295,990],"paidRank":988,"kernelDimension":2,
        "allSixTangentSlicesRetained":True,
        "bothPaidCandidateHashesMatched":True,"candidateSHA256":expected,
        "all10200OriginalHighProductsVerified":True,
        "normalFourAndFiveNotClaimedExhausted":True}
    return W,Ch

def seed_known_constant(d,m,j,u,a,binding,prefix,Bext,L,B1,C,C7,H,Y,head_piv,result):
    """The paid rank and exact column-span identity supply a complete kernel."""
    rank=592;nr,n=Bext.nrows(),Bext.ncols()
    require((nr,n)==(1088,594),"Original one-RHS constant matrix")
    Q=d.sub(m,L,range(20,155),[20,21])
    require(m.matrix_zero(B1*Q),"Complete projected constant two-kernel")
    # The canonical free rows are recovered from the actual two columns.
    R,r=Q.transpose().rref()
    require(r==2,"True independent two constant columns")
    free=m.pivot_columns(R,r);del R
    G=d.sub(m,Q,free)
    require(G.det(),"Two actual free constant coordinates")
    Q=Q*G.inv()
    K=m.fmpq_mat(n,2)
    for i in range(135):
        for k in range(2):K[i,k]=Q[i,k]
    require(m.matrix_zero(Bext*K),"All original known constant kernel rows")
    piv=[i for i in range(n) if i not in set(free)]
    meta={"constantSHA256":m.matrix_hash(Bext),"rank":rank,
          "pivotColumns":piv,"freeColumns":free,
          "allOriginalConstantKernelRowsVerified":True,
          "completenessUsesPaidRank592AndVerifiedColumnSpan":True}
    cached_matrix(d,m,a,binding,prefix+"-constant-kernel",K,meta,result)
    old=d.load_matrix(m,a,binding,prefix+"-unit",result)
    if old is not None:return
    d.guard(a,"one predetermined field profile for actual constant unit",3)
    A=nmod_mat(rank,nr,[0]*(rank*nr),PROFILE_PRIME)
    maxbits=0
    for i in range(nr):
        den=1;values=[]
        for k,p in enumerate(piv):
            x=Bext[i,p]
            if x:
                nn=int(x.numer());dd=int(x.denom())
                den=den//gcd(den,dd)*dd;values.append((k,nn,dd))
        nums=[(k,nn*(den//dd)) for k,nn,dd in values]
        content=0
        for _,nn in nums:content=gcd(content,abs(nn))
        content=content or 1
        for k,nn in nums:
            value=nn//content;A[k,i]=value%PROFILE_PRIME
            maxbits=max(maxbits,abs(value).bit_length())
    RR,rf=A.rref();del A
    if rf==rank:
        rows=m.pivot_columns(RR,rf)
        method="predetermined17-primitive-original-row-unit"
    else:
        # Only the actual constant coefficient matrix; no RHS is appended.
        d.guard(a,"exact original constant row fallback",3)
        RQ,rq=d.sub(m,Bext,range(nr),piv).transpose().rref()
        require(rq==rank,"Paid complete rank592 in exact original coordinates")
        rows=m.pivot_columns(RQ,rq);del RQ
        method="exact-original-constant-row-fallback"
    del RR
    U=d.sub(m,Bext,rows,piv)
    umeta={"constantSHA256":m.matrix_hash(Bext),"rank":rank,
           "rows":rows,"columns":piv,"genuineRationalUnit":True,
           "constantKernelSHA256":m.matrix_hash(K),
           "profile":{"method":method,"actualPrimitiveFieldRank":int(rf),
                      "fieldPrime":PROFILE_PRIME,
                      "maxPrimitiveCoefficientBits":maxbits,
                      "noPrimeScan":True,"actualRHSNotScaledOrChanged":True}}
    d.save_matrix(m,a,binding,prefix+"-unit",U,umeta,result,True)

def run(d,m,j,u,a,binding,inputs,result):
    paid=inputs["first"];hpaid=inputs["h3"];tpaid=inputs["tangent"]
    coeff=d.original_at_two(m,j,2)
    require(coeff["physical"]==paid["physicalCoefficientSHA256"],
            "Every original coefficient0..2 matches the paid original model")
    result["parameters"]["physicalCoefficientSHA256"]=coeff["physical"]
    L=d.cached_constant_heads(d,m,j,a,binding,coeff,result)
    require(m.matrix_hash(L)==paid["checkpointPhases"]["constant-heads"]["matrixSHA256"],
            "Complete original22-head matrix exactly matches the paid one")
    B1,C,C7,head_piv,L0,L1,R2,E,Frame,projected=reconstruct_projected_families(
        d,m,j,a,binding,coeff,L,paid,result)
    W,Ch=true_two_cubics(d,m,j,a,binding,coeff,L,hpaid,tpaid,result)
    B=d.vjoin(m,j,[d.hjoin(m,[j.block(m,coeff,0,r,t) for t in (1,2)])
                  for r in (0,1)])
    require(m.matrix_hash(B)==tpaid["first-tangent-cubicConstantUnit"]["constantSHA256"],
            "All original B585 entries match paid rank583")
    H=d.load_matrix(m,a,binding,"first-leading-map",result)[0]
    Y=d.sub(m,L1,range(20,155))
    # The original seven quotient columns plus all B and Ch have the SAME
    # column span as the already verified609-column matrix of rank592.
    qcols=m.join_columns(B,Ch)
    Bext=m.join_columns(qcols,C7)
    prefix="one-second-actual"
    seed_known_constant(d,m,j,u,a,binding,prefix,Bext,L,B1,C,C7,H,Y,head_piv,result)
    F=R2*E
    cached_matrix(d,m,a,binding,"one-second-original-forcing",F,
                  {"originalRows":1088,"heads":1,"higher5100ActuallyZero":True},result)
    K,meta=u.complete_kernel(d,m,j,a,binding,prefix,Bext,F,592,result)
    selected=None
    for c in range(K.ncols()):
        if K[594,c]:
            selected=c;break
    success=selected is not None
    result["parameters"]["actualOneRHS"]={
        "constantShape":[1088,594],"constantRank":592,
        "newNonhomogeneousColumns":1,"completeLowSchurRank":meta["schurRank"],
        "allOriginalLowRowsVerified":True,"fullHighHomogeneousColumnsRetained":2,
        "firstIncomingBasisColumns":7,"homogeneousConstantKernelDimension":2,
        "selectedExtraLeadingLiftExists":success,
        "failureWouldOnlyRestrictNormalAtMostThree":True}
    if not success:
        result["parameters"]["conclusion"]={
            "completeCharacteristicZeroSecondRankExact":None,
            "completeCharacteristicZeroSecondRankInterval":[0,1],
            "trueSecondLeadingHeadsCertified":14,
            "normalAtMostThreeSecondHeadDimensionExact":14,
            "noFullNegativeConclusionFromRestrictedCorrection":True,
            "h0LocalMembershipNotDecided":True}
        return
    V=(m.fmpq(1)/K[594,selected])*columns(d,m,K,[selected])
    require(V[594,0]==1,"Actual new leading coefficient normalized")
    b=d.sub(m,V,range(587,594))
    A0=L0*E
    A1=L1*E+columns(d,m,L,head_piv)*b
    A2low=d.append_zero_pure(m,d.sub(m,V,range(585)))
    A2high=W*d.sub(m,V,range(585,587))
    A2=d.vjoin(m,j,[A2low,A2high])
    d.verify_jets(m,j,coeff,[A0,A1,A2],[1,1,3],result,"oneNewTrueSecondLift")
    # Normalize the combined fifteen heads back to the paid canonical first frame.
    Finv=Frame.inv();require(Frame*Finv==identity(m,15),"Actual leading frame inverse")
    full=[]
    for k,(P,A) in enumerate(zip(projected,[A0,A1,A2])):
        rows=1595 if k==2 else 155
        X=m.join_columns(embed(m,P,rows),embed(m,A,rows))*Finv
        full.append(X)
    require(full[0]==L0,"Same complete canonical original15 first heads")
    d.verify_jets(m,j,coeff,full,[1,1,3],result,"completeSecondFifteen")
    sq=d.square_read(m,j,full[2],3)
    for name,X in (("second-lambda0",full[0]),("second-lambda1",full[1]),
                   ("second-lambda2",full[2]),("second-square-read",sq),
                   ("new-extra-second-lambda0",A0),("new-extra-second-lambda1",A1),
                   ("new-extra-second-lambda2",A2)):
        cached_matrix(d,m,a,binding,name,X,{},result)
    result["parameters"]["completeSecondFamily"]={
        "leadingDimension":15,"completeSecondConnectionRankOverQ":0,
        "lambdaNormalDegreeBounds":[1,1,3],
        "lambdaSHA256":[m.matrix_hash(X) for X in full],
        "all6188OriginalRowsAndThreeLayersVerified":True,
        "allFirstIncomingParametersRetainedModuloExactBImage":True,
        "allLowerFirst15AndConstant22CochainsSavedForFurtherJets":True,
        "sameHeadNormalAtLeastTwoReadingInvariantUsesCompleteFirstSupport":True,
        "nineLambda2SquareReadShape":[9,15],
        "nineLambda2SquareReadSHA256":m.matrix_hash(sq),
        "nineLambda2SquareReadAllZero":m.matrix_zero(sq),
        "firstNonzeroLambda2SquareRead":d.first_nonzero(sq),
        "nonzeroReadIsNotAH0ObstructionWithoutTrueThirdLift":True}
    result["parameters"]["conclusion"]={
        "completeCharacteristicZeroSecondRankExact":0,
        "completeCharacteristicZeroSecondRankInterval":[0,0],
        "trueSecondLeadingHeadsCertified":15,
        "positiveConclusionUsesFullFirstCompletenessAndActualOriginalProducts":True,
        "noCharacteristicZeroConclusionBorrowedFromFieldSecondRank":True,
        "h0LocalMembershipNotDecided":True,
        "noGlobalOrOtherPointMembershipClaim":True}

def main():
    p=argparse.ArgumentParser()
    for name in ("paid-probe","generator","jet-actions","unit-schur-helper","constant-receipt",
                 "first-receipt","full-first-receipt","projection-receipt","h3-receipt",
                 "tangent-receipt","checkpoint-dir","out"):
        p.add_argument("--"+name,required=True)
    p.add_argument("--remaining-seconds",type=float,default=600)
    p.add_argument("--memory-mib",type=int,default=4096)
    a=p.parse_args()
    require(0<a.remaining_seconds<=900 and 1024<=a.memory_mib<=8192,
            "Explicit shared resource bounds")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    pins={"paidProbe":(a.paid_probe,BASE_SHA),"generator":(a.generator,GEN_SHA),
          "jetActions":(a.jet_actions,ACT_SHA),"unitHelper":(a.unit_schur_helper,UNIT_SHA),
          "constantReceipt":(a.constant_receipt,CONST_SHA),
          "firstReceipt":(a.first_receipt,FIRST_SHA),
          "fullFirstReceipt":(a.full_first_receipt,FULL_FIRST_SHA),
          "projectionReceipt":(a.projection_receipt,PROJECTION_SHA),
          "h3Receipt":(a.h3_receipt,H3_SHA),"tangentReceipt":(a.tangent_receipt,TANGENT_SHA)}
    for label,(path,digest) in pins.items():
        require(sha(path)==digest,"Pinned original source/actual receipt "+label)
    inputs={}
    for label,path in (("first",a.first_receipt),("fullfirst",a.full_first_receipt),
                       ("projection",a.projection_receipt),("h3",a.h3_receipt),
                       ("tangent",a.tangent_receipt)):
        out=json.loads(Path(path).read_bytes())
        require(out["result"]["status"]=="completed","Completed original ancestor "+label)
        inputs[label]=out["result"]["parameters"]
    require(inputs["first"]["firstRestrictedFamily"]["leadingDimension"]==15
            and inputs["fullfirst"]["conclusion"]["completeFirstConnectionRankOverQExact"]==7,
            "Same15 first heads are now known complete over Q")
    require(inputs["projection"]["projectedTorsionLengthExact"]==12
            and inputs["projection"]["localGenerationBothDirectionsVerified"]
            and inputs["projection"]["all54AddedRowsAreGMULTIPLES"],
            "True original projection, with no division by vanishing g")
    require(inputs["h3"]["conclusion"]["completeNormalThreeHighKernelDimensionIfExact"]==2
            and inputs["h3"]["rationalUpperCertificate"]["all10200OriginalProductsVerified"],
            "Complete true Q H3 homogeneous kernel")
    require(inputs["tangent"]["first-tangent-cubicCompleteSchurKernel"]["rank"]==592
            and inputs["tangent"]["tangentCubicExtendedFirstFamilyVerification"][
                "all6188OriginalRowsVerified"],"Paid same low augmented rank592")
    d=module_at("r150_one_second_original_base",a.paid_probe)
    m=module_at("r150_one_second_original_generator",a.generator)
    j=module_at("r150_one_second_original_actions",a.jet_actions)
    u=module_at("r150_one_second_actual_unit",a.unit_schur_helper)
    d.ARGS=a
    a.unit_algorithm="dixon";a.unit_batch_columns=1;a.max_new_unit_groups=1
    a._new_unit_groups=0
    started=time.monotonic();a._deadline=started+a.remaining_seconds
    binding=d.small_hash({"format":"r150-two-one-true-Q-second-input-v1",
        "selfSHA256":sha(__file__),"inputs":{k:v[1] for k,v in pins.items()},
        "allOriginalSources":6188,"originalParameter":"t=s-2",
        "projectedFirstHeads":15,"projectedSecondHeads":14,
        "newLeadingRHS":1,"knownHighKernelDimension":2,
        "unitProfilePrime":PROFILE_PRIME})
    result={"format":"r150-two-one-true-Q-second-connection-v1","status":"started",
        "parameters":{"binding":binding,"selfSHA256":sha(__file__),
        "inputSHA256":{k:v[1] for k,v in pins.items()},
        "sharedSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
        "allMatricesTemporary":True,"noLargeRecomputableDataUploaded":True,
        "noOldHugeIncompatibleUnitSolutionsRebuilt":True}}
    def alarm(_s,_f):raise d.SafeStop("Shared true-Q second-connection budget exhausted")
    signal.signal(signal.SIGALRM,alarm)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    try:
        run(d,m,j,u,a,binding,inputs,result);result["status"]="completed"
    except d.SafeStop as exc:
        result["status"]="prefix-completed";result["error"]=str(exc)
    except BaseException as exc:
        result["status"]="failed";result["error"]=type(exc).__name__+": "+str(exc);raise
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        result["elapsedSeconds"]=time.monotonic()-started
        mp=Path(a.checkpoint_dir)/"manifest.json"
        if mp.exists():result["parameters"]["temporaryManifest"]={
            "binding":binding,"bytes":mp.stat().st_size,"sha256":sha(mp)}
        d.compact_metadata(result)
        raw=d.canonical_bytes(result)
        require(len(raw)<90000,"Only a small mathematical receipt is persistent")
        d.atomic_json(a.out,result)
        print(json.dumps({"status":result["status"],"receipt":a.out,
            "bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),
            "elapsedSeconds":result["elapsedSeconds"]}),flush=True)

if __name__=="__main__":main()
