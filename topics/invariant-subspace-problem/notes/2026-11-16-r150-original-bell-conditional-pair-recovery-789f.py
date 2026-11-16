#!/usr/bin/env python3
"""Conditional original Bell pair-stage recovery; no inference from missing logs.
Author: Astra-ISP-789f / normal_annihilator. AI-assisted GPT-6 Astra Pro.
Date: 2026-11-16. All mathematical files remain temporary.
"""
from __future__ import annotations
import argparse, importlib.util, json, os, resource, shutil, signal, subprocess, time
from pathlib import Path
FORMAT="r150-original-bell-conditional-whole-candidate-pairs-v1"
PARENT_SHA="da80b727c47a050f3e268f00d1d6598336866a41b354d6aecb5edbb1ca1e730d"
PARENT_BYTES=31156
class Budget(Exception): pass
def need(c,s):
    if not c: raise ValueError(s)
def module(p):
    z=importlib.util.spec_from_file_location("paid_original_bell_driver",p)
    m=importlib.util.module_from_spec(z);z.loader.exec_module(m);return m
def scan_phases(p):
    phases=[];bad=[]
    with p.open("r",encoding="utf-8",errors="replace") as f:
        for line in f:
            line=line.strip()
            if line.startswith("@@PHASE "):phases.append(line)
            if line.startswith("@@FAIL "):bad.append(line)
    return phases,bad
def ring(fd,original):
    return ['ring r=127,('+','.join(fd.NAMES)+'),wp('+','.join(map(str,fd.WEIGHTS))+');',
        'short=0; option(redSB); option(redTail);',
        'ideal Original='+','.join(fd.singular_poly(p,fd.NAMES) for p in original)+';']
def candidate_script(fd,original,degree,previous):
    old=fd.engine_script(original,fd.NAMES,fd.WEIGHTS,fd.SOURCE_WEIGHTS,degree,previous)
    marker="matrix OriginalDifference=matrix(Original)*Sources-matrix(G);"
    need(old.count(marker)==1,"exact paid engine candidate boundary")
    prefix=old.split(marker)[0]
    return prefix+"\n"+'\n'.join([
        "int i; int j; int k;",
        "proc dumpPolynomial(poly value) {",
        "while(value!=0) {",
        'print("@@TERM "+string(int(leadcoef(value)))+" "+string(leadexp(value)));',
        "value=value-lead(value); } }",
        'print("@@BEGIN 127 18 18 "+string(ng));',
        "for(j=1;j<=ng;j++){",
        'print("@@G "+string(j-1)+" "+string(size(G[j])));',
        'dumpPolynomial(G[j]); print("@@ENDPOLY"); }',
        "for(i=1;i<=18;i++){ for(j=1;j<=ng;j++){ if(Sources[i,j]!=0){",
        'print("@@S "+string(i-1)+" "+string(j-1)+" "+string(size(Sources[i,j])));',
        'dumpPolynomial(Sources[i,j]); print("@@ENDPOLY"); } } }',
        'print("@@CANDIDATE-END '+str(degree)+'");',"quit;"])+"\n"
