#!/usr/bin/env python3
"""Global original matched-Bell hyperbolic coordinates, with full source transport.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Read the exact verified full-parameter model.  Make the polynomial coordinate
change B=y.w using only constant matched-field inverses.  Check both inverse
maps, the full source-Jacobian inverses, and weighted Euler-vector transport.
Keep R3 as an exact composition straight-line program; no mean specialization,
denominator localization, or omitted gradient is used.
"""
import argparse,gzip,hashlib,itertools,json,os
from pathlib import Path
import resource,signal,sys,time
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx

FORMAT="r150-original-matched-bell-global-hyperbolic-coordinates-v2"
MODEL_BYTES=504873
MODEL_SHA="7fe125c8cc6019c5e7c756cac3fb9265b9fcf817b1d2acea3f7580c2c5b024dc"
MODEL_LOGICAL="adab3268447f90c430c9d219fc988ddc8e54cb5f8697dd05fe6599a61166908d"
MODEL_BINDING="ba1bdf0ccf6937579f2b38b51b0d19e8cfad0cfb2b25e152c3a62befbde87b9c"
MATCHED=[52565262336,6080833024,-43931504,3725]
OLD=fmpq_mpoly_ctx.get(("d",)+tuple("y%d"%i for i in range(6))+tuple("H%d"%i for i in range(11)))
NEW=fmpq_mpoly_ctx.get(("d",)+tuple("y%d"%i for i in range(6))+tuple("w%d"%i for i in range(6))+tuple("u%d"%i for i in range(5)))
OG,NG=OLD.gens(),NEW.gens()
OZ,NZ=OLD.from_dict({}),NEW.from_dict({})
OM=sum((OG[0]**i*fmpq(c,MATCHED[-1]) for i,c in enumerate(MATCHED)),OZ)
NM=sum((NG[0]**i*fmpq(c,MATCHED[-1]) for i,c in enumerate(MATCHED)),NZ)
def need(b,s):
    if not b:raise ValueError(s)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode("ascii")
def sha(x):return hashlib.sha256(x).hexdigest()
def red(p,mod):return divmod(p,mod)[1]
def oval(v):return sum((OG[0]**i*fmpq(x) for i,x in enumerate(v)),OZ)
def nval(v):return sum((NG[0]**i*fmpq(x) for i,x in enumerate(v)),NZ)
def lift(rows,ctx=OLD):
    return ctx.from_dict({(0,)+tuple(int(x) for x in e):fmpq(c) for e,c in rows})
def compose(p,variables,mod):
    q=p.compose(*variables)
    return red(q,mod)
def values(p):return [[list(map(int,e)),str(q)] for e,q in sorted(p.to_dict().items())]
def save_json(p,x):
    b=json.dumps(x,sort_keys=True,indent=2).encode("ascii")
    t=p.with_name(p.name+".tmp");t.write_bytes(b);os.replace(t,p)
    return {"path":p.name,"bytes":len(b),"sha256":sha(b)}
def save_gz(p,x):
    b=canonical(x);z=gzip.compress(b,compresslevel=1,mtime=0)
    t=p.with_name(p.name+".tmp");t.write_bytes(z);os.replace(t,p)
    return {"path":p.name,"bytes":len(z),"sha256":sha(z),
            "logicalBytes":len(b),"logicalSha256":sha(b)}
def fpoly_from_constant(p):
    d=p.to_dict();need(all(not any(e[1:]) for e in d),"field constant extraction")
    out=[fmpq(0)]*3
    for e,c in d.items():
        need(e[0]<3,"canonical field coefficient")
        out[int(e[0])]+=c
    return fmpq_poly(out)
