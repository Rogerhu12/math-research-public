#!/usr/bin/env python3
"""Complete original quintic Koszul-span gate and all300 multiplied-low sources.

Author: Astra-ISP-789f / normal_annihilator, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

The source uses all385 original cubic source coordinates, all126 quintic
outputs, all275 linear multiples of the55 original Koszul sources and all300
ordinary quadratic multiples of the original low20 sources. Rank259 is a gate,
not a preset answer. Field coordinates are never lifted as exact E coefficients.
"""
from __future__ import annotations
import argparse,gzip,hashlib,itertools,json,os,resource,signal,sys,time
from pathlib import Path
from flint import nmod_mat
sys.set_int_max_str_digits(0)
FORMAT="r150-original-quintic-koszul-span259-unit127-v1"
P=127;ROOT=100
HIGH={"format":"r150-original-quartic-syzygy95-small-field-gate127-v1","binding":"9f0ee10f7e4cece784d8140d063f94c210105e7dded9f811710d6ec6f2825fa1","source":{"bytes":15520,"path":"2026-11-16-r150-original-quartic-syzygy95-small-field-gate127-789f.py","sha256":"b6f72e376aa403ff540a01927ea0dd4ac136099cb7be16fe201f91e95968cc4c"},"phases":{"complete-original-quartic95-unit":{"bytes":20816,"logicalBytes":63121,"logicalSha256":"b711688351ce47161d8e898f1322a2e4e0c355bf8d7033d7a6bb2884a95343eb","path":"complete-original-quartic95-unit.json.gz","sha256":"71d679b394ab9c58f542c576690397d8f1cbcba627d74daffd72f9bbb2e3302e"},"whole-original-quartic95-input":{"bytes":16730,"logicalBytes":95934,"logicalSha256":"bf86bf186cd64d3ed78e0bf66b794bca62aa72e71abd3de3335e905c7cea0589","path":"whole-original-quartic95-input.json.gz","sha256":"a2d91336495f29ff2a15958ab26cf2cefcb782eb2e7acac2c88d90fb91a2de07"}},"manifest":{"path":"original-quartic95-manifest.json","bytes":901,"sha256":"11ad47693c39437e3f7d4711a84817e87d96392886802471116da34e1f79dacc"}}
MIXED={"format":"r150-original-koszul55-mixed95-source-unit127-v1","binding":"b0d3f4b6dfefddccd68f804561d74188c109c151329ac525e2f7b0d2e90a6232","source":{"path":"2026-11-16-r150-original-koszul55-mixed95-source-unit127-789f.py","bytes":16461,"sha256":"fc1dfea5219a773af1140c3c9e8ba52bcb6acfd36ae67bd325c9317e416d0ab5"},"phases":{"complete-original-koszul55-mixed95-unit":{"bytes":24225,"logicalBytes":86134,"logicalSha256":"4214f41007b68fef5ecf152c769030cd1fb850dbd87d350ea49efd5da55885db","path":"complete-original-koszul55-mixed95-unit.json.gz","sha256":"4309a9164324c4e7ccf214d25b97c96845feb0e93a0dd0998e6e0a226c5e0841"}},"manifest":{"path":"original-koszul55-mixed95-manifest.json","bytes":628,"sha256":"d9211fac3cc3ff06abd00b8ff2b2dec4cb9efc685a6f982027f6a998651054e5"}}
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
    x=identity(p);need(all(x[k]==d[k] for k in ("bytes","sha256")),"exact whole file "+Path(p).name)
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
def selected(A,rows,cols):return mat([[int(A[i,j]) for j in cols] for i in rows])
def checked(a,n,m,label):
    need(type(a) is list and len(a)==n and all(type(r) is list and len(r)==m for r in a),label+" whole shape")
    need(all(type(x) is int and 0<=x<P for r in a for x in r),label+" canonical field coefficients")
    return mat(a)
def pivots(A):
    rr,r=A.rref();r=int(r)
    ps=[next(j for j in range(A.ncols()) if rr[i,j]) for i in range(r)]
    need(ps==sorted(set(ps)) and len(ps)==r,"ordered original source pivots")
    return rr,r,ps
