#!/usr/bin/env python3
"""Continue the ACTUAL R150 core row module over Q[s,Sigma^-1].

AI (ChatGPT / literature_audit), 2026-11-15 UTC.
Parent core and unfinished row are preserved.  Thirteen parent source
combinations are checked before they become DAG leaves.  Only the six
already-known support factors may be divided out.  A reachable operation
DAG is replayed on those verified leaves and the original56 rows, followed
by reverse reduction of all original56 rows.  This certifies equality over
the localized ring, NOT equality of the unlocalized Q[s] row modules.
Large artifacts remain temporary immutable checkpoints.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import resource
import signal
import sys
import time
from flint import fmpq, fmpq_poly, fmpz

CORE_SOURCE_SHA="727175cf485a8ba5b5146a4cc6e749962e109c9e42265a2dd45f58cecdf933fb"
PARENT_BINDING="ce358eac629541da0c9d35fd29c66424fa0d89ded97cfec93f324cf56e9d16ba"
PARENT_MANIFEST_SHA="c43828673dc6513c43042e4452c91d146e78a26a15b3b82aa3f9e8a87ff49aa9"
PARENT_STATE_SHA="42d998c95906cf0ad9e8cef8660b115027e4ad671b332ca6493bb025f237ff41"
PARENT_PAYLOAD_SHA="52d7d5f3b735ab0b3da8465f888485b0a29168b49502cfadb9770313f7c8dd4f"
CORE_LOGICAL_SHA="752d21d7ca74ee5235c05ade9048ef48f120891c567abfb5132a4b2b33b745c8"
FORMAT="r150-localized-polynomial-row-module-dag-continuation-v1"

def packp(p):
    return {"n":[str(x) for x in p.numer().coeffs()],"d":str(p.denom())}

def unpackp(x):
    return fmpq_poly([fmpz(v) for v in x["n"]],fmpz(x["d"]))

def packrow(row):
    return [packp(p) for p in row]

def unpackrow(row):
    return [unpackp(p) for p in row]

def packmat(A):
    return [None if row is None else packrow(row) for row in A]

def unpackmat(A):
    return [None if row is None else unpackrow(row) for row in A]

def fullhash(d,A):
    return d.sha(d.canonical(packmat(A)))

def prim(d,row):
    den=1
    for p in row:
        den=math.lcm(den,int(p.denom()))
    rr=[p*den for p in row]
    content=0
    for p in rr:
        content=math.gcd(content,abs(int(p.numer().content())))
    if not content:
        return row,fmpq(1)
    scale=fmpq(den,content)
    if next(p for p in rr if p).leading_coefficient()<0:
        scale=-scale
    return [scale*p for p in row],scale

def normalize(d,row):
    """An explicit S-unit normalization, never an unknown-factor division."""
    row,c0=prim(d,row)
    powers=[0]*6
    if not any(row):
        return row,c0,powers
    first=next(i for i,p in enumerate(row) if p)
    for k,f in enumerate(d.FACTORS):
        while True:
            q,r=divmod(row[first],f)
            if r:
                break
            quot=[None]*len(row);quot[first]=q
            ok=True
            for j,p in enumerate(row):
                if j==first:
                    continue
                qq,rr=divmod(p,f)
                if rr:
                    ok=False
                    break
                quot[j]=qq
            if not ok:
                break
            row=quot;powers[k]+=1
    row,c1=prim(d,row)
    return row,c0*c1,powers

def apply_normalizer(d,row,scale,powers):
    require(len(powers)==6 and all(isinstance(k,int) and k>=0 for k in powers),
            "Only explicit known support factors")
    row=[fmpq(scale)*p for p in row]
    for f,k in zip(d.FACTORS,powers):
        if k:
            divisor=f**k
            row=[d.poly_exact(p,divisor,"DAG known-unit normalization") for p in row]
    return row

def require(ok,msg):
    if not ok:
        raise AssertionError(msg)

def get_parent(d,path):
    path=Path(path)
    mid=d.file_id(path/"checkpoint-manifest.json")
    require(mid["sha256"]==PARENT_MANIFEST_SHA,"Immutable parent manifest identity")
    parent=d.Cache(path,PARENT_BINDING)
    rec=parent.manifest["phases"]["row-module-state"]
    require(rec["sha256"]==PARENT_STATE_SHA and rec["payloadSha256"]==PARENT_PAYLOAD_SHA,
            "Exact actual unfinished row state")
    state=parent.get("row-module-state")
    core=d.decm(parent.get("polynomial-core")["core"])
    require(len(core)==56 and all(len(r)==22 for r in core) and d.phash(core)==CORE_LOGICAL_SHA,
            "Actual original56 core")
    require(state["nextInputRow"]==20 and state["operations"]==2416,
            "Actual prefix counters")
    return parent,state,core,mid

def verify_parent_leaves(d,state,A,cache):
    entries=[("basis",i,row,state["provenance"][i])
             for i,row in enumerate(state["basis"]) if row is not None]
    if any(state["current"]):
        entries.append(("current",0,state["current"],state["currentProvenance"]))
    require(len(entries)==13,"Actual12 basis rows and actual pending20th row")
    verified=0
    if cache.has("parent-source-verification"):
        verified=cache.get("parent-source-verification")["verifiedLeaves"]
    require(isinstance(verified,int) and 0<=verified<=len(entries),
            "Verified parent leaf checkpoint range")
    leaves=[]
    AT=d.transpose(A)
    for k,(kind,index,row,provenance) in enumerate(entries):
        value=[d.decp(p) for p in row]
        if k>=verified:
            coeff=[d.decp(p) for p in provenance]
            require(d.mv(AT,coeff)==value,"Full original56 polynomial source identity "+str(k))
            cache.put("parent-source-verification",
                      {"verifiedLeaves":k+1,"parentPayloadSha256":PARENT_PAYLOAD_SHA},True,
                      {"verifiedOriginal56SourceLeaves":k+1,
                       "originalPolynomialProductCoordinates":22*(k+1)})
            d.tick()
        leaves.append({"kind":"parent","which":kind,"slot":index,"value":value})
    return leaves

def row_statistics(A):
    nnz=0;deg=-1;bits=0;den=0;rows=0
    for row in A:
        if row is None:
            continue
        rows+=1
        for p in row:
            if p:
                nnz+=1;deg=max(deg,int(p.degree()))
                bits=max(bits,int(p.numer().height_bits()))
                den=max(den,int(p.denom()).bit_length())
    return {"rows":rows,"nonzeroPolynomials":nnz,"maximumDegree":deg,
            "maximumNumeratorBits":bits,"maximumDenominatorBits":den}

def localized_basis(d,A,parent_state,leaves,cache):
    if cache.has("localized-basis-complete"):
        return cache.get("localized-basis-complete")
    if cache.has("localized-row-state"):
        st=cache.get("localized-row-state")
        basis=unpackmat(st["basis"]);current=unpackrow(st["current"])
        ids=st["basisNodeIds"];curid=st["currentNodeId"]
        nodes=st["nodes"];row=st["nextInputRow"];ops=st["operations"]
        divisions=st["knownFactorDivisions"];timing=st["timing"]
    else:
        basis=[None]*22;ids=[None]*22;current=[];curid=None
        nodes=[{"kind":"parent","which":x["which"],"slot":x["slot"]} for x in leaves]
        for i,leaf in enumerate(leaves):
            rr,scale,powers=normalize(d,leaf["value"])
            nid=len(nodes)
            nodes.append({"kind":"operation","left":i,"right":None,
                          "quotient":packp(d.Z),"scale":str(scale),"knownPowers":powers})
            if leaf["which"]=="basis":
                slot=leaf["slot"]
                require(d.leading(rr)[0]==slot,"Known normalization preserves leading position")
                basis[slot]=rr;ids[slot]=nid
            else:
                current=rr;curid=nid
        row=parent_state["nextInputRow"];ops=0
        divisions=sum(sum(n.get("knownPowers",[])) for n in nodes)
        timing={"quotientSeconds":0.0,"rowArithmeticSeconds":0.0,
                "normalizationSeconds":0.0,"checkpointSeconds":0.0}
    last_save=time.monotonic()

    def save():
        nonlocal last_save
        start=time.monotonic()
        payload={"basis":packmat(basis),"current":packrow(current),"basisNodeIds":ids,
                 "currentNodeId":curid,"nodes":nodes,"nextInputRow":row,
                 "operations":ops,"knownFactorDivisions":divisions,"timing":timing,
                 "oldOperationsAlreadyPaid":2416}
        summary={"inputRowsStarted":row,"completedInputRows":row-int(any(current)),
                 "basisRows":sum(x is not None for x in basis),
                 "newWholePolynomialRowOperations":ops,"dagNodes":len(nodes),
                 "knownFactorDivisions":divisions,"basisStatistics":row_statistics(basis),
                 "currentStatistics":row_statistics([current]),"candidateOnly":True}
        cache.put("localized-row-state",payload,False,summary)
        timing["checkpointSeconds"]+=time.monotonic()-start
        last_save=time.monotonic()

    def boundary(force=False):
        if force or time.monotonic()-last_save>=45 or time.monotonic()>=d.DEADLINE:
            save()
        d.tick()

    boundary(True)
    while row<56 or any(current):
        boundary()
        if not any(current):
            value=A[row][:]
            leafid=len(nodes);nodes.append({"kind":"original","row":row})
            rr,scale,powers=normalize(d,value)
            nid=len(nodes)
            nodes.append({"kind":"operation","left":leafid,"right":None,
                          "quotient":packp(d.Z),"scale":str(scale),"knownPowers":powers})
            current=rr;curid=nid;row+=1;divisions+=sum(powers)
            if not any(current):
                current=[];curid=None
                continue
        while any(current):
            p,degree,lc=d.leading(current)
            if basis[p] is None:
                basis[p]=current;ids[p]=curid
                current=[];curid=None
                break
            if degree<int(basis[p][p].degree()):
                current,basis[p]=basis[p],current
                curid,ids[p]=ids[p],curid
                p,degree,lc=d.leading(current)
            old_leading=(degree,p)
            start=time.monotonic()
            q,rem=divmod(current[p],basis[p][p])
            require(q,"Nonzero complete leading quotient")
            timing["quotientSeconds"]+=time.monotonic()-start
            start=time.monotonic()
            rr=[x-q*y for x,y in zip(current,basis[p])]
            require(rr[p]==rem,"Leading polynomial remainder retained exactly")
            timing["rowArithmeticSeconds"]+=time.monotonic()-start
            start=time.monotonic()
            rr,scale,powers=normalize(d,rr)
            timing["normalizationSeconds"]+=time.monotonic()-start
            newlead=d.leading(rr)
            require(newlead is None or (newlead[1],newlead[0])<old_leading,
                    "Strict leading degree-position decrease")
            nid=len(nodes)
            nodes.append({"kind":"operation","left":curid,"right":ids[p],
                          "quotient":packp(q),"scale":str(scale),"knownPowers":powers})
            current=rr;curid=nid;ops+=1;divisions+=sum(powers)
            boundary()
        if not any(current):
            current=[];curid=None
        boundary()
    require(all(x is not None for x in basis),"Actual full22 leading positions")
    save()
    result={"basis":packmat(basis),"basisNodeIds":ids,"nodes":nodes,
            "operations":ops,"knownFactorDivisions":divisions,"timing":timing,
            "candidateOnlyUntilForwardAndReverseVerified":True}
    cache.put("localized-basis-complete",result,False,
              {"basis":row_statistics(basis),"dagNodes":len(nodes),
               "candidateOnly":True,"newWholePolynomialRowOperations":ops})
    return result

def replay_sources(d,A,leaves,result,cache):
    basis=unpackmat(result["basis"]);nodes=result["nodes"];final=result["basisNodeIds"]
    daghash=d.sha(d.canonical({"nodes":nodes,"final":final}))
    if cache.has("localized-dag-verified"):
        require(cache.get("localized-dag-verified")["dagSha256"]==daghash,"Verified DAG binding")
        return
    needed=set(final)
    for i in range(len(nodes)-1,-1,-1):
        if i in needed and nodes[i]["kind"]=="operation":
            needed.add(nodes[i]["left"])
            if nodes[i]["right"] is not None:
                needed.add(nodes[i]["right"])
    uses=[0]*len(nodes)
    for i in needed:
        n=nodes[i]
        if n["kind"]=="operation":
            uses[n["left"]]+=1
            if n["right"] is not None:
                uses[n["right"]]+=1
    for i in final:
        uses[i]+=1
    values={};start_index=0
    if cache.has("localized-dag-replay-state"):
        state=cache.get("localized-dag-replay-state")
        require(state["dagSha256"]==daghash,"Actual replay DAG identity")
        values={int(i):unpackrow(v) for i,v in state["activeValues"].items()}
        uses=state["remainingUses"];start_index=state["nextNode"]
    leafmap={(x["which"],x["slot"]):x["value"] for x in leaves}
    last_save=time.monotonic()
    for i in range(start_index,len(nodes)):
        if i not in needed:
            continue
        n=nodes[i]
        if n["kind"]=="parent":
            value=leafmap[(n["which"],n["slot"])]
        elif n["kind"]=="original":
            value=A[n["row"]]
        else:
            left=n["left"];right=n["right"]
            value=values[left][:]
            if right is not None:
                q=unpackp(n["quotient"])
                value=[x-q*y for x,y in zip(value,values[right])]
            value=apply_normalizer(d,value,n["scale"],n["knownPowers"])
            for old in (left,right):
                if old is not None:
                    uses[old]-=1
                    if uses[old]==0:
                        del values[old]
        if uses[i]:
            values[i]=value
        if time.monotonic()-last_save>=45 or time.monotonic()>=d.DEADLINE:
            cache.put("localized-dag-replay-state",
                      {"dagSha256":daghash,"nextNode":i+1,"remainingUses":uses,
                       "activeValues":{str(k):packrow(v) for k,v in values.items()}},False,
                      {"actualNodesReplayedThrough":i,"activePolynomialRows":len(values)})
            last_save=time.monotonic()
        d.tick()
    require(all(values[nid]==basis[j] for j,nid in enumerate(final)),
            "Every final22 row exactly replayed from actual original sources")
    cache.put("localized-dag-verified",
              {"dagSha256":daghash,"nodes":len(nodes),"reachableNodes":len(needed),
               "all22FinalSourceRowsVerified":True,
               "sourceDenominatorsSupportedOnlyOnKnownSigma":True},True,
              {"all22ForwardLocalizedSourceIdentitiesVerified":True,
               "originalPolynomialCoordinates":484,"reachableNodes":len(needed)})

def reverse_sources(d,A,result,cache):
    basis=unpackmat(result["basis"])
    bh=fullhash(d,basis)
    done=0
    if cache.has("localized-reverse"):
        rec=cache.get("localized-reverse")
        require(rec["basisSha256"]==bh,"Reverse basis identity")
        done=rec["verifiedRows"]
    for i in range(done,56):
        r=A[i][:]
        steps=0
        while any(r):
            # Known-factor division enlarged the polynomial row module.
            # Every original row must therefore reduce without localization.
            p,degree,lc=d.leading(r)
            b=basis[p]
            require(degree>=int(b[p].degree()),"Original row fails polynomial reverse membership")
            q,rem=divmod(r[p],b[p])
            oldlead=(degree,p)
            r=[x-q*y for x,y in zip(r,b)]
            require(r[p]==rem,"Reverse full quotient remainder")
            lead=d.leading(r)
            require(lead is None or (lead[1],lead[0])<oldlead,"Reverse leading decrease")
            steps+=1
            d.tick()
        cache.put("localized-reverse",
                  {"basisSha256":bh,"verifiedRows":i+1},True,
                  {"allOriginalRowsVerifiedThrough":i,"lastRowOperations":steps})
        d.tick()
    cache.put("localized-module-verified",
              {"basis":result["basis"],"basisSha256":bh,
               "all22ForwardLocalizedSourceIdentitiesVerified":True,
               "all56OriginalRowsReverseVerified":True,
               "reverseInclusionAlreadyOverPolynomialRing":True,
               "onlyLocalizedRowModuleEqualityClaimed":True},True,
              {"rank":22,"localizedRing":"Q[s,Sigma0^-1]",
               "allForwardAndReverseOriginalRowsVerified":True,
               "all56ReverseRowsVerifiedOverQPolynomialRing":True})

def determinant(d,result,cache):
    if cache.has("localized-outside-gcd"):
        return
    if cache.has("localized-hermite-state"):
        st=cache.get("localized-hermite-state");A=unpackmat(st["matrix"]);start=st["nextColumn"]
    else:
        A=unpackmat(result["basis"]);start=0
    extra_divisions=0
    for k in range(start,22):
        d.tick()
        choices=[i for i in range(k,22) if A[i][k]]
        require(choices,"Full rank during localized Hermite")
        p=min(choices,key=lambda i:(int(A[i][k].degree()),i))
        A[p],A[k]=A[k],A[p]
        for i in range(k+1,22):
            while A[i][k]:
                q,r=divmod(A[i][k],A[k][k])
                A[i]=[x-q*y for x,y in zip(A[i],A[k])]
                A[i],scale,powers=normalize(d,A[i]);extra_divisions+=sum(powers)
                if A[i][k]:
                    require(int(A[i][k].degree())<int(A[k][k].degree()),
                            "Localized Hermite Euclidean decrease")
                    A[i],A[k]=A[k],A[i]
                d.tick()
        require(all(not A[i][k] for i in range(k+1,22)),"All lower entries zero")
        cache.put("localized-hermite-state",
                  {"matrix":packmat(A),"nextColumn":k+1},False,
                  {"completedColumns":k+1,"knownUnitDivisionsThisCall":extra_divisions})
    out=d.O
    for i in range(22):
        out=out*A[i][i]
    require(out,"Nonzero localized determinant")
    valuations=[]
    for f in d.FACTORS:
        e=0
        while True:
            q,r=divmod(out,f)
            if r:
                break
            out=q;e+=1
        valuations.append(e)
    out=out/out.leading_coefficient()
    require(all(out.gcd(f).degree()==0 for f in d.FACTORS),
            "Outside gcd is coprime to every known support factor")
    require(int(out.degree())<=158,"Independent original outside degree bound at infinity65")
    cache.put("localized-outside-gcd",
              {"outsideGcdMonic":packp(out),"degree":int(out.degree()),
               "removedKnownValuationsFromFinalTriangularRepresentative":valuations,
               "trueOriginalProjectionOutsideCompleteDivisor":True,
               "doesNotClaimUnlocalizedRowModuleEquality":True},True,
              {"outsideKnownSupportGcdDegree":int(out.degree()),
               "outsideGcdSha256":d.sha(d.canonical(packp(out))),
               "allOriginalForwardAndReverseSourceChecksPassed":True,
               "nineTargetRemainingMultiplierDegreeUpperBound":158-int(out.degree()),
               "sameOriginalSourceCostUpperBound":8531-int(out.degree()),
               "doesNotByItselfProveOriginalH0GlobalMembership":True})

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--core-source",required=True)
    p.add_argument("--parent-checkpoints",required=True)
    p.add_argument("--out",required=True)
    p.add_argument("--through",choices=("module","gcd"),default="gcd")
    p.add_argument("--remaining-seconds",type=float,default=600)
    p.add_argument("--memory-mib",type=int,default=4096)
    args=p.parse_args()
    require(args.remaining_seconds>0 and args.memory_mib>=1024,"Resource bounds")
    resource.setrlimit(resource.RLIMIT_AS,(args.memory_mib*1024**2,args.memory_mib*1024**2))
    sys.set_int_max_str_digits(0)
    source=Path(args.core_source).read_bytes()
    require(hashlib.sha256(source).hexdigest()==CORE_SOURCE_SHA,"Frozen original core source")
    spec=importlib.util.spec_from_file_location("paid_original_global_core",args.core_source)
    d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
    began=time.monotonic()
    d.DEADLINE=began+max(.01,args.remaining_seconds-min(30,args.remaining_seconds/5))
    signal.signal(signal.SIGALRM,lambda sig,frame: (_ for _ in ()).throw(d.BudgetStop("Shared actual deadline")))
    signal.setitimer(signal.ITIMER_REAL,args.remaining_seconds)
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    binding=d.sha(d.canonical({"format":FORMAT,"self":d.file_id(__file__),
                              "coreSourceSha256":CORE_SOURCE_SHA,"parentBinding":PARENT_BINDING,
                              "parentStatePayloadSha256":PARENT_PAYLOAD_SHA,"coreLogicalSha256":CORE_LOGICAL_SHA,
                              "localizationFactors":[d.encp(f) for f in d.FACTORS]}))
    cache=d.Cache(out/"checkpoints",binding)
    rec={"format":FORMAT,"binding":binding,"status":"started",
         "parameters":{"script":d.file_id(__file__),"coreSource":d.file_id(args.core_source),
                       "parentBinding":PARENT_BINDING,"parentManifestSha256":PARENT_MANIFEST_SHA,
                       "parentStatePayloadSha256":PARENT_PAYLOAD_SHA,"through":args.through,
                       "remainingSeconds":args.remaining_seconds,"memoryMiB":args.memory_mib,
                       "keepsActualPending20thRow":True,"coreNotRecomputed":True,
                       "temporaryLargeArraysOnly":True,"rowModuleRing":"Q[s,Sigma0^-1]"}}
    try:
        parent,state,A,mid=get_parent(d,args.parent_checkpoints)
        leaves=verify_parent_leaves(d,state,A,cache)
        # Release all expanded56-vector provenance once the actual root identities
        # are verified; descendants retain the source provenance as an exact DAG.
        state.pop("provenance",None);state.pop("currentProvenance",None)
        result=localized_basis(d,A,state,leaves,cache)
        del state
        replay_sources(d,A,leaves,result,cache)
        reverse_sources(d,A,result,cache)
        if args.through=="gcd":
            determinant(d,result,cache)
        rec["status"]="completed"
    except d.BudgetStop as e:
        rec["status"]="budget-checkpoint";rec["message"]=str(e)
    except BaseException as e:
        rec["status"]="failed";rec["error"]={"type":type(e).__name__,"message":str(e)}
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        cache.manifest=json.loads(cache.path.read_text())
        rec["elapsedSeconds"]=time.monotonic()-began
        rec["parameters"]["checkpointManifest"]=d.file_id(cache.path)
        rec["parameters"]["checkpointPhases"]=cache.manifest["phases"]
        rec["newOriginalH0GlobalMembershipClaim"]=False
        data=d.canonical(rec);require(len(data)<80000,"Small receipt budget")
        d.atomic_json(out/"localized-row-module-dag-receipt.json",rec)
        print(data.decode(),flush=True)
    return 0 if rec["status"] in ("completed","budget-checkpoint") else 1

if __name__=="__main__":
    raise SystemExit(main())
