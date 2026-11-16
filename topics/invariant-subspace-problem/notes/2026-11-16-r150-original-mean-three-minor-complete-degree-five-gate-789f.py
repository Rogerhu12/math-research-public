#!/usr/bin/env python3
"""Complete 3-minor Macaulay gate for the four original mean matrices.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Keep all80 original 3x3 minors of M(y)=[T1y,...,T4y], every multiplier
in degrees3,4,5, and every homogeneous output monomial.  A full finite
field row rank proves a nonzero fixed E source minor and hence a true
power of the mean ideal in I3(M).  A deficient profile proves no E
upper bound and is retained only as a bounded field result.
"""
import argparse,gzip,hashlib,itertools,json,os,resource,signal,sys,time
from pathlib import Path
from flint import fmpq,nmod_mat

FORMAT="r150-original-mean-three-minor-complete-degree-five-gate-v1"
PARENT={"bytes":2208219,"sha256":"1928d85c9cb6a40cbbf038e39d65bd0b72dffe900d0da6c600070966444acc12",
"logicalSha256":"7c37ad0846331a5ad9bf96d7c0086e2c65d65fe8831081dc34c778365592197d",
"binding":"2c120983a234d63f52e19d0f81a8f486b3d5dad5ca010f1ad74ebe9c7045e7f0"}
MATCHED=[52565262336,6080833024,-43931504,3725]
PRIME=127;ROOT=100
def need(b,s):
    if not b:raise ValueError(s)
def sha(x):return hashlib.sha256(x).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def key(t):
    e=[0]*6
    for i in t:e[i]+=1
    return tuple(e)
def mons(d):return [key(t) for t in itertools.combinations_with_replacement(range(6),d)]
def save_json(p,x):
    b=json.dumps(x,sort_keys=True,indent=2).encode();t=p.with_name(p.name+".tmp");t.write_bytes(b);os.replace(t,p)
    return {"path":p.name,"bytes":len(b),"sha256":sha(b)}
def save_gz(p,x):
    b=canon(x);z=gzip.compress(b,compresslevel=1,mtime=0);t=p.with_name(p.name+".tmp");t.write_bytes(z);os.replace(t,p)
    return {"path":p.name,"bytes":len(z),"sha256":sha(z),"logicalBytes":len(b),"logicalSha256":sha(b)}
def coeff(v):
    ans=0
    for j,s in enumerate(v):
        q=fmpq(s);den=int(q.denom()%PRIME);need(den!=0,"every actual E coefficient denominator is a chosen-prime unit")
        ans=(ans+int(q.numer()%PRIME)*pow(den,-1,PRIME)*pow(ROOT,j,PRIME))%PRIME
    return ans
