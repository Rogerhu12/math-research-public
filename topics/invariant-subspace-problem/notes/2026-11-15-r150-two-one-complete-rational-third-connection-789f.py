#!/usr/bin/env python3
"""Complete true-Q third connection at s=2: one RHS on the paid592 unit.

Author: Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro.
Requires the ACTUAL complete5100x3762 high rank3760 proof, hence full beta2=1.
All fourteen full second heads coincide with the actual projected heads.
The full third incoming image is old M594 PLUS the already paid second
residual direction. Only ONE new592-row solve is performed. The old X2,
S2, original unit, complete homogeneous2 and primitive row scales are reused.
RHS compatible => beta3=0/head14. RHS incompatible => beta3=1/head13.
The latter gives full length12 and W=0 by the actual projected exact sequence.
No finite-field cochain is promoted; every accepted jet is multiplied back
on all6188 original rows and all four parameter coefficients.
"""
import argparse
from copy import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import signal
import sys
import time

BASE_SHA="8f55c5b5f0db2a7dd9b0b042e00cd506fd6e38698b9dc264a602e3dc8ccb510b"
GEN_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACT_SHA="2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
FOUR_SHA="7b0ec2814a716e236d2dce048d0c8b1b6cea6bca8400e54d846b8e403aa1b7b9"
UNIT_SHA="36356983e71ee1e67677da1a7a5f7aebf2987db282a5447a741b6a6af93084d5"
PAID_SHA="950aecf40605fbd3156c223d7e18d4ee1821940386872f59d88cc24f756ed1a2"
HIGH_SHA="1582aa530b7439636798e33cf447ce46c3e85b352ab47b1e236cccc56525584a"
PARENT_BINDING="3de42bed91acf562cce951f7c79f9e4f871cbd31ec82e7430d03bb97198f970f"
HIGH_BINDING="28bddf30e73c27eb623837d9569c9b43db83bd93f54d6ce84eedef0f24d0e862"

def require(ok,message):
    if not ok:raise AssertionError(message)
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);sys.modules[name]=out
    spec.loader.exec_module(out);return out
def eye(m,n):
    return m.fmpq_mat([[int(i==k) for k in range(n)] for i in range(n)])
def embed(m,X,nrows):
    require(X.nrows()<=nrows,"Exact original-coordinate zero extension")
    Z=m.fmpq_mat(nrows,X.ncols())
    for i in range(X.nrows()):
        for k in range(X.ncols()):Z[i,k]=X[i,k]
    return Z
def cols(d,m,X,which):
    return d.sub(m,X,range(X.nrows()),which)
def save(d,m,a,binding,name,X,meta,result):
    old=d.load_matrix(m,a,binding,name,result)
    if old is None:d.save_matrix(m,a,binding,name,X,meta,result,True)
    else:
        M,mm,v=old
        require(v and M==X and mm==meta,"Same verified child phase "+name)
    return X
def parent_phase(d,m,a,pp,name,result,loaded):
    if name in loaded:return loaded[name]
    pa=copy(a);pa.checkpoint_dir=a.paid_checkpoint_dir
    dummy={"parameters":{}}
    out=d.load_matrix(m,pa,PARENT_BINDING,name,dummy)
    require(out is not None and out[2],"Actual verified parent phase "+name)
    actual=d.manifest(pa,PARENT_BINDING)["phases"][name]
    paid=pp["checkpointPhases"][name]
    for k in ("shape","bytes","matrixSHA256","fileSHA256","verified"):
        require(actual[k]==paid[k],"Parent source identity "+name+" / "+k)
    result["parameters"].setdefault("parentPhaseIdentities",{})[name]=paid
    loaded[name]=out;return out