def parse_candidate(fd,p,degree):
    basis=None;sources=[];active=None;terms=[];declared=0;done=False;seen=set()
    with p.open("r",encoding="utf-8",errors="replace") as f:
        for raw in f:
            s=raw.strip()
            if not s.startswith("@@"):continue
            if s.startswith("@@PHASE"):continue
            need(not s.startswith("@@FAIL"),"candidate engine explicit failure")
            z=s.split()
            if z[0]=="@@BEGIN":
                need(basis is None and len(z)==5 and list(map(int,z[1:4]))==[127,18,18],"candidate original ring")
                n=int(z[4]);need(n>0,"nonempty candidate");basis=[None]*n
            elif z[0] in ("@@G","@@S"):
                need(basis is not None and active is None,"candidate polynomial boundary")
                if z[0]=="@@G":
                    need(len(z)==3,"candidate G record");j,declared=map(int,z[1:])
                    need(0<=j<len(basis) and basis[j] is None,"candidate unique G");active=("G",j)
                else:
                    need(len(z)==4,"candidate source record");i,j,declared=map(int,z[1:])
                    need(0<=i<18 and 0<=j<len(basis) and (i,j) not in seen,"candidate unique original source")
                    seen.add((i,j));active=("S",i,j)
                need(declared>0,"candidate nonzero polynomial");terms=[]
            elif z[0]=="@@TERM":
                need(active is not None,"candidate term placement")
                _,co,ex=s.split(None,2);co=int(co)%127
                ee=tuple(int(x) for x in ex.replace("[","").replace("]","").replace(" ","").split(","))
                need(len(ee)==18 and min(ee)>=0 and co!=0,"candidate full monomial");terms.append([list(ee),co])
            elif z[0]=="@@ENDPOLY":
                need(active is not None and len(terms)==declared,"candidate complete polynomial")
                dd=fd.record_dict(terms,18);need(len(dd)==declared,"candidate no repeated monomial")
                p0=fd.poly_record(dd)
                if active[0]=="G":basis[active[1]]=p0
                else:sources.append([active[1],active[2],p0])
                active=None
            elif z[0]=="@@CANDIDATE-END":
                need(not done and basis is not None and active is None and int(z[1])==degree,"candidate complete transaction");done=True
            else:raise ValueError("unknown candidate marker "+s[:120])
    need(done and basis is not None and all(basis),"all candidate records retained")
    dw=[]
    for p0 in basis:
        ds={sum(e*w for e,w in zip(ex,fd.WEIGHTS)) for ex,c in p0}
        need(len(ds)==1,"candidate homogeneous basis")
        d=next(iter(ds));need(0<d<=degree,"candidate exact bounded degree");dw.append(d)
    for i,j,p0 in sources:
        need(all(sum(e*w for e,w in zip(ex,fd.WEIGHTS))==dw[j]-fd.SOURCE_WEIGHTS[i] for ex,c in p0),
            "candidate source exact homogeneous weight")
    return {"basis":basis,"sources":sources,"basisWeights":dw,"candidateThroughWeight":degree,
        "allOriginalSourceProductsVerifiedInSingular":False,
        "allOriginalGeneratorsReducedToZero":False,
        "allPairsThroughBoundVerifiedOrCoprimeCriterion":False}
def verification_script(fd,original,data,mode,degree,cursor=0,counts=(0,0,0)):
    lines=ring(fd,original)
    lines+=["ideal G="+",".join(fd.singular_poly(p,fd.NAMES) for p in data["basis"])+";",
        "int ng=size(G);","int i; int j; int k;","degBound=0;"]
    if mode=="sources":
        lines+=["matrix Sources[18]["+str(len(data["basis"]))+"];"]
        for i,j,p in data["sources"]:lines.append("Sources[%d,%d]=%s;"%(i+1,j+1,fd.singular_poly(p,fd.NAMES)))
        lines+=["matrix difference=matrix(Original)*Sources-matrix(G);",
            "for(j=1;j<=ng;j++){ if(difference[1,j]!=0){",
            'print("@@FAIL original-source-product"); quit; } }',
            "for(i=1;i<=18;i++){if(reduce(Original[i],G)!=0){",
            'print("@@FAIL reverse-original-generator"); quit; } }',
            'print("@@SOURCE-COMPLETE");',"quit;"]
    else:
        lines+=["intvec ww="+",".join(map(str,fd.WEIGHTS))+";",
            "intvec ei; intvec ej; int exponent; int pairWeight; int coprime;",
            "poly lm; poly sp; poly remainder;","int pair=0;",
            "int checkedPairs=%d; int productPairs=%d; int outsidePairs=%d;"%tuple(counts),
            "for(i=1;i<=ng;i++){ei=leadexp(G[i]); for(j=i+1;j<=ng;j++){",
            "if(pair>="+str(cursor)+"){",
            "ej=leadexp(G[j]);lm=1;pairWeight=0;coprime=1;",
            "for(k=1;k<=18;k++){exponent=ei[k];if(ej[k]>exponent){exponent=ej[k];}",
            "if(ei[k]>0 && ej[k]>0){coprime=0;}",
            "pairWeight=pairWeight+ww[k]*exponent;if(exponent>0){lm=lm*var(k)^exponent;} }",
            "if(pairWeight>"+str(degree)+"){outsidePairs++;}",
            "else{if(coprime==1){productPairs++;}else{",
            "sp=(lm/lead(G[i]))*G[i]-(lm/lead(G[j]))*G[j];remainder=reduce(sp,G);",
            'if(remainder!=0){print("@@FAIL complete-bounded-Buchberger-pair "+string(pair));quit;}',
            "checkedPairs++;} } }","pair++;",
            "if(pair>"+str(cursor)+" && pair%256==0){",
            'print("@@PAIR-COMMIT "+string(pair)+" "+string(checkedPairs)+" "+string(productPairs)+" "+string(outsidePairs));}',
            "} }",
            'print("@@PAIR-COMMIT "+string(pair)+" "+string(checkedPairs)+" "+string(productPairs)+" "+string(outsidePairs));',
            'print("@@PAIR-COMPLETE");',"quit;"]
    return "\n".join(lines)+"\n"