def paid_manifest(out,source,pin):
    si=exact(source,pin["source"]);need(si==pin["source"],"exact original parent source name")
    mp=out/pin["manifest"]["path"];exact(mp,pin["manifest"]);obj=json.loads(mp.read_bytes())
    need(obj=={"format":pin["format"]+"-manifest","binding":pin["binding"],"source":pin["source"],"phases":pin["phases"]},
         "complete original parent manifest without substituted descriptors")
    return obj
def paid_phase(out,manifest,pin,name):
    d=pin["phases"][name];need(manifest["phases"].get(name)==d,"complete paid phase descriptor")
    p=out/d["path"];exact(p,d);raw=gzip.decompress(p.read_bytes())
    need(len(raw)==d["logicalBytes"] and sha(raw)==d["logicalSha256"],"whole paid logical phase "+name)
    z=json.loads(raw);need(z["format"]==pin["format"]+"-phase" and z["binding"]==pin["binding"],"same paid phase binding")
    return z["data"]
def main():
    ap=argparse.ArgumentParser()
    for k in ("high95-source","high95-out","mixed95-source","mixed95-out","out"):
        ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--seconds",type=float,default=60)
    ap.add_argument("--memory-mib",type=int,default=512)
    a=ap.parse_args()
    need(0<a.seconds<=180 and 256<=a.memory_mib<=1024,"bounded original small quintic gate")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    a.out.mkdir(parents=True,exist_ok=True)
    need(not any(a.out.iterdir()),"fresh independent quintic output; no unimplemented continuation")
    start=time.monotonic();deadline=start+a.seconds;own=identity(Path(__file__))
    code=1;binding=None;phases={}
    rec={"format":FORMAT,"source":own,"status":"running","parameters":{
        "seconds":a.seconds,"memoryMiB":a.memory_mib,"prime":P,"coefficientRoot":ROOT,
        "rank259Prefilled":False,"parameterMatricesConstructed":False,
        "exactECoefficientArraysComputed":False,"BellIdentityClaimed":False}}
    def alarm(sig=None,frame=None):raise Budget("actual original quintic gate wall budget")
    def tick():
        if time.monotonic()+3>=deadline:raise Budget("whole original quintic gate phase budget")
    def event(name,**kw):
        rec["parameters"]["lastEvent"]=name
        print(json.dumps({"phase":name,"elapsedSeconds":time.monotonic()-start,
            "peakRssKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**kw},separators=(",",":")),flush=True)
    def save(name,data):
        raw=canon({"format":FORMAT+"-phase","binding":binding,"data":data})
        p=a.out/(name+".json.gz");atomic(p,gzip.compress(raw,compresslevel=1,mtime=0))
        d={**identity(p),"logicalBytes":len(raw),"logicalSha256":sha(raw)}
        nxt=dict(phases);nxt[name]=d
        atomic(a.out/"original-quintic-koszul259-manifest.json",canon({
            "format":FORMAT+"-manifest","binding":binding,"source":own,"phases":nxt}))
        phases[name]=d;return d
    signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds)
    try:
        import flint
        need(tuple(sys.version_info[:3])==(3,12,14) and flint.__version__=="0.9.0","fixed original coefficient runtime")
        hm=paid_manifest(a.high95_out,a.high95_source,HIGH)
        hi=paid_phase(a.high95_out,hm,HIGH,"whole-original-quartic95-input")
        hp=paid_phase(a.high95_out,hm,HIGH,"complete-original-quartic95-unit")
        mm=paid_manifest(a.mixed95_out,a.mixed95_source,MIXED)
        mix=paid_phase(a.mixed95_out,mm,MIXED,"complete-original-koszul55-mixed95-unit")
        need(sha(canon(hi["semantic"]))==HIGH["binding"],"same complete original high95 semantic")
        M2,M3,M5=mons(5,2),mons(5,3),mons(5,5)
        i2={e:i for i,e in enumerate(M2)};i3={e:i for i,e in enumerate(M3)}
        clabel=[(g,k) for g in range(11) for k in range(5)]
        sem0=hi["semantic"]
        need(sem0["quadraticRows"]==[list(e) for e in M2] and sem0["cubicRows"]==[list(e) for e in M3] and
             sem0["cubicSourceLabels"]==[list(x) for x in clabel] and sem0["selectedLowSeedIds"]==LOW_IDS,
             "complete same original low20 and ordinary monomial dictionaries")
        need(sem0["prime"]==P and sem0["root"]==ROOT and
             sem0["matchedCubic"]==[52565262336,6080833024,-43931504,3725],"same original E and legal coefficient place")
        Q=checked(hi["allOriginalQuadraticCoefficients"],11,15,"original quadratic tops")
        Z=checked(hi["selectedLow20SourceMatrix"],55,20,"original selected cubic syzygies")
        q=tab(Q);need(int(Q.rank())==11 and int(Z.rank())==20,"same actual original eleven and low20 ranks")
        need(hp["rank"]==95 and hp["originalUnitDeterminant127"]==38 and
             hi["all700LowKernelProductsVerified"] is True and
             hp["all6600OriginalHighCoordinatesVerified"] is True and hp["all16500OriginalSourceSpanCoordinatesVerified"] is True,
             "completed original quartic kernel and high-source theorem inputs")
        need(mix["koszulRank"]==55 and mix["mixedRank"]==95 and mix["mixedOriginal95UnitDeterminant127"]==69 and
             mix["selectedOriginalMultipliedColumnIds"]==list(range(34))+list(range(40,45))+[60] and
             mix["actualOriginalUnitRows"]==hp["originalUnitRows"] and
             mix["all25575OriginalFullSourceCoordinatesVerified"] is True and mix["all18050MixedInverseProductsVerified"] is True,
             "same completed original mixed95 source selection")
        source_labels=[(g,m) for g in range(11) for m in M3]
        pairs=list(itertools.combinations(range(11),2))
        klabels=[(ell,aa,bb) for ell in range(5) for aa,bb in pairs]
        hlabels=[(mi,s) for mi in range(15) for s in range(20)]
        dictionaries={"quadraticMonomials":[list(e) for e in M2],"cubicMonomials":[list(e) for e in M3],
            "quinticMonomials":[list(e) for e in M5],"original385SourceLabels":[[g,list(m)] for g,m in source_labels],
            "all275KoszulLabels":[list(x) for x in klabels],"all300MultipliedLowLabels":[list(x) for x in hlabels],
            "selectedLowSeedIds":LOW_IDS}
        need(len(M2)==15 and len(M3)==35 and len(M5)==126 and len(source_labels)==385 and len(klabels)==275 and len(hlabels)==300,
             "all original dimensions and complete dictionaries")
        semantic={"format":FORMAT,"source":own,"high95":HIGH,"mixed95":MIXED,"prime":P,"root":ROOT,
            "dictionarySha256":sha(canon(dictionaries)),"ordinarySourceShape":[385,275],
            "completeTargetShape":[385,300],"originalOutputShape":[126,385],
            "originalLowSeedIds":LOW_IDS,"maximumKernelDimension":259,
            "selectionRule":"all275 original linear Koszul multiples in (ell,a,b) order; original-column pivots and original-row unit"}
        binding=sha(canon(semantic));rec["binding"]=binding;rec["parameters"]["semantic"]=semantic
        darr=[]
        for e in M5:
            row=[]
            for g,m in source_labels:
                rem=tuple(e[k]-m[k] for k in range(5))
                row.append(q[g][i2[rem]] if min(rem)>=0 and rem in i2 else 0)
            darr.append(row)
        D=mat(darr);dr=int(D.rank())
        need(dr==126,"complete original quintic map is actually surjective")
        karr=[[0]*275 for _ in range(385)]
        for c,(ell,aa,bb) in enumerate(klabels):
            for m,e in enumerate(M2):
                ee=list(e);ee[ell]+=1;rr=i3[tuple(ee)]
                karr[35*bb+rr][c]=(karr[35*bb+rr][c]+q[aa][m])%P
                karr[35*aa+rr][c]=(karr[35*aa+rr][c]-q[bb][m])%P
        K=mat(karr)
        harr=[[0]*300 for _ in range(385)]
        for c,(mi,s) in enumerate(hlabels):
            for g,k in clabel:
                e=list(M2[mi]);e[k]+=1;rr=35*g+i3[tuple(e)]
                harr[rr][c]=(harr[rr][c]+int(Z[5*g+k,s]))%P
        H=mat(harr)
        need(D*K==zero(126,275),"all34650 original quintic Koszul-kernel products")
        need(D*H==zero(126,300),"all37800 original complete300 multiplied-low kernel products")
        inp={"semantic":semantic,"dictionaries":dictionaries,"originalElevenQuadraticCoefficients":q,
            "originalQuinticMatrix":darr,"all275OriginalLinearKoszulMultiples":karr,
            "all300OriginalQuadraticLowMultiples":harr,"originalQuinticRank":dr,
            "all34650OriginalKoszulKernelProductsVerified":True,"all37800CompleteTargetKernelProductsVerified":True}
        save("whole-original-quintic259-input",inp)
        event("whole-original-quintic259-input",rankD5=dr,koszulColumns=275,completeTargets=300)
        tick();rr,kr,cols=pivots(K)
        need(kr<=259,"all original Koszul columns lie in the259-dimensional kernel")
        rec["parameters"].update({"originalQuinticRank":dr,"originalKoszulRank":kr,"remainingKernelQuotientDimension":259-kr,
            "all34650OriginalKoszulKernelProductsVerified":True,"all37800CompleteTargetKernelProductsVerified":True})
        if kr<259:
            rec["parameters"]["exactEQuinticKoszulSpanProved"]=False
            rec["status"]="completed-diagnostic";code=0;return code
        KB=selected(K,range(385),cols)
        _,ur,rows=pivots(KB.transpose())
        need(ur==259 and len(rows)==259 and len(cols)==259,"actual original259 row and column unit")
        A=selected(K,rows,cols);det=int(A.det());need(det!=0,"actual original259 nonzero legal-place minor")
        AI=A.inv();need(A*AI==eye(259) and AI*A==eye(259),"all134162 original259 inverse products")
        tick();allcoords=AI*selected(K,rows,range(275))
        need(KB*allcoords==K,"all105875 original275-column complete span products")
        hcoords=AI*selected(H,rows,range(300))
        need(KB*hcoords==H,"all115500 original300-target complete source products")
        free=[j for j in range(275) if j not in cols]
        need(len(free)==16,"complete original linear Koszul relation dimension16")
        relations=[[0]*16 for _ in range(275)]
        for j,col in enumerate(free):
            relations[col][j]=1
            for i,pv in enumerate(cols):relations[pv][j]=(-int(rr[i,col]))%P
        RM=mat(relations)
        need(K*RM==zero(385,16),"all6160 complete original sixteen relation products")
        need(selected(allcoords,range(259),cols)==eye(259),"all67081 original selected-coordinate identities")
        res={"original259UnitRows":rows,"original259UnitColumns":cols,"original259UnitColumnLabels":[list(klabels[j]) for j in cols],
            "original259UnitDeterminant127":det,"original259UnitInverse":tab(AI),
            "fieldAll275Coordinates":tab(allcoords),"fieldAll300TargetCoordinates":tab(hcoords),
            "completeSixteenRelationFreeIndices":free,"completeSixteenRelations":relations,
            "rankD5":126,"rankKoszul":259,"kernelQuotientDimension":0,"linearKoszulRelationDimension":16,
            "all134162OriginalUnitInverseProductsVerified":True,"all105875OriginalKoszulSpanProductsVerified":True,
            "all115500CompleteTargetSourceProductsVerified":True,"all6160CompleteRelationProductsVerified":True,
            "all67081SelectedIdentityProductsVerified":True,"exactEQuinticKoszulSpanProved":True,
            "exactECoordinateArraysComputed":False,
            "exactEConclusionMethod":"same original E259 unit plus exact original D5K5 and D5H identities; use the original adjugate, never lifted field coefficients",
            "conditionalOriginalGradientGeneratorBound":120,"conditionalOriginalBellGeneratorBound":130,
            "newBellIdentityClaimed":False}
        save("complete-original-quintic259-unit",res)
        rec["parameters"].update({k:v for k,v in res.items() if k not in
            ("original259UnitInverse","fieldAll275Coordinates","fieldAll300TargetCoordinates","completeSixteenRelations")})
        event("complete-original-quintic259-unit",rank=259,unitDeterminant127=det,all300TargetsVerified=True)
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
        atomic(a.out/"original-quintic-koszul259-receipt.json",canon(rec))
        print(json.dumps(rec,separators=(",",":")),flush=True)
if __name__=="__main__":raise SystemExit(main())