def matrix_rows(A):return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--mean-out",required=True);ap.add_argument("--out",required=True)
    ap.add_argument("--seconds",type=float,default=120);ap.add_argument("--memory-mib",type=int,default=1024);a=ap.parse_args()
    need(0<a.seconds<=300 and 512<=a.memory_mib<=4096,"bounded complete 3-minor gate")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2);out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    ss=sha(Path(__file__).read_bytes());binding=sha(canon({"format":FORMAT,"sourceSha256":ss,"parent":PARENT,"prime":PRIME,"root":ROOT,"degrees":[3,4,5]}))
    rec={"format":FORMAT,"binding":binding,"sourceSha256":ss,"parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib}};start=time.monotonic();code=1
    def timeout(sig,fr):raise TimeoutError("bounded complete original mean minor gate")
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds)
    try:
        path=Path(a.mean_out)/"complete-original-four-mean-quadratic-matrices.json.gz"
        z=path.read_bytes();need(len(z)==PARENT["bytes"] and sha(z)==PARENT["sha256"],"whole original four-matrix file")
        b=gzip.decompress(z);need(sha(b)==PARENT["logicalSha256"],"whole original four-matrix logical bytes")
        v=json.loads(b);need(v["binding"]==PARENT["binding"],"same complete six-mean original source binding")
        data=v["data"];need(data["symmetryIdentities"]==[True]*4,"four actually symmetric original E matrices")
        need(sum(q*pow(ROOT,j,PRIME) for j,q in enumerate(MATCHED))%PRIME==0,"actual matched-field root")
        T=[[[coeff(c) for c in row] for row in mat] for mat in data["matrices"]]
        need(len(T)==4 and all(len(mat)==6 and all(len(row)==6 for row in mat) for mat in T),"all144 original matrix entries")
        need(all(int(nmod_mat(mat,PRIME).det())!=0 for mat in T),"all four original residue units")
        dictionary=[{"rows":list(rr),"columns":list(cc)} for rr in itertools.combinations(range(6),3) for cc in itertools.combinations(range(4),3)]
        need(len(dictionary)==80,"all80 original three-minor labels")
        degree3=mons(3);I3={e:i for i,e in enumerate(degree3)};minors=[]
        permutations=list(itertools.permutations(range(3)))
        for lab in dictionary:
            row=[0]*len(degree3)
            for perm in permutations:
                sign=-1 if sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))%2 else 1
                L=[T[lab["columns"][perm[k]]][lab["rows"][k]] for k in range(3)]
                for i in range(6):
                    for j in range(6):
                        for k in range(6):
                            pos=I3[key([i,j,k])]
                            row[pos]=(row[pos]+sign*L[0][i]*L[1][j]*L[2][k])%PRIME
            minors.append(row)
        # Independent direct determinant checks audit the coefficient
        # assembly; the complete source is the full symbolic expansion.
        points=[[int(i==j) for i in range(6)] for j in range(6)]+[[1,2,3,4,5,6]]
        evaluations=0
        for y in points:
            M=[[sum(T[j][i][k]*y[k] for k in range(6))%PRIME for j in range(4)] for i in range(6)]
            for row,lab in zip(minors,dictionary):
                value=sum(c*__import__("functools").reduce(lambda x,y:x*y,(pow(y[i],e[i],PRIME) for i in range(6)),1) for c,e in zip(row,degree3))%PRIME
                sub=nmod_mat([[M[i][j] for j in lab["columns"]] for i in lab["rows"]],PRIME)
                need(value==int(sub.det()),"all560 independent original minor evaluation checks");evaluations+=1
        stages=[];unit=None
        for degree in [3,4,5]:
            output=mons(degree);index={e:i for i,e in enumerate(output)};mult=mons(degree-3)
            sources=[{"minorIndex":j,"multiplier":list(e)} for j in range(80) for e in mult]
            A=[[0]*len(sources) for _ in output]
            for j,minor in enumerate(minors):
                for k,e in enumerate(mult):
                    col=j*len(mult)+k
                    for c,t in zip(minor,degree3):
                        if c:
                            pos=index[tuple(x+y for x,y in zip(e,t))];A[pos][col]=(A[pos][col]+c)%PRIME
            mat=nmod_mat(A,PRIME);R,r=mat.rref();r=int(r)
            stage={"degree":degree,"outputRows":len(output),"allOriginalSourceColumns":len(sources),"actualFieldRank":r}
            stages.append(stage)
            if r==len(output):
                piv=[next(j for j in range(len(sources)) if int(R[i,j])) for i in range(r)]
                U=nmod_mat([[row[j] for j in piv] for row in A],PRIME);V=U.inv()
                I=nmod_mat([[int(i==j) for j in range(r)] for i in range(r)],PRIME)
                need(U*V==I and V*U==I,"all original selected-unit inverse coordinates")
                unit={"degree":degree,"selectedOriginalSourceColumns":piv,"selectedOriginalSourceLabels":[sources[j] for j in piv],
                      "allOriginalOutputMonomials":[list(e) for e in output],
                      "unit":matrix_rows(U),"inverse":matrix_rows(V),"determinant":int(U.det()),
                      "allInverseProductCoordinates":2*r*r}
                break
        model={"parentBinding":PARENT["binding"],"matchedCubic":MATCHED,"prime":PRIME,"root":ROOT,
            "allFourOriginalResidueMatrices":T,"all80OriginalMinorLabels":dictionary,
            "all56CubicMonomials":[list(e) for e in degree3],"all80CompleteResidueMinorCoefficientRows":minors,
            "completeDegreeProfiles":stages,"completeOriginalUnitCertificate":unit,
            "exactEOperatorDefinition":"Use the same full original E minor-coefficient matrix and the same selected columns; adj(U_E)/det(U_E) is a fixed E source operator.",
            "deficientFieldProfilesNotUsedAsCharacteristicZeroUpperBounds":True}
        desc=save_gz(out/"complete-original-mean-three-minor-gate.json.gz",{"format":FORMAT+"-model","binding":binding,"data":model})
        rec["parameters"].update({"model":desc,"all144OriginalMatrixEntriesRetained":True,"allActualCoefficientDenominators127Units":True,
           "all80OriginalThreeMinorsRetained":True,"all560DirectDeterminantEvaluationsVerified":evaluations==560,
           "completeDegreeProfiles":stages,"fullOriginalPowerCertificateComplete":unit is not None,
           "certifiedPowerOfOriginalMeanIdeal":unit["degree"] if unit else None,
           "selectedUnitDeterminant127":unit["determinant"] if unit else None,
           "allSelectedUnitInverseCoordinatesVerified":unit is not None,
           "rankAtLeastThreeForEveryNonzeroMeanOverE":unit is not None,
           "globalFreeSevenClaimed":False,"fullOriginalCriticalIdealSolved":False})
        rec["status"]="completed" if unit else "completed-bounded-field-profile";code=0
    except BaseException as e:
        rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=75 if isinstance(e,TimeoutError) else 1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-start;rec["maxResidentKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        desc=save_json(out/"original-mean-three-minor-gate-receipt.json",rec)
        print(json.dumps({"status":rec["status"],"exitCode":code,"binding":binding,"elapsedSeconds":rec["elapsedSeconds"],"receipt":desc,"parameters":rec["parameters"]},sort_keys=True),flush=True)
    return code
if __name__=="__main__":sys.exit(main())