def pair_transcript(p,start,counts,total):
    last=start;cc=list(counts);complete=False;bad=[]
    with p.open("r",encoding="utf-8",errors="replace") as f:
        for raw in f:
            s=raw.strip()
            if s.startswith("@@FAIL"):bad.append(s)
            elif s.startswith("@@PAIR-COMMIT "):
                z=list(map(int,s.split()[1:]));need(len(z)==4,"complete pair transaction fields")
                k,c=z[0],z[1:]
                need(last<=k<=total and all(a>=b for a,b in zip(c,cc)) and sum(c)==k,"whole pair prefix transaction")
                need(k==total or k%256==0,"whole fixed pair block")
                last,cc=k,c
            elif s=="@@PAIR-COMPLETE":complete=True
    if complete:need(last==total,"all original basis pairs accounted")
    return last,cc,complete,bad
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--parent-driver",type=Path,required=True)
    ap.add_argument("--parent-out",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--singular",default="Singular")
    ap.add_argument("--seconds",type=float,default=900)
    ap.add_argument("--memory-mib",type=int,default=4096)
    a=ap.parse_args();need(0<a.seconds<=900 and 512<=a.memory_mib<=8192,"bounded child resources")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    a.out.mkdir(parents=True,exist_ok=True);began=time.monotonic();deadline=began+a.seconds
    fd=module(a.parent_driver);pid=fd.identity(a.parent_driver)
    need(pid["bytes"]==PARENT_BYTES and pid["sha256"]==PARENT_SHA,"paid immutable parent source")
    own=fd.identity(Path(__file__));receipt=a.out/"conditional-original-bell-pair-recovery-receipt.json"
    parent_receipt=a.parent_out/"original-full-bell-homogeneous-source-prefix-receipt.json"
    pr=fd.identity(parent_receipt);parent=json.loads(parent_receipt.read_bytes())
    need(parent["format"]==fd.FORMAT and parent["source"]["sha256"]==PARENT_SHA,"actual parent receipt source")
    expected=fd.digest(fd.canonical({"format":fd.FORMAT,"sourceSha256":PARENT_SHA,"helperSha256":fd.HELPER_SHA,
        "prime":fd.PRIME,"matchedPlace":fd.PLACE,"variables":fd.NAMES,"weights":fd.WEIGHTS,
        "originalSourceWeights":fd.SOURCE_WEIGHTS,"algorithm":"weighted-homogeneous-liftstd-plus-all-bounded-pairs"}))
    need(parent["binding"]==expected,"parent original semantic binding")
    binding=fd.digest(fd.canonical({"format":FORMAT,"sourceSha256":own["sha256"],"parentSourceSHA256":PARENT_SHA,
        "parentReceipt":pr,"parentBinding":expected,"algorithm":"conditional-pairs-only-candidate-source-whole256pair-prefix"}))
    rec={"format":FORMAT,"binding":binding,"source":own,"status":"running",
        "parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib,"parentReceipt":pr,
            "parentBinding":expected,"parentUnfinishedCandidatesReused":False,
            "characteristicZeroConclusion":False,"stages":[]}}
    mp=a.out/"manifest.json";state={"format":FORMAT+"-manifest","binding":binding,"generation":0,"pairEvidence":[]}
    child=None
    def save():
        rec["elapsedSeconds"]=time.monotonic()-began
        rec["parameters"]["peakParentRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rec["parameters"]["peakChildRssKiB"]=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        fd.json_save(receipt,rec)
    def checkpoint():
        fd.json_save(mp,state);rec["parameters"]["manifest"]=fd.identity(mp);save()
    def tick():
        if time.monotonic()>=deadline-8:raise Budget("conditional whole-candidate recovery budget")
    def stop(signum,frame):raise Budget("signal "+str(signum))
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    def run_script(label,script):
        nonlocal child
        tick();state["generation"]+=1;checkpoint();g=state["generation"]
        sp=a.out/("%04d-%s.sing"%(g,label));lp=a.out/("%04d-%s.log"%(g,label))
        fd.atomic(sp,script.encode("ascii"));stage={"name":label,"script":fd.identity(sp),"status":"running"}
        rec["parameters"]["stages"].append(stage);save();start=time.monotonic();budget=False
        try:
            with lp.open("wb") as out:
                child=subprocess.Popen([str(engine),"-q",str(sp)],stdout=out,stderr=subprocess.STDOUT)
                last=time.monotonic()
                while child.poll() is None:
                    tick()
                    if time.monotonic()-last>=30:
                        print(json.dumps({"phase":label,"elapsedSeconds":time.monotonic()-start},separators=(",",":")),flush=True);last=time.monotonic()
                    time.sleep(.2)
                rc=child.returncode;child=None
        except Budget:
            budget=True
            if child is not None and child.poll() is None:
                child.terminate()
                try:child.wait(timeout=5)
                except subprocess.TimeoutExpired:child.kill();child.wait()
            child=None;rc=75
        stage.update(status="budget" if budget else "returned",exitCode=rc,elapsedSeconds=time.monotonic()-start,log=fd.identity(lp));save()
        return lp,rc,budget
    code=1
    try:
        save()
        need(parent.get("status") in ("budget-checkpoint","completed","completed-prefix","failed"),"terminal parent status")
        stages=parent["parameters"].get("stages",[])
        last=stages[-1] if stages else None
        authorized=False
        if parent["status"]=="budget-checkpoint" and last is not None and last.get("status")=="unfinished-whole-degree":
            need(last["name"].startswith("complete-original-weight-"),"only actual original degree is eligible")
            ld=last.get("log");need(isinstance(ld,dict),"actual last original log exists")
            lp=a.parent_out/ld["path"];need(fd.identity(lp)==ld,"actual full unfinished log SHA")
            phases,bad=scan_phases(lp);need(not bad,"do not resume an explicit mathematical engine failure")
            rec["parameters"]["parentActualLog"]=ld;rec["parameters"]["parentActualPhases"]=phases
            authorized=("@@PHASE all-original-source-identities-verified" in phases and
                "@@PHASE complete-bounded-Buchberger-check-verified" not in phases)
        if not authorized:
            rec["status"]="completed-diagnostic"
            rec["parameters"]["outcome"]="no-confirmed-source-complete-pair-stage-no-reconstruction"
            rec["parameters"]["noStdOrOriginalProductCompletionInferred"]=True
            rec["parameters"]["noMathematicalNegativeConclusion"]=True;code=0
        else:
            degree=int(last["degree"])
            need(last["name"]=="complete-original-weight-%02d"%degree,"exact interrupted degree label")
            pm=json.loads((a.parent_out/"manifest.json").read_bytes())
            need(pm["format"]==fd.FORMAT+"-manifest" and pm["binding"]==expected,"same complete parent checkpoint")
            mdl=fd.gz_load(a.parent_out,pm["model"]);need(mdl["binding"]==expected,"same original model binding")
            model=mdl["data"];need(model["all17OriginalGradientPolynomialsVerified"] and model["allMeanAndHankelVariablesRetained"],"original complete polynomial model")
            st=fd.gz_load(a.parent_out,pm["selfTest"])
            need(st["binding"]==expected and st["degree2HasNoPureParameterPower"] and
                st["degree3ResumedWithSameOriginalSources"] and st["allIndependentFlintOriginalProductsVerified"],"actual paid independent two-degree selftest")
            previous=None;d=4
            for item in pm["completedDegrees"]:
                need(item["degree"]==d+1,"consecutive paid parent degrees")
                pp=fd.gz_load(a.parent_out,item["output"]);need(pp["binding"]==expected,"parent degree binding")
                previous=pp["data"];d=item["degree"]
                need(previous["verifiedThroughWeight"]==d and previous["allOriginalSourceProductsVerifiedInSingular"] and
                    previous["allOriginalGeneratorsReducedToZero"] and previous["allPairsThroughBoundVerifiedOrCoprimeCriterion"],"whole verified parent degree")
            need(d+1==degree and "positiveCandidate" not in pm,"only first uncompleted original degree")
            rec["parameters"].update(parentLastWholeDegree=d if previous else 0,interruptedDegree=degree,
                actualPairsOnlyBranch=True,allOriginalVariablesRetained=True)
            engine=shutil.which(a.singular) if not Path(a.singular).is_file() else str(a.singular)
            need(engine is not None,"actual Singular executable")
            if mp.exists():
                state=json.loads(mp.read_bytes());need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding,"same child whole-candidate binding")
            if "candidate" not in state:
                if "completeCandidateLog" in state:
                    lp=a.out/state["completeCandidateLog"]["path"]
                    need(fd.identity(lp)==state["completeCandidateLog"],"retained whole candidate log SHA")
                else:
                    lp,rc,budget=run_script("reconstruct-candidate-before-pairs",
                        candidate_script(fd,model["fieldHomogeneousGenerators"],degree,previous))
                    with lp.open("r",encoding="utf-8",errors="replace") as f:
                        complete_marker=any(line.strip()=="@@CANDIDATE-END "+str(degree) for line in f)
                    if complete_marker:
                        state["completeCandidateLog"]=fd.identity(lp);checkpoint()
                    if budget:raise Budget("whole candidate log retained only when its final marker exists")
                    need(rc==0 and complete_marker,"candidate Singular completion")
                cand=parse_candidate(fd,lp,degree)
                state["candidate"]=fd.gz_save(a.out/"complete-unverified-original-candidate.json.gz",
                    {"format":FORMAT+"-candidate","binding":binding,"data":cand,"producerLog":fd.identity(lp)})
                state["pairCursor"]=0;state["pairCounts"]=[0,0,0];checkpoint()
            cd=fd.gz_load(a.out,state["candidate"]);need(cd["binding"]==binding,"whole retained child candidate")
            cand=cd["data"];need(cand["candidateThroughWeight"]==degree,"same retained degree")
            if "sourcesVerified" not in state:
                lp,rc,budget=run_script("verify-all-original-sources-and-reverse",
                    verification_script(fd,model["fieldHomogeneousGenerators"],cand,"sources",degree))
                if budget:raise Budget("whole candidate retained; source verification unfinished")
                need(rc==0,"original source verifier completion")
                phases,bad=scan_phases(lp);need(not bad,"original source verifier failure")
                tags=[x.strip() for x in lp.read_text(errors="replace").splitlines() if x.strip().startswith("@@")]
                need(tags==["@@SOURCE-COMPLETE"],"all original products and reverse containment")
                state["sourcesVerified"]=fd.identity(lp);checkpoint()
            else:
                p=a.out/state["sourcesVerified"]["path"];need(fd.identity(p)==state["sourcesVerified"],"paid original-source verification transcript")
                need("@@SOURCE-COMPLETE" in p.read_text(errors="replace"),"paid source verification complete marker")
            total=len(cand["basis"])*(len(cand["basis"])-1)//2
            cursor=0;counts=[0,0,0]
            for ev in state["pairEvidence"]:
                need(ev["startCursor"]==cursor and ev["startCounts"]==counts,"complete consecutive pair evidence")
                p=a.out/ev["log"]["path"];need(fd.identity(p)==ev["log"],"whole committed pair transcript SHA")
                cursor,counts,done,bad=pair_transcript(p,cursor,counts,total)
                need(not bad and cursor==ev["endCursor"] and counts==ev["endCounts"],"committed exact pair prefix")
            need(cursor==state["pairCursor"] and counts==state["pairCounts"],"all paid pair cursor coordinates")
            if cursor<total:
                oldcursor,oldcounts=cursor,list(counts)
                lp,rc,budget=run_script("verify-complete-bounded-pairs",
                    verification_script(fd,model["fieldHomogeneousGenerators"],cand,"pairs",degree,cursor,counts))
                cursor,counts,done,bad=pair_transcript(lp,cursor,counts,total)
                need(not bad,"complete original bounded pair failure")
                state["pairEvidence"].append({"log":fd.identity(lp),"startCursor":oldcursor,"startCounts":oldcounts,
                    "endCursor":cursor,"endCounts":counts})
                state["pairCursor"]=cursor;state["pairCounts"]=counts;checkpoint()
                if budget:raise Budget("whole candidate and whole pair blocks retained")
                need(rc==0 and done,"complete pair verifier terminal marker")
            need(cursor==total and sum(counts)==total,"all original basis pairs complete")
            data=dict(cand);data.update(verifiedThroughWeight=degree,allOriginalSourceProductsVerifiedInSingular=True,
                allOriginalGeneratorsReducedToZero=True,allPairsThroughBoundVerifiedOrCoprimeCriterion=True,
                explicitBuchbergerPairs=counts[0],coprimeLeadingProductCriterionPairs=counts[1],higherWeightPairsRetainedForLater=counts[2])
            state["verifiedDegree"]=fd.gz_save(a.out/"complete-verified-original-degree.json.gz",
                {"format":FORMAT+"-verified-degree","binding":binding,"data":data})
            pos=fd.field_positive(model,data,binding)
            if pos is not None:
                state["positiveCandidate"]=fd.gz_save(a.out/"complete-original-affine-field-source-for-one.json.gz",pos)
                rec["parameters"]["candidateSupportTerms"]=pos["totalSourceTerms"]
                rec["parameters"]["positiveCandidate"]=state["positiveCandidate"]
                rec["parameters"]["outcome"]="verified-field-source-for-one-child-E-adapter-still-required"
            else:rec["parameters"]["outcome"]="one-complete-original-degree-without-field-one-source"
            rec["parameters"].update(verifiedDegree=degree,basisColumns=len(cand["basis"]),allOriginalSourceProductsVerified=True,
                allOriginalGeneratorsReducedToZero=True,completeBoundedPairCounts=counts,
                parentCheckpointUnmodified=True,childExactELiftAlreadyRun=False)
            rec["status"]="completed";code=0;checkpoint()
    except Budget as e:
        rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        rec["parameters"]["noMathematicalNegativeConclusion"]=True;code=75
    except BaseException as e:
        rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1
    finally:
        if child is not None and child.poll() is None:
            child.terminate()
            try:child.wait(timeout=5)
            except subprocess.TimeoutExpired:child.kill();child.wait()
        if mp.exists():rec["parameters"]["manifest"]=fd.identity(mp)
        save()
    print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True);return code
if __name__=="__main__":raise SystemExit(main())
