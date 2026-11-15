#!/usr/bin/env python3
"""Pair the actual finite-zero fifth-left jets with the nine ORIGINAL targets.

Original t_j=(sum_a binom(j,a)(-s)^(j-a)m_a)^2 becomes n_j^2
under the full co-moving substitution.  Since h0 has zero order3 and every
paid lambda0/lambda1 has normal degree<=1, the only coefficient below s^6 is
h0[3] * lambda2(n_j^2) at s^5.

Rebuild only the paid second-normal canonical 1088x595 correction, then use
the actual third/fourth/fifth leading matrices in the small receipts.
Later Q ambiguities are one-normal and do not change quadratic coordinates.
No third/fourth/fifth elimination, no old NF, no new large Macaulay matrix.
A nonzero result excludes membership in the fixed full6188 Q[s] module.
A zero result is only no obstruction from these particular seven jets.
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

    # Full original target substitution.  Linear binomial inversion is checked
    # coefficientwise; its square is exactly the old native two-index formula.
    for j in range(2,11):
        inv=[sum(comb(j,aa)*(-1)**(j-aa)*comb(aa,rr)
                 for aa in range(rr,j+1)) for rr in range(j+1)]
        require(inv==[0]*j+[1],"Original target binomial substitution failed")
        for aa in range(j+1):
            for bb in range(aa,j+1):
                native=comb(j,aa)*comb(j,bb)*(1 if aa==bb else 2)*(-1)**(2*j-aa-bb)
                square=comb(j,aa)*(-1)**(j-aa)*comb(j,bb)*(-1)**(j-bb)
                square*=1 if aa==bb else 2
                require(native==square,"Original native target coefficient formula")

    # Pure leading families have lambda2 supported only in one-normal targets.
    # Every later Q addition is also one-normal.  Thus only these exact nine
    # rows of H enter the quadratic-target coefficient for the actual fifth jets.
    raw=m.fmpq_mat([[H[two_index[(0,0,j,j)],k] for k in range(3)]
                    for j in range(2,11)])
    normlead=m.submatrix(leading,range(10,13),range(7))
    pair=raw*normlead
    nonzero=[j+2 for j in range(9)
             if any(pair[j,k] for k in range(7))]
    matrix=[[str(pair[j,k]) for k in range(7)] for j in range(9)]
    witnesses=[]
    for j in range(9):
        for k in range(7):
            if pair[j,k]:
                witnesses.append({"target":j+2,"paidFifthJet":k,
                                  "lambda2SquareCoefficient":str(pair[j,k])})
                break
    h03=-2*(-8)**2*864**2*9600
    require(h03==-917294284800,"Original integer h0 third coefficient")
    input_files={
        key:{"bytes":Path(path).stat().st_size,"sha256":digest(path)}
        for key,path in (
            ("firstGenerator",a.generator),("secondGenerator",a.normal_generator),
            ("fifthGenerator",a.fifth_generator),
            ("firstReceipt",a.first_connection_receipt),
            ("secondReceipt",a.second_normal_receipt),
            ("thirdReceipt",a.third_receipt),("fourthReceipt",a.fourth_receipt),
            ("fifthReceipt",a.fifth_receipt))}
    out.update({"status":"completed","obstructedTargets":nonzero,
                "allNineTargetsChecked":True,"pairingSHA256":m.matrix_hash(pair)})
    out["parameters"].update({
        "inputFiles":input_files,"targetLabels":list(range(2,11)),
        "actualOriginalTarget":"(sum_a binom(j,a)(-s)^(j-a)*m_a)^2",
        "completeComovingTarget":"n_j^2",
        "allOriginalTargetSubstitutionsVerified":True,
        "all1088PaidSecondCanonicalCorrectionRowsVerified":True,
        "completeSecondCanonicalCorrectionSHA256":m.matrix_hash(cert),
        "allLaterActualLeadingHashesVerified":True,
        "leadingThirteenBySevenSHA256":m.matrix_hash(leading),
        "rawNineByThreeSecondPairingSHA256":m.matrix_hash(raw),
        "rawNineByThreeSecondPairing":[[str(raw[j,k]) for k in range(3)] for j in range(9)],
        "pairingNineBySeven":matrix,"pairingSHA256":m.matrix_hash(pair),
        "obstructedTargets":nonzero,"witnesses":witnesses,
        "h0ZeroOrder":3,
        "h0Definition":"s^3*(s-2)*Fplus^2*Fminus^2*E8",
        "h0ThirdCoefficient":str(h03),
        "originalFactorCoefficientsAscending":{"Fplus":[-8,32,-25,5],
            "Fminus":[864,864,135,5],
            "E8":[9600,-25472,-3392,15936,-2888,-936,153,50,5]},
        "targetProductThroughOrderFive":"s^5*h0[3]*lambda2(n_j^2) modulo s^6",
        "lambda0AndLambda1PairingsZeroByNormalDegree":True,
        "laterQAmbiguitiesDoNotAffectQuadraticTargetCoordinates":True,
        "sourceRowUnitScalingsDoNotScaleOriginalTarget":True,
        "full6188ModuleUsed":True,
        "noThirdFourthFifthRREFRecomputed":True,
        "noLargeNormalFormRecomputed":True,
        "noIdealDegreeBeyondOriginalSourceModuleClaimed":True,
        "negativeScope":"Nonzero target columns exclude membership in the fixed complete6188 Q[s] Macaulay source module.",
        "zeroScope":"Zero columns give no obstruction from these particular seven paid fifth jets; no membership claim.",
        "largeDataPersisted":False,
    })

def main():
    ap=argparse.ArgumentParser()
    for key in ("generator","normal-generator","fifth-generator",
                "first-connection-receipt","second-normal-receipt",
                "third-receipt","fourth-receipt","fifth-receipt","out"):
        ap.add_argument("--"+key,required=True)
    ap.add_argument("--remaining-seconds",type=float,default=20)
    a=ap.parse_args()
    require(a.remaining_seconds>0,"Positive shared budget")
    resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
    signal.signal(signal.SIGTERM,stopped)
    a.started=time.monotonic()
    result={"format":"r150-zero-paid-fifth-jets-original-target-pairing-v1",
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