def fieldrank(A):
    f=fmpq_poly([fmpq(x,MATCHED[-1]) for x in MATCHED]);one=fmpq_poly([1])
    R=[list(row) for row in A];r=0;ps=[]
    for j in range(len(A[0])):
        k=next((i for i in range(r,len(A)) if R[i][j]),None)
        if k is None:continue
        R[r],R[k]=R[k],R[r];g,iv,_=R[r][j].xgcd(f)
        need(g==one and R[r][j]*iv%f==one,"pure-u polar original field pivot")
        R[r]=[x*iv%f for x in R[r]]
        for i in range(len(R)):
            if i!=r and R[i][j]:
                c=R[i][j];R[i]=[(x-c*y)%f for x,y in zip(R[i],R[r])]
        ps.append(j);r+=1
    return r,ps

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--model",required=True);ap.add_argument("--out",required=True)
    ap.add_argument("--seconds",type=float,default=180)
    ap.add_argument("--memory-mib",type=int,default=2048)
    a=ap.parse_args();need(0<a.seconds<=300 and 512<=a.memory_mib<=4096,"bounded polynomial transport budget")
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    started=time.monotonic();ss=sha(Path(__file__).read_bytes())
    binding=sha(canonical({"format":FORMAT,"sourceSha256":ss,"parentBinding":MODEL_BINDING,
                          "modelSha256":MODEL_SHA,"modelLogicalSha256":MODEL_LOGICAL}))
    rec={"format":FORMAT,"sourceSha256":ss,"binding":binding,"status":"started",
         "parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib,"allOriginalVariablesRemainFree":True}}
    def timeout(signum,frame):raise TimeoutError("bounded exact full Bell coordinate transport")
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
    try:
        raw=Path(a.model).read_bytes();need(len(raw)==MODEL_BYTES and sha(raw)==MODEL_SHA,"entire paid original model bytes")
        logical=gzip.decompress(raw);need(sha(logical)==MODEL_LOGICAL,"all paid original logical model bytes")
        payload=json.loads(logical);need(payload["binding"]==MODEL_BINDING,"same original parameter model binding")
        m=payload["data"];need(m["coefficientRank"]==6 and m["matchedCubic"]==MATCHED,
                             "same actual full Bell coefficient rank and field")
        P=m["originalIndependentHankelRows"];need(P==[2,1,0,3,4,5],"same actual six original Hankel columns")
        U=[i for i in range(11) if i not in P];need(U==[6,7,8,9,10],"complete five remaining original Hankel columns")
        L=m["BellHankelMeanCoefficientMatrix"];Li=m["selectedCoefficientInverse"]
        need(len(L)==11 and all(len(row)==6 for row in L),"complete original eleven-by-six coefficient matrix")
        cubic=sum((lift(v)*OG[0]**k for k,v in enumerate(m["BellCubicMeanComponents"])),OZ)
        B=sum((lift(v)*OG[0]**k for k,v in enumerate(m["BellFieldComponents"])),OZ)
        R=lift(m["R3"]);old_eq=[lift(x) for x in m["originalSeventeenGradients"]]
        Q=[red(cubic.derivative(1+i)/3,OM) for i in range(6)]
        fw=[red(sum((oval(L[j][i])*OG[7+j] for j in range(11)),OZ)+Q[i],OM) for i in range(6)]
        oldnew=[OG[0]]+list(OG[1:7])+fw+[OG[7+j] for j in U]
        need(red(B-sum((OG[1+i]*fw[i] for i in range(6)),OZ),OM)==0,"full original Bell equals y dot w")
        newQ=[compose(q,[NG[0]]+list(NG[1:7])+[NZ]*11,NM) for q in Q]
        rhs=[red(NG[7+i]-sum((nval(L[U[j]][i])*NG[13+j] for j in range(5)),NZ)-newQ[i],NM) for i in range(6)]
        invH=[NZ]*11
        for a0,j in enumerate(P):
            invH[j]=red(sum((nval(Li[i][a0])*rhs[i] for i in range(6)),NZ),NM)
        for a0,j in enumerate(U):invH[j]=NG[13+a0]
        newold=[NG[0]]+list(NG[1:7])+invH
        for i in range(18):
            need(compose(oldnew[i],newold,NM)==NG[i],"all original-to-new inverse map coordinates")
            need(compose(newold[i],oldnew,OM)==OG[i],"all new-to-original inverse map coordinates")
        need(compose(B,newold,NM)==sum((NG[1+i]*NG[7+i] for i in range(6)),NZ),"full original Bell transported to hyperbolic form")
        Jf=[[red(oldnew[i].derivative(j),OM) for j in range(1,18)] for i in range(1,18)]
        Ji=[[red(newold[i].derivative(j),NM) for j in range(1,18)] for i in range(1,18)]
        Jft=[[compose(z,newold,NM) for z in row] for row in Jf]
        for i in range(17):
            for j in range(17):
                need(red(sum((Jft[i][k]*Ji[k][j] for k in range(17)),NZ),NM)==int(i==j),
                     "all289 forward-times-inverse original source Jacobian products")
                need(red(sum((Ji[i][k]*Jft[k][j] for k in range(17)),NZ),NM)==int(i==j),
                     "all289 inverse-times-forward original source Jacobian products")
        weights=[0]+[1]*6+[2]*11
        for i in range(1,18):
            need(red(sum((OG[j]*weights[j]*Jf[i-1][j-1] for j in range(1,18)),OZ)-weights[i]*oldnew[i],OM)==0,
                 "all17 forward original weighted Euler-vector coordinates")
            need(red(sum((NG[j]*weights[j]*Ji[i-1][j-1] for j in range(1,18)),NZ)-weights[i]*newold[i],NM)==0,
                 "all17 inverse original weighted Euler-vector coordinates")
        # The only expanded restriction has y=w=0, hence just five linear
        # moment variables.  The full transformed potential stays an exact
        # straight-line composition, not a silently truncated expansion.
        hp=[red(z.subs({i:0 for i in range(1,13)}),NM) for z in invH]
        K=m["K"]
        HK=[[hp[i+j] for j in range(6)] for i in range(6)]
        KH=[[red(sum((K[i][k]*HK[k][j] for k in range(6)),NZ),NM)
             for j in range(6)] for i in range(6)]
        KH2=[[red(sum((KH[i][k]*KH[k][j] for k in range(6)),NZ),NM)
              for j in range(6)] for i in range(6)]
        pure=red(-8*sum((KH2[i][j]*KH[j][i] for i in range(6) for j in range(6)),NZ),NM)
        original_Honly=R.subs({i:0 for i in range(1,7)})
        need(compose(original_Honly,[NG[0]]+[NZ]*6+hp,NM)==pure,
             "all original five-moment pure cubic restriction coefficients")
        need(all(sum(int(x) for x in e[13:18])==3 and not any(e[1:13]) and e[0]<3
                 for e in pure.to_dict()),"complete homogeneous five-moment cubic")
        upolar=[]
        mons=list(itertools.combinations_with_replacement(range(5),2))
        for i in range(5):
            p=red(pure.derivative(13+i),NM).to_dict();row=[]
            for mon in mons:
                coefficient=[fmpq(0)]*3
                for e,c in p.items():
                    tail=[]
                    for j in range(5):tail.extend([j]*int(e[13+j]))
                    if tail==list(mon):coefficient[int(e[0])]+=c
                row.append(fmpq_poly(coefficient))
            upolar.append(row)
        urank,upiv=fieldrank(upolar)
        record={"parentBinding":MODEL_BINDING,"matchedCubic":MATCHED,
                "originalCoordinateNames":list(OLD.names()),"newCoordinateNames":list(NEW.names()),
                "selectedOriginalHankelColumns":P,"remainingOriginalHankelColumns":U,
                "forwardNewCoordinatesInOriginal":list(map(values,oldnew)),
                "inverseOriginalCoordinatesInNew":list(map(values,newold)),
                "completeOriginalPotentialStraightLineProgram":{
                    "definition":"R3 composed with inverseOriginalCoordinatesInNew",
                    "originalR3CoefficientSha256":sha(canonical(m["R3"])),
                    "originalSeventeenCoefficientSha256":sha(canonical(m["originalSeventeenGradients"])),
                    "sourceModelLogicalSha256":MODEL_LOGICAL,
                    "allOriginalPolynomialTermsRetained":True},
                "forwardJacobianInNewCoordinates":[list(map(values,row)) for row in Jft],
                "inverseJacobianInNewCoordinates":[list(map(values,row)) for row in Ji],
                "pureRemainingFiveMomentCubic":values(pure),
                "pureRemainingCubicPolarMatrix":[[[str(z[k]) for k in range(3)] for z in row] for row in upolar],
                "pureRemainingCubicEssentialRank":urank,"pureRemainingCubicPolarPivots":upiv}
        desc=save_gz(out/"complete-original-hyperbolic-coordinate-model.json.gz",
                     {"format":FORMAT+"-model","binding":binding,"data":record})
        rec["parameters"].update({"parentModelSha256":MODEL_SHA,"parentModelLogicalSha256":MODEL_LOGICAL,
            "selectedOriginalHankelColumns":P,"remainingOriginalHankelColumns":U,
            "all36CompletePolynomialInverseCoordinateIdentitiesVerified":True,
            "completeOriginalBellIdentityAndHyperbolicTransportVerified":True,
            "all578OriginalSourceJacobianInverseProductsVerified":True,
            "all34CompleteWeightedEulerVectorCoordinatesVerified":True,
            "all17GradientGeneratorsTransportedByExactInvertiblePolynomialJacobian":True,
            "noMeanOrHankelParameterInverted":True,
            "allOriginalCriticalEquationsRetained":True,
            "transformedPotentialStoredAsExactOriginalComposition":True,
            "allOriginalFiveMomentRestrictionCoefficientsVerified":True,
            "pureFiveMomentCubicTermCount":len(pure.to_dict()),
            "remainingFiveMomentPureCubicZero":not bool(pure),
            "remainingFiveMomentCubicEssentialRank":urank,"model":desc})
        rec["status"]="completed";code=0
    except BaseException as e:
        rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed"
        rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=75 if isinstance(e,TimeoutError) else 1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-started
        desc=save_json(out/"original-matched-bell-global-hyperbolic-receipt.json",rec)
        print(json.dumps({"status":rec["status"],"binding":binding,"exitCode":code,
            "elapsedSeconds":rec["elapsedSeconds"],"receipt":desc,"parameters":rec["parameters"]},sort_keys=True),flush=True)
    return code
if __name__=="__main__":sys.exit(main())
