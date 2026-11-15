#!/usr/bin/env python3
"""R150 exact FULL zero third connection after paid r1=4,r2=0.

Restore all23 paid second heads, not the later5->4->2 representative family.
Ten pure heads are exact for all parameters.  The other13 use their original
canonical first/second sections, whose hashes and all original products are
checked.  No paid1088-row RREF, top/middle RREF, or full inverse is repeated.
Three lost second-section RHS are restored with the paid582 unit.

The complete2-dimensional high homogeneous space recovers ALL4347 nonpure
A0 corrections.  Third forcing has all5100 high rows zero.  The low system is
[B592,Ch2,R3(13)] on1088 original rows; all6188 final products are checked.
Since beta2=0, earlier second-cochain choices change R3 only in W1.  Thus
13 minus the actual head projection rank is the FULL third connection rank.
All cochains and full kernels remain job-temporary for subsequent true pages.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import time

FIRST_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACTIONS_SHA="4e63c72c550e8f90c022b086d3758f8e7b12edf4fb16a0ef387bc1a92f97366a"
PARENT_SHA="a6c423b98d70e06fb5a28797f09a11300129ec59128921c1e2d5c0e54fa8b5f2"
HELPER_SHA="36356983e71ee1e67677da1a7a5f7aebf2987db282a5447a741b6a6af93084d5"
REUSE_SHA="b46ca6a4fc594b53687d692986229edc97ca770e21ac6332703eaf998c9e0b67"
SIXTH_SHA="0f30617b728af521fe9d928e37a0ee04a2274abd9d148e033a23c29c20ff10f1"
SIXTH_MANIFEST_SHA="89fbd83c0d75ed64b6be2dfc77f2128cc903971585b16796ee3456613907da44"
SIXTH_BINDING="2ab96ac89edbf80802073e1278419af544682d9d7f6186ce27aa0fcc6559c7da"
FIRST_RECEIPT_SHA="03c80c0185cc7ea19a6b8aec57f3fcb905f4b6299c5bad2fdc872229bce85548"
PURE_RECEIPT_SHA="9fa21a1f33225c470af62e4186046ff93281f4647bcb126c32f239bf355f846a"
SECOND_RECEIPT_SHA="2bf6ad79a39cace74510f195bae244abb620b4ca138a87c5c9b99d7cf2c282c8"
THIRD_RECEIPT_SHA="8fae063a281b65d9dc8710597f886093c08ba44f53bb690b11e3b3f0e9b0d8cf"
FORMAT="r150-zero-complete-third-full-high-temporary-v1"

def req(ok,msg):
    if not ok: raise AssertionError(msg)

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(1048576),b""): h.update(block)
    return h.hexdigest()

def small_hash(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def module_at(name,path):
    import importlib.util
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
    return m

def completed(d,path,want):
    req(sha(path)==want,"Exact paid small receipt "+str(path))
    o=d.read_json(path)
    req(o["exitCode"]==0 and o["result"]["status"]=="completed","Actual completed receipt")
    return o["result"]

def field(o,key):
    return o.get(key,o.get("parameters",{}).get(key))

def eye(m,n):
    return m.fmpq_mat([[int(i==j) for j in range(n)] for i in range(n)])

def low(m,j,coeff,order,sections,ncols):
    return j.join_vertical(m,[j.apply(m,coeff,order,sr,sections,ncols) for sr in (0,1)])

def all_rows(m,j,coeff,order,sections,ncols):
    return j.join_vertical(m,[j.apply_sparse(m,coeff,order,sr,sections,ncols)
                              for sr in range(4)])

def adopt_constants(d,m,w,a,binding,prefix,constants,result):
    for suffix,(M,meta) in constants.items():
        w.adopt(d,m,a,binding,prefix+"-"+suffix,M,meta,result)

def head_basis(m,K,start,count):
    H=m.submatrix(K,range(start,start+count),range(K.ncols()))
    rr,r=H.rref();choice=m.pivot_columns(rr,r)
    return m.submatrix(K,range(K.nrows()),choice),m.submatrix(H,range(count),choice),r

def pack_sections(m,j,co):
    blocks=[];ranges={};offset=0
    for k,section in enumerate(co):
        for sr,X in sorted(section.items()):
            name="lambda"+str(k)+"Normal"+str(sr)
            ranges[name]={"start":offset,"stop":offset+X.nrows(),
                          "matrixSHA256":m.matrix_hash(X)}
            blocks.append(X);offset+=X.nrows()
    return j.join_vertical(m,blocks),ranges

def unpack_sections(m,pack,ranges,order):
    out=[{} for _ in range(order+1)]
    for key,q in ranges.items():
        left,right=key.split("Normal")
        k=int(left[6:]);sr=int(right)
        X=m.submatrix(pack,range(q["start"],q["stop"]),range(pack.ncols()))
        req(m.matrix_hash(X)==q["matrixSHA256"],"Actual cochain range "+key)
        out[k][sr]=X
    return out

def square_readouts(m,j,co):
    index={v:i for i,v in enumerate(j.target_columns(2))}
    nc=next(iter(co[0].values())).ncols();out={}
    for k,section in enumerate(co):
        X=section.get(2)
        R=(m.fmpq_mat(9,nc) if X is None else
           m.fmpq_mat(9,nc,[X[index[(0,0,(i,i))],c]
                            for i in range(2,11) for c in range(nc)]))
        data=[[str(R[i,c]) for c in range(nc)] for i in range(9)]
        q={"matrixSHA256":m.matrix_hash(R),"allEntriesZero":m.matrix_zero(R)}
        if len(json.dumps(data))<9000: q["nineByLeading"]=data
        else: q["valuesInTemporaryCochainOnly"]=True
        out["lambda"+str(k)]=q
    return out

def check_jets(m,j,coeff,co,order,ncols):
    for k in range(order+1):
        for sr in range(4):
            R=m.fmpq_mat(len(j.source_rows(sr)),ncols)
            for v in range(k+1):
                R+=j.apply_sparse(m,coeff,k-v,sr,co[v],ncols)
            req(m.matrix_zero(R),"All original source rows at order "+str(k)+" sector "+str(sr))

def restore_second(d,m,j,u,w,a,binding,coeff,B,constants,first,pure,second,oldthird,result):
    phase="complete-paid-second-cochains"
    cached=d.load_matrix(m,a,binding,phase,result)
    if cached is not None:
        pack,meta,verified=cached
        req(verified and [pack.nrows(),pack.ncols()]==[875,23]
            and meta["allThreeOrdersAll6188RowsVerified"]
            and meta["oldFirstCoefficientSHA256"]==oldthird["fixedLeft2FirstCoefficientSHA256"]
            and meta["oldSecondCoefficientSHA256"]==oldthird["fixedLeft2SecondCoefficientSHA256"],
            "Complete paid second source checkpoint")
        co=unpack_sections(m,pack,meta["ranges"],2)
        return co,meta
    P0=j.block(m,coeff,0,0,1);P1=j.block(m,coeff,1,0,1)
    Q,r0,pc,_=m.nullspace(P0)
    U,rt,pr,_=m.nullspace(P0.transpose())
    C=U.transpose()*P1*Q
    V,rc,_,_=m.nullspace(C)
    req(r0==rt==128 and rc==4 and V.ncols()==3,"Paid first-page dimensions")
    for key,X in (("P0",P0),("P1",P1),("Q",Q),("leftKernel",U),
                  ("connecting",C),("annihilators",V)):
        req(m.matrix_hash(X)==first["matrixSha256"][key],"Paid first canonical hash "+key)
    q0=Q*V
    W=m.fmpq_mat(135,3)
    z=m.submatrix(P0,pr,pc).solve(m.submatrix(P1*q0,pr,range(3)),algorithm="dixon")
    for i,p in enumerate(pc):
        for c in range(3): W[p,c]=z[i,c]
    req(P0*W==P1*q0 and m.matrix_hash(W)==first["matrixSha256"]["originalCorrection"],
        "All170 original first corrections and canonical section")

    R2=all_rows(m,j,coeff,2,{1:q0},3)+all_rows(m,j,coeff,1,{1:-W},3)
    req(m.matrix_zero(m.submatrix(R2,range(1088,6188),range(3))),"All high normal second RHS")
    C2=m.submatrix(R2,range(1088),range(3))
    req(m.matrix_hash(m.join_columns(B,C2))==second["augmentedMatrixSHA256"],
        "Original paid second full matrix hash")
    prefix="paid-second-restored-unit"
    adopt_constants(d,m,w,a,binding,prefix,constants,result)
    K2,kmeta=u.complete_kernel(d,m,j,a,binding,prefix,B,C2,582,result)
    req(kmeta["rank"]==582 and [K2.nrows(),K2.ncols()]==[595,13],
        "Paid complete second normal reconstruction")
    cert=m.submatrix(K2,range(595),range(10,13))
    req(m.submatrix(cert,range(592,595),range(3))==eye(m,3),
        "Paid three normal second leading identity")
    req(m.matrix_hash(cert)==second["completeCorrectionSHA256"],
        "Actual original canonical normal second section")
    Hnormal=m.submatrix(cert,range(585),range(3))
    Bnormal=m.submatrix(cert,range(585,592),range(3))

    pure_columns=j.target_columns(0)
    pure_index={v:i for i,v in enumerate(pure_columns)}
    pure_ten=[(aa,deg-aa+2,()) for deg in range(4) for aa in range(deg+1)]
    pure_ids=[pure_index[v] for v in pure_ten]
    exact_ids=[i for i,(_,bb,_) in enumerate(pure_columns) if bb<=1]
    req(len(pure_ids)==len(exact_ids)==10 and len(set(pure_ids+exact_ids))==20,
        "All20 actual pure heads separated")
    S2=m.submatrix(j.block(m,coeff,2,0,0),range(170),pure_ids)
    req(m.matrix_hash(S2)==pure["matrixSHA256"]["S"],"Original pure second RHS")
    small=m.join_columns(P0,P1*Q)
    _,rs,sc,_=m.nullspace(small);_,rst,sr,_=m.nullspace(small.transpose())
    req(rs==rst==132,"Paid pure correction unit")
    Pcert=m.fmpq_mat(142,10)
    y=m.submatrix(small,sr,sc).solve(m.submatrix(S2,sr,range(10)),algorithm="dixon")
    for i,p in enumerate(sc):
        for c in range(10): Pcert[p,c]=y[i,c]
    req(small*Pcert==S2 and m.matrix_hash(Pcert)==pure["matrixSHA256"]["completeOriginalCorrection"],
        "All1700 original pure second corrections and canonical section")
    Wpure=m.submatrix(Pcert,range(135),range(10))
    Bpure=m.submatrix(Pcert,range(135,142),range(10))
    l1=m.join_columns(-Q*Bpure,-W+Q*Bnormal)
    l2=m.fmpq_mat(585,13)
    for i in range(135):
        for c in range(10): l2[i,c]=-Wpure[i,c]
    for i in range(585):
        for c in range(3): l2[i,10+c]=Hnormal[i,c]
    req(m.matrix_hash(l1)==oldthird["fixedLeft2FirstCoefficientSHA256"]
        and m.matrix_hash(l2)==oldthird["fixedLeft2SecondCoefficientSHA256"],
        "All13 original paid second representatives match")
    h0pure=m.fmpq_mat(20,23);h0normal=m.fmpq_mat(135,23)
    for c,i in enumerate(pure_ids): h0pure[i,c]=1
    for i in range(135):
        for c in range(3): h0normal[i,10+c]=q0[i,c]
    for c,i in enumerate(exact_ids): h0pure[i,13+c]=1
    co=[
        {0:h0pure,1:h0normal},
        {1:m.join_columns(l1,m.fmpq_mat(135,10))},
        {1:m.join_columns(m.submatrix(l2,range(135),range(13)),m.fmpq_mat(135,10)),
         2:m.join_columns(m.submatrix(l2,range(135,585),range(13)),m.fmpq_mat(450,10))}
    ]
    _,head_rank=j.join_vertical(m,[h0pure,h0normal]).rref()
    req(head_rank==23,"Independent full second leading space")
    check_jets(m,j,coeff,co,2,23)
    exact={0:m.submatrix(h0pure,range(20),range(13,23))}
    for k in range(4):
        req(m.matrix_zero(all_rows(m,j,coeff,k,exact,10)),
            "Actual exact-pure original coefficients through new order")
    pack,ranges=pack_sections(m,j,co)
    meta={"chart":"zero","order":2,"leadingColumns":23,"ranges":ranges,
          "oldFirstCoefficientSHA256":m.matrix_hash(l1),
          "oldSecondCoefficientSHA256":m.matrix_hash(l2),
          "nonexactLeadingIndices":list(range(13)),"exactPureIndices":list(range(13,23)),
          "actualPureTargetCoordinates":pure_ids,"actualExactPureTargetCoordinates":exact_ids,
          "allThreeOrdersAll6188RowsVerified":True,"actualLeadingRank":23,
          "completeSecondHeadsByPaidFirstRank4And23IndependentHeads":True,
          "exactPureAllParameterProof":"F(s)|plane=d^2 times the original pure polynomial; b<=1 reads zero",
          "noOld1088RowRrefRepeated":True,"noCompleteInverseConstructed":True}
    d.save_matrix(m,a,binding,phase,pack,meta,result,True)
    return co,meta

def seed_homogeneous_solutions(d,m,w,a,binding,prefix,B,C,Ch,Xh,Qz,constants,result):
    adopt_constants(d,m,w,a,binding,prefix,constants,result)
    U,umeta=constants["unit"];I=umeta["rows"]
    bsha=m.matrix_hash(B);csha=m.matrix_hash(C);usha=m.matrix_hash(U)
    for c in range(2):
        col=m.submatrix(Xh,range(582),[c])
        req(m.matrix_zero(U*col+m.submatrix(Ch,I,[c])),"All582 original inherited homogeneous-unit rows")
        phase=prefix+"-rhs-column-%04d"%c
        meta={"column":c,"constantSHA256":bsha,"rhsSHA256":csha,
              "unitSHA256":usha,"allOriginalUnitRowsVerified":True,
              "originalUnitProductCoordinates":582,
              "algorithm":"paid-source-linear-combination","nativeSeconds":0.0,
              "nativeSolveUsed":False,"oldHeadKernelSHA256":m.matrix_hash(Qz)}
        old=d.load_matrix(m,a,binding,phase,result)
        if old is None: d.save_matrix(m,a,binding,phase,col,meta,result,True)
        else:
            X,xmeta,verified=old
            req(verified and X==col and xmeta==meta,"Actual inherited homogeneous solution checkpoint")

def run(d,m,j,u,w,a,result):
    sixth=completed(d,a.sixth_receipt,SIXTH_SHA);paid=sixth["parameters"]
    req(paid["independentSixthLeadingCount"]==5 and paid["all6188OriginalSixthRowsVerified"]
        and paid["middleKernelDimension"]==9 and paid["allTopAndMiddleHomogeneousKernelsRetained"],
        "Original complete high-space ancestor")
    manifest_path=Path(a.sixth_checkpoint_dir)/"sixth-checkpoint.json"
    req(sha(manifest_path)==SIXTH_MANIFEST_SHA,"Paid sixth manifest bytes")
    manifest=d.read_json(manifest_path)
    req(manifest["format"]==w.OLD_FORMAT and manifest["binding"]==SIXTH_BINDING,
        "Paid complete sixth binding")
    first_result=completed(d,a.first_connection_receipt,FIRST_RECEIPT_SHA)
    charts=[x for x in first_result["parameters"]["charts"] if x["chart"]=="zero"]
    req(len(charts)==1,"Actual finite-zero first chart")
    first=charts[0]
    pure_result=completed(d,a.second_pure_receipt,PURE_RECEIPT_SHA)
    normal_result=completed(d,a.second_normal_receipt,SECOND_RECEIPT_SHA)
    third_result=completed(d,a.old_third_receipt,THIRD_RECEIPT_SHA)
    pure=pure_result["parameters"];second=normal_result["parameters"];oldthird=third_result["parameters"]
    req(field(pure_result,"pureConnectionEnvelopeRank")==0
        and field(normal_result,"normalSecondConnectionEnvelopeRank")==0
        and field(third_result,"thirdConnectionEnvelopeRank")==1,
        "Actual paid second and restricted third evidence")
    inputs={"script":sha(__file__),"first":FIRST_SHA,"actions":ACTIONS_SHA,
            "parent":PARENT_SHA,"helper":HELPER_SHA,"reuse":REUSE_SHA,
            "sixthReceipt":SIXTH_SHA,"sixthManifest":SIXTH_MANIFEST_SHA,
            "firstReceipt":FIRST_RECEIPT_SHA,"pureSecondReceipt":PURE_RECEIPT_SHA,
            "normalSecondReceipt":SECOND_RECEIPT_SHA,"oldThirdReceipt":THIRD_RECEIPT_SHA}
    binding=small_hash(inputs)
    result["parameters"].update({"checkpointBinding":binding,"checkpointSemanticInputs":inputs})
    coeff=j.original_coefficients(m,"zero",3)
    for key,value in oldthird["originalThirdJetSHA256"].items():
        req(coeff["physical"].get(key)==value,"Original physical third coefficient "+key)
    result["parameters"]["originalPhysicalHashesThroughOrder3"]=coeff["physical"]
    P0=j.block(m,coeff,0,0,1)
    Q,rq,_,_=m.nullspace(P0)
    req(rq==128 and [Q.nrows(),Q.ncols()]==[135,7],"Complete constant normal head")
    for sr in range(4):
        req(m.matrix_zero(j.apply(m,coeff,0,sr,{1:Q},7)),"All original constant Q identities")
    J0=j.join_vertical(m,[m.join_columns(j.block(m,coeff,0,sr,1),
                                         j.block(m,coeff,0,sr,2)) for sr in (0,1)])
    B1=low(m,j,coeff,1,{1:Q},7)
    B=m.join_columns(J0,B1)
    req([B.nrows(),B.ncols()]==[1088,592],"Original constant low matrix")
    constants={}
    for suffix in ("constant-kernel","unit","primitive-unit"):
        X,meta=w.load_paid(d,m,a,manifest,paid,"low-unit-"+suffix,result)
        if suffix!="primitive-unit":
            req(meta["constantSHA256"]==m.matrix_hash(B),"Unchanged complete low constant block")
        constants[suffix]=(X,meta)

    co2,meta2=restore_second(d,m,j,u,w,a,binding,coeff,B,constants,first,pure,second,oldthird,result)
    result["parameters"].update({"all23PaidSecondHeadsRestored":True,
        "allSecondOrdersAll6188RowsVerified":True,"secondCochainSHA256":m.matrix_hash(pack_sections(m,j,co2)[0]),
        "allEarlierSecondRepresentativeChangesPaidByExactBeta2Zero":True})
    if a.through=="second":
        result["status"]="stage-completed";return
    phase="all-thirteen-original-third-residuals"
    old=d.load_matrix(m,a,binding,phase,result)
    co13=[{sr:m.submatrix(X,range(X.nrows()),range(13)) for sr,X in sec.items()} for sec in co2]
    if old is None:
        R=m.fmpq_mat(6188,13)
        for k in range(3): R+=all_rows(m,j,coeff,3-k,co13[k],13)
        req(m.matrix_zero(m.submatrix(R,range(1088,6188),range(13))),"All5100 high original third residuals")
        req(m.matrix_hash(m.submatrix(R,range(1088),range(13)))==oldthird["all13ThirdResidualColumnsSHA256"],
            "Same all13 original third residuals")
        rmeta={"all6188OriginalRowsRetained":True,"all5100HighRowsActuallyZero":True,
               "oldAll13LowResidualSHA256":oldthird["all13ThirdResidualColumnsSHA256"],
               "physicalSHA256":small_hash(coeff["physical"])}
        d.save_matrix(m,a,binding,phase,R,rmeta,result,True)
    else:
        R,rmeta,verified=old
        req(verified and [R.nrows(),R.ncols()]==[6188,13]
            and rmeta["all5100HighRowsActuallyZero"]
            and rmeta["physicalSHA256"]==small_hash(coeff["physical"]),
            "Complete original residual checkpoint")
    result["parameters"]["all13OriginalThirdResidualSHA256"]=m.matrix_hash(R)
    if a.through=="residual":
        result["status"]="stage-completed";return
    mid,midmeta=w.load_paid(d,m,a,manifest,paid,"middle-complete-lift",result)
    req([mid.nrows(),mid.ncols()]==[3769,9] and midmeta["allTopAndMiddleHomogeneousKernelsRetained"],
        "Paid complete middle parameterization")
    Nh,Qz=w.build_high_homogeneous(d,m,j,a,coeff,mid,binding,result);del mid
    oldC,_=w.load_paid(d,m,a,manifest,paid,"low-actual-rhs",result)
    oldX,xmeta=w.load_paid(d,m,a,manifest,paid,"low-unit-unit-rhs-solution",result)
    req(xmeta["rhsSHA256"]==m.matrix_hash(oldC) and xmeta["allOriginalUnitRHSRowsVerified"],
        "Old homogeneous source transport")
    Ch=oldC*Qz;Xh=oldX*Qz;del oldC,oldX
    nsect={3:m.submatrix(Nh,range(990),range(2)),
           4:m.submatrix(Nh,range(990,2475),range(2)),
           5:m.submatrix(Nh,range(2475,3762),range(2))}
    req(Ch==low(m,j,coeff,0,nsect,2),"All original low rows of complete high homogeneous columns")
    C=m.join_columns(Ch,m.submatrix(R,range(1088),range(13)))
    prefix="complete-third-unit"
    seed_homogeneous_solutions(d,m,w,a,binding,prefix,B,C,Ch,Xh,Qz,constants,result)
    K,kmeta=u.complete_kernel(d,m,j,a,binding,prefix,B,C,582,result)
    req(K.nrows()==607,"Complete original correction and13 head dimensions")
    S,smeta,sverified=d.load_matrix(m,a,binding,prefix+"-full-schur",result)
    req(sverified and smeta["allOriginalRowsRetained"],"All1088 full Schur rows")
    _,hom_rank=m.submatrix(S,range(1088),range(2)).rref()
    req(hom_rank==2,"Full high homogeneous contribution on the low quotient")
    selected,head,r=head_basis(m,K,594,13)
    req(K.ncols()-r==10,"Complete original zero-head fiber")
    beta3=13-r
    req(beta3==kmeta["rank"]-584 and 0<=beta3<=1,
        "Complete third rank and paid previous upper bound")
    b=m.submatrix(selected,range(585,592),range(r))
    high=Nh*m.submatrix(selected,range(592,594),range(r))
    H23=m.fmpq_mat(23,r+10)
    for i in range(13):
        for c in range(r): H23[i,c]=head[i,c]
    for c in range(10): H23[13+c,r+c]=1
    actual=[{sr:X*H23 for sr,X in sec.items()} for sec in co2]
    actual[2][1]+=m.join_columns(Q*b,m.fmpq_mat(135,10))
    lo=m.submatrix(selected,range(585),range(r))
    third={1:m.submatrix(lo,range(135),range(r)),
           2:m.submatrix(lo,range(135,585),range(r)),
           3:m.submatrix(high,range(990),range(r)),
           4:m.submatrix(high,range(990,2475),range(r)),
           5:m.submatrix(high,range(2475,3762),range(r))}
    actual.append({sr:m.join_columns(X,m.fmpq_mat(X.nrows(),10)) for sr,X in third.items()})
    check_jets(m,j,coeff,actual,3,r+10)
    _,actual_head_rank=j.join_vertical(m,[actual[0][0],actual[0][1]]).rref()
    req(actual_head_rank==r+10==23-beta3,"Full independent third head space")
    pack,ranges=pack_sections(m,j,actual)
    meta={"chart":"zero","parameter":"s","order":3,"leadingColumns":r+10,"ranges":ranges,
          "allFourOrdersAll6188RowsVerified":True,"completeSecondHeadSpaceUsed":True,
          "exactFirstConnectionRank":4,"exactSecondConnectionRank":0,
          "exactThirdConnectionRank":beta3,"allEarlierChoicesQuotientedByW1":True,
          "leadingInFull23SecondBasis":[[str(H23[i,c]) for c in range(r+10)] for i in range(23)],
          "allHighAndLowHomogeneousCorrectionsRetained":True,
          "nextPageIncoming":"M0 plus M1 K0 plus all13 original R3 columns; transport R3 by s times saved second cochains",
          "targetSquareReadouts":square_readouts(m,j,actual),"temporaryOnly":True}
    d.save_matrix(m,a,binding,"complete-full-third-cochains",pack,meta,result,True)
    result.update({"status":"completed","fullZeroThirdConnectionRank":beta3,
                   "fullThirdLeadingDimension":r+10,
                   "fullZeroMaximalMinorOrderLowerBound":59-beta3,
                   "fullZeroSubmaximalMinorOrderLowerBound":50-beta3})
    result["parameters"].update({
        "completeLowMatrixShape":[1088,607],"completeLowRank":kmeta["rank"],
        "completeLowKernelDimension":K.ncols(),"completeZeroHeadFiberDimension":10,
        "all13NonexactThirdLeadingProjectionRank":r,"fullThirdLeadingDimension":r+10,
        "exactFirstConnectionRank":4,"exactSecondConnectionRank":0,"fullZeroThirdConnectionRank":beta3,
        "all4347NonpureCorrectionCoordinatesRetained":True,"fullLowConstantRankAfterHighElimination":584,
        "allFourOrdersAll6188RowsVerified":True,"fullThirdConnectionNotMerelyEnvelope":True,
        "allEarlierChoicesQuotientedByW1":True,"wholeCochainShape":[pack.nrows(),pack.ncols()],
        "wholeCochainSHA256":m.matrix_hash(pack),"wholeCochainRanges":ranges,
        "targetSquareReadouts":meta["targetSquareReadouts"],
        "originalPhysicalHashesThroughOrder3":coeff["physical"],
        "fullZeroMaximalMinorOrderLowerBound":59-beta3,
        "fullZeroSubmaximalMinorOrderLowerBound":50-beta3,
        "currentFactorDegreeLowerBound":105-beta3,
        "noTopOrMiddleRrefRepeated":True,"noOld1088RowRrefRepeated":True,
        "noCompleteInverseConstructed":True,"newFinalOriginalProductCoordinates":4*6188*(r+10),
        "nextPageNeedsCompleteThirdIncoming":True,"fullTargetMembershipNotClaimed":True,
        "actualNonexactThirdLeadingInPaid13":[[str(head[i,c]) for c in range(r)] for i in range(13)]})

def main():
    p=argparse.ArgumentParser()
    for name in ("parent-driver","unit-schur-helper","reused-driver","generator","jet-actions",
                 "sixth-receipt","sixth-checkpoint-dir","first-connection-receipt",
                 "second-pure-receipt","second-normal-receipt","old-third-receipt",
                 "checkpoint-dir","out"):
        p.add_argument("--"+name,required=True)
    p.add_argument("--through",choices=("second","residual","final"),default="final")
    p.add_argument("--remaining-seconds",type=float,default=180.0)
    p.add_argument("--memory-mib",type=int,default=2048)
    p.add_argument("--unit-algorithm",choices=("dixon","fflu"),default="dixon")
    p.add_argument("--unit-batch-columns",type=int,choices=(1,2),default=1)
    p.add_argument("--max-new-unit-groups",type=int,default=64)
    a=p.parse_args()
    req(a.remaining_seconds>0 and 512<=a.memory_mib<=8192 and a.max_new_unit_groups>0,
        "Explicit shared bounded resources")
    for path,want in ((a.parent_driver,PARENT_SHA),(a.unit_schur_helper,HELPER_SHA),
                      (a.reused_driver,REUSE_SHA),(a.generator,FIRST_SHA),(a.jet_actions,ACTIONS_SHA)):
        req(sha(path)==want,"Pinned source dependency "+str(path))
    req(Path(a.checkpoint_dir).resolve()!=Path(a.sixth_checkpoint_dir).resolve(),
        "New checkpoint distinct from paid sixth")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,a.memory_mib*1024**2))
    d=module_at("r150_complete3_storage",a.parent_driver)
    m=module_at("r150_complete3_generator",a.generator)
    j=module_at("r150_complete3_actions",a.jet_actions)
    u=module_at("r150_complete3_rhs_unit",a.unit_schur_helper)
    w=module_at("r150_complete3_paid_high_reuse",a.reused_driver)
    d.FORMAT=FORMAT
    started=time.monotonic();a._deadline=started+a.remaining_seconds
    result={"format":"r150-zero-complete-third-reused-full-high-v1","status":"started",
            "arithmetic":"exact rational python-flint","scriptSHA256":sha(__file__),
            "parameters":{"naturalParameter":"s","sharedSeconds":a.remaining_seconds,
                "memoryMiB":a.memory_mib,"through":a.through,
                "checkpointDirectory":str(Path(a.checkpoint_dir)),"paidDirectoryReadOnly":True,
                "sourceStrata":[170,918,2295,2805],"all6188OriginalSourcesRetained":True,
                "sourceMultiplierTransport":"m_j=sum_(k<=j)binom(j,k)s^(j-k)n_k on ALL degree<=3 multipliers",
                "targetLeftTransport":"A_new=T A_old V; lambda_old=T^T lambda_new",
                "temporaryOnly":True,"largeDataUploadedOrCommitted":False}}
    signal.signal(signal.SIGALRM,d.request_stop);signal.signal(signal.SIGTERM,d.request_stop)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    try:
        run(d,m,j,u,w,a,result)
    except d.SafeStop as exc:
        result["status"]="incomplete";result["error"]=str(exc)
    except BaseException as exc:
        result["status"]="failed";result["error"]=type(exc).__name__+": "+str(exc)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        result["elapsedSeconds"]=time.monotonic()-started
        man=Path(a.checkpoint_dir)/"sixth-checkpoint.json"
        if man.exists():
            result["parameters"]["checkpointManifestSHA256"]=sha(man)
            result["parameters"]["checkpointManifestBytes"]=man.stat().st_size
        raw=json.dumps(result,sort_keys=True,indent=2).encode()
        req(len(raw)<100000,"Small permanent receipt only")
        out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True)
        tmp=out.with_name(out.name+".tmp");tmp.write_bytes(raw);os.replace(tmp,out)
        print(json.dumps({"status":result["status"],"receipt":str(out),
            "receiptBytes":len(raw),"receiptSHA256":hashlib.sha256(raw).hexdigest(),
            "elapsedSeconds":result["elapsedSeconds"],
            "fullZeroThirdConnectionRank":result.get("fullZeroThirdConnectionRank"),
            "fullThirdLeadingDimension":result.get("fullThirdLeadingDimension")},sort_keys=True),flush=True)

if __name__=="__main__":
    main()