def exact_kernel(d,m,j,a,binding,name,M,rank,result):
    old=d.load_matrix(m,a,binding,name,result);msha=m.matrix_hash(M)
    if old is None:
        d.guard(a,name+" small original projected kernel",2)
        rr,r=M.rref()
        require(r==rank,"Actual paid projected connection rank "+name)
        K,piv,free=j.canonical_kernel(m,rr,r);del rr
        meta={"matrixSHA256":msha,"rank":r,"pivotColumns":piv,
              "freeColumns":free,"allOriginalRowsRetained":True}
        d.save_matrix(m,a,binding,name,K,meta,result,False)
    else:
        K,meta,v=old
        require(meta["matrixSHA256"]==msha and meta["rank"]==rank,
                "Same projected source matrix "+name)
    require(m.matrix_zero(M*K),"All actual projected kernel products "+name)
    for i,f in enumerate(meta["freeColumns"]):
        for k,g in enumerate(meta["freeColumns"]):
            require(K[g,i]==int(i==k),"Canonical free identity "+name)
    meta["allOriginalKernelRowsVerified"]=True
    d.save_matrix(m,a,binding,name,K,meta,result,True)
    return K,meta
def coordinates_in(d,m,L,V):
    rr,r=L.transpose().rref()
    require(r==L.ncols(),"Complete original constant kernel independent")
    rows=m.pivot_columns(rr,r);del rr
    U=d.sub(m,L,rows)
    X=U.solve(d.sub(m,V,rows))
    require(L*X==V,"All actual coordinates in original constant kernel")
    return X

