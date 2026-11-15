#!/usr/bin/env python3
"""Read lambda3(n_j^2) in the actual finite-zero fifth-left jets.

Original t_j=(sum_a binom(j,a)(-s)^(j-a)m_a)^2 becomes n_j^2
under the full co-moving substitution.  Since h0 has zero order3 and every
paid lambda0/lambda1 has normal degree<=1, the only coefficient below s^6 is
h0[3] * lambda2(n_j^2) at s^5.

Rebuild the paid second and third canonical corrections, then use
the actual third/fourth/fifth leading matrices in the small receipts.
Later Q ambiguities are one-normal and do not change quadratic coordinates.
No fourth/fifth elimination, no old NF, no new large Macaulay matrix.
The lambda2 pairing is checked against the already completed zero receipt.
The new lambda3 readout alone is NOT a membership obstruction: a real sixth
left extension is required before its s^6 coefficient can be used.
"""
import argparse
import hashlib
import importlib.util
import json
from math import comb
import os
from pathlib import Path
import resource
import signal
import time

FIRST_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
SECOND_SHA="c8dde441995f3c9b57728a68ec7b29aa56e9abfbbee280fc334961b64e561403"
FIFTH_SHA="94151693c2a0a9b8fc0eb84d442d6742818503b3cd069bffd82f95f1b0bc1f1b"
STOP=False

def require(ok,msg):
    if not ok: raise AssertionError(msg)

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def module_at(name,path):
    sp=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m

def receipt(path):
    obj=json.loads(Path(path).read_text())
    r=obj.get("result",obj)
    require(r.get("status")=="completed","Paid receipt incomplete")
    return r

def field(r,key):
    return r.get(key,r.get("parameters",{}).get(key))

def columns(m,seq,nrows):
    require(all(len(x)==nrows for x in seq),"Paid leading column dimension")
    return m.fmpq_mat([[m.fmpq(seq[j][i]) for j in range(len(seq))]
                       for i in range(nrows)])

def write_json(path,obj):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    tmp.write_text(json.dumps(obj,sort_keys=True,separators=(",",":"))+"\n")
    os.replace(tmp,path)

def stopped(signum,frame):
    global STOP
    STOP=True

