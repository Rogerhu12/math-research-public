#!/usr/bin/env python3
"""Six complete original mean relations in the actual ten-generator module.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Read all twelve verified original normal-form rows.  Invert only the
actual constant six-dimensional mixed-quadratic unit, retain every
parameter coefficient, and verify all six-by-sixteen original products.
Ten coordinates mean module generation, never unproved freeness.
"""
import argparse,gzip,hashlib,importlib.util,itertools,json,os
from pathlib import Path
import resource,signal,sys,time
from flint import fmpq,fmpq_poly

FORMAT="r150-original-six-mean-relations-in-ten-generators-v1"
NF_SOURCE_SHA="23f99635b7abe21ff9bd621175fd2d9d82ffd6146690cac7c7b893f443382117"
NF={"bytes":1921,"sha256":"ca4c3d98675ab404cb2b8e05c8ddacd32c02d936f751cf05fe572eb57d510e48",
"logicalSha256":"d58cf0f99c7d2fee7087ca76297d30e70dd4b8ba830ab7b42709b7ab8c6ccc52",
"binding":"8fb21996da88d9abaa7d8a0c96208129603808d7c5c1e03b9acf6caa1dca6545"}
LEAD={"bytes":1653920,"sha256":"005484500176a294a3a14788843f1ad50031f2e2bce3e599c512e45ac5dacbb6",
"logicalSha256":"da5839f34930081d56df84d9d803daf2b226ac98de8364135463f6f94b6db1d2",
"binding":"41ee91c353da2b8a33bbb631d46bc48e11709dcf42e131ebf4d417c7a3e98b63"}
MATCHED=[52565262336,6080833024,-43931504,3725]
def need(b,s):
    if not b:raise ValueError(s)
def sha(x):return hashlib.sha256(x).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def load_gz(p,d,binding):
    z=p.read_bytes();need(len(z)==d["bytes"] and sha(z)==d["sha256"],"complete original bytes "+p.name)
    b=gzip.decompress(z);need(sha(b)==d["logicalSha256"],"complete original logical bytes "+p.name)
    v=json.loads(b);need(v["binding"]==binding,"same original phase binding "+p.name)
    return v["data"]
def field_inverse(A,mod):
    n=len(A);one=fmpq_poly([1]);zero=fmpq_poly()
    R=[list(a)+[fmpq_poly([int(i==j)]) for j in range(n)] for i,a in enumerate(A)]
    for j in range(n):
        k=next((i for i in range(j,n) if R[i][j]),None);need(k is not None,"actual original six-dimensional E unit")
        R[j],R[k]=R[k],R[j];g,v,_=R[j][j].xgcd(mod);need(g==one,"actual E inverse gcd")
        v%=mod;need(R[j][j]*v%mod==one,"original E pivot inverse product")
        R[j]=[x*v%mod for x in R[j]]
        for i in range(n):
            if i!=j and R[i][j]:
                z=R[i][j];R[i]=[(a-z*b)%mod for a,b in zip(R[i],R[j])]
    V=[row[n:] for row in R]
    for i in range(n):
        for j in range(n):
            need(sum((A[i][k]*V[k][j] for k in range(n)),zero)%mod==fmpq_poly([int(i==j)]),"all36 actual right E inverse products")
            need(sum((V[i][k]*A[k][j] for k in range(n)),zero)%mod==fmpq_poly([int(i==j)]),"all36 actual left E inverse products")
    return V