def run(d,m,j,f,u,a,binding,pp,result):
    coeff=f.original_at_two(m,j,3)
    for k,value in pp["physicalCoefficientSHA256"].items():
        require(coeff["physical"][k]==value,"Every paid0..2 original coefficient "+k)
    result["parameters"]["physicalCoefficientSHA256"]=coeff["physical"]
    loaded={}
    def old(name):return parent_phase(d,m,a,pp,name,result,loaded)
    L=old("constant-heads")[0];H=old("first-leading-map")[0]
    L0=old("first-lambda0")[0];L1=old("first-lambda1")[0]
    P=[old("projected-second-lambda"+str(k))[0] for k in range(3)]
    Z=old("projected-second-leading")[0]
    E=old("missing-second-leading")[0]
    F2=old("second-leading-frame")[0]
    W=old("full-cubic-high-kernel")[0]
    Ch=old("full-cubic-low-return")[0]
    require([L.nrows(),L.ncols()]==[155,22] and
            [H.nrows(),H.ncols()]==[22,15] and
            all([X.nrows(),X.ncols()]==[155,14] for X in P),
            "All original complete constant/first/second families")
    require(L0==L*H and P[0]==L0*Z and F2==m.join_columns(Z,E)
            and F2.det(),"Same actual full second leading frame")
    require(m.matrix_zero(d.sub(m,L1,range(20))),
            "The paid canonical first correction has its actual zero pure prefix")
    # P[1] may have genuine pure constant-kernel corrections. They are kept
    # exactly as paid; only P[2], formed by the projected B1 lift, has zero pure rows.

    B1=d.vjoin(m,j,[j.block(m,coeff,0,r,1) for r in (0,1)])
    B=d.vjoin(m,j,[d.hjoin(m,[j.block(m,coeff,0,r,t) for t in (1,2)])
                  for r in (0,1)])
    C=d.apply_rows(m,j,coeff,1,d.sections(m,j,L,1),22,(0,1))
    hp=pp["firstReconstruction"]["incomingColumns"]
    require(hp==[9,10,11,14,15,16,17],"Original seven incoming axes")
    C7=cols(d,m,C,hp)
    hf=[i for i in range(22) if i not in hp]
    EF=m.fmpq_mat(15,22)
    for i,k in enumerate(hf):EF[i,k]=1
    require(EF*H==eye(m,15),"Original first free-head identity")
    Q=eye(m,22)-H*EF
    require(m.matrix_zero(d.sub(m,Q,hf)) and
            C==-B1*d.sub(m,L1,range(20,155))*EF+C7*d.sub(m,Q,hp),
            "All22 constant first corrections retained in original seven image columns")
    actual_ch=d.apply_rows(m,j,coeff,0,{3:W},2,(0,1))
    require(Ch==actual_ch,"Same original complete high-kernel low return")
    M=d.hjoin(m,[B,Ch,C7])
    N,nmeta,_=old("one-second-actual-constant-kernel")
    U,umeta,_=old("one-second-actual-unit")
    X2,x2meta,_=old("one-second-actual-unit-rhs-solution")
    S2,s2meta,_=old("one-second-actual-full-schur")
    r2=old("one-second-original-forcing")[0]
    bsha=m.matrix_hash(M);usha=m.matrix_hash(U)
    require([M.nrows(),M.ncols()]==[1088,594] and
            bsha==pp["one-second-actualConstantUnit"]["constantSHA256"]
            and nmeta["constantSHA256"]==bsha and nmeta["rank"]==592,
            "All original paid594 constant columns unchanged")
    I=umeta["rows"];PC=umeta["columns"]
    require(len(I)==len(PC)==592 and U==d.sub(m,M,I,PC)
            and PC==nmeta["pivotColumns"] and
            m.matrix_zero(M*N),"Same true592 unit and complete homogeneous2")
    for c,fr in enumerate(nmeta["freeColumns"]):
        for k,gr in enumerate(nmeta["freeColumns"]):
            require(N[gr,c]==int(c==k),"Complete unchanged old kernel free identity")
    MP=cols(d,m,M,PC)
    require(m.matrix_zero(U*X2+d.sub(m,r2,I)) and
            S2==r2+MP*X2 and not m.matrix_zero(S2) and
            m.matrix_zero(d.sub(m,S2,I)),"Paid unscaled second X2/S2 all original rows")

    R2=d.apply_rows(m,j,coeff,2,d.sections(m,j,L0,1),15,(0,1))
    R2+=d.apply_rows(m,j,coeff,1,d.sections(m,j,L1,1),15,(0,1))
    require(R2*E==r2,"Exact old unique second forcing")
    second_constant=coordinates_in(d,m,L,P[1]-L1*Z)
    require(m.matrix_zero(R2*Z+C*second_constant+
                         B1*d.sub(m,P[2],range(20,155))),
            "All15 second incoming directions lie in oldM plus the paid r2")
    require(F2*F2.inv()==eye(m,15),"Full15 first-head frame; no incoming direction lost")

    R3=d.apply_rows(m,j,coeff,3,d.sections(m,j,P[0],1),14,(0,1))
    R3+=d.apply_rows(m,j,coeff,2,d.sections(m,j,P[1],1),14,(0,1))
    R3+=d.apply_rows(m,j,coeff,1,d.sections(m,j,P[2],1),14,(0,1))
    RH=d.apply_rows(m,j,coeff,3,d.sections(m,j,P[0],1),14,(2,3))
    RH+=d.apply_rows(m,j,coeff,2,d.sections(m,j,P[1],1),14,(2,3))
    RH+=d.apply_rows(m,j,coeff,1,d.sections(m,j,P[2],1),14,(2,3))
    require(m.matrix_zero(RH),"All5100 actual third forcing rows zero for every full second head")
    result["parameters"]["completeIncoming"]={
        "completeConstantHeads":22,"completeFirstHeads":15,"completeSecondHeads":14,
        "allFirstIncomingRetainedModuloOriginalM":True,
        "allSecondIncomingRetainedModuloOriginalMPlusPaidR2":True,
        "all71400OriginalHighThirdForcingCoordinatesZero":True,
        "originalWholeHighKernelDimension":2,
        "allNormalFourAndFiveCorrectionsExhaustedByPaidCompleteHighRank":True,
        "baseConstantShape":[1088,594],"baseConstantRank":592,
        "completeThirdIncomingRankIncludingPaidR2":593,
        "paidR2SHA256":m.matrix_hash(r2),"paidX2SHA256":m.matrix_hash(X2),
        "paidS2SHA256":m.matrix_hash(S2),
        "noOldUnitSelectionOrOldRHSSolveRepeated":True}

    # Only a small original projected kernel, no old592 constant RREF.
    Mproj=d.hjoin(m,[B1,C,R2,R3])
    require([Mproj.nrows(),Mproj.ncols()]==[1088,186],"Original projected third matrix")
    K3,km=exact_kernel(d,m,j,a,binding,"projected-third-kernel",Mproj,142,result)
    selected,Z3,rhead=d.leading_basis(m,j,K3,172,14)
    require(rhead==13 and K3.ncols()==44,"True projected third13 heads and31 zero heads")
    b=d.sub(m,selected,range(135,157))
    v=d.sub(m,selected,range(157,172))
    T=[P[0]*Z3,P[1]*Z3+L0*v,P[2]*Z3+L1*v+L*b,
       d.append_zero_pure(m,d.sub(m,selected,range(135)))]
    d.verify_jets(m,j,coeff,T,[1,1,1,1],result,"projectedThirdThirteen")
    for k,X in enumerate(T):
        save(d,m,a,binding,"projected-third-lambda"+str(k),X,{},result)
    save(d,m,a,binding,"projected-third-leading",Z3,{},result)
    LF,r,_,_=m.nullspace(Z3.transpose())
    require(r==13 and LF.ncols()==1,"Exactly one missing third head")
    qhead=next(i for i in range(14) if LF[i,0])
    E3=m.fmpq_mat(14,1);E3[qhead,0]=1
    Frame=m.join_columns(Z3,E3)
    require(Frame.det(),"True13 heads plus actual missing coordinate span all14")
    r3=R3*E3
    save(d,m,a,binding,"one-third-original-forcing",r3,
         {"completeOriginalLowRows":1088,"allHigher5100RowsZero":True},result)
    save(d,m,a,binding,"one-third-missing-leading",E3,{},result)
    save(d,m,a,binding,"third-leading-frame",Frame,{},result)

    prefix="one-third-on-paid-unit"
    # The constant row scales are copied, never recomputed or mixed with RHS.
    AP,apmeta,apverified=old("one-second-actual-primitive-unit")
    require(apverified and apmeta["unitSHA256"]==usha and
            apmeta["allOriginalConstantRowScalingsVerified"] and
            apmeta["RHSNotUsedToScaleUnit"],"Paid unchanged original primitive unit")
    save(d,m,a,binding,prefix+"-primitive-unit",AP,apmeta,result)
    csha=m.matrix_hash(r3)
    X3=u.solve_actual_rhs_columns(d,m,a,binding,prefix,U,r3,I,bsha,csha,usha,result)
    require(m.matrix_zero(U*X3+d.sub(m,r3,I)),"Every original592 new unit equation")
    S3=r3+MP*X3
    require(m.matrix_zero(d.sub(m,S3,I)),"All original selected unit rows zero")
    save(d,m,a,binding,"one-third-new-unit-solution",X3,
         {"constantSHA256":bsha,"unitSHA256":usha,"rhsSHA256":csha},result)
    save(d,m,a,binding,"one-third-new-full-schur",S3,{},result)
    SP=m.join_columns(S2,S3);rr,srank=SP.rref();del rr
    require(srank in (1,2),"Full two-column actual Schur rank")
    first=next(i for i in range(1088) if S2[i,0])
    ratio=S3[first,0]/S2[first,0]
    residual=S3-ratio*S2
    compatible=m.matrix_zero(residual)
    require(compatible==(srank==1),"Full original Schur collinearity")
    save(d,m,a,binding,"one-third-paid-plus-new-schur",SP,{},result)
    save(d,m,a,binding,"one-third-complete-incoming-quotient-residual",residual,
         {"ratio":str(ratio),"normalizingOriginalRow":first},result)
    result["parameters"]["oneThirdRHS"]={
        "missingSecondHeadCoordinate":qhead,"newUnitRHSColumns":1,
        "sameOriginal592UnitUsed":True,"paidSecondRHSReSolved":False,
        "all1088OriginalSchurRowsRetained":True,
        "paidPlusNewSchurRank":srank,"completeThirdConnectionRank":srank-1,
        "uniqueMissingThirdRHSCompatible":compatible,
        "ratioInActualOriginalSchurCoordinates":str(ratio),
        "normalizingOriginalRow":first,
        "completeIncomingRank":593,"fullAugmentedRank":592+srank,
        "all594OldColumnsAndTwoHomogeneousDirectionsRetained":True}
    if compatible:
        small=X3-ratio*X2
        coordinates=m.fmpq_mat(594,1)
        for i,pcol in enumerate(PC):coordinates[pcol,0]=small[i,0]
        vnew=-ratio*E
        bnew=d.sub(m,coordinates,range(587,594))
        high=W*d.sub(m,coordinates,range(585,587))
        low=d.append_zero_pure(m,d.sub(m,coordinates,range(585)))
        A=[P[0]*E3,P[1]*E3+L0*vnew,
           P[2]*E3+L1*vnew+cols(d,m,L,hp)*bnew,
           d.vjoin(m,j,[low,high])]
        require(m.matrix_zero(M*coordinates+r3-ratio*r2),
                "Complete original new low relation including genuine second incoming")
        d.verify_jets(m,j,coeff,A,[1,1,1,3],result,"oneNewTrueThirdLift")
        Fi=Frame.inv();require(Frame*Fi==eye(m,14),"Actual complete third head normalization")
        family=[]
        for k in range(4):
            rows=1595 if k==3 else 155
            family.append(m.join_columns(embed(m,T[k],rows),embed(m,A[k],rows))*Fi)
        require(family[0]==P[0],"Same full canonical second heads")
        headmap=eye(m,14);heads=14
        d.verify_jets(m,j,coeff,family,[1,1,1,3],result,"completeThirdFourteen")
    else:
        family=[T[0],T[1],T[2],embed(m,T[3],1595)]
        headmap=Z3;heads=13
    for k,X in enumerate(family):
        save(d,m,a,binding,"complete-third-lambda"+str(k),X,{},result)
    save(d,m,a,binding,"complete-third-leading-to-second",headmap,{},result)
    sq=d.square_read(m,j,family[3],3)
    save(d,m,a,binding,"complete-third-square-read",sq,{},result)
    result["parameters"]["completeThirdFamily"]={
        "heads":heads,"rank":14-heads,"lambdaNormalDegreeBounds":[1,1,1,3],
        "lambdaSHA256":[m.matrix_hash(X) for X in family],
        "headToSecondSHA256":m.matrix_hash(headmap),
        "all6188OriginalRowsAndFourLayersVerified":True,
        "allLowerFirst15Second14Constant22ShiftFamiliesRetained":True,
        "nineLambda3SquareReadShape":[9,heads],
        "nineLambda3SquareReadSHA256":m.matrix_hash(sq),
        "nineLambda3SquareReadAllZero":m.matrix_zero(sq),
        "firstNonzeroLambda3SquareRead":d.first_nonzero(sq)}
    result["parameters"]["conclusion"]={
        "completeCharacteristicZeroFirstConnection":7,
        "completeCharacteristicZeroSecondConnection":1,
        "completeCharacteristicZeroThirdConnection":14-heads,
        "completeThirdHeadDimension":heads,
        "completePositiveSmithExponentsIfDetermined":
            [1,1,1,1,1,1,1,2,3] if not compatible else None,
        "fullCharacteristicZeroLocalLengthInterval":[12,12] if not compatible else[13,14],
        "projectedLengthExact":12,
        "normalQuadraticTorsionQuotientLengthExact":0 if not compatible else None,
        "allNineOriginalSquaresLocallyInImage":True if not compatible else None,
        "allNineOriginalH0TargetsLocallyInImage":True if not compatible else None,
        "localMembershipWhenTrueUsesLengthDifferenceNotFiniteJetAlone":True,
        "noGlobalOrOtherPointMembershipClaim":True,
        "finiteFieldNegativeNeverUsedAsQNegative":True}

