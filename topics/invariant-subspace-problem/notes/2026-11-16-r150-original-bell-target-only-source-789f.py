#!/usr/bin/env python3
"""Direct weighted discovery and one original Bell source, without full liftstd.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
std is only a candidate finder. A positive result requires all eighteen
original homogeneous products and independent FLINT affine multiplication.
No absence, incomplete basis, budget exit, or field identity is promoted
to a characteristic-zero conclusion. Mathematical arrays stay temporary.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, re, resource, shutil, signal
import subprocess, time
from pathlib import Path
from flint import nmod_mpoly_ctx

FORMAT="r150-original-bell-target-only-source-v1"
MODEL_SHA="da80b727c47a050f3e268f00d1d6598336866a41b354d6aecb5edbb1ca1e730d"
MODEL_BYTES=31156
HELPER_SHA="31df769fb0fd3a41eb7606f500aae8b46952219c24927bd3265ed3dc34d7fe10"
HELPER_BYTES=16964
ALGORITHM="std-only-candidate-then-degBound-zero-single-original-lift-and-two-flint-products"
P=127
class Budget(Exception): pass
def need(v,m):
    if not v: raise ValueError(m)
def raw_identity(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda:f.read(1048576),b""):h.update(chunk)
    return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def module(p):
    sp=importlib.util.spec_from_file_location("paid_complete_bell_model",p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def semantic(own_sha,degree):
    return {"format":FORMAT,"sourceSha256":own_sha,"modelDriverSHA256":MODEL_SHA,
        "helperSHA256":HELPER_SHA,"prime":127,"matchedPlace":100,
        "discoveryDegree":degree,"algorithm":ALGORITHM}
def ss(p,mode=""):
    s=str(p)
    need(not any(x in s for x in ('"',"\\","\r","\n")),"literal safe Singular temporary path")
    return '"'+mode+s+'"'
def ring(fd,original,names=None,weights=None):
    names=fd.NAMES if names is None else tuple(names)
    weights=fd.WEIGHTS if weights is None else tuple(weights)
    return ["ring r=127,("+",".join(names)+"),wp("+",".join(map(str,weights))+");",
        "short=0; option(redSB); option(redTail);",
        "ideal Original="+",".join(fd.singular_poly(p,names) for p in original)+";"]
def read_markers(p):
    markers=[];bad=[]
    with p.open("r",encoding="utf-8",errors="replace") as f:
        for line in f:
            s=line.strip()
            if s.startswith("@@"): markers.append(s)
            if s.startswith("@@FAIL") or s.startswith("?"): bad.append(s[:500])
    need(len(markers)<=10000 and len(bad)<=10000,"bounded diagnostic marker count")
    return markers,bad
def marker_once(markers,prefix,required=True):
    z=[x for x in markers if x.startswith(prefix)]
    need(len(z)<=1,"unique stage marker "+prefix)
    if required: need(len(z)==1,"complete stage marker "+prefix)
    return z[0] if z else None
def parse_fast_polynomial(p,names):
    """Parse only Singular short=0 expanded prime-field monomials, not code."""
    text="".join(p.read_text(encoding="ascii").split())
    if text=="0": return {}
    need(text and text[0] not in "*^","nonempty expanded polynomial")
    pieces=re.findall(r"[+-]?[^+-]+",text)
    need("".join(pieces)==text,"complete expanded polynomial tokenization")
    where={s:i for i,s in enumerate(names)};out={}
    for term in pieces:
        coefficient=1
        if term[0] in "+-":
            if term[0]=="-": coefficient=-1
            term=term[1:]
        need(term,"nonempty signed monomial")
        exponent=[0]*len(names)
        for factor in term.split("*"):
            if factor.isdigit():
                coefficient=coefficient*int(factor)%P;continue
            z=factor.split("^")
            need(len(z)<=2 and z[0] in where,"literal variable in expanded monomial")
            k=1 if len(z)==1 else int(z[1])
            need(k>=0 and (len(z)==1 or z[1].isdigit()),"nonnegative literal exponent")
            exponent[where[z[0]]]+=k
        e=tuple(exponent);out[e]=(out.get(e,0)+coefficient)%P
    return {e:c for e,c in out.items() if c}
def selftest_script(out):
    g=out/"selftest-degree2.ssi";s=out/"selftest-single-source.ssi"
    lines=[
        "ring r=127,(x,tt),wp(1,1); short=0; option(redSB); option(redTail);",
        "ideal Original=x^2-tt^2,x*tt;",
        "int i; int k; int power; int pure; int found; intvec ex;",
        "degBound=2; ideal G2=std(Original);",
        "for(i=1;i<=size(G2);i++){",
        "if(G2[i]!=0){",
        "poly z=G2[i]; while(z!=0){ex=leadexp(z);",
        'if(ex[1]+ex[2]>2){print("@@FAIL degree2-bound");quit;} z=z-lead(z);}',
        "if(size(G2[i])==1){ex=leadexp(G2[i]);",
        'if(ex[1]==0){print("@@FAIL degree2-pure");quit;}} }}',
        "write("+ss(g,"ssi:w ")+",G2); def G2copy=read("+ss(g,"ssi:r ")+");",
        'if(size(G2copy)!=size(G2)){print("@@FAIL ssi-shape");quit;}',
        "for(i=1;i<=size(G2);i++){",
        'if(G2[i]!=G2copy[i]){print("@@FAIL ssi-polynomial");quit;}}',
        'print("@@SELFTEST-DEGREE2 "+string(size(G2)));',
        "degBound=3; ideal G3=std(G2copy+Original); found=0;",
        "for(i=1;i<=size(G3);i++){if(size(G3[i])==1){ex=leadexp(G3[i]);",
        "if(ex[1]==0 && ex[2]==3){found=1;}}}",
        'if(found!=1){print("@@FAIL continued-degree3");quit;}',
        'print("@@SELFTEST-DEGREE3 "+string(size(G3)));',
        "degBound=0; ideal Target=tt^3; matrix Units;",
        'matrix Source=lift(Original,Target,Units,"std");',
        'if(nrows(Source)!=2 || ncols(Source)!=1){print("@@FAIL lift-shape");quit;}',
        'if(nrows(Units)!=1 || ncols(Units)!=1 || Units[1,1]!=1){print("@@FAIL lift-unit");quit;}',
        "matrix Difference=matrix(Original)*Source-matrix(Target);",
        'if(Difference[1,1]!=0){print("@@FAIL lift-original-product");quit;}',
        "write("+ss(s,"ssi:w ")+",Source); def SourceCopy=read("+ss(s,"ssi:r ")+");",
        'if(nrows(SourceCopy)!=2 || ncols(SourceCopy)!=1){print("@@FAIL source-ssi-shape");quit;}',
        'for(i=1;i<=2;i++){if(Source[i,1]!=SourceCopy[i,1]){print("@@FAIL source-ssi-product");quit;}}',
        "write("+ss(out/"selftest-source-0.txt",":w ")+",Source[1,1]);",
        "write("+ss(out/"selftest-source-1.txt",":w ")+",Source[2,1]);",
        "write("+ss(out/"selftest-parser.txt",":w ")+",-5*x^4+3*x*tt^3+7);",
        'print("@@SELFTEST-COMPLETE");quit;']
    return "\n".join(lines)+"\n"
def discovery_script(fd,model,out,degree):
    g=out/"whole-discovery-basis.ssi"
    lines=ring(fd,model["fieldHomogeneousGenerators"])
    lines+=["int i; int j; int pure; int selected=0; int power=0; intvec ex; number co=0;",
        "degBound="+str(degree)+";",
        'print("@@STD-START '+str(degree)+'");',
        "ideal G=std(Original);",
        'print("@@STD-RETURN "+string(size(G)));',
        "write("+ss(g,"ssi:w ")+",G);",
        'print("@@STD-SSI-WRITTEN");',
        "def Gcopy=read("+ss(g,"ssi:r ")+");",
        'if(size(Gcopy)!=size(G)){print("@@FAIL whole-G-ssi-shape");quit;}',
        "for(i=1;i<=size(G);i++){",
        'if(Gcopy[i]!=G[i]){print("@@FAIL whole-G-ssi-product");quit;}}',
        'print("@@STD-SSI-ROUNDTRIP");',
        "for(i=1;i<=size(G);i++){if(size(G[i])==1){",
        "ex=leadexp(G[i]);pure=1;",
        "for(j=1;j<=17;j++){if(ex[j]!=0){pure=0;}}",
        "if(pure==1 && ex[18]>0){",
        "if(selected==0 || ex[18]<power){selected=i;power=ex[18];co=leadcoef(G[i]);}}}}",
        'print("@@STD-END '+str(degree)+' "+string(size(G))+" "+string(selected)+" "+string(power)+" "+string(int(co)));',
        "quit;"]
    return "\n".join(lines)+"\n"
def lift_script(fd,model,out,power):
    s=out/"whole-single-original-source.ssi"
    lines=ring(fd,model["fieldHomogeneousGenerators"])
    lines+=["degBound=0;","ideal Target=tt^"+str(power)+";","matrix Units;",
        'print("@@LIFT-START '+str(power)+'");',
        'matrix Source=lift(Original,Target,Units,"std");',
        'print("@@LIFT-RETURN");',
        'if(nrows(Source)!=18 || ncols(Source)!=1){print("@@FAIL original-source-shape");quit;}',
        'if(nrows(Units)!=1 || ncols(Units)!=1 || Units[1,1]!=1){print("@@FAIL original-source-unit");quit;}',
        "write("+ss(s,"ssi:w ")+",Source);",
        "def Copy=read("+ss(s,"ssi:r ")+");",
        'if(nrows(Copy)!=18 || ncols(Copy)!=1){print("@@FAIL source-copy-shape");quit;}',
        "int i; for(i=1;i<=18;i++){",
        'if(Copy[i,1]!=Source[i,1]){print("@@FAIL source-copy-product");quit;}}',
        'print("@@LIFT-CANDIDATE-END '+str(power)+'");',"quit;"]
    return "\n".join(lines)+"\n"
def verify_script(fd,model,out,power,first,product_paid):
    lines=ring(fd,model["fieldHomogeneousGenerators"])
    lines+=["degBound=0;","def Source=read("+ss(out/"whole-single-original-source.ssi","ssi:r ")+");",
        'if(nrows(Source)!=18 || ncols(Source)!=1){print("@@FAIL verified-source-shape");quit;}']
    if not product_paid:
        lines+=["matrix OriginalDifference=matrix(Original)*Source-matrix(ideal(tt^"+str(power)+"));",
            'if(OriginalDifference[1,1]!=0){print("@@FAIL original-source-product");quit;}',
            'print("@@ORIGINAL-HOMOGENEOUS-PRODUCT-VERIFIED");']
    for i in range(first,18):
        lines+=["write("+ss(out/("source-%02d.txt"%i),":w ")+",Source[%d,1]);"%(i+1),
            'print("@@SOURCE-TEXT '+str(i)+' "+string(size(Source[%d,1])));'%(i+1)]
    lines+=['print("@@SOURCE-TEXT-END");',"quit;"]
    return "\n".join(lines)+"\n"
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--model-driver",type=Path,required=True)
    ap.add_argument("--helper",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--singular",default="Singular")
    ap.add_argument("--degree",type=int,default=9)
    ap.add_argument("--seconds",type=float,default=600)
    ap.add_argument("--memory-mib",type=int,default=4096)
    a=ap.parse_args()
    need(a.degree==9,"this frozen first positive discovery uses only weight9")
    need(0<a.seconds<=3600 and 512<=a.memory_mib<=8192,"bounded resources")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    mpin=raw_identity(a.model_driver);hpin=raw_identity(a.helper)
    need(mpin["bytes"]==MODEL_BYTES and mpin["sha256"]==MODEL_SHA,"immutable original model driver")
    need(hpin["bytes"]==HELPER_BYTES and hpin["sha256"]==HELPER_SHA,"immutable complete physical model helper")
    fd=module(a.model_driver)
    own=fd.identity(Path(__file__));sem=semantic(own["sha256"],a.degree);binding=fd.digest(fd.canonical(sem))
    a.out.mkdir(parents=True,exist_ok=True)
    start=time.monotonic();deadline=start+a.seconds;child=None
    receipt=a.out/"original-bell-target-only-source-receipt.json"
    manifest=a.out/"manifest.json"
    state={"format":FORMAT+"-manifest","binding":binding,"semantic":sem,"generation":0,"sourceTexts":[]}
    rec={"format":FORMAT,"binding":binding,"source":own,"status":"running","parameters":{
        "seconds":a.seconds,"memoryMiB":a.memory_mib,"discoveryDegree":a.degree,
        "modelDriver":mpin,"helper":hpin,"allOriginal17VariablesRetained":True,
        "standardBasisCompletenessClaimed":False,"allBoundedPairsVerified":False,
        "characteristicZeroConclusion":False,"stages":[]}}
    def save():
        rec["elapsedSeconds"]=time.monotonic()-start
        rec["parameters"]["peakParentRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rec["parameters"]["peakChildRssKiB"]=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        # All phase descriptors and cursors are SMALL; never include polynomial arrays.
        rec["parameters"]["wholePhaseState"]=state
        fd.json_save(receipt,rec)
    def checkpoint():
        fd.json_save(manifest,state);rec["parameters"]["manifest"]=fd.identity(manifest);save()
    def tick():
        if time.monotonic()>=deadline-8:raise Budget("whole-phase target-only budget")
    def stop(signum,frame):raise Budget("signal "+str(signum))
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    def run_stage(name,script):
        nonlocal child
        tick();state["generation"]+=1;checkpoint();g=state["generation"]
        sp=a.out/("%04d-%s.sing"%(g,name));lp=a.out/("%04d-%s.log"%(g,name))
        fd.atomic(sp,script.encode("ascii"))
        stage={"name":name,"script":fd.identity(sp),"status":"running"}
        rec["parameters"]["stages"].append(stage);save();began=time.monotonic();budget=False
        try:
            with lp.open("wb") as f:
                child=subprocess.Popen([str(engine),"-q",str(sp)],stdout=f,stderr=subprocess.STDOUT)
                report=time.monotonic()
                while child.poll() is None:
                    tick()
                    if time.monotonic()-report>=30:
                        print(json.dumps({"phase":name,"elapsedSeconds":time.monotonic()-began,
                            "stdCheckpoint":"discovery" in state,"sourceCheckpoint":"singleSource" in state},separators=(",",":")),flush=True)
                        report=time.monotonic()
                    time.sleep(.2)
                rc=child.returncode;child=None
        except Budget:
            budget=True
            if child is not None and child.poll() is None:
                child.terminate()
                try:child.wait(timeout=5)
                except subprocess.TimeoutExpired:child.kill();child.wait()
            child=None;rc=75
        marks,bad=read_markers(lp)
        with lp.open("rb") as f:
            f.seek(max(0,lp.stat().st_size-4096));tail=f.read().decode("utf-8",errors="replace")
        stage.update(status="budget" if budget else "returned",exitCode=rc,
            elapsedSeconds=time.monotonic()-began,log=fd.identity(lp),
            actualMarkers=marks,diagnosticTail=tail)
        save();need(not bad,"explicit Singular failure: "+repr(bad[:3]))
        if not budget:need(rc==0,"successful Singular process")
        return lp,marks,budget
    def checked_file(desc):
        p=a.out/desc["path"]
        need(fd.identity(p)==desc,"whole retained temporary file SHA");return p
    code=1
    try:
        if manifest.exists():
            state=json.loads(manifest.read_bytes())
            need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding and state["semantic"]==sem,
                "same exact target-only semantic checkpoint")
        save()
        engine=shutil.which(a.singular) if not Path(a.singular).is_file() else str(a.singular)
        need(engine is not None,"actual installed Singular")
        engine=Path(engine).resolve()
        version=subprocess.run([str(engine),"--version"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=15)
        need(version.returncode==0,"actual Singular version")
        actual_engine={"binary":fd.identity(engine),"versionFirstLine":version.stdout.splitlines()[0]}
        if "engine" in state:need(state["engine"]==actual_engine,"same engine for whole SSI checkpoints")
        else:state["engine"]=actual_engine;checkpoint()
        rec["parameters"]["engine"]=actual_engine
        if "model" not in state:
            tick();m=fd.module(a.helper);model=fd.prepare(m)
            need(model["all17OriginalGradientPolynomialsVerified"] and model["allMeanAndHankelVariablesRetained"],
                "all original polynomial and Euler checks")
            state["model"]=fd.gz_save(a.out/"complete-original-model.json.gz",
                {"format":FORMAT+"-model","binding":binding,"data":model})
            state["modelDataSHA256"]=fd.digest(fd.canonical(model));checkpoint()
        packed=fd.gz_load(a.out,state["model"])
        need(packed["binding"]==binding and fd.digest(fd.canonical(packed["data"]))==state["modelDataSHA256"],
            "same complete original model data")
        model=packed["data"]
        rec["parameters"]["place"]=model["place"]
        rec["parameters"]["originalGradientTermCounts"]=[len(p) for p in model["originalSeventeenGradients"]]
        if "selftest" not in state:
            lp,marks,budget=run_stage("actual-std-ssi-one-target-selftest",selftest_script(a.out))
            complete=marker_once(marks,"@@SELFTEST-COMPLETE",False)
            if complete:
                need(marker_once(marks,"@@SELFTEST-DEGREE2 ") and marker_once(marks,"@@SELFTEST-DEGREE3 "),"both actual degrees")
                ctx=nmod_mpoly_ctx.get(("x","tt"),127,"lex")
                s0=parse_fast_polynomial(a.out/"selftest-source-0.txt",("x","tt"))
                s1=parse_fast_polynomial(a.out/"selftest-source-1.txt",("x","tt"))
                z=ctx.from_dict({(2,0):1,(0,2):126})*ctx.from_dict(s0)+ctx.from_dict({(1,1):1})*ctx.from_dict(s1)
                need(z==ctx.from_dict({(0,3):1}),"independent FLINT one-target selftest product")
                fast=parse_fast_polynomial(a.out/"selftest-parser.txt",("x","tt"))
                need(fast=={(4,0):122,(1,3):3,(0,0):7},"exact short-zero text parsing with signs and powers")
                state["selftest"]={"log":fd.identity(lp),"degree2NoPureParameter":True,
                    "degree3ContinuedFromActualG2":True,"wholeBasisAndSourceSSIRoundTrips":True,
                    "liftDegBoundExplicitlyZero":True,"liftUnitsIdentityVerified":True,
                    "allOriginalSourceProductsVerified":True,"independentFlintProductVerified":True,
                    "fastParserOriginalPolynomialVerified":True}
                checkpoint()
            if budget:raise Budget("selftest complete phases retained only at exact end marker")
            need(complete is not None,"complete actual independent selftest")
        else:
            testpath=checked_file(state["selftest"]["log"]);marks,bad=read_markers(testpath)
            need(not bad and marker_once(marks,"@@SELFTEST-COMPLETE"),"actual complete cached selftest transcript")
            need(all(v is True for k,v in state["selftest"].items() if k!="log"),"all cached selftest arithmetic gates")
        if "discovery" not in state:
            lp,marks,budget=run_stage("direct-original-std-weight9",discovery_script(fd,model,a.out,a.degree))
            end=marker_once(marks,"@@STD-END ",False)
            if end:
                vals=list(map(int,end.split()[1:]))
                need(len(vals)==5 and vals[0]==a.degree and vals[1]>0,"whole actual discovery metadata")
                degree,n,index,power,co=vals
                need((index==0 and power==0 and co==0) or
                    (1<=index<=n and 1<=power<=degree and co%P!=0),"literal pure parameter candidate")
                need(marker_once(marks,"@@STD-SSI-ROUNDTRIP"),"all saved basis polynomials reread equally")
                state["discovery"]={"log":fd.identity(lp),"basis":fd.identity(a.out/"whole-discovery-basis.ssi"),
                    "degree":degree,"basisColumns":n,"selectedOneBasedColumn":index,
                    "parameterPower":power,"coefficient":co%P,
                    "wholeSSIRoundtripVerified":True,"allBasisOriginalSourcesVerified":False,
                    "completeBoundedBuchbergerVerified":False}
                checkpoint()
            if budget:raise Budget("std complete SSI phase retained only after roundtrip and end marker")
            need(end is not None,"actual whole discovery end marker")
        checked_file(state["discovery"]["log"]);checked_file(state["discovery"]["basis"])
        discovery=state["discovery"]
        marks,bad=read_markers(a.out/discovery["log"]["path"])
        need(not bad and marker_once(marks,"@@STD-SSI-ROUNDTRIP"),"actual whole discovery transcript")
        values=list(map(int,marker_once(marks,"@@STD-END ").split()[1:]))
        need(values[:4]==[discovery["degree"],discovery["basisColumns"],discovery["selectedOneBasedColumn"],discovery["parameterPower"]]
            and values[4]%127==discovery["coefficient"],"discovery metadata equals actual transcript")
        if discovery["selectedOneBasedColumn"]==0:
            rec["status"]="completed-discovery";rec["parameters"]["outcome"]="returned-weight9-candidate-has-no-pure-parameter-column"
            rec["parameters"]["noMathematicalNegativeConclusion"]=True;code=0
        else:
            power=discovery["parameterPower"]
            # The already paid same-place complete weighted-six obstruction excludes power<=8.
            need(power==9,"same-place square nonmembership excludes all pure powers through8")
            rec["parameters"]["homogeneousParameterPower"]=power
            if "singleSource" not in state:
                lp,marks,budget=run_stage("lift-one-original-target-unbounded",lift_script(fd,model,a.out,power))
                end=marker_once(marks,"@@LIFT-CANDIDATE-END ",False)
                if end:
                    need(end=="@@LIFT-CANDIDATE-END "+str(power),"same literal lifted target")
                    state["singleSource"]={"log":fd.identity(lp),"sourceSSI":fd.identity(a.out/"whole-single-original-source.ssi"),
                        "rows":18,"columns":1,"unitsIdentityVerified":True,"wholeSSIRoundtripVerified":True,
                        "degBound":0,"allOriginalSourceProductsVerified":False}
                    checkpoint()
                if budget:raise Budget("one whole source candidate saved only after exact source SSI end")
                need(end is not None,"complete one-target source candidate")
            checked_file(state["singleSource"]["log"]);checked_file(state["singleSource"]["sourceSSI"])
            if "homogeneousProduct" in state:
                marks,bad=read_markers(checked_file(state["homogeneousProduct"]))
                need(not bad and marker_once(marks,"@@ORIGINAL-HOMOGENEOUS-PRODUCT-VERIFIED"),"actual paid original product transcript")
            for i,one in enumerate(state["sourceTexts"]):
                need(one["index"]==i,"consecutive whole source text files");checked_file(one["file"])
            if len(state["sourceTexts"])<18:
                first=len(state["sourceTexts"]);paid="homogeneousProduct" in state
                lp,marks,budget=run_stage("verify-one-source-and-dump-only18",
                    verify_script(fd,model,a.out,power,first,paid))
                full=marker_once(marks,"@@ORIGINAL-HOMOGENEOUS-PRODUCT-VERIFIED",False)
                if full:state["homogeneousProduct"]=fd.identity(lp)
                need(paid or full is not None or budget,"actual original product marker")
                for marker in marks:
                    if marker.startswith("@@SOURCE-TEXT "):
                        i,n=map(int,marker.split()[1:])
                        need(i==len(state["sourceTexts"]) and 0<=i<18 and n>=0,"next complete original source text")
                        state["sourceTexts"].append({"index":i,"termsBeforeHomogeneousExtraction":n,
                            "file":fd.identity(a.out/("source-%02d.txt"%i))})
                checkpoint()
                if budget:raise Budget("original source product and whole polynomial text prefix retained")
                need(marker_once(marks,"@@SOURCE-TEXT-END") and len(state["sourceTexts"])==18 and
                    "homogeneousProduct" in state,"all eighteen original source polynomials")
            ctx=nmod_mpoly_ctx.get(fd.NAMES,127,"lex")
            affine_ctx=nmod_mpoly_ctx.get(fd.NAMES[:-1],127,"lex")
            homogeneous=ctx.from_dict({});affine=affine_ctx.from_dict({})
            full=[];sources=[];discarded=0
            for i,desc in enumerate(state["sourceTexts"]):
                tick();raw=parse_fast_polynomial(checked_file(desc["file"]),fd.NAMES)
                need(len(raw)==desc["termsBeforeHomogeneousExtraction"],"complete original polynomial term count")
                ss0={e:c for e,c in raw.items() if sum(x*w for x,w in zip(e,fd.WEIGHTS))==power-fd.SOURCE_WEIGHTS[i]}
                discarded+=len(raw)-len(ss0);full.append(fd.poly_record(ss0))
                homogeneous+=ctx.from_dict(fd.record_dict(model["fieldHomogeneousGenerators"][i],18))*ctx.from_dict(ss0)
                aa={}
                for e,c in ss0.items():fd.add_term(aa,e[:-1],c)
                sources.append(fd.poly_record(aa))
                affine+=affine_ctx.from_dict(fd.record_dict(model["fieldAffineGenerators"][i],17))*affine_ctx.from_dict(aa)
            target=(0,)*17+(power,)
            need(homogeneous==ctx.from_dict({target:1}),"independent full18-variable original homogeneous source product")
            need(affine==affine_ctx.from_dict({(0,)*17:1}),"independent full17-variable original affine source for one")
            positive={"format":FORMAT+"-positive","binding":binding,"prime":127,"matchedPlace":100,
                "homogeneousParameterPower":power,"homogeneousBasisColumn":discovery["selectedOneBasedColumn"]-1,
                "originalAffineSourceLabels":fd.SOURCE_LABELS[:-1]+["Bell-minus-one"],
                "fullOriginalHomogeneousSources":full,"fullOriginalAffineSources":sources,
                "sourceTermCounts":[len(s) for s in sources],"totalSourceTerms":sum(len(s) for s in sources),
                "nonTargetWeightTermsDiscarded":discarded,"allOriginal17ParametersRetained":True,
                "all18FieldOriginalSourceProductsVerified":True,"all18HomogeneousOriginalProductsVerified":True,
                "independentFlintHomogeneousAndAffineProductsVerified":True,
                "standardBasisCompletenessClaimed":False,"characteristicZeroOriginalIdentityVerified":False}
            state["positiveCandidate"]=fd.gz_save(a.out/"complete-original-affine-field-source-for-one.json.gz",positive)
            state["positiveDataSHA256"]=fd.digest(fd.canonical(positive))
            rec["parameters"].update(positiveCandidate=state["positiveCandidate"],
                candidateSourceTerms=positive["totalSourceTerms"],all18FieldOriginalSourceProductsVerified=True,
                bothIndependentFlintProductsVerified=True,exactEConsumerAlreadyRun=False,
                outcome="verified-single-original-field-source-for-one")
            rec["status"]="completed";code=0
        checkpoint()
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
        if manifest.exists():rec["parameters"]["manifest"]=fd.identity(manifest)
        save()
    print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True);return code
if __name__=="__main__":raise SystemExit(main())
