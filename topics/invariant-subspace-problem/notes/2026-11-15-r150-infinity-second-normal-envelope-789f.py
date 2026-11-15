#!/usr/bin/env python3
"""R150: remaining-normal second-connection envelope at the true infinity.

Only the original parameter coefficient u^2 is new.  No old NF/Dixon is run.
The complete 17 physical equations are expanded after the same reversal and
co-moving moments as the paid first-connection generator.

There are 170 pure and 918 one-normal source rows.  Corrections use all 135
one-normal and 450 two-normal target coordinates, plus all seven constant
normal cokernel ambiguities in the first correction.  One exact RREF of the
1088 x 595 augmented matrix provides genuine second-order LEFT jets.

Its residual rank is an UPPER bound for the full second connection.  A
positive residual is not a lower bound: corrections using higher normal
target degree have deliberately not been ruled out.

Only code, parameters and a small receipt persist.  All matrices are temporary.
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

GENERATOR_SHA256 = "2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"

def require(ok, message):
    if not ok:
        raise AssertionError(message)

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def read_result(path):
    obj = json.loads(Path(path).read_text())
    result = obj.get("result", obj)
    require(result.get("status") == "completed", "Paid input is not complete")
    return result

def read_paid_first(path):
    result = read_result(path)
    charts = result.get("parameters", result).get("charts", [])
    charts = [c for c in charts if c.get("chart") == "infinity"]
    require(len(charts) == 1, "Expected the paid infinity chart")
    c = charts[0]
    require(c["P0Rank"] == 128 and c["transverseEnvelopeConnectionRank"] == 4,
            "Paid first-page rank mismatch")
    require(c["all170ExactCorrectionRowsVerified"]
            and c["allP0NullspaceIdentitiesVerified"],
            "Paid first-page complete identities missing")
    return c

def read_paid_pure(path):
    r = read_result(path)
    p = r.get("parameters", {})
    def field(key):
        return r.get(key, p.get(key))
    require(field("pureConnectionEnvelopeRank") == 0,
            "Paid infinity pure second envelope is not zero")
    require(field("all170ExactSecondLeftJetCorrectionRowsVerified")
            and field("all17PureSecondJetCoefficientsVerified")
            and field("allSmallPaidFirstPageHashesVerified"),
            "Paid pure second-page full identities missing")
    require(p.get("naturalParameter") == "u=1/s",
            "Second-pure input is not the natural infinity chart")
    return r

def load_generator(path):
    spec = importlib.util.spec_from_file_location("r150_paid_first_generator", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def build_second_evaluator(m, K):
    J2 = m.polynomial_power_kernel(K, 2)
    J3 = m.polynomial_power_kernel(K, 3)
    invJ3 = J3.inv()
    identity = m.fmpq_mat([[int(i == j) for j in range(16)] for i in range(16)])
    require(invJ3 * J3 == identity, "Original J3 inverse failed")
    require(J2.det() != 0, "Original J2 became singular")
    pp = [[K[i, k] for i in range(6)] for k in range(3)]
    yy = [[m.ONE if i == k else m.ZERO for i in range(6)] for k in range(3)]
    maps = []
    for k in range(3):
        B = m.fmpq_mat([[pp[k][i-j] if 0 <= i-j < 6 else m.ZERO
                         for j in range(11)] for i in range(16)])
        maps.append(invJ3 * B * J2)

    def lp(tensor, vector):
        return m.fmpq_mat([[sum((tensor[i+j+k]*vector[k] for k in range(6)),
                                m.ZERO)
                             for j in range(6)] for i in range(6)])

    def contract(tensor, Q):
        return [sum((tensor[i+j+k]*Q[j,k] for j in range(6) for k in range(6)),
                    m.ZERO) for i in range(6)]

    def polar(N):
        KNK = K*N*K
        return [sum((KNK[i,j] for i in range(6) for j in range(6)
                     if i+j == degree), m.ZERO) for degree in range(11)]

    def evaluate(moment_jets):
        require(len(moment_jets) == 3, "Three parameter coefficients required")
        M = [m.hankel(v) for v in moment_jets]
        KM = [K*X for X in M]
        KMK = [X*K for X in KM]
        tensors = []
        MKM = []
        tau = []
        for k in range(3):
            tensor = m.fmpq_mat(16, 1)
            quadratic = m.fmpq_mat(6, 6)
            for r in range(k+1):
                tensor += maps[r] * m.column(moment_jets[k-r])
                quadratic += M[r]*K*M[k-r]
            tensors.append(m.values(tensor))
            MKM.append(quadratic)
            tau.append(sum((m.trace(KM[r]*KM[k-r]) for r in range(k+1)), m.ZERO))
        answer = []
        for k in range(3):
            N = 4*MKM[k]
            gamma = [m.ZERO]*6
            for r in range(k+1):
                N += 6*lp(tensors[r], pp[k-r])
                gp = m.values(MKM[r]*m.column(pp[k-r]))
                gc = contract(tensors[r], KMK[k-r])
                gamma = [gamma[i] + 2*tau[r]*yy[k-r][i]
                         + 8*gp[i] - 12*gc[i] for i in range(6)]
            answer.append(polar(N) + gamma)
        return answer

    hashes = {"J2":m.matrix_hash(J2), "J3":m.matrix_hash(J3),
              "L_y0":m.matrix_hash(maps[0]), "L_y1":m.matrix_hash(maps[1]),
              "L_y2":m.matrix_hash(maps[2])}
    return evaluate, hashes

def build_original_coefficients(m):
    K = m.fmpq_mat([[m.ORIGINAL_K[5-i][5-j] for j in range(6)] for i in range(6)])
    evaluate, hashes = build_second_evaluator(m, K)
    def moment(j):
        return [m.sequence(j+k, comb(j+k,k)) for k in range(3)]
    def add(A, B):
        return [m.add_vectors(A[k], B[k]) for k in range(3)]
    def neg(A):
        return [m.scale_vector(A[k], -1) for k in range(3)]
    tangent = [moment(0), moment(1)]
    plane_cases = [(tangent[0],0), (tangent[1],1),
                   (neg(tangent[0]),0), (neg(tangent[1]),-1),
                   (add(tangent[0],tangent[1]),1)]
    seed = [0]*8+[-8,-16,-8]+[0]*6
    for jets, d in plane_cases:
        F = evaluate(jets)
        require(all(not x for order in F[:2] for x in order),
                "Full co-moving tangent constant/first coefficient failed")
        require(F[2] == [m.fmpq(d*d*x) for x in seed],
                "Full17 true pure second coefficient failed")
    normal = {}
    Fnormal = {}
    quad = {}
    for j in range(2,11):
        Z = moment(j)
        F = evaluate(Z)
        Fn = evaluate(neg(Z))
        Fnormal[j] = F
        linear = [[(F[k][i]-Fn[k][i])/2 for i in range(17)] for k in range(3)]
        modes = [linear]
        for A in tangent:
            FA, Fplus = evaluate(A), evaluate(add(A,Z))
            # At order2, FA is not zero; retain the subtraction.
            modes.append([[Fplus[k][i]-F[k][i]-FA[k][i]
                           for i in range(17)] for k in range(3)])
        normal[j] = modes
        quad[(j,j)] = [(F[0][i]+Fn[0][i])/2 for i in range(17)]
    for j in range(2,11):
        for k in range(j+1,11):
            Fsum = evaluate(add(moment(j),moment(k)))
            quad[(j,k)] = [Fsum[0][i]-Fnormal[j][0][i]-Fnormal[k][0][i]
                           for i in range(17)]
    cols = [(a,degree-a,j) for degree in range(5)
            for a in range(degree+1) for j in range(2,11)]
    rows = [(i,a,degree-a) for i in range(17) for degree in range(4)
            for a in range(degree+1)]
    index = {t:j for j,t in enumerate(cols)}
    P = [m.fmpq_mat(170,135) for _ in range(3)]
    for row,(i,a,b) in enumerate(rows):
        for j in range(2,11):
            for mode,(da,db) in enumerate(((0,0),(1,0),(0,1))):
                col = index[(a+da,b+db,j)]
                for k in range(3):
                    P[k][row,col] += normal[j][mode][k][i]
    return P, cols, rows, normal, quad, seed, hashes

def run(a, result):
    require(sha(a.generator) == GENERATOR_SHA256, "Paid original generator SHA mismatch")
    paid = read_paid_first(a.first_connection_receipt)
    read_paid_pure(a.second_pure_receipt)
    m = load_generator(a.generator)
    P, cols, pure_rows, linear, quad, seed, origin_hashes = build_original_coefficients(m)
    P0,P1,P2 = P
    Q,r0,pivcols,_ = m.nullspace(P0)
    U,rt,pivrows,_ = m.nullspace(P0.transpose())
    C = U.transpose()*P1*Q
    V,rc,_,_ = m.nullspace(C)
    require(r0 == rt == 128 and rc == 4 and V.ncols() == 3,
            "Paid complete first-page dimensions changed")
    for name,M in (("P0",P0),("P1",P1),("Q",Q),
                   ("leftKernel",U),("connecting",C),("annihilators",V)):
        require(m.matrix_hash(M) == paid["matrixSha256"][name],
                "Paid first-page exact hash mismatch: "+name)
    for name in ("J2","J3","L_y0","L_y1"):
        require(origin_hashes[name] == paid["matrixSha256"][name],
                "Original physical coefficient hash mismatch: "+name)

    # q0 = QV and lambda1 = -W are the paid full first left jets.
    q0 = Q*V
    target = P1*q0
    unit = m.submatrix(P0,pivrows,pivcols)
    small = unit.solve(m.submatrix(target,pivrows,range(3)))
    W = m.fmpq_mat(135,3)
    for i,c in enumerate(pivcols):
        for j in range(3):
            W[c,j] = small[i,j]
    require(P0*W == target, "All170 paid first left-jet correction rows failed")
    require(m.matrix_hash(W) == paid["matrixSha256"]["originalCorrection"],
            "Paid first left-jet correction section changed")

    pairs = [(j,k) for j in range(2,11) for k in range(j,11)]
    two_cols = [(a,degree-a,j,k) for degree in range(4)
                for a in range(degree+1) for j,k in pairs]
    one_rows = [(i,a,degree-a,j) for i in range(17) for degree in range(3)
                for a in range(degree+1) for j in range(2,11)]
    require(len(cols)==135 and len(two_cols)==450 and len(one_rows)==918,
            "Complete low-normal dimensions failed")
    one_index = {t:j for j,t in enumerate(cols)}
    two_index = {t:135+j for j,t in enumerate(two_cols)}

    # Columns 0:585 are the true A0.T correction map.
    # Columns 585:592 are true A1.T Q first-correction ambiguities.
    # Columns 592:595 are A2.T q0 - A1.T W.
    M = m.fmpq_mat(1088,595)
    P1Q = P1*Q
    Rpure = P2*q0-P1*W
    for row,(i,a0,b0) in enumerate(pure_rows):
        for col in range(135):
            M[row,col] = P0[row,col]
        for j,k in pairs:
            M[row,two_index[(a0,b0,j,k)]] += quad[(j,k)][i]
        for j in range(7):
            M[row,585+j] = P1Q[row,j]
        for j in range(3):
            M[row,592+j] = Rpure[row,j]

    for rr,(i,a0,b0,l) in enumerate(one_rows):
        row = 170+rr
        for j in range(2,11):
            x,y = min(j,l),max(j,l)
            for mode,(da,db) in enumerate(((0,0),(1,0),(0,1))):
                M[row,two_index[(a0+da,b0+db,x,y)]] += linear[j][mode][0][i]
        # F0/F1|plane=0.  Only F2|plane times this one-normal source remains.
        target_col = one_index[(a0,b0+2,l)]
        for j in range(3):
            M[row,592+j] = seed[i]*q0[target_col,j]

    result["parameters"].update({
        "sourceRows":{"pure":170,"oneNormal":918,"omittedByNormalDegree":5100},
        "targetCorrections":{"oneNormal":135,"twoNormal":450},
        "matrixShape":[1088,595],
        "columnBlocks":{"A0Transpose":[0,585],"A1TransposeQ":[585,592],
                        "threeSecondResiduals":[592,595]},
        "originalJetSHA256":dict(origin_hashes,P2=m.matrix_hash(P2)),
        "augmentedMatrixSHA256":m.matrix_hash(M),
        "allPaidFirstPageHashesVerified":True,
        "all170PaidFirstLeftJetCorrectionsVerified":True,
        "all17OriginalPureSecondCoefficientsVerified":True,
    })

    # One exact rational elimination, with the paid leading ranks checked.
    R,rank = M.rref()
    piv = m.pivot_columns(R,rank)
    rA0 = sum(c<585 for c in piv)
    rbase = sum(c<592 for c in piv)
    require(rA0 == 578, "Complete low-normal A0.T rank differs from paid cokernel")
    require(rbase == 582, "Complete first ambiguity rank differs from paid beta1")
    residual_rank = rank-rbase
    require(0 <= residual_rank <= 3, "Invalid normal second residual rank")
    final_free = [c for c in range(592,595) if c not in set(piv)]
    require(len(final_free) == 3-residual_rank, "Final leading kernel dimension")

    certificates = m.fmpq_mat(595,len(final_free))
    for j,c in enumerate(final_free):
        certificates[c,j] = 1
        for i,p in enumerate(piv):
            certificates[p,j] = -R[i,c]
    require(m.matrix_zero(M*certificates),
            "All1088 true second left-jet correction rows failed")
    leading = m.submatrix(certificates,range(592,595),range(len(final_free)))
    for j,c in enumerate(final_free):
        for k,d in enumerate(final_free):
            require(leading[d-592,j] == (1 if j==k else 0),
                    "Leading normal annihilator independence failed")

    # No target-coordinate or source-lift restriction is promoted to equality.
    result.update({
        "status":"completed",
        "normalSecondConnectionEnvelopeRank":residual_rank,
        "fullSecondConnectionRankUpperBound":residual_rank,
        "fullInfinityMaximalMinorOrderLowerBound":34-residual_rank,
        "fullInfinitySubmaximalMinorOrderLowerBound":31-residual_rank,
    })
    result["parameters"].update({
        "A0TransposeLowNormalRank":rA0,
        "completeFirstAmbiguityRank":rbase,
        "augmentedRank":rank,
        "normalSecondConnectionEnvelopeRank":residual_rank,
        "normalLeadingAnnihilatorsInPaidThreeBasis":
            [[str(leading[i,j]) for i in range(3)] for j in range(len(final_free))],
        "normalLeadingFreeIndices":[c-592 for c in final_free],
        "all1088ExactSecondLeftJetCorrectionRowsVerified":True,
        "all5100RemainingOriginalSourceRowsZeroByNormalDegree":True,
        "all6188OriginalSourcesRetainedInProof":True,
        "completeCorrectionSHA256":m.matrix_hash(certificates),
        "leadingAnnihilatorSHA256":m.matrix_hash(leading),
        "fullSecondConnectionRankUpperBound":residual_rank,
        "fullInfinityMaximalMinorOrderLowerBound":34-residual_rank,
        "fullInfinitySubmaximalMinorOrderLowerBound":31-residual_rank,
        "notAFullSecondConnectionLowerBound":True,
        "higherNormalTargetCorrectionsNotExcluded":True,
        "smallSourceRelationsAssumedToLift":False,
        "oldNormalFormsRecomputed":False,
        "largeMacaulayMatrixConstructed":False,
        "largeRecomputableDataPersisted":False,
    })

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--generator",required=True)
    p.add_argument("--first-connection-receipt",required=True)
    p.add_argument("--second-pure-receipt",required=True)
    p.add_argument("--out",required=True)
    p.add_argument("--remaining-seconds",type=float,default=30.0)
    a=p.parse_args()
    require(a.remaining_seconds>0,"Positive actual shared time required")
    resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
    started=time.monotonic()
    result={
        "format":"r150-original-infinity-second-normal-envelope-v1",
        "status":"started",
        "arithmetic":"exact rational python-flint",
        "scriptSHA256":sha(__file__),
        "parameters":{
            "naturalParameter":"u=1/s",
            "chart":"infinity after exact reversal and co-moving moments",
            "generatorSHA256":sha(a.generator),
            "paidFirstReceiptSHA256":sha(a.first_connection_receipt),
            "paidSecondPureReceiptSHA256":sha(a.second_pure_receipt),
            "sharedSeconds":a.remaining_seconds,
            "memoryMiB":512,
            "largestMatrixEntryCount":1088*595,
            "equationOrder":"N0..N10,Gamma0..Gamma5",
            "oneTargetOrder":"degree=0..4;a=0..degree;j=2..10",
            "twoTargetOrder":"degree=0..3;a=0..degree;2<=j<=k<=10",
            "pureSourceOrder":"eq=0..16;degree=0..3;a=0..degree",
            "oneSourceOrder":"eq=0..16;degree=0..2;a=0..degree;j=2..10",
        },
    }
    def alarm(signum,frame):
        raise TimeoutError("Shared original second-normal budget exhausted")
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
        path=Path(a.out)
        path.parent.mkdir(parents=True,exist_ok=True)
        raw=json.dumps(result,sort_keys=True,indent=2).encode("utf-8")
        require(len(raw)<100000,"Small receipt contract exceeded")
        temp=path.with_name(path.name+".tmp")
        temp.write_bytes(raw)
        os.replace(temp,path)
        print(json.dumps({
            "status":result["status"],"receipt":str(path),
            "receiptBytes":len(raw),"receiptSHA256":hashlib.sha256(raw).hexdigest(),
            "elapsedSeconds":result["elapsedSeconds"],
            "normalSecondConnectionEnvelopeRank":
                result.get("normalSecondConnectionEnvelopeRank"),
            "fullSecondConnectionRankUpperBound":
                result.get("fullSecondConnectionRankUpperBound"),
        }),flush=True)

if __name__=="__main__":
    main()