def main():
    p=argparse.ArgumentParser()
    for key in ("paid-probe","generator","jet-actions","two-four-generator",
                "unit-schur-helper","paid-second-receipt","paid-high-receipt",
                "paid-checkpoint-dir","checkpoint-dir","out"):
        p.add_argument("--"+key,required=True)
    p.add_argument("--remaining-seconds",type=float,default=180)
    p.add_argument("--memory-mib",type=int,default=4096)
    a=p.parse_args()
    require(0<a.remaining_seconds<=900 and 1024<=a.memory_mib<=8192,"Explicit shared resources")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    pins={"paidProbe":(a.paid_probe,BASE_SHA),"generator":(a.generator,GEN_SHA),
          "jetActions":(a.jet_actions,ACT_SHA),"twoFourGenerator":(a.two_four_generator,FOUR_SHA),
          "unitHelper":(a.unit_schur_helper,UNIT_SHA),
          "paidSecondReceipt":(a.paid_second_receipt,PAID_SHA),
          "paidHighReceipt":(a.paid_high_receipt,HIGH_SHA)}
    for label,(path,digest) in pins.items():
        require(sha(path)==digest,"Pinned original source/actual result "+label)
    require(Path(a.checkpoint_dir).resolve()!=Path(a.paid_checkpoint_dir).resolve(),
            "Read-only ancestor and distinct child directory")
    po=json.loads(Path(a.paid_second_receipt).read_bytes());pp=po["result"]["parameters"]
    ho=json.loads(Path(a.paid_high_receipt).read_bytes());hp=ho["result"]["parameters"]
    require(po["result"]["status"]==ho["result"]["status"]=="completed"
            and po["exitCode"]==ho["exitCode"]==0,
            "Both actual original ancestors completed")
    require(pp["binding"]==PARENT_BINDING and hp["binding"]==HIGH_BINDING
            and hp["paidBinding"]==PARENT_BINDING,
            "Same complete high-kernel proof over the actual second computation")
    require(hp["conclusion"]["completeHighRationalRankExact"]==3760 and
            hp["conclusion"]["completeCharacteristicZeroSecondRankExact"]==1 and
            hp["conclusion"]["completeSecondHeadDimensionExact"]==14,
            "Actual full beta2=1, never a conditional restricted hypothesis")
    require(pp["actualOneRHS"]["completeLowSchurRank"]==1 and
            pp["one-second-actualCompleteSchurKernel"]["rank"]==593 and
            pp["projectedSecondFourteenVerification"]["all6188OriginalRowsVerified"],
            "Actual paid unique second obstruction and fourteen true source jets")
    d=module_at("r150_one_third_base",a.paid_probe)
    m=module_at("r150_one_third_physical",a.generator)
    j=module_at("r150_one_third_actions",a.jet_actions)
    f=module_at("r150_one_third_coefficients",a.two_four_generator)
    u=module_at("r150_one_third_actual_unit",a.unit_schur_helper)
    started=time.monotonic();a._deadline=started+a.remaining_seconds
    d.ARGS=a;a.unit_algorithm="dixon";a.unit_batch_columns=1
    a.max_new_unit_groups=1;a._new_unit_groups=0
    binding=d.small_hash({"format":"r150-two-one-complete-Q-third-input-v1",
        "selfSHA256":sha(__file__),"inputSHA256":{k:v[1] for k,v in pins.items()},
        "paidSecondBinding":PARENT_BINDING,"paidHighBinding":HIGH_BINDING,
        "originalParameter":"t=s-2","allOriginalSourceRows":6188,
        "fullFirstHeads":15,"fullSecondHeads":14,"projectedThirdHeads":13,
        "onlyNewUnitRHS":1,"unitSize":592,"thirdIncomingIncludesPaidSecondResidual":True})
    result={"format":"r150-two-one-complete-Q-third-connection-v1","status":"started",
        "parameters":{"binding":binding,"selfSHA256":sha(__file__),
        "inputSHA256":{k:v[1] for k,v in pins.items()},
        "sharedSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
        "parentBinding":PARENT_BINDING,"completeHighBinding":HIGH_BINDING,
        "ancestorCacheReadOnly":True,"noOldUnitOrRHSSolveRepeated":True,
        "noHigherNormalBlockRankRepeated":True,"allMatricesTemporary":True,
        "noLargeRecomputableDataUploaded":True}}
    def alarm(_s,_f):raise d.SafeStop("Actual shared third-connection budget exhausted")
    signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    try:
        run(d,m,j,f,u,a,binding,pp,result);result["status"]="completed"
    except d.SafeStop as exc:
        result["status"]="prefix-completed";result["error"]=str(exc)
    except BaseException as exc:
        result["status"]="failed";result["error"]=type(exc).__name__+": "+str(exc);raise
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        result["elapsedSeconds"]=time.monotonic()-started
        d.compact_metadata(result);raw=d.canonical_bytes(result)
        require(len(raw)<90000,"Small complete-third mathematical receipt")
        d.atomic_json(a.out,result)
        print(json.dumps({"status":result["status"],"receipt":a.out,"bytes":len(raw),
            "sha256":hashlib.sha256(raw).hexdigest(),
            "elapsedSeconds":result["elapsedSeconds"]}),flush=True)
if __name__=="__main__":main()