def run(a,out):
    start=a.started
    def budget(phase):
        if STOP or time.monotonic()-start>=a.remaining_seconds:
            raise TimeoutError("Shared budget before "+phase)
    require(digest(a.generator)==FIRST_SHA,"First generator source changed")
    require(digest(a.normal_generator)==SECOND_SHA,"Second generator source changed")
    require(digest(a.fifth_generator)==FIFTH_SHA,"Fifth generator source changed")
    f=module_at("r150_paid_zero_fifth",a.fifth_generator)
    n=module_at("r150_paid_zero_second",a.normal_generator)
    m=module_at("r150_paid_original_first",a.generator)
    first=n.read_paid_first(a.first_connection_receipt)
    second=receipt(a.second_normal_receipt)
    third=receipt(a.third_receipt)
    fourth=receipt(a.fourth_receipt)
    fifth=receipt(a.fifth_receipt)
    sp=second["parameters"]
    require(field(second,"all1088ExactSecondLeftJetCorrectionRowsVerified")
            and field(second,"all6188OriginalSourcesRetainedInProof"),
            "Paid second identities missing")
    require(field(third,"all6188OriginalSourcesRetainedInProof")
            and field(fourth,"all6188OriginalSourcesRetainedInProof")
            and field(fifth,"all6188OriginalSourcesRetainedInFifthProof"),
            "Paid later full-source identities missing")
    require(field(third,"sumFirstThreeConnectionRanksUpperBound")==5
            and field(fourth,"independentFourthLeadingCount")==9
            and field(fifth,"independentFifthLeadingCount")==7,
            "Wrong actual zero endpoint family")
    require(fifth["scriptSHA256"]==FIFTH_SHA
            and field(fifth,"naturalParameter")=="s",
            "Fifth receipt is not actual zero source")
    Z3=columns(m,field(third,"leadingAnnihilatorsInPaidThirteenBasis"),13)
    Z4=columns(m,field(fourth,"leadingAnnihilatorsInPaidTwelveBasis"),12)
    Z5=columns(m,field(fifth,"leadingAnnihilatorsInPaidNineBasis"),9)
    require((Z3.ncols(),Z4.ncols(),Z5.ncols())==(12,9,7),
            "Actual leading family dimensions")
    for M,r,key in ((Z3,third,"leadingAnnihilatorSHA256"),
                    (Z4,fourth,"leadingAnnihilatorSHA256"),
                    (Z5,fifth,"fifthLeadingAnnihilatorSHA256")):
        require(m.matrix_hash(M)==field(r,key),"Actual leading bytes changed: "+key)
    leading=Z3*Z4*Z5
    budget("paid second coefficients")
    P,cols,pure_rows,linear,quad0,seed2,physical=n.build_original_coefficients(m)
    P0,P1,P2=P
    Q,r0,pivcols,_=m.nullspace(P0)
    U,rt,pivrows,_=m.nullspace(P0.transpose())
    C=U.transpose()*P1*Q
    V,rc,_,_=m.nullspace(C)
    require(r0==rt==128 and rc==4 and V.ncols()==3,"Paid first dimensions")
    for key,M in (("P0",P0),("P1",P1),("Q",Q),("leftKernel",U),
                  ("connecting",C),("annihilators",V)):
        require(m.matrix_hash(M)==first["matrixSha256"][key],
                "Paid first matrix SHA changed: "+key)
    for key in ("J2","J3","L_y0","L_y1","L_y2"):
        require(physical[key]==sp["originalJetSHA256"][key],
                "Paid original second coefficient changed: "+key)
    require(m.matrix_hash(P2)==sp["originalJetSHA256"]["P2"],"Paid P2 changed")
    q0=Q*V
    target=P1*q0
    W=m.fmpq_mat(135,3)
    small=m.submatrix(P0,pivrows,pivcols).solve(
        m.submatrix(target,pivrows,range(3)))
    for i,p in enumerate(pivcols):
        for j in range(3): W[p,j]=small[i,j]
    require(P0*W==target
            and m.matrix_hash(W)==first["matrixSha256"]["originalCorrection"],
            "All170 original first corrections/section")
    pairs=[(j,k) for j in range(2,11) for k in range(j,11)]
    two_cols=[(aa,degree-aa,j,k) for degree in range(4)
              for aa in range(degree+1) for j,k in pairs]
    one_rows=[(i,aa,degree-aa,j) for i in range(17) for degree in range(3)
              for aa in range(degree+1) for j in range(2,11)]
    one_index={t:j for j,t in enumerate(cols)}
    two_index={t:135+j for j,t in enumerate(two_cols)}
    J0=f.make_J(m,0,P0,linear,quad0,pure_rows,one_rows,two_index,pairs)
    J1=m.fmpq_mat(1088,7)
    P1Q=P1*Q
    for i in range(170):
        for j in range(7): J1[i,j]=P1Q[i,j]
    R2=m.fmpq_mat(1088,3)
    rp=P2*q0-P1*W
    for i in range(170):
        for j in range(3): R2[i,j]=rp[i,j]
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        for j in range(3):
            R2[170+rr,j]=seed2[i]*q0[one_index[(aa,bb+2,l)],j]
    M2=m.join_columns(m.join_columns(J0,J1),R2)
    require(m.matrix_hash(M2)==sp["augmentedMatrixSHA256"],
            "Paid full second matrix changed")
    budget("single paid second correction RREF")
    cert,rank,piv,free=f.extract_final_kernel(m,M2,592,582,582)
    require(free==[592,593,594]
            and m.matrix_hash(cert)==sp["completeCorrectionSHA256"],
            "Paid second canonical full source correction changed")
    require(m.matrix_zero(M2*cert),"All1088 second correction rows failed")
    H=m.submatrix(cert,range(585),range(3))

    # All target transformations are the original binomial squares.
    for j in range(2,11):
        inv=[sum(comb(j,aa)*(-1)**(j-aa)*comb(aa,rr)
                 for aa in range(rr,j+1)) for rr in range(j+1)]
        require(inv==[0]*j+[1],"Original target binomial substitution")
    raw2=m.fmpq_mat([[H[two_index[(0,0,j,j)],k] for k in range(3)]
                    for j in range(2,11)])
    pair2=raw2*m.submatrix(leading,range(10,13),range(7))
    require(m.matrix_hash(raw2)=="bbc4d48ba43feb38f601eccea7cc8bba168f7c3f844630694f2d4cb08353243d"
            and m.matrix_hash(pair2)=="50781d98bb92faafbe14ada9db16b30b1c1142776f5cbfb941b73489f02829a6"
            and m.matrix_zero(raw2) and m.matrix_zero(pair2),
            "Previously paid exact target lambda2 pairing changed")

    pure=n.read_paid_pure(a.second_pure_receipt)
    pure_hash=field(pure,"matrixSHA256")
    pure_cols=[(aa,degree-aa+2) for degree in range(4) for aa in range(degree+1)]
    pure_index={t:j for j,t in enumerate(pure_cols)}
    S2=m.fmpq_mat(170,10)
    for rr,(i,aa,bb) in enumerate(pure_rows):
        S2[rr,pure_index[(aa,bb+2)]]=seed2[i]
    require(m.matrix_hash(S2)==pure_hash["S"],"Paid pure second seed")
    small_aug=m.join_columns(P0,P1Q)
    _,rsmall,acols,_=m.nullspace(small_aug)
    _,rsmallT,arows,_=m.nullspace(small_aug.transpose())
    require(rsmall==rsmallT==132,"Paid pure second rank")
    Pcert=m.fmpq_mat(142,10)
    sol=m.submatrix(small_aug,arows,acols).solve(
        m.submatrix(S2,arows,range(10)))
    for i,col in enumerate(acols):
        for j in range(10): Pcert[col,j]=sol[i,j]
    require(small_aug*Pcert==S2
            and m.matrix_hash(Pcert)==pure_hash["completeOriginalCorrection"],
            "All1700 actual pure second corrections")
    Wpure=m.submatrix(Pcert,range(135),range(10))
    Bpure=m.submatrix(Pcert,range(135,142),range(10))
    Bnormal=m.submatrix(cert,range(585,592),range(3))
    lam1=m.join_columns(-Q*Bpure,-W+Q*Bnormal)
    lam2=m.fmpq_mat(585,13)
    for i in range(135):
        for j in range(10): lam2[i,j]=-Wpure[i,j]
    for i in range(585):
        for j in range(3): lam2[i,10+j]=H[i,j]
    tp=third["parameters"]
    require(m.matrix_hash(lam1)==tp["fixedLeft2FirstCoefficientSHA256"]
            and m.matrix_hash(lam2)==tp["fixedLeft2SecondCoefficientSHA256"],
            "Actual complete paid second jets changed")
    budget("paid original third residual")
    P3,quad1,seed3,physical3,_,_=f.third_coefficients(m,sp["originalJetSHA256"])
    for key,val in physical3.items():
        require(val==tp["originalThirdJetSHA256"][key],
                "Paid original third coefficient changed: "+key)
    A1low=f.make_J(m,1,P1,linear,quad1,pure_rows,one_rows,two_index,pairs)
    R3=m.fmpq_mat(1088,13)
    np3=P3*q0
    for row,(i,aa,bb) in enumerate(pure_rows):
        R3[row,pure_index[(aa,bb+2)]]=seed3[i]
        for j in range(3): R3[row,10+j]=np3[row,j]
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        idx=one_index[(aa,bb+2,l)]
        for j in range(3): R3[170+rr,10+j]=seed3[i]*q0[idx,j]
    term=P2*lam1
    for row in range(170):
        for j in range(13): R3[row,j]+=term[row,j]
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        idx=one_index[(aa,bb+2,l)]
        for j in range(13): R3[170+rr,j]+=seed2[i]*lam1[idx,j]
    R3+=A1low*lam2
    require(m.matrix_hash(A1low)==tp["A1TransposeLowNormalSHA256"]
            and m.matrix_hash(R3)==tp["all13ThirdResidualColumnsSHA256"],
            "Paid original third full residual changed")
    M3=m.join_columns(m.join_columns(J0,J1),R3)
    require(m.matrix_hash(M3)==tp["thirdAugmentedMatrixSHA256"],
            "Paid original third canonical matrix changed")
    budget("single paid third correction RREF")
    cert3,r3,piv3,free3=f.extract_final_kernel(m,M3,592,582,583)
    require(free3==list(range(592,604))
            and m.matrix_hash(cert3)==tp["completeThirdCorrectionSHA256"],
            "Paid original third canonical section changed")
    require(m.matrix_zero(M3*cert3),"All1088 original third correction rows")
    require(m.submatrix(cert3,range(592,605),range(12))==Z3,
            "Actual third leading section incompatible")
    third_coefficient=m.submatrix(cert3,range(585),range(12))
    raw3=m.fmpq_mat([[third_coefficient[two_index[(0,0,j,j)],k]
                      for k in range(12)] for j in range(2,11)])
    # In passing from the third to the fourth jet lambda3 adds Q B4.
    # It has only one normal factor; the fifth step adds Q B5 to lambda4.
    pair3=raw3*Z4*Z5
    candidates=[j+2 for j in range(9) if any(pair3[j,k] for k in range(7))]
    h03=-2*(-8)**2*864**2*9600
    require(h03==-917294284800,"Actual integer h0 third coefficient")
    h0pair3=h03*pair3
    input_files={
        key:{"bytes":Path(path).stat().st_size,"sha256":digest(path)}
        for key,path in (
            ("firstGenerator",a.generator),("secondGenerator",a.normal_generator),
            ("fifthGenerator",a.fifth_generator),
            ("firstReceipt",a.first_connection_receipt),
            ("secondNormalReceipt",a.second_normal_receipt),
            ("secondPureReceipt",a.second_pure_receipt),
            ("thirdReceipt",a.third_receipt),("fourthReceipt",a.fourth_receipt),
            ("fifthReceipt",a.fifth_receipt))}
    out.update({"status":"completed","nonzeroThirdSquareTargets":candidates,
                "allNineTargetsChecked":True,"thirdSquarePairingSHA256":m.matrix_hash(pair3)})
    out["parameters"].update({
        "inputFiles":input_files,"targetLabels":list(range(2,11)),
        "actualOriginalTarget":"(sum_a binom(j,a)(-s)^(j-a)*m_a)^2",
        "completeComovingTarget":"n_j^2",
        "allOriginalTargetSubstitutionsVerified":True,
        "all1088PaidSecondCanonicalCorrectionRowsVerified":True,
        "all1700PaidPureSecondCanonicalCorrectionRowsVerified":True,
        "all1088PaidThirdCanonicalCorrectionRowsVerified":True,
        "completeSecondCanonicalCorrectionSHA256":m.matrix_hash(cert),
        "completeThirdCanonicalCorrectionSHA256":m.matrix_hash(cert3),
        "allLaterActualLeadingHashesVerified":True,
        "allPaidLambda2TargetPairingsRemainZero":True,
        "rawNineByTwelveThirdPairingSHA256":m.matrix_hash(raw3),
        "rawNineByTwelveThirdPairing":[[str(raw3[j,k]) for k in range(12)] for j in range(9)],
        "thirdPairingNineBySeven":[[str(pair3[j,k]) for k in range(7)] for j in range(9)],
        "thirdSquarePairingSHA256":m.matrix_hash(pair3),
        "h0SixthPairingNineBySeven":[[str(h0pair3[j,k]) for k in range(7)] for j in range(9)],
        "h0SixthPairingSHA256":m.matrix_hash(h0pair3),
        "nonzeroThirdSquareTargets":candidates,
        "h0ZeroOrder":3,"h0ThirdCoefficient":str(h03),
        "targetSixthCoefficient":"h0[3]*lambda3(n_j^2), because all earlier pairings are zero",
        "fourthQAmbiguityAtLambda3IsOneNormal":True,
        "fifthQAmbiguityChangesOnlyLambda4":True,
        "noFourthFifthRREFRecomputed":True,
        "noLargeNormalFormRecomputed":True,
        "notAMembershipObstructionWithoutActualSixthLift":True,
        "zeroScope":"Zero pairs remain zero for every linear combination of these fixed seven jets and their one-normal Q ambiguity at lambda5; other fifth jets are not covered.",
        "largeDataPersisted":False,
    })

