#!/usr/bin/env python3
"""Complete original twelve-gradient normal forms in the actual squarefree32 algebra.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Rebuild the original N/Gamma contractions in the exact matched cubic field,
using the whole verified polynomial inverse map.  Keep all17 source
generators.  The five u derivatives are checked against the whole paid
top cubic.  Only the true constant five-square coefficient matrix is
inverted.  All twelve full normal-form/source identities are multiplied
back as complete free-parameter polynomials.  No parameter fiber, random
specialization, or assumption about the remaining ideal is used.
"""
import argparse,gzip,hashlib,itertools,json,os
from pathlib import Path
import resource,signal,sys,time
from flint import fmpq,fmpq_mat,fmpq_poly,fmpq_mpoly,fmpq_mpoly_ctx

FORMAT="r150-original-complete-twelve-gradient-low-normal-forms-v2"
PARENTS={
"hyperbolic":{"bytes":1777288,"sha256":"46537ffbe520ff47df2f18448541a3d2608578ca067a0c865b43e8c44ab55fdc","logical":"5a10a784f9d9ee9455f97bdd8a077ff32f1d75eefba392e5c58e5cd6f5de5ee3","binding":"d939c3506ce8276d82c662f382ae4ffe5c93163929ec1931c2174ecf001c1a8f"},
"squarefree":{"bytes":578763,"sha256":"4be5d8a3a900799d41e5428671e1453a30082f0fdb8c3c2a130b416563031c42","logical":"b74faeb4ddf0a8ea38f6ece1585c437b01611f06cd11a1822ce9e145b902e62f","binding":"67f86e42cd7b1e01e30ca0184d136e2983842cfd6df31d28bd3d75fc8a0e8b33"}}
MATCHED=[52565262336,6080833024,-43931504,3725]
KRAW=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]]
J3DET=23366320238786911411830138211362846399922176000
C=fmpq_mpoly_ctx.get(("d",)+tuple("y%d"%i for i in range(6))+tuple("w%d"%i for i in range(6))+tuple("u%d"%i for i in range(5)))
X=C.gens();Z=C.from_dict({})
MOD=sum((X[0]**i*fmpq(a,MATCHED[-1]) for i,a in enumerate(MATCHED)),Z)
FMOD=fmpq_poly([fmpq(a,MATCHED[-1]) for a in MATCHED])
U0=(0,)*5
CROSS=list(itertools.combinations(range(5),2))

def need(b,s):
    if not b:raise ValueError(s)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def sha(x):return hashlib.sha256(x).hexdigest()