def frank(A,p):
    a=[list(r) for r in A];k=0
    for j in range(len(a[0])):
        i=next((i for i in range(k,len(a)) if a[i][j]%p),None)
        if i is None:continue
        a[k],a[i]=a[i],a[k];v=pow(a[k][j],-1,p);a[k]=[x*v%p for x in a[k]]
        for i in range(k+1,len(a)):
            z=a[i][j]
            if z:a[i]=[(x-z*y)%p for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    return k
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--low-out",required=True);ap.add_argument("--leading-out",required=True)
    ap.add_argument("--nf-generator",required=True);ap.add_argument("--out",required=True)
    ap.add_argument("--seconds",type=float,default=600);ap.add_argument("--memory-mib",type=int,default=4096);a=ap.parse_args()
    need(0<a.seconds<=900 and 1024<=a.memory_mib<=8192,"bounded exact six-mean consumer")
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True);resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    start=time.monotonic();ss=sha(Path(__file__).read_bytes());binding=sha(canon({"format":FORMAT,"sourceSha256":ss,"nf":NF,"leading":LEAD,"nfSourceSha256":NF_SOURCE_SHA}))
    rec={"format":FORMAT,"binding":binding,"sourceSha256":ss,"parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib}}
    def event(s):
        rec["parameters"]["lastCompletedPhase"]=s;print(json.dumps({"phase":s,"elapsedSeconds":time.monotonic()-start}),flush=True)
    def timeout(sig,fr):raise TimeoutError("bounded exact original six-mean relations")
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1;m=None
    try:
        path=Path(a.nf_generator);need(sha(path.read_bytes())==NF_SOURCE_SHA,"exact original NF arithmetic/streaming helper")
        sp=importlib.util.spec_from_file_location("paid_original_nf",path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
        base=Path(a.low_out);n=load_gz(base/"complete-original-twelve-gradient-low-normal-forms.json.gz",NF,NF["binding"])
        h=load_gz(Path(a.leading_out)/"complete-original-eleven-quadratic-leading-model.json.gz",LEAD,LEAD["binding"])
        need(n["matchedCubic"]==h["matchedCubic"]==MATCHED and h["parentBinding"]==NF["binding"],"same original field and parent")
        selected=h["actualFieldCertificate"]["wQuadraticSelectedColumns"]
        need(len(selected)==6 and len(set(selected))==6,"six distinct actual original mixed columns")
        fullLow=[m.U0]+[m.ukey(i) for i in range(5)]+[m.ukey(i,j) for i,j in m.CROSS]
        kept=[i for i in range(16) if i not in [6+j for j in selected]]
        need([list(fullLow[i]) for i in kept]==h["tenOriginalGeneratingMonomials"],"exact original ten-generator order")
        W=[];LW=[]
        for j in range(6):
            d=n["completeVerifiedNormalFormRows"][6+j];v=load_gz(base/d["path"],d,NF["binding"])
            need(v["row"]==6+j and v["gradient"]=="dw%d"%j and v["completeOriginalPolynomialSourceIdentityVerified"],"whole original w row identity")
            W.append([m.lift(t) for t in v["normalFormCoefficients"]]);LW.append([m.lift(t) for t in v["originalFiveGradientSourceCoefficients"]])
            need(len(W[-1])==16 and len(LW[-1])==5,"complete original w and source coordinates")
            top={tuple(e):fmpq_poly([fmpq(z) for z in c]) for e,c in h["allElevenLeadingQuadratics"][5+j]}
            for k,pair in enumerate(m.CROSS):
                need(m.constfield(W[-1][6+k])==top.get(m.ukey(*pair),fmpq_poly()),"all60 leading coefficients agree with actual original complete-cubic model")
            for z in LW[-1]:m.constfield(z)
            del v
        U=[[m.constfield(W[i][6+j]) for j in selected] for i in range(6)]
        V=field_inverse(U,m.FMOD);VP=[[m.field(m.fv(x)) for x in row] for row in V]
        unit=m.save_gz(out/"complete-original-six-mixed-quadratic-inverse.json.gz",
            {"format":FORMAT+"-constant-unit","binding":binding,"data":{
                "selectedOriginalMixedColumns":selected,"unit":[list(map(m.fv,row)) for row in U],
                "inverse":[list(map(m.fv,row)) for row in V]}})
        rec["parameters"]["constantUnit"]=unit;event("complete-original-six-dimensional-exact-unit")
        rows=[];T=[[[fmpq_poly() for _ in range(6)] for _ in range(6)] for _ in range(4)]
        coeffProducts=0;sourceProducts=0
        for i in range(6):
            desc=n["completeVerifiedNormalFormRows"][i];v=load_gz(base/desc["path"],desc,NF["binding"])
            need(v["row"]==i and v["gradient"]=="dy%d"%i and v["completeOriginalPolynomialSourceIdentityVerified"],"whole original mean row identity")
            Y=[m.lift(t) for t in v["normalFormCoefficients"]];LY=[m.lift(t) for t in v["originalFiveGradientSourceCoefficients"]]
            need(len(Y)==16 and len(LY)==5,"all original mean row and source coordinates");del v
            alpha=[Y[6+j] for j in selected]
            mu=[m.red(sum((alpha[j]*VP[j][k] for j in range(6)),m.Z)) for k in range(6)]
            for z in mu:
                m.check_weight(z,1,False);need(all(not any(e[7:]) for e in z.to_dict()),"complete source multiplier is linear only in y")
            full=[m.red(Y[k]-sum((mu[j]*W[j][k] for j in range(6)),m.Z)) for k in range(16)]
            need(all(full[6+j]==0 for j in selected),"all six original eliminated mixed coordinates zero")
            small=[full[k] for k in kept]
            for k in range(16):
                a0=small[kept.index(k)] if k in kept else m.Z
                need(m.red(Y[k]-a0-sum((mu[j]*W[j][k] for j in range(6)),m.Z))==0,"all96 complete original parameter-coefficient source products")
                coeffProducts+=1
            nu=[m.red(LY[k]-sum((mu[j]*LW[j][k] for j in range(6)),m.Z)) for k in range(5)]
            for k in range(5):
                need(m.red(nu[k]+sum((mu[j]*LW[j][k] for j in range(6)),m.Z)-LY[k])==0,"all30 exact composed original five-source coefficients")
                m.check_weight(nu[k],1,False);need(all(not any(e[7:]) for e in nu[k].to_dict()),"composed correction remains linear only in y");sourceProducts+=1
            for k,z in zip(kept,small):m.check_weight(z,5-2*sum(fullLow[k]),False)
            for j,z in enumerate(small[6:]):
                td=[[fmpq(0)]*3 for _ in range(6)]
                for e,c in z.to_dict().items():
                    need(e[0]<3 and sum(e[1:7])==1 and not any(e[7:]),"complete remaining quadratic coefficient is linear in y")
                    a0=list(e[1:7]).index(1);td[a0][int(e[0])]+=c
                T[j][i]=[fmpq_poly(x) for x in td]
            rd=m.save_gz(out/("complete-original-ten-coordinate-mean-%02d.json.gz"%(i+1)),
                {"format":FORMAT+"-complete-mean-row","binding":binding,"data":{
                    "row":i,"normalFormTenCoefficients":small,
                    "originalFiveUGradientSourceCoefficients":nu,
                    "originalSixWGradientSourceCoefficients":mu,
                    "identity":"Gy_i-small_i=sum nu_ik*F_k+sum mu_ij*Gw_j",
                    "completeSixteenCoefficientIdentityVerified":True}})
            rows.append(rd);rec["parameters"]["completeMeanRows"]=rows
            m.save_json(out/"original-six-mean-relations-checkpoint.json",{"format":FORMAT+"-checkpoint","binding":binding,"constantUnit":unit,"completeMeanRows":rows})
            event("complete-original-ten-coordinate-mean-%02d"%(i+1))
            del Y,LY,alpha,mu,nu,small,full
        symmetric=[all(T[l][i][j]==T[l][j][i] for i in range(6) for j in range(6)) for l in range(4)]
        allcoef=[z[k] for mat in T for row in mat for z in row for k in range(3)]
        finite=None
        for p in [127,131,137,139,149,151,157,163,167,173]:
            if any(int(z.denom()%p)==0 for z in allcoef):continue
            roots=[d for d in range(p) if sum(a0*pow(d,j,p) for j,a0 in enumerate(MATCHED))%p==0]
            if not roots:continue
            d=roots[0]
            def val(z):return sum(int(z[j].numer()%p)*pow(int(z[j].denom()%p),-1,p)*pow(d,j,p) for j in range(3))%p
            mats=[[[val(x) for x in row] for row in mat] for mat in T]
            finite={"prime":p,"root":d,"allRationalDenominatorsUnits":True,
                "individualRankLowerBounds":[frank(mat,p) for mat in mats],
                "stackedCommonKernelRankLowerBound":frank([row for mat in mats for row in mat],p)}
            break
        tensor=m.save_gz(out/"complete-original-four-mean-quadratic-matrices.json.gz",
            {"format":FORMAT+"-quadratic-tensor","binding":binding,"data":{
                "fourMonomials":h["tenOriginalGeneratingMonomials"][6:],
                "matrices":[[[m.fv(z) for z in row] for row in mat] for mat in T],
                "symmetryIdentities":symmetric,"fieldRankLowerBounds":finite}})
        model=m.save_gz(out/"complete-original-six-mean-ten-generator-model.json.gz",
            {"format":FORMAT+"-model","binding":binding,"data":{
                "parentNormalFormBinding":NF["binding"],"parentLeadingBinding":LEAD["binding"],
                "tenGeneratingMonomials":h["tenOriginalGeneratingMonomials"],"constantUnit":unit,
                "sixCompleteMeanRows":rows,"completeQuadraticTensor":tensor,
                "sourceIdentity":"Gy_i-small_i=sum nu_ik F_k+sum mu_ij Gw_j",
                "moduleGeneratorIndependenceOrFreenessClaimed":False,
                "allMeanRelationsAndTheirIdealProductsStillRequired":True}})
        rec["parameters"].update({"model":model,"quadraticTensor":tensor,"all72ExactConstantEInverseCoordinatesVerified":True,
            "all96OriginalParameterCoefficientIdentitiesVerified":coeffProducts==96,
            "all30ComposedOriginalFiveSourceIdentitiesVerified":sourceProducts==30,
            "allSixOriginalMeanRelationsRetained":True,"allSixSourceCorrectionsLinearOnlyInY":True,
            "completeMeanMatrixShape":[6,10],"completeOriginalMomentCorrectionShape":[6,11],
            "allFourQuadraticMatricesSymmetric":all(symmetric),"actualQuadraticFieldRankLowerBounds":finite,
            "noParameterSpecializedOrInverted":True,"fullCriticalIdealSolved":False})
        rec["status"]="completed";code=0
    except BaseException as e:
        rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed"
        rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=75 if isinstance(e,TimeoutError) else 1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-start
        rec["maxResidentKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        path=out/"original-six-mean-ten-generator-receipt.json";b=json.dumps(rec,sort_keys=True,indent=2).encode();path.write_bytes(b)
        desc={"path":path.name,"bytes":len(b),"sha256":sha(b)}
        print(json.dumps({"status":rec["status"],"exitCode":code,"binding":binding,"elapsedSeconds":rec["elapsedSeconds"],"receipt":desc,"parameters":rec["parameters"]},sort_keys=True),flush=True)
    return code
if __name__=="__main__":sys.exit(main())