def main():
    ap=argparse.ArgumentParser()
    for key in ("generator","normal-generator","fifth-generator",
                "first-connection-receipt","second-normal-receipt","second-pure-receipt",
                "third-receipt","fourth-receipt","fifth-receipt","out"):
        ap.add_argument("--"+key,required=True)
    ap.add_argument("--remaining-seconds",type=float,default=20)
    a=ap.parse_args()
    require(a.remaining_seconds>0,"Positive shared budget")
    resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
    signal.signal(signal.SIGTERM,stopped)
    a.started=time.monotonic()
    result={"format":"r150-zero-paid-fifth-jets-third-square-readout-v1",
            "status":"started","parameters":{
                "sharedSeconds":a.remaining_seconds,"memoryMiB":512,
                "scriptSHA256":digest(__file__)}}
    exit_code=0
    try:
        run(a,result)
    except TimeoutError as exc:
        result["status"]="paused";result["message"]=str(exc);exit_code=75
    except Exception as exc:
        result["status"]="failed";result["message"]=type(exc).__name__+": "+str(exc)
        exit_code=1
    finally:
        result["elapsedSeconds"]=time.monotonic()-a.started
        result["scriptSHA256"]=digest(__file__)
        write_json(a.out,result)
        print(json.dumps(result,sort_keys=True,separators=(",",":")),flush=True)
    return exit_code

if __name__=="__main__":
    raise SystemExit(main())
