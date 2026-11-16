#!/usr/bin/env python3
"""Original fifty-five Koszul sources and mixed original95 unit.

Author: Astra-ISP-789f / normal_annihilator, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

Only the paid quartic source dictionaries and completed rank95 phases are read.
The field selects original columns of the same E matrix; exact E coefficients
are defined by that original minor, never by lifting field coordinates.
No parameter polynomial matrices, Bell identities, or new E coefficient arrays
are computed here. All mathematical arrays remain in the temporary directory.
"""
from __future__ import annotations
import argparse,gzip,hashlib,itertools,json,os,resource,signal,sys,time
from pathlib import Path
from flint import nmod_mat
sys.set_int_max_str_digits(0)
FORMAT="r150-original-koszul55-mixed95-source-unit127-v1"
P=127;ROOT=100
PARENT={"format":"r150-original-quartic-syzygy95-small-field-gate127-v1","binding":"9f0ee10f7e4cece784d8140d063f94c210105e7dded9f811710d6ec6f2825fa1","source":{"bytes":15520,"path":"2026-11-16-r150-original-quartic-syzygy95-small-field-gate127-789f.py","sha256":"b6f72e376aa403ff540a01927ea0dd4ac136099cb7be16fe201f91e95968cc4c"},"phases":{"complete-original-quartic95-unit":{"bytes":20816,"logicalBytes":63121,"logicalSha256":"b711688351ce47161d8e898f1322a2e4e0c355bf8d7033d7a6bb2884a95343eb","path":"complete-original-quartic95-unit.json.gz","sha256":"71d679b394ab9c58f542c576690397d8f1cbcba627d74daffd72f9bbb2e3302e"},"whole-original-quartic95-input":{"bytes":16730,"logicalBytes":95934,"logicalSha256":"bf86bf186cd64d3ed78e0bf66b794bca62aa72e71abd3de3335e905c7cea0589","path":"whole-original-quartic95-input.json.gz","sha256":"a2d91336495f29ff2a15958ab26cf2cefcb782eb2e7acac2c88d90fb91a2de07"}},"manifest":{"path":"original-quartic95-manifest.json","bytes":901,"sha256":"11ad47693c39437e3f7d4711a84817e87d96392886802471116da34e1f79dacc"}}
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
    x=identity(p)
    need(all(x[k]==d[k] for k in ("bytes","sha256")),"exact whole file "+Path(p).name)
    return x
def atomic(p,b):
    p=Path(p);t=p.with_name(p.name+".tmp")
    with t.open("wb") as f:f.write(b);f.flush();os.fsync(f.fileno())
    os.replace(t,p)
def mons(n,d):
    out=[]
    for inds in itertools.combinations_with_replacement(range(n),d):
        e=[0]*n
        for i in inds:e[i]+=1
        out.append(tuple(e))
    return out
def mat(a):return nmod_mat(a,P)
def tab(A):return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def eye(n):return mat([[int(i==j) for j in range(n)] for i in range(n)])
def zero(n,m):return nmod_mat(n,m,[0]*(n*m),P)
def select(A,rows,cols):return mat([[int(A[i,j]) for j in cols] for i in rows])
def matrix_checked(a,n,m,label):
    need(type(a) is list and len(a)==n and all(type(r) is list and len(r)==m for r in a),label+" dimensions")
    need(all(type(x) is int and 0<=x<P for r in a for x in r),label+" canonical original field coefficients")
    return mat(a)
def pivots(A):
    rr,r=A.rref();r=int(r)
    ps=[next(j for j in range(A.ncols()) if rr[i,j]) for i in range(r)]
    need(ps==sorted(set(ps)) and len(ps)==r,"ordered original-column rank profile")
    return rr,r,ps
def parent_phase(out,manifest,name):
    d=PARENT["phases"][name]
    need(manifest["phases"].get(name)==d,"exact paid phase descriptor "+name)
    p=out/d["path"];exact(p,d)
    raw=gzip.decompress(p.read_bytes())
    need(len(raw)==d["logicalBytes"] and sha(raw)==d["logicalSha256"],"whole paid logical phase "+name)
    z=json.loads(raw)
    need(z.get("format")==PARENT["format"]+"-phase" and z.get("binding")==PARENT["binding"],
         "same paid original phase format and binding "+name)
    return z["data"]
