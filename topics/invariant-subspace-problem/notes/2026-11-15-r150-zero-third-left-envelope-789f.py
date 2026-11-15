#!/usr/bin/env python3
"""R150: original finite-zero third-left-jet envelope, after 23 left2 jets.

Rebuild and bind the PAID small first and second charts/corrections.
Only original coefficient s^3 is new.  Ten pure functionals with d-degree<=1
are exact for all s.  The other ten pure and three normal left2 jets give
13 third residual columns, supported on the same 1088 source rows.

A0.T correction uses all135 one-normal+450 two-normal target coordinates.
A1.T Q preserves the second-correction ambiguity.  One new1088x605 rational
RREF gives actual left3 jets.  Its residual rank k gives only
r1+r2+r3 <= 4+k.  We retain the paid r1<=4 and r1+r2<=4;
r1=4 and beta2=0 are NOT assumed.  Higher-normal corrections are not excluded.

All matrices are job-temporary.  Persist only this code and a small receipt.
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

FIRST_SHA256="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
SECOND_SHA256="c8dde441995f3c9b57728a68ec7b29aa56e9abfbbee280fc334961b64e561403"

def require(ok,message):
    if not ok:
        raise AssertionError(message)

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def field(result,key):
    return result.get(key,result.get("parameters",{}).get(key))

def result_at(path):
    obj=json.loads(Path(path).read_text())
    obj=obj.get("result",obj)
    require(obj.get("status")=="completed","Paid input incomplete")
    return obj

def third_coefficients(m,paid_hashes):
    K=m.fmpq_mat(m.ORIGINAL_K)
    J2=m.polynomial_power_kernel(K,2)
    J3=m.polynomial_power_kernel(K,3)
    J3inv=J3.inv()
    require(J3inv*J3==m.fmpq_mat([[int(i==j) for j in range(16)] for i in range(16)]),
            "Original J3 inverse failed")
    p=[[K[i,k] for i in range(6)] for k in range(4)]
    y=[[m.ONE if i==k else m.ZERO for i in range(6)] for k in range(4)]
    maps=[]
    for k in range(4):
        B=m.fmpq_mat([[p[k][i-j] if 0<=i-j<6 else m.ZERO
                       for j in range(11)] for i in range(16)])
        maps.append(J3inv*B*J2)
    hashes={"J2":m.matrix_hash(J2),"J3":m.matrix_hash(J3)}
    for k in range(4):
        hashes["L_y"+str(k)]=m.matrix_hash(maps[k])
    for key in ("J2","J3","L_y0","L_y1","L_y2"):
        require(hashes[key]==paid_hashes[key],"Paid physical map changed: "+key)

    def moment(j):
        return [m.sequence(j+k,comb(j+k,k)) for k in range(4)]
    def add(A,B):
        return [m.add_vectors(A[k],B[k]) for k in range(4)]
    def neg(A):
        return [m.scale_vector(A[k],-1) for k in range(4)]
    def lp(t,v):
        return m.fmpq_mat([[sum((t[i+j+k]*v[k] for k in range(6)),m.ZERO)
                             for j in range(6)] for i in range(6)])
    def contract(t,Q):
        return [sum((t[i+j+k]*Q[j,k] for j in range(6) for k in range(6)),m.ZERO)
                for i in range(6)]

    def F3(jets):
        M=[m.hankel(v) for v in jets]
        KM=[K*X for X in M]
        KMK=[X*K for X in KM]
        tensors=[]; quadratic=[]; tau=[]
        for k in range(4):
            l=m.fmpq_mat(16,1)
            Q=m.fmpq_mat(6,6)
            for r in range(k+1):
                l+=maps[r]*m.column(jets[k-r])
                Q+=M[r]*K*M[k-r]
            tensors.append(m.values(l))
            quadratic.append(Q)
            tau.append(sum((m.trace(KM[r]*KM[k-r]) for r in range(k+1)),m.ZERO))
        N=4*quadratic[3]
        gamma=[m.ZERO]*6
        for r in range(4):
            N+=6*lp(tensors[r],p[3-r])
            gp=m.values(quadratic[r]*m.column(p[3-r]))
            gc=contract(tensors[r],KMK[3-r])
            gamma=[gamma[i]+2*tau[r]*y[3-r][i]+8*gp[i]-12*gc[i]
                   for i in range(6)]
        KNK=K*N*K
        polar=[sum((KNK[i,j] for i in range(6) for j in range(6)
                    if i+j==degree),m.ZERO) for degree in range(11)]
        return polar+gamma

    tangent=[moment(0),moment(1)]
    seed3=[0]*7+[-30720,10144,-1600,160]+[0]*6
    for jets,d in ((tangent[0],0),(tangent[1],1),(neg(tangent[0]),0),
                   (neg(tangent[1]),-1),(add(tangent[0],tangent[1]),1)):
        require(F3(jets)==[m.fmpq(d*d*x) for x in seed3],
                "True all17 finite-zero pure third coefficient failed")
    coeff={}
    for j in range(2,11):
        Z=moment(j); F=F3(Z); Fn=F3(neg(Z))
        modes=[[(F[i]-Fn[i])/2 for i in range(17)]]
        for A in tangent:
            FA,Fs=F3(A),F3(add(A,Z))
            modes.append([Fs[i]-F[i]-FA[i] for i in range(17)])
        coeff[j]=modes
    cols=[(a,degree-a,j) for degree in range(5)
          for a in range(degree+1) for j in range(2,11)]
    rows=[(i,a,degree-a) for i in range(17) for degree in range(4)
          for a in range(degree+1)]
    idx={t:j for j,t in enumerate(cols)}
    P3=m.fmpq_mat(170,135)
    for rr,(i,a,b) in enumerate(rows):
        for j in range(2,11):
            for mode,(da,db) in enumerate(((0,0),(1,0),(0,1))):
                P3[rr,idx[(a+da,b+db,j)]]+=coeff[j][mode][i]

    # A1.T on the second-normal part of the paid second correction.
    # This uses exactly the original paid first physical evaluator.
    first_eval,first_hashes=m.original_jet_evaluator(K)
    for key in first_hashes:
        require(first_hashes[key]==paid_hashes[key],"Paid first evaluator map mismatch")
    first_normal={}
    quad1={}
    for j in range(2,11):
        Z=m.shifted_jet(j)
        F=first_eval(*Z)
        Fn=first_eval(*(m.scale_vector(v,-1) for v in Z))
        first_normal[j]=F
        quad1[(j,j)]=[(F[1][i]+Fn[1][i])/2 for i in range(17)]
    for j in range(2,11):
        for k in range(j+1,11):
            A=m.shifted_jet(j);B=m.shifted_jet(k)
            Fs=first_eval(*(m.add_vectors(A[r],B[r]) for r in range(2)))
            quad1[(j,k)]=[Fs[1][i]-first_normal[j][1][i]-first_normal[k][1][i]
                          for i in range(17)]
    hashes["P3"]=m.matrix_hash(P3)
    return P3,quad1,seed3,hashes

def make_J(m,order,P,linear,quadratic,pure_rows,one_rows,two_index,pairs):
    J=m.fmpq_mat(1088,585)
    for rr,(i,a,b) in enumerate(pure_rows):
        for col in range(135):
            J[rr,col]=P[rr,col]
        for j,k in pairs:
            J[rr,two_index[(a,b,j,k)]]+=quadratic[(j,k)][i]
    for rr,(i,a,b,l) in enumerate(one_rows):
        row=170+rr
        for j in range(2,11):
            x,y=min(j,l),max(j,l)
            for mode,(da,db) in enumerate(((0,0),(1,0),(0,1))):
                J[row,two_index[(a+da,b+db,x,y)]]+=linear[j][mode][order][i]
    return J

def extract_final_kernel(m,M,start,expected_prefix,expected_rank=None):
    R,rank=M.rref()
    piv=m.pivot_columns(R,rank)
    prefix=sum(c<start for c in piv)
    require(prefix==expected_prefix,"Paid leading block rank changed")
    if expected_rank is not None:
        require(rank==expected_rank,"Paid augmented rank changed")
    free=[c for c in range(start,M.ncols()) if c not in set(piv)]
    C=m.fmpq_mat(M.ncols(),len(free))
    for j,c in enumerate(free):
        C[c,j]=1
        for i,p in enumerate(piv):
            C[p,j]=-R[i,c]
    require(m.matrix_zero(M*C),"Full original correction multiplication failed")
    return C,rank,piv,free

def run(a,result):
    require(sha(a.generator)==FIRST_SHA256,"Paid first generator SHA mismatch")
    require(sha(a.normal_generator)==SECOND_SHA256,"Paid second generator SHA mismatch")
    n=module_at("r150_paid_second_normal",a.normal_generator)
    m=module_at("r150_paid_first",a.generator)
    first=n.read_paid_first(a.first_connection_receipt)
    pure=n.read_paid_pure(a.second_pure_receipt)
    second=result_at(a.second_normal_receipt)
    require(field(second,"sumFirstTwoConnectionRanksUpperBound")==4
            and field(second,"firstConnectionExactRankNotAssumed")
            and second["parameters"].get("naturalParameter")=="s"
            and field(second,"all1088ExactSecondLeftJetCorrectionRowsVerified")
            and field(second,"all6188OriginalSourcesRetainedInProof"),
            "Paid finite-zero 23 complete left2 jets are missing")
    second_hashes=second["parameters"]
    pure_hashes=field(pure,"matrixSHA256")

    P,cols,pure_rows,linear,quad0,seed2,physical=n.build_original_coefficients(m)
    P0,P1,P2=P
    Q,r0,pivcols,_=m.nullspace(P0)
    U,rt,pivrows,_=m.nullspace(P0.transpose())
    C=U.transpose()*P1*Q
    V,rc,_,_=m.nullspace(C)
    require(r0==rt==128 and rc==4 and V.ncols()==3,"Paid first-page dimensions")
    for key,M in (("P0",P0),("P1",P1),("Q",Q),("leftKernel",U),
                  ("connecting",C),("annihilators",V)):
        require(m.matrix_hash(M)==first["matrixSha256"][key],
                "Paid first matrix hash mismatch: "+key)
    for key in ("J2","J3","L_y0","L_y1","L_y2"):
        require(physical[key]==second_hashes["originalJetSHA256"][key],
                "Paid second physical coefficient mismatch: "+key)
    require(m.matrix_hash(P2)==second_hashes["originalJetSHA256"]["P2"],
            "Paid P2 matrix changed")
    q0=Q*V
    target=P1*q0
    W=m.fmpq_mat(135,3)
    small=m.submatrix(P0,pivrows,pivcols).solve(
        m.submatrix(target,pivrows,range(3)))
    for i,p in enumerate(pivcols):
        for j in range(3):
            W[p,j]=small[i,j]
    require(P0*W==target,"All170 first corrections failed")
    require(m.matrix_hash(W)==first["matrixSha256"]["originalCorrection"],
            "Paid first correction section changed")

    pairs=[(j,k) for j in range(2,11) for k in range(j,11)]
    two_cols=[(a,degree-a,j,k) for degree in range(4)
              for a in range(degree+1) for j,k in pairs]
    one_rows=[(i,a,degree-a,j) for i in range(17) for degree in range(3)
              for a in range(degree+1) for j in range(2,11)]
    one_index={t:j for j,t in enumerate(cols)}
    two_index={t:135+j for j,t in enumerate(two_cols)}
    J0=make_J(m,0,P0,linear,quad0,pure_rows,one_rows,two_index,pairs)
    J1=m.fmpq_mat(1088,7)
    P1Q=P1*Q
    for i in range(170):
        for j in range(7):
            J1[i,j]=P1Q[i,j]
    R2=m.fmpq_mat(1088,3)
    rp=P2*q0-P1*W
    for i in range(170):
        for j in range(3):
            R2[i,j]=rp[i,j]
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        for j in range(3):
            R2[170+rr,j]=seed2[i]*q0[one_index[(aa,bb+2,l)],j]
    base=m.join_columns(J0,J1)
    M2=m.join_columns(base,R2)
    require(m.matrix_hash(M2)==second_hashes["augmentedMatrixSHA256"],
            "Paid full second augmented matrix changed")
    Ncert,r2,piv2,free2=extract_final_kernel(m,M2,592,582,582)
    require(free2==[592,593,594],"Paid second leading identity changed")
    require(sum(c<585 for c in piv2)==578,"Paid A0 correction rank changed")
    require(m.matrix_hash(Ncert)==second_hashes["completeCorrectionSHA256"],
            "Paid complete second correction section changed")
    Hnormal=m.submatrix(Ncert,range(585),range(3))
    Bnormal=m.submatrix(Ncert,range(585,592),range(3))
    del M2,Ncert

    pure_cols=[(aa,degree-aa+2) for degree in range(4) for aa in range(degree+1)]
    pure_index={t:j for j,t in enumerate(pure_cols)}
    S2=m.fmpq_mat(170,10)
    for rr,(i,aa,bb) in enumerate(pure_rows):
        S2[rr,pure_index[(aa,bb+2)]]=seed2[i]
    require(m.matrix_hash(S2)==pure_hashes["S"],"Paid pure second seed matrix changed")
    small_aug=m.join_columns(P0,P1Q)
    _,rsmall,acols,_=m.nullspace(small_aug)
    _,rsmallT,arows,_=m.nullspace(small_aug.transpose())
    require(rsmall==rsmallT==132,"Paid pure second correction rank changed")
    Pcert=m.fmpq_mat(142,10)
    unit=m.submatrix(small_aug,arows,acols)
    sol=unit.solve(m.submatrix(S2,arows,range(10)))
    for i,col in enumerate(acols):
        for j in range(10):
            Pcert[col,j]=sol[i,j]
    require(small_aug*Pcert==S2,"All1700 pure second corrections failed")
    require(m.matrix_hash(Pcert)==pure_hashes["completeOriginalCorrection"],
            "Paid pure second correction section changed")
    Wpure=m.submatrix(Pcert,range(135),range(10))
    Bpure=m.submatrix(Pcert,range(135,142),range(10))

    lam1=m.join_columns(-Q*Bpure,-W+Q*Bnormal)
    lam2=m.fmpq_mat(585,13)
    for i in range(135):
        for j in range(10):
            lam2[i,j]=-Wpure[i,j]
    for i in range(585):
        for j in range(3):
            lam2[i,10+j]=Hnormal[i,j]
    require(lam1.ncols()==13,"All13 fixed left2 jets retained")
    result["parameters"].update({
        "allPaidFirstHashesVerified":True,
        "allPaidSecondHashesVerified":True,
        "all1700PureSecondCorrectionRowsVerified":True,
        "all1088NormalSecondCorrectionRowsVerified":True,
        "paidSecondNormalCanonicalSectionRetained":True,
        "paidSecondPureCanonicalSectionRetained":True,
        "fixedLeft2FirstCoefficientSHA256":m.matrix_hash(lam1),
        "fixedLeft2SecondCoefficientSHA256":m.matrix_hash(lam2),
    })

    P3,quad1,seed3,third_hashes=third_coefficients(m,second_hashes["originalJetSHA256"])
    A1low=make_J(m,1,P1,linear,quad1,pure_rows,one_rows,two_index,pairs)
    R3=m.fmpq_mat(1088,13)
    np3=P3*q0
    for row,(i,aa,bb) in enumerate(pure_rows):
        R3[row,pure_index[(aa,bb+2)]]=seed3[i]
        for j in range(3):
            R3[row,10+j]=np3[row,j]
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        row=170+rr
        target=one_index[(aa,bb+2,l)]
        for j in range(3):
            R3[row,10+j]=seed3[i]*q0[target,j]
    # A2.T lambda1, including its true pure F2 term on one-normal sources.
    term=P2*lam1
    for row in range(170):
        for j in range(13):
            R3[row,j]+=term[row,j]
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        target=one_index[(aa,bb+2,l)]
        for j in range(13):
            R3[170+rr,j]+=seed2[i]*lam1[target,j]
    # A1.T lambda2 keeps all second-normal output coordinates.
    R3+=A1low*lam2
    M3=m.join_columns(base,R3)
    require(M3.nrows()==1088 and M3.ncols()==605,"Third matrix dimensions")
    result["parameters"].update({
        "originalThirdJetSHA256":third_hashes,
        "all17PureThirdCoefficientsVerified":True,
        "pureThirdSeedEquationOrder":seed3,
        "A1TransposeLowNormalSHA256":m.matrix_hash(A1low),
        "all13ThirdResidualColumnsSHA256":m.matrix_hash(R3),
        "thirdAugmentedMatrixSHA256":m.matrix_hash(M3),
    })

    cert,rank,piv,free=extract_final_kernel(m,M3,592,582)
    k=rank-582
    require(0<=k<=13 and len(free)==13-k,"Third residual-rank identity failed")
    require(sum(c<585 for c in piv)==578,"Original A0 prefix rank changed")
    leading=m.submatrix(cert,range(592,605),range(len(free)))
    for j,c in enumerate(free):
        for l,d in enumerate(free):
            require(leading[d-592,j]==(1 if j==l else 0),
                    "Third leading annihilator independence failed")
    first_three_upper=4+k
    dmax=max(34,44-k)
    dsub=max(31,40-k)
    result.update({
        "status":"completed",
        "thirdConnectionEnvelopeRank":k,
        "sumFirstThreeConnectionRanksUpperBound":first_three_upper,
        "fullThirdConnectionRankConditionalUpperBound":"r3 <= 4+k-r1-r2",
        "firstConnectionExactRankNotAssumed":True,
        "fullZeroMaximalMinorOrderLowerBound":dmax,
        "fullZeroSubmaximalMinorOrderLowerBound":dsub,
    })
    result["parameters"].update({
        "baseRank":582,"augmentedRank":rank,
        "thirdConnectionEnvelopeRank":k,
        "sumFirstThreeConnectionRanksUpperBound":first_three_upper,
        "fullThirdConnectionRankConditionalUpperBound":"r3 <= 4+k-r1-r2",
        "firstConnectionExactRankNotAssumed":True,
        "fullZeroMaximalMinorOrderLowerBound":dmax,
        "fullZeroSubmaximalMinorOrderLowerBound":dsub,
        "leadingAnnihilatorsInPaidThirteenBasis":
            [[str(leading[i,j]) for i in range(13)] for j in range(len(free))],
        "leadingFreeIndices":[c-592 for c in free],
        "all1088ThirdLeftJetCorrectionRowsVerified":True,
        "all5100RemainingOriginalSourceRowsZeroByNormalDegree":True,
        "all6188OriginalSourcesRetainedInProof":True,
        "tenOtherPureLeftFunctionalsExactForAllParameters":True,
        "completeThirdCorrectionSHA256":m.matrix_hash(cert),
        "leadingAnnihilatorSHA256":m.matrix_hash(leading),
        "notAFullThirdConnectionLowerBound":True,
        "higherNormalTargetCorrectionsNotExcluded":True,
        "smallSourceRelationsAssumedToLift":False,
        "oldNormalFormsRecomputed":False,
        "largeMacaulayMatrixConstructed":False,
        "largeRecomputableDataPersisted":False,
    })

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--generator",required=True)
    p.add_argument("--normal-generator",required=True)
    p.add_argument("--first-connection-receipt",required=True)
    p.add_argument("--second-pure-receipt",required=True)
    p.add_argument("--second-normal-receipt",required=True)
    p.add_argument("--out",required=True)
    p.add_argument("--remaining-seconds",type=float,default=30.0)
    a=p.parse_args()
    require(a.remaining_seconds>0,"Positive actual shared time required")
    resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
    started=time.monotonic()
    result={
        "format":"r150-original-zero-third-left-envelope-v1",
        "status":"started","arithmetic":"exact rational python-flint",
        "scriptSHA256":sha(__file__),
        "parameters":{
            "naturalParameter":"s",
            "chart":"finite zero in original s and co-moving moments",
            "generatorSHA256":sha(a.generator),
            "normalGeneratorSHA256":sha(a.normal_generator),
            "firstReceiptSHA256":sha(a.first_connection_receipt),
            "secondPureReceiptSHA256":sha(a.second_pure_receipt),
            "secondNormalReceiptSHA256":sha(a.second_normal_receipt),
            "sharedSeconds":a.remaining_seconds,"memoryMiB":512,
            "matrixShape":[1088,605],"largestMatrixEntryCount":1088*605,
            "leadingOrder":"ten d^2*c^a*d^b pure functionals, then three paid normal jets",
            "pureOrder":"degree=0..3;a=0..degree;monomial c^a*d^(degree-a+2)",
            "sourceMultiplierTransport":
                "m_j=sum_(k<=j)binom(j,k)s^(j-k)n_k; invertible on all degree<=3 monomials",
            "targetLeftTransport":"A_new=T A_old V implies lambda_old=T^T lambda_new",
        },
    }
    def alarm(signum,frame):
        raise TimeoutError("Shared original third-jet budget exhausted")
    signal.signal(signal.SIGALRM,alarm)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    try:
        run(a,result)
    except BaseException as exc:
        result["status"]="incomplete"
        result["error"]=type(exc).__name__+": "+str(exc)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        result["elapsedSeconds"]=time.monotonic()-started
        path=Path(a.out);path.parent.mkdir(parents=True,exist_ok=True)
        raw=json.dumps(result,sort_keys=True,indent=2).encode("utf-8")
        require(len(raw)<100000,"Small receipt contract exceeded")
        temp=path.with_name(path.name+".tmp");temp.write_bytes(raw);os.replace(temp,path)
        print(json.dumps({
            "status":result["status"],"receipt":str(path),
            "receiptBytes":len(raw),"receiptSHA256":hashlib.sha256(raw).hexdigest(),
            "elapsedSeconds":result["elapsedSeconds"],
            "thirdConnectionEnvelopeRank":result.get("thirdConnectionEnvelopeRank"),
            "sumFirstThreeConnectionRanksUpperBound":
                result.get("sumFirstThreeConnectionRanksUpperBound"),
            "fullZeroMaximalMinorOrderLowerBound":
                result.get("fullZeroMaximalMinorOrderLowerBound"),
        }),flush=True)

if __name__=="__main__":
    main()
