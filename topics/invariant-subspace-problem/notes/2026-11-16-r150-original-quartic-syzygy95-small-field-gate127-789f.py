#!/usr/bin/env python3
"""Original quartic-syzygy 95 unit gate at the paid coefficient place.

Author: Astra-ISP-789f / normal_annihilator, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

All matrices use the original eleven quadratic tops and source dictionaries.
A field rank95 unit specifies an original E minor; field coordinates are NOT
lifted as exact E coefficients. No new Bell membership is claimed. All arrays
remain temporary. This source is independent of the interrupted exact run.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,itertools,json,os,resource,signal,sys,time
from pathlib import Path
from flint import nmod_mat
sys.set_int_max_str_digits(0)
FORMAT="r150-original-quartic-syzygy95-small-field-gate127-v1"
P=127;ROOT=100
HELPER={"bytes":33539,"sha256":"d9d98bc379e322e9c212b7ad7721399ec8b1bab9970a2755700338f7053d47da"}
FIELD_SOURCE={"bytes":23879,"sha256":"4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4"}
KEEP=[(1,4),(2,3),(2,4),(3,4)]
LOW_IDS=[10*j+k for j in range(4) for k in range(1,6)]
class Budget(Exception):pass
def need(ok,msg):
    if not ok:raise ValueError(msg)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(p):
    p=Path(p);h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def exact(p,d):
    a=identity(p);need(all(a[k]==d[k] for k in ("bytes","sha256")),"exact source "+Path(p).name);return a
def atomic(p,b):
    p=Path(p);t=p.with_name(p.name+".tmp")
    with t.open("wb") as f:f.write(b);f.flush();os.fsync(f.fileno())
    os.replace(t,p)
def mons(n,d):
    result=[]
    for inds in itertools.combinations_with_replacement(range(n),d):
        e=[0]*n
        for i in inds:e[i]+=1
        result.append(tuple(e))
    return result
def mat(a):return nmod_mat(a,P)
def tab(A):return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def eye(n):return mat([[int(i==j) for j in range(n)] for i in range(n)])
def zero(n,m):return nmod_mat(n,m,[0]*(n*m),P)
def selected(A,rows,cols):return mat([[int(A[i,j]) for j in cols] for i in rows])
def pivots(A):
    rr,r=A.rref()
    ps=[next(j for j in range(A.ncols()) if rr[i,j]) for i in range(r)]
    need(ps==sorted(set(ps)) and len(ps)==r,"complete original-column pivot dictionary")
    return rr,r,ps
def main():
    ap=argparse.ArgumentParser()
    for k in ("exact-helper","field-model-source","field-model-out","out"):ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--seconds",type=float,default=30)
    ap.add_argument("--memory-mib",type=int,default=512)
    a=ap.parse_args();need(0<a.seconds<=180 and 256<=a.memory_mib<=1024,"bounded small original field gate")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    a.out.mkdir(parents=True,exist_ok=True)
    need(not any(a.out.iterdir()),"fresh independent small-gate output; no unimplemented continuation")
    start=time.monotonic();deadline=start+a.seconds
    code=1;own=identity(Path(__file__));binding=None;phases={}
    rec={"format":FORMAT,"source":own,"status":"running","parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib,
        "prime":P,"coefficientRoot":ROOT,"exactEHighCoefficientArraysComputed":False,"BellUnitClaimed":False}}
    def tick():
        if time.monotonic()+5>=deadline:raise Budget("whole small original quartic gate budget")
    def alarm(sig=None,frame=None):raise Budget("actual small original quartic gate wall budget")
    def event(name,**kw):
        rec["parameters"]["lastEvent"]=name
        print(json.dumps({"phase":name,"elapsedSeconds":time.monotonic()-start,
            "peakRssKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**kw},separators=(",",":")),flush=True)
    def save(name,data):
        raw=canon({"format":FORMAT+"-phase","binding":binding,"data":data})
        p=a.out/(name+".json.gz");atomic(p,gzip.compress(raw,compresslevel=1,mtime=0))
        desc={**identity(p),"logicalBytes":len(raw),"logicalSha256":sha(raw)};phases[name]=desc
        atomic(a.out/"original-quartic95-manifest.json",canon({"format":FORMAT+"-manifest","binding":binding,
            "source":own,"phases":phases}));return desc
    signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds)
    try:
        import flint
        need(tuple(sys.version_info[:3])==(3,12,14) and flint.__version__=="0.9.0","fixed original small-field runtime")
        exact(a.exact_helper,HELPER);exact(a.field_model_source,FIELD_SOURCE)
        sp=importlib.util.spec_from_file_location("quartic95_paid_exact_helper",a.exact_helper)
        h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
        need(h.PRIME==P and h.ROOT==ROOT and h.KEEP==KEEP,"same original coefficient place and retained quadratics")
        paid,parent=h.read_paid_base(a.field_model_out)
        M2,M3,M4=mons(5,2),mons(5,3),mons(5,4)
        p2={e:i for i,e in enumerate(M2)};p3={e:i for i,e in enumerate(M3)};p4={e:i for i,e in enumerate(M4)}
        keep=[tuple(int(k==i)+int(k==j) for k in range(5)) for i,j in KEEP]
        kp=[p2[e] for e in keep];elim=[i for i in range(15) if i not in kp]
        need(M2==h.M2 and M3==h.M3 and elim==h.ELIM,"same original ordinary source dictionaries")
        q=paid["top"];need(len(q)==11 and all(len(r)==15 for r in q),"all165 original quadratic coefficients")
        Q=mat(q);A2=mat([[q[g][j] for g in range(11)] for j in elim]);AI=mat(paid["quadraticUnitInverse"])
        need(tab(A2)==paid["quadraticUnit"] and int(A2.det())==paid["quadraticUnitDeterminant127"]!=0,
             "all original eleven-source unit coefficients")
        need(A2*AI==eye(11) and AI*A2==eye(11),"all242 original quadratic inverse products")
        alpha=[];rho=[]
        for j in range(15):
            v=[int(AI[g,elim.index(j)]) if j in elim else 0 for g in range(11)]
            qa=[sum(q[g][k]*v[g] for g in range(11))%P for k in range(15)]
            rr=[(int(j==k)-qa[k])%P for k in kp]
            need(all((qa[k]+(rr[kp.index(k)] if k in kp else 0))%P==int(j==k) for k in range(15)),
                 "all225 complete original quadratic normal-source products")
            alpha.append(v);rho.append(rr)
        clabel=[(g,k) for g in range(11) for k in range(5)]
        C=[]
        for e in M3:
            row=[]
            for g,k in clabel:
                if e[k]:
                    t=list(e);t[k]-=1;row.append(q[g][p2[tuple(t)]])
                else:row.append(0)
            C.append(row)
        C=mat(C)
        need([list(x) for x in clabel]==paid["all55OriginalCubicLabels"] and
             [list(x) for x in M3]==paid["all35OriginalCubicMonomials"],"all original cubic row and source labels")
        cr,crank,cp=pivots(C)
        need(crank==35 and cp==list(range(35))==paid["selectedOriginalCubicColumns"],
             "same complete original35 cubic rank profile")
        CB=selected(C,range(35),cp);CI=mat(paid["cubicUnitInverse"])
        need(tab(CB)==paid["cubicUnit"] and int(CB.det())==32==paid["cubicUnitDeterminant127"] and
             CB*CI==eye(35) and CI*CB==eye(35),"all2450 original cubic unit inverse products")
        X={};paths=[]
        for i in range(5):
            for v,e0 in enumerate(keep):
                e=list(e0);e[i]+=1;e=tuple(e)
                if e not in X:X[e]=[int(CI[k,p3[e]]) if k<35 else 0 for k in range(55)]
                paths.append((i,v,e))
        xkeys=sorted(X)
        need(len(xkeys)==16,"all20 original border paths use exactly sixteen cubic monomials")
        XM=mat([[X[e][r] for e in xkeys] for r in range(55)])
        need(C*XM==mat([[int(e==f) for f in xkeys] for e in M3]),"all560 original sixteen cubic source products")
        lowlabels=[(0,j,k) for j in range(1,5) for k in range(5)]
        need([10*(j-1)+1+k for i,j,k in lowlabels]==LOW_IDS,"same selected original low20 indices")
        Z=[]
        for i,j,k in lowlabels:
            ik=p2[tuple(int(a==i)+int(a==k) for a in range(5))]
            jk=p2[tuple(int(a==j)+int(a==k) for a in range(5))]
            z=[0]*55
            for g in range(11):
                z[5*g+j]=(z[5*g+j]+alpha[ik][g])%P
                z[5*g+i]=(z[5*g+i]-alpha[jk][g])%P
            for v,e0 in enumerate(keep):
                ej=list(e0);ej[j]+=1;ei=list(e0);ei[i]+=1
                for r in range(55):z[r]=(z[r]+rho[ik][v]*X[tuple(ej)][r]-rho[jk][v]*X[tuple(ei)][r])%P
            Z.append(z)
        Z=mat([[Z[s][r] for s in range(20)] for r in range(55)])
        need(C*Z==zero(35,20),"all700 original selected cubic-kernel products")
        projected=selected(Z,range(35,55),range(20));lowdet=int(projected.det())
        need(lowdet!=0 and Z.rank()==20,"same original low20 basis, not inferred from a column count")
        dlabel=[(g,e) for g in range(11) for e in M2]
        D=[]
        for e in M4:
            row=[]
            for g,m in dlabel:
                r=tuple(e[k]-m[k] for k in range(5))
                row.append(q[g][p2[r]] if min(r)>=0 and r in p2 else 0)
            D.append(row)
        D=mat(D);need(D.rank()==70,"complete original quartic output rank70")
        def shift_source(v,ell):
            result=[0]*165
            for g,k in clabel:
                e=tuple(int(a==ell)+int(a==k) for a in range(5));t=15*g+p2[e]
                result[t]=(result[t]+v[5*g+k])%P
            return result
        ulabels=[(ell,s) for ell in range(5) for s in range(20)]
        Ucols=[shift_source([int(Z[r,s]) for r in range(55)],ell) for ell,s in ulabels]
        UM=mat([[v[r] for v in Ucols] for r in range(165)])
        need(D*UM==zero(70,100),"all7000 original multiplied cubic-syzygy products")
        pairs=list(itertools.combinations(range(5),2));hlabels=[];Hcols=[]
        for i,j in pairs:
            for v,e0 in enumerate(keep):
                ei=list(e0);ei[i]+=1;ej=list(e0);ej[j]+=1
                left=shift_source(X[tuple(ei)],j);right=shift_source(X[tuple(ej)],i)
                Hcols.append([(a-b)%P for a,b in zip(left,right)]);hlabels.append((i,j,v))
        HM=mat([[v[r] for v in Hcols] for r in range(165)])
        need(D*HM==zero(70,40),"all2800 original high leading-source syzygy products")
        semantic={"format":FORMAT,"source":own,"helper":HELPER,"fieldSource":FIELD_SOURCE,"paidParent":parent,
            "prime":P,"root":ROOT,"matchedCubic":h.MATCHED,"quadraticRows":[list(e) for e in M2],"cubicRows":[list(e) for e in M3],
            "quarticRows":[list(e) for e in M4],"cubicSourceLabels":[list(x) for x in clabel],
            "quarticSourceLabels":[[g,list(e)] for g,e in dlabel],
            "selectedLowLabels":[list(x) for x in lowlabels],"selectedLowSeedIds":LOW_IDS,
            "multipliedLowLabels":[list(x) for x in ulabels],"allHighLabels":[list(x) for x in hlabels]}
        binding=sha(canon(semantic));rec["binding"]=binding;rec["parameters"]["semantic"]=semantic
        constants={"semantic":semantic,"allOriginalQuadraticCoefficients":q,"originalCubicMatrix":tab(C),
            "selectedLow20SourceMatrix":tab(Z),"originalQuarticMatrix":tab(D),"allHundredMultipliedLowSources":tab(UM),
            "allFortyHighLeadingSources":tab(HM),"lowProjectedDeterminant127":lowdet,
            "all242QuadraticInverseProductsVerified":True,"all225QuadraticSourceProductsVerified":True,
            "all2450CubicInverseProductsVerified":True,"all560CubicBorderProductsVerified":True,
            "all700LowKernelProductsVerified":True,"all7000MultipliedLowKernelProductsVerified":True,
            "all2800HighKernelProductsVerified":True}
        save("whole-original-quartic95-input",constants);event("whole-original-quartic95-input")
        tick();rr,rank,cols=pivots(UM)
        need(rank<=95,"original quartic kernel has dimension95")
        rec["parameters"].update({"originalQuarticRank":70,"multipliedLowRank":rank,"remainingKernelDimension":95-rank,
            "allOriginalProductGatesVerified":True,"lowProjectedDeterminant127":lowdet})
        if rank<95:
            rec["status"]="completed-diagnostic";rec["parameters"]["exactE95SurjectivityProved"]=False;code=0;return code
        UB=selected(UM,range(165),cols);rt,rk,rows=pivots(UB.transpose())
        need(rk==95 and len(rows)==95,"actual original95 row and column unit")
        A=selected(UM,rows,cols);det=int(A.det());need(det!=0,"actual original unit95 determinant")
        AI95=A.inv();need(A*AI95==eye(95) and AI95*A==eye(95),"all18050 original unit95 inverse products")
        beta=AI95*selected(HM,rows,range(40))
        need(UB*beta==HM,"all6600 complete original high source coordinates in the multiplied low basis")
        allbeta=AI95*selected(UM,rows,range(100))
        need(UB*allbeta==UM,"all16500 original multiplied-source span coordinates")
        free=[j for j in range(100) if j not in cols]
        need(len(free)==5,"actual five complete linear second syzygy directions")
        K=[[0]*5 for _ in range(100)]
        for a0,j in enumerate(free):
            K[j][a0]=1
            for i,p in enumerate(cols):K[p][a0]=(-int(rr[i,j]))%P
        KM=mat(K);need(UM*KM==zero(165,5),"all825 original complete second-syzygy products")
        result={"originalUnitRows":rows,"originalUnitColumns":cols,"originalUnitDeterminant127":det,
            "unitInverse":tab(AI95),"fieldHighCoordinates":tab(beta),"fieldAllMultipliedCoordinates":tab(allbeta),
            "completeFiveKernelFreeIndices":free,"completeFiveKernelColumns":K,"rank":95,
            "all18050OriginalUnitInverseProductsVerified":True,"all6600OriginalHighCoordinatesVerified":True,
            "all16500OriginalSourceSpanCoordinatesVerified":True,"all825CompleteSecondSyzygyProductsVerified":True,
            "exactEConclusionMethod":"same original E95 minor has nonzero legal-place residue; adjugate over E, not lifted field coefficients",
            "originalEHighSourceCoefficientArraysComputed":False,"newBellMembershipConclusion":False}
        save("complete-original-quartic95-unit",result);event("complete-original-quartic95-unit",rank=95,unitDeterminant127=det)
        rec["parameters"].update({"exactE95SurjectivityProved":True,"originalUnitDeterminant127":det,
            "all18050OriginalUnitInverseProductsVerified":True,"all6600OriginalHighCoordinatesVerified":True,
            "all16500OriginalSourceSpanCoordinatesVerified":True,"all825CompleteSecondSyzygyProductsVerified":True,
            "conditionalExactESeedBoundAfterCanonicalSourceTheorem":270})
        rec["status"]="completed";code=0;return code
    except Budget as e:
        rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=75;return code
    except BaseException as e:
        rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1;return code
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        rec["parameters"]["elapsedSeconds"]=time.monotonic()-start
        rec["parameters"]["peakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rec["parameters"]["exitCode"]=code;rec["parameters"]["completePhases"]=phases
        atomic(a.out/"original-quartic95-receipt.json",canon(rec))
        print(json.dumps(rec,separators=(",",":")),flush=True)
if __name__=="__main__":raise SystemExit(main())