def main():
    ap=argparse.ArgumentParser()
    for k in ("parent-source","parent-out","out"):ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--seconds",type=float,default=60)
    ap.add_argument("--memory-mib",type=int,default=512)
    a=ap.parse_args()
    need(0<a.seconds<=180 and 256<=a.memory_mib<=1024,"bounded mixed95 original-source consumer")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    a.out.mkdir(parents=True,exist_ok=True)
    need(not any(a.out.iterdir()),"fresh independent output; no unimplemented continuation")
    start=time.monotonic();deadline=start+a.seconds
    own=identity(Path(__file__));binding=None;phases={};code=1
    rec={"format":FORMAT,"source":own,"status":"running","parameters":{
        "seconds":a.seconds,"memoryMiB":a.memory_mib,"prime":P,"coefficientRoot":ROOT,
        "parentRank95Repeated":False,"parameterMatricesConstructed":False,
        "exactECoordinateArraysComputed":False,"BellMembershipClaimed":False}}
    def alarm(sig=None,frame=None):raise Budget("actual whole mixed95 wall budget")
    def tick():
        if time.monotonic()+3>=deadline:raise Budget("whole mixed95 phase budget")
    def event(name,**kw):
        rec["parameters"]["lastEvent"]=name
        print(json.dumps({"phase":name,"elapsedSeconds":time.monotonic()-start,
            "peakRssKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**kw},separators=(",",":")),flush=True)
    def save(name,data):
        raw=canon({"format":FORMAT+"-phase","binding":binding,"data":data})
        p=a.out/(name+".json.gz");atomic(p,gzip.compress(raw,compresslevel=1,mtime=0))
        d={**identity(p),"logicalBytes":len(raw),"logicalSha256":sha(raw)}
        newer=dict(phases);newer[name]=d
        atomic(a.out/"original-koszul55-mixed95-manifest.json",canon({
            "format":FORMAT+"-manifest","binding":binding,"source":own,"phases":newer}))
        phases[name]=d
        return d
    signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds)
    try:
        import flint
        need(tuple(sys.version_info[:3])==(3,12,14) and flint.__version__=="0.9.0","fixed original mathematical runtime")
        actual_source=exact(a.parent_source,PARENT["source"])
        need(actual_source["path"]==PARENT["source"]["path"],"same original parent source basename")
        mp=a.parent_out/PARENT["manifest"]["path"];exact(mp,PARENT["manifest"])
        pm=json.loads(mp.read_bytes())
        need(pm=={"format":PARENT["format"]+"-manifest","binding":PARENT["binding"],
            "source":PARENT["source"],"phases":PARENT["phases"]},"complete paid manifest, without descriptor substitution")
        inp=parent_phase(a.parent_out,pm,"whole-original-quartic95-input")
        paid=parent_phase(a.parent_out,pm,"complete-original-quartic95-unit")
        sem=inp["semantic"]
        need(sha(canon(sem))==PARENT["binding"] and sem.get("format")==PARENT["format"] and
             sem.get("source")==PARENT["source"] and sem.get("prime")==P and sem.get("root")==ROOT,
             "complete original parent semantic binding")
        M2,M3,M4=mons(5,2),mons(5,3),mons(5,4)
        p2={e:i for i,e in enumerate(M2)}
        clabel=[(g,k) for g in range(11) for k in range(5)]
        dlabel=[(g,e) for g in range(11) for e in M2]
        lowlabels=[(0,j,k) for j in range(1,5) for k in range(5)]
        tlabels=[(ell,s) for ell in range(5) for s in range(20)]
        need(sem["quadraticRows"]==[list(e) for e in M2] and sem["cubicRows"]==[list(e) for e in M3] and
             sem["quarticRows"]==[list(e) for e in M4],"all original ordinary-monomial row dictionaries")
        need(sem["cubicSourceLabels"]==[list(x) for x in clabel] and
             sem["quarticSourceLabels"]==[[g,list(e)] for g,e in dlabel] and
             sem["selectedLowLabels"]==[list(x) for x in lowlabels] and
             sem["selectedLowSeedIds"]==LOW_IDS and sem["multipliedLowLabels"]==[list(x) for x in tlabels],
             "complete original eleven-source, low20 and multiplied100 column dictionaries")
        q=inp["allOriginalQuadraticCoefficients"]
        Q=matrix_checked(q,11,15,"all original quadratic tops")
        Z=matrix_checked(inp["selectedLow20SourceMatrix"],55,20,"paid selected twenty cubic sources")
        D=matrix_checked(inp["originalQuarticMatrix"],70,165,"paid complete quartic multiplication")
        T=matrix_checked(inp["allHundredMultipliedLowSources"],165,100,"paid all100 multiplied low sources")
        need(int(Q.rank())==11,"original eleven quadratic tops independent at the legal coefficient place")
        need(paid["rank"]==95 and paid["originalUnitDeterminant127"]==38 and
             inp["lowProjectedDeterminant127"]==64,"same actual original rank95 and low20 units")
        for k in ("all242QuadraticInverseProductsVerified","all225QuadraticSourceProductsVerified",
                  "all2450CubicInverseProductsVerified","all560CubicBorderProductsVerified",
                  "all700LowKernelProductsVerified","all7000MultipliedLowKernelProductsVerified",
                  "all2800HighKernelProductsVerified"):
            need(inp.get(k) is True,"paid complete input gate "+k)
        for k in ("all18050OriginalUnitInverseProductsVerified","all6600OriginalHighCoordinatesVerified",
                  "all16500OriginalSourceSpanCoordinatesVerified","all825CompleteSecondSyzygyProductsVerified"):
            need(paid.get(k) is True,"paid completed rank95 gate "+k)
        rows=paid["originalUnitRows"];oldcols=paid["originalUnitColumns"]
        need(len(rows)==95 and rows==sorted(set(rows)) and all(type(i) is int and 0<=i<165 for i in rows),
             "actual original95 row projection")
        need(len(oldcols)==95 and oldcols==sorted(set(oldcols)) and all(type(i) is int and 0<=i<100 for i in oldcols),
             "actual old95 original column dictionary")
        rebuiltD=[]
        for e in M4:
            r=[]
            for g,m in dlabel:
                rem=tuple(e[k]-m[k] for k in range(5))
                r.append(q[g][p2[rem]] if min(rem)>=0 and rem in p2 else 0)
            rebuiltD.append(r)
        need(D==mat(rebuiltD),"all11550 original D coordinates reconstructed from the same q coefficients")
        rebuiltT=[[0]*100 for _ in range(165)]
        for c,(ell,s) in enumerate(tlabels):
            for g,k in clabel:
                e=tuple(int(a==ell)+int(a==k) for a in range(5))
                rr=15*g+p2[e]
                rebuiltT[rr][c]=(rebuiltT[rr][c]+int(Z[5*g+k,s]))%P
        need(T==mat(rebuiltT),"all16500 original T coordinates reconstructed from the same twenty sources")
        semantic={"format":FORMAT,"source":own,"parent":PARENT,"prime":P,"root":ROOT,
            "originalQuarticSourceLabels":sem["quarticSourceLabels"],
            "actualOriginalUnitRows":rows,"koszulSourceLabels":[list(x) for x in itertools.combinations(range(11),2)],
            "allOriginalMultipliedLabels":sem["multipliedLowLabels"],"selectedLowSeedIds":LOW_IDS,
            "selectionRule":"original55 Koszul columns first, then original100 multiplied-low columns in their paid order"}
        binding=sha(canon(semantic));rec["binding"]=binding;rec["parameters"]["semantic"]=semantic
        event("paid-whole-original-dictionaries-verified");tick()
        klabels=list(itertools.combinations(range(11),2))
        Karr=[[0]*55 for _ in range(165)]
        for c,(aa,bb) in enumerate(klabels):
            for m in range(15):
                Karr[15*bb+m][c]=(Karr[15*bb+m][c]+q[aa][m])%P
                Karr[15*aa+m][c]=(Karr[15*aa+m][c]-q[bb][m])%P
        K=mat(Karr)
        need(int(K.rank())==55 and D*K==zero(70,55),"all55 original Koszul sources independent and all3850 original products zero")
        KI=select(K,rows,range(55));TI=select(T,rows,range(100))
        combined=mat([[int(KI[i,j]) for j in range(55)]+[int(TI[i,j]) for j in range(100)] for i in range(95)])
        rr,mixedrank,pc=pivots(combined)
        need(mixedrank==95 and pc[:55]==list(range(55)),"original Koszul55 followed by exactly40 actual original T pivots")
        chosen=[j-55 for j in pc[55:]]
        need(len(chosen)==40 and chosen==sorted(set(chosen)) and all(0<=j<100 for j in chosen),
             "complete forty original multiplied-low source labels")
        mixed=mat([[int(K[i,j]) for j in range(55)]+[int(T[i,j]) for j in chosen] for i in range(165)])
        MI=select(mixed,rows,range(95));det=int(MI.det())
        need(det!=0,"same original mixed95 minor has a nonzero legal-place residue")
        inverse=MI.inv()
        need(MI*inverse==eye(95) and inverse*MI==eye(95),"all18050 new mixed95 inverse coordinates")
        tick();coords=inverse*combined
        original155=mat([[int(K[i,j]) for j in range(55)]+[int(T[i,j]) for j in range(100)] for i in range(165)])
        need(mixed*coords==original155,"all25575 full original-source coordinates for every Koszul and multiplied-low column")
        need(select(coords,range(95),pc)==eye(95),"all9025 complete selected mixed-column identity coordinates")
        selected40=select(coords,range(95),[55+j for j in chosen])
        need(selected40==mat([[int(i==55+j) for j in range(40)] for i in range(95)]),
             "all3800 selected40 coordinate normalizations")
        labels=[tlabels[j] for j in chosen]
        sourceids=[[ell,LOW_IDS[s]] for ell,s in labels]
        result={"original55KoszulLabels":[list(x) for x in klabels],"original55KoszulCoefficients":Karr,
            "actualOriginalUnitRows":rows,"originalMixedPivotColumns":pc,
            "selectedOriginalMultipliedColumnIds":chosen,"selectedOriginalMultipliedLabels":[list(x) for x in labels],
            "selectedOriginalLowSeedLabels":sourceids,"mixedOriginal95UnitDeterminant127":det,
            "mixedOriginal95UnitInverse":tab(inverse),"fieldAll155OriginalCoordinates":tab(coords),
            "koszulRank":55,"mixedRank":95,"koszulQuotientDimension":40,
            "all11550OriginalQuarticCoordinatesReconstructed":True,"all16500OriginalMultipliedCoordinatesReconstructed":True,
            "all3850OriginalKoszulProductsVerified":True,"all18050MixedInverseProductsVerified":True,
            "all25575OriginalFullSourceCoordinatesVerified":True,"all9025SelectedMixedIdentityCoordinatesVerified":True,
            "all3800SelectedFortyIdentityCoordinatesVerified":True,
            "exactECoordinateArraysComputed":False,
            "exactEConclusionMethod":"same original mixed E minor; exact coefficients from its adjugate, not lifted field coordinates",
            "originalParameterMatricesConstructed":False,"newBellMembershipConclusion":False}
        desc=save("complete-original-koszul55-mixed95-unit",result)
        rec["parameters"].update({k:v for k,v in result.items() if k not in
            ("original55KoszulCoefficients","mixedOriginal95UnitInverse","fieldAll155OriginalCoordinates")})
        rec["parameters"]["conditionalOriginalEGradientGeneratorBound"]=200
        rec["parameters"]["conditionalOriginalEBellGeneratorBound"]=210
        rec["parameters"]["completePhase"]=desc
        event("complete-original-koszul55-mixed95-unit",rank=95,koszulRank=55,selectedCount=40,
              mixedUnitDeterminant127=det,all25575OriginalCoordinatesVerified=True)
        rec["status"]="completed";code=0;return code
    except Budget as e:
        rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=75;return code
    except BaseException as e:
        rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=1;return code
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        rec["parameters"]["elapsedSeconds"]=time.monotonic()-start
        rec["parameters"]["peakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rec["parameters"]["exitCode"]=code;rec["parameters"]["completePhases"]=phases
        rec["parameters"]["interruptedExactConstantsStageClaimedComplete"]=False
        atomic(a.out/"original-koszul55-mixed95-receipt.json",canon(rec))
        print(json.dumps(rec,separators=(",",":")),flush=True)
if __name__=="__main__":raise SystemExit(main())