def red(x):return divmod(x,MOD)[1]
def lift(v):return C.from_dict({tuple(e):fmpq(c) for e,c in v})
def field(v):return sum((X[0]**i*fmpq(c) for i,c in enumerate(v)),Z)
def fv(x):return [str(x[i]) for i in range(3)]
def values(p):return [[list(map(int,e)),str(c)] for e,c in sorted(p.to_dict().items())]
def mm(A,B):
    return [[red(sum((A[i][k]*B[k][j] for k in range(len(B))),Z)) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,b):return [red(sum((a*x for a,x in zip(row,b)),Z)) for row in A]
def dot(a,b):return red(sum((x*y for x,y in zip(a,b)),Z))
def tr(A):return sum((A[i][i] for i in range(len(A))),Z)
def conv(a,b):
    out=[Z for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return [red(x) for x in out]
def save_json(p,x):
    b=json.dumps(x,sort_keys=True,indent=2).encode();t=p.with_name(p.name+".tmp");t.write_bytes(b);os.replace(t,p)
    return {"path":p.name,"bytes":len(b),"sha256":sha(b)}
def file_sha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        while True:
            b=f.read(1024*1024)
            if not b:break
            h.update(b)
    return h.hexdigest()
def save_gz(p,x):
    # Canonical JSON is emitted incrementally.  In particular, never turn
    # all twelve rows of large exact coefficients into strings at once.
    t=p.with_name(p.name+".tmp");h=hashlib.sha256();size=0
    with t.open("wb") as raw:
        with gzip.GzipFile(filename="",mode="wb",fileobj=raw,compresslevel=1,mtime=0) as z:
            def write(s):
                nonlocal size
                b=s.encode();h.update(b);size+=len(b);z.write(b)
            def emit(v):
                if isinstance(v,fmpq_mpoly):
                    write("[")
                    for i,(e,c) in enumerate(sorted(v.to_dict().items())):
                        if i:write(",")
                        emit([list(map(int,e)),str(c)])
                    write("]")
                elif isinstance(v,dict):
                    write("{")
                    for i,k in enumerate(sorted(v)):
                        if i:write(",")
                        write(json.dumps(k,ensure_ascii=True));write(":");emit(v[k])
                    write("}")
                elif isinstance(v,(list,tuple)):
                    write("[")
                    for i,q in enumerate(v):
                        if i:write(",")
                        emit(q)
                    write("]")
                else:write(json.dumps(v,ensure_ascii=True,separators=(",",":")))
            emit(x)
    os.replace(t,p)
    return {"path":p.name,"bytes":p.stat().st_size,"sha256":file_sha(p),
            "logicalBytes":size,"logicalSha256":h.hexdigest()}
def read_parent(path,key):
    d=PARENTS[key];raw=Path(path).read_bytes();need(len(raw)==d["bytes"] and sha(raw)==d["sha256"],"whole original "+key+" bytes")
    b=gzip.decompress(raw);need(sha(b)==d["logical"],"whole original "+key+" logical")
    p=json.loads(b);need(p["binding"]==d["binding"],"whole original "+key+" binding")
    return p["data"]
def j3inv():
    b={(i,j):KRAW[i][j] for i in range(6) for j in range(6) if KRAW[i][j]};p={(0,0):1}
    for _ in range(3):
        q={}
        for (i,j),a in p.items():
            for (k,l),c in b.items():q[i+k,j+l]=q.get((i+k,j+l),0)+a*c
        p={k:v for k,v in q.items() if v}
    J=fmpq_mat([[p.get((i,j),0) for j in range(16)] for i in range(16)])
    need(J.det()==J3DET,"literal original J3 determinant")
    V=J.inv();I=fmpq_mat([[int(i==j) for j in range(16)] for i in range(16)])
    need(J*V==I and V*J==I,"all512 actual original J3 inverse products")
    return V
def split_u(p):
    out={}
    for e,q in p.to_dict().items():
        e=tuple(map(int,e));u=e[13:];need(sum(u)<=2 and e[0]<3,"all original transported gradient terms have u degree at most2")
        v=e[:13]+(0,)*5;di=out.setdefault(u,{})
        di[v]=di.get(v,fmpq(0))+q
    return {u:C.from_dict(v) for u,v in out.items()}
def ukey(i,j=None):
    v=[0]*5;v[i]+=1
    if j is not None:v[j]+=1
    return tuple(v)
def constfield(p):
    out=[fmpq(0)]*3
    for e,c in p.to_dict().items():
        need(e[0]<3 and not any(e[1:]),"fixed original matched-field coefficient")
        out[int(e[0])]+=c
    return fmpq_poly(out)
def inverse_field(A):
    n=len(A);R=[list(row)+[fmpq_poly([int(i==j)]) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next((i for i in range(j,n) if R[i][j]),None);need(k is not None,"true original square-coefficient field unit")
        R[j],R[k]=R[k],R[j];g,v,_=R[j][j].xgcd(FMOD);need(g==fmpq_poly([1]),"true fixed field inverse")
        v%=FMOD;need(R[j][j]*v%FMOD==fmpq_poly([1]),"actual fixed field pivot inverse product")
        R[j]=[x*v%FMOD for x in R[j]]
        for i in range(n):
            if i!=j and R[i][j]:
                a=R[i][j];R[i]=[(x-a*y)%FMOD for x,y in zip(R[i],R[j])]
    V=[row[n:] for row in R]
    for i in range(n):
        for j in range(n):
            need(sum((A[i][k]*V[k][j] for k in range(n)),fmpq_poly())%FMOD==fmpq_poly([int(i==j)]),"all25 original square right-inverse products")
            need(sum((V[i][k]*A[k][j] for k in range(n)),fmpq_poly())%FMOD==fmpq_poly([int(i==j)]),"all25 original square left-inverse products")
    return V
def check_weight(p,w,allow_u=True):
    need(all(sum(e[i] for i in range(1,7))+2*sum(e[7:])==w and (allow_u or not any(e[13:]))
             for e in p.to_dict()),"complete original weighted parameter coefficients")
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--hyperbolic",required=True);ap.add_argument("--squarefree",required=True);ap.add_argument("--out",required=True)
    ap.add_argument("--seconds",type=float,default=300);ap.add_argument("--memory-mib",type=int,default=4096)
    a=ap.parse_args();need(0<a.seconds<=600 and 1024<=a.memory_mib<=8192,"bounded original low normal-form budget")
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True);resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    started=time.monotonic();ss=sha(Path(__file__).read_bytes())
    binding=sha(canon({"format":FORMAT,"sourceSha256":ss,"parents":PARENTS,"matchedCubic":MATCHED}))
    rec={"format":FORMAT,"binding":binding,"sourceSha256":ss,"status":"started","parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib}}
    def event(phase):
        rec["parameters"]["lastCompletedPhase"]=phase
        print(json.dumps({"phase":phase,"elapsedSeconds":time.monotonic()-started}),flush=True)
    def timeout(sig,fr):raise TimeoutError("bounded exact original low normal forms")
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
    try:
        h=read_parent(a.hyperbolic,"hyperbolic");sf=read_parent(a.squarefree,"squarefree")
        need(h["matchedCubic"]==MATCHED and sf["matchedCubic"]==MATCHED,"same original number field")
        need(len(sf["standardMonomials32"])==32,"same whole squarefree32 basis")
        old=[lift(v) for v in h["inverseOriginalCoordinatesInNew"]]
        need(old[:7]==list(X[:7]),"same original mean variables and field parameter")
        H=[[old[7+i+j] for j in range(6)] for i in range(6)]
        Ji=[[lift(v) for v in row] for row in h["inverseJacobianInNewCoordinates"]]
        for i in range(17):
            for j in range(17):need(red(old[i+1].derivative(j+1))==Ji[i][j],"all289 actual inverse source-Jacobian entries")
        Qorig=[{tuple(e):fmpq_poly([fmpq(x) for x in v]) for e,v in row} for row in sf["originalFiveQuadraticPartials"]]
        SQ=[[row.get(ukey(j,j),fmpq_poly()) for j in range(5)] for row in Qorig]
        SQinv=inverse_field(SQ);SQip=[[field(fv(v)) for v in row] for row in SQinv]
        inverseDesc=save_gz(out/"exact-original-five-square-inverse.json.gz",{"format":FORMAT+"-square-inverse","binding":binding,"matrix":[list(map(fv,row)) for row in SQ],"inverse":[list(map(fv,row)) for row in SQinv]})
        rec["parameters"]["squareInverse"]=inverseDesc;event("exact-original-five-square-inverse")
        Jinv=j3inv();y=list(X[1:7]);p=mv(KRAW,y);F=dot(y,p)/2
        KH=mm(KRAW,H);KH2=mm(KH,KH);HKH=mm(H,KH);KHK=mm(KRAW,mm(H,KRAW))
        Hp=mv(H,p);b=dot(p,Hp);tau2=tr(KH2)
        polar=[sum((KHK[i][j] for i in range(6) for j in range(6) if i+j==k),Z) for k in range(11)]
        d=conv(conv(p,p),p);e=conv(polar,p);ell=[d[i]-6*e[i] for i in range(16)]
        V=[red(-sum((ell[j]*Jinv[i,j] for j in range(16)),Z)/4) for i in range(16)]
        N=[[red(F*y[i]*y[j]-2*F*H[i][j]-2*(y[i]*Hp[j]+Hp[i]*y[j])
             +4*sum((V[i+j+k]*p[k] for k in range(6)),Z)+4*HKH[i][j]) for j in range(6)] for i in range(6)]
        KNK=mm(KRAW,mm(N,KRAW))
        eqH=[red(-6*sum((KNK[i][j] for i in range(6) for j in range(6) if i+j==m),Z)) for m in range(11)]
        event("complete-original-eleven-Hankel-gradients")
        HKHp=mv(HKH,p)
        Gam=[red((F**2-2*b+2*tau2)*y[i]-4*F*Hp[i]+8*HKHp[i]
                  +4*sum((V[i+j+k]*p[j]*p[k] for j in range(6) for k in range(6)),Z)
                  -8*sum((V[i+j+k]*KHK[j][k] for j in range(6) for k in range(6)),Z)) for i in range(6)]
        eqY=[3*v for v in mv(KRAW,Gam)];gold=eqY+eqH
        event("complete-original-six-mean-gradients")
        transported=[]
        for i in range(17):
            transported.append(red(sum((Ji[j][i]*gold[j] for j in range(17) if Ji[j][i]),Z)))
        for i,v in enumerate(transported):check_weight(v,5 if i<6 else 4)
        uf=transported[12:];splitF=[split_u(v) for v in uf]
        Avec=[[s.get(ukey(j),Z) for j in range(5)] for s in splitF]
        Bvec=[s.get(U0,Z) for s in splitF]
        for i,s in enumerate(splitF):
            for mon in (ukey(j,k) for j in range(5) for k in range(j,5)):
                need(constfield(s.get(mon,Z))==Qorig[i].get(mon,fmpq_poly()),"all225 original top quadratic field coordinates")
            check_weight(Bvec[i],4,False)
            for j in range(5):
                check_weight(Avec[i][j],2,False)
                need(Avec[i][j]==Avec[j][i],"all25 exact original Hessian symmetries")
        event("complete-five-u-gradients-with-original-top-and-symmetric-Hessian")
        # Independent first-direction trace formula for all five constant terms.
        substitutions={13+i:0 for i in range(5)}
        H0=[[z.subs(substitutions) for z in row] for row in H]
        KH0=mm(KRAW,H0);KH02=mm(KH0,KH0);ell0=[z.subs(substitutions) for z in ell]
        Jell0=[sum((ell0[j]*Jinv[i,j] for j in range(16)),Z) for i in range(16)]
        for a0 in range(5):
            Ni=[[red(H[i][j].derivative(13+a0)) for j in range(6)] for i in range(6)]
            need(all(all(not any(e[1:]) for e in z.to_dict()) for row in Ni for z in row),"original fixed u-direction is a constant physical matrix")
            KNi=mm(KRAW,Ni);KNiK=mm(KNi,KRAW)
            qni=[sum((KNiK[i][j] for i in range(6) for j in range(6) if i+j==k),Z) for k in range(11)]
            eni=conv(qni,p)
            traceformula=red(-6*F*dot(p,mv(Ni,p))+12*F*tr(mm(KH0,KNi))
                             +24*dot(p,mv(mm(Ni,KH0),p))
                             -24*tr(mm(KH02,KNi))+6*dot(eni,Jell0))
            need(traceformula==Bvec[a0],"all five independent original directional-trace constant polynomials")
        event("all-five-independent-original-trace-identities")
        LOW=[U0]+[ukey(i) for i in range(5)]+[ukey(i,j) for i,j in CROSS]
        fiveModel={"parentBindings":{k:v["binding"] for k,v in PARENTS.items()},
            "matchedCubic":MATCHED,"sameFiveTopQuadratics":sf["originalFiveQuadraticPartials"],
            "squareCoefficientMatrix":[list(map(fv,row)) for row in SQ],
            "squareCoefficientMatrixInverse":[list(map(fv,row)) for row in SQinv],
            "fiveULinearHessianCoefficients":Avec,"fiveUConstantCoefficients":Bvec,
            "lowStandardMonomials16":[list(e) for e in LOW]}
        fiveDesc=save_gz(out/"complete-original-five-u-gradient-coefficients.json.gz",
            {"format":FORMAT+"-five-gradients","binding":binding,"data":fiveModel})
        rec["parameters"]["fiveGradientModel"]=fiveDesc
        # The old physical contractions are no longer needed after their
        # complete transport and the five independent trace checks.
        del gold,eqY,eqH,Gam,N,KNK,KH,KH2,HKH,KHK,Hp,HKHp,V,ell,Jell0,ell0,H0,KH0,KH02
        rowDescs=[];checks=0
        for row in range(12):
            G=transported[row]
            sp=split_u(G);alpha=[sp.get(ukey(i,i),Z) for i in range(5)]
            for z in alpha:
                check_weight(z,1 if row<6 else 0,False)
                need(all(not any(e[7:]) for e in z.to_dict()),"remaining quadratic coefficient depends only on linear mean or constants")
            lam=[red(sum((alpha[j]*SQip[j][i] for j in range(5)),Z)) for i in range(5)]
            for z in lam:check_weight(z,1 if row<6 else 0,False)
            coeff=[]
            for mon in LOW:
                value=sp.get(mon,Z)
                if mon==U0:value-=sum((lam[i]*Bvec[i] for i in range(5)),Z)
                elif sum(mon)==1:value-=sum((lam[i]*Avec[i][mon.index(1)] for i in range(5)),Z)
                else:value-=sum((lam[i]*field(fv(Qorig[i].get(mon,fmpq_poly()))) for i in range(5)),Z)
                coeff.append(red(value))
            normal=sum((c*C.from_dict({(0,)*13+mon:1}) for c,mon in zip(coeff,LOW)),Z)
            need(red(G-normal-sum((lam[i]*uf[i] for i in range(5)),Z))==0,"complete original low normal-form/source polynomial identity")
            need(set(split_u(normal)).issubset(LOW),"all normal-form monomials are the16 paid squarefree low basis")
            rowDesc=save_gz(out/("complete-original-normal-form-%02d.json.gz"%(row+1)),
                {"format":FORMAT+"-verified-row","binding":binding,
                 "data":{"row":row,"gradient":("dy%d"%row if row<6 else "dw%d"%(row-6)),
                         "normalFormCoefficients":coeff,"originalFiveGradientSourceCoefficients":lam,
                         "completeOriginalPolynomialSourceIdentityVerified":True}})
            rowDescs.append(rowDesc);checks+=1
            rec["parameters"]["completeVerifiedNormalFormRows"]=rowDescs
            save_json(out/"original-twelve-gradient-low-normal-forms-checkpoint.json",
                      {"format":FORMAT+"-checkpoint","binding":binding,
                       "fiveGradientModel":fiveDesc,"completeVerifiedNormalFormRows":rowDescs})
            event("complete-original-normal-form-%02d"%(row+1))
            transported[row]=None
            del sp,alpha,lam,coeff,normal,G
        model={"parentBindings":{k:v["binding"] for k,v in PARENTS.items()},"matchedCubic":MATCHED,
            "oldGradientOrder":["dy%d"%i for i in range(6)]+["dH%d"%i for i in range(11)],
            "newGradientOrder":["dy%d"%i for i in range(6)]+["dw%d"%i for i in range(6)]+["du%d"%i for i in range(5)],
            "fiveGradientModel":fiveDesc,"completeVerifiedNormalFormRows":rowDescs,
            "sourceIdentity":"G_j-NF_j=sum_i lambda_ji F_i, after the complete original inverse Jacobian transport",
            "allTwelveRemainingIdealRelationsRetained":True}
        desc=save_gz(out/"complete-original-twelve-gradient-low-normal-forms.json.gz",
                     {"format":FORMAT+"-model","binding":binding,"data":model})
        rec["parameters"].update({"model":desc,"all17OriginalSourcesRetained":True,
            "all512LiteralJ3InverseCoordinatesVerified":True,"all289OriginalInverseSourceJacobianEntriesVerified":True,
            "all50ExactSquareCoefficientInverseProductsVerified":True,
            "all225OriginalTopQuadraticFieldCoordinatesVerified":True,
            "all25ExactOriginalHessianSymmetriesVerified":True,
            "allFiveIndependentOriginalDirectionalTraceIdentitiesVerified":True,
            "completeNormalFormMatrixShape":[12,16],"completeOriginalCorrectionSourceShape":[12,5],
            "allTwelveCompleteOriginalPolynomialNormalFormIdentitiesVerified":checks==12,
            "allFiveLowerUGradientsComputedWithoutFullPotentialExpansion":True,
            "noMeanOrHankelParameterSpecialized":True,"noParameterDenominatorIntroduced":True,
            "quadraticCoefficientWeights":[1]*6+[0]*6,
            "allRemainingIdealConsequencesSolved":False})
        rec["status"]="completed";code=0
    except BaseException as e:
        rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed"
        rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=75 if isinstance(e,TimeoutError) else 1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-started;rec["maxResidentKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        desc=save_json(out/"original-twelve-gradient-low-normal-forms-receipt.json",rec)
        print(json.dumps({"status":rec["status"],"binding":binding,"exitCode":code,
              "elapsedSeconds":rec["elapsedSeconds"],"receipt":desc,"parameters":rec["parameters"]},sort_keys=True),flush=True)
    return code
if __name__=="__main__":sys.exit(main())
