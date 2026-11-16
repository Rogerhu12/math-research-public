#!/usr/bin/env python3
"""Discover three rational components of the original Bell cube over F127.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

The ideal has all seventeen original gradients and all seventeen variables.
Only target sources are extracted. Neither a nonzero reduction nor a budget
exit is a nonmembership certificate. Exact Q multiplication is a separate gate.
All polynomial arrays and Singular SSI checkpoints are temporary only.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,resource,shutil,signal,subprocess,time
from pathlib import Path
from flint import fmpq,nmod_mpoly_ctx

FORMAT="r150-original-bell-cube-three-rational-targets-v1"
MODEL_BYTES=31156
MODEL_SHA="da80b727c47a050f3e268f00d1d6598336866a41b354d6aecb5edbb1ca1e730d"
HELPER_BYTES=16964
HELPER_SHA="31df769fb0fd3a41eb7606f500aae8b46952219c24927bd3265ed3dc34d7fe10"
UTILITY_BYTES=26853
UTILITY_SHA="8ac1e9275f9e3d3412f2744c0fe31acc06d58eda677ec270c9a37e39f9372b39"
UTILITY_FORMAT="r150-original-bell-target-only-source-v1"
P=127
WEIGHTS=(1,)*6+(2,)*11
SOURCE_WEIGHTS=(4,)*11+(5,)*6
ALGORITHM="original17-std-weight9-discovery-three-Q-components-and-target-only-original17-by3-lift"
class Budget(Exception):pass
def need(ok,message):
    if not ok:raise ValueError(message)
def module(p,name):
    sp=importlib.util.spec_from_file_location(name,p)
    z=importlib.util.module_from_spec(sp);sp.loader.exec_module(z);return z
def raw_identity(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def semantic(own_sha):
    return {"format":FORMAT,"sourceSha256":own_sha,"modelDriverSHA256":MODEL_SHA,
        "helperSHA256":HELPER_SHA,"utilitySHA256":UTILITY_SHA,"prime":127,
        "originalVariableCount":17,"originalGradientCount":17,"targetCount":3,
        "weight":9,"coefficientBasis":["1","d","d^2"],"algorithm":ALGORITHM}
def qpoly(m,p):
    return m.CTX.from_dict({tuple(e):fmpq(c) for e,c in p})
def prepare(fd,m):
    model=fd.prepare(m)
    need(model["all17OriginalGradientPolynomialsVerified"] and
         model["allWeightedEulerCoefficientsVerified"] and
         model["allMeanAndHankelVariablesRetained"],"all complete original model gates")
    bell=[qpoly(m,p) for p in model["BellFieldComponents"]]
    F=m.Field();cube=F.mul_polys(F.mul_polys(bell,bell),bell)
    for z in cube:m.weighted(z,9)
    targets=[];count=0
    for z in cube:
        p={}
        for e,c in z.to_dict().items():
            v=fd.q127(c);count+=1
            if v:p[tuple(map(int,e))]=v
        targets.append(fd.poly_record(p))
    need(all(targets),"all three rational target components remain nonzero at the fixed prime")
    original=model["fieldAffineGenerators"][:17]
    need(len(original)==17 and all(
        all(len(e)==17 and sum(x*w for x,w in zip(e,WEIGHTS))==SOURCE_WEIGHTS[i] for e,c in p)
        for i,p in enumerate(original)),"all original seventeen weighted field generators")
    ctx=nmod_mpoly_ctx.get(tuple(model["variableNames"][:-1]),127,"lex")
    evaluated=ctx.from_dict({})
    for k,p in enumerate(targets):
        evaluated+=ctx.from_dict(fd.record_dict(p,17))*pow(100,k,127)
    fb={}
    for k,z in enumerate(bell):
        for e,c in z.to_dict().items():fd.add_term(fb,tuple(map(int,e)),fd.q127(c)*pow(100,k,127))
    need(evaluated==ctx.from_dict(fb)**3,"three rational components equal the original matched-place cube")
    model.update(naturalCubeRationalComponents=[m.pv(z) for z in cube],
        fieldNaturalCubeRationalComponents=targets,fieldOriginalSeventeenGenerators=original,
        rationalTargetIntegralCoefficientCount=count,
        allThreeTargetsWeightNineVerified=True,allThreeFieldComponentsRecombineToOriginalCube=True)
    return model
def ring(fd,model):
    names=tuple(model["variableNames"][:-1])
    return ["ring r=127,("+",".join(names)+"),wp("+",".join(map(str,WEIGHTS))+");",
        "short=0; option(redSB); option(redTail);",
        "ideal Original="+",".join(fd.singular_poly(p,names) for p in model["fieldOriginalSeventeenGenerators"])+";",
        "ideal Targets="+",".join(fd.singular_poly(p,names) for p in model["fieldNaturalCubeRationalComponents"])+";"]
def selftest_script(ut,out):
    base=ut.selftest_script(out)
    last='print("@@SELFTEST-COMPLETE");quit;'
    need(base.count(last)==1,"one frozen selftest final marker")
    tail=[
        'print("@@SELFTEST-COMPLETE");',
        "degBound=0; ideal Targets3=tt^3,x*tt^2,x^2*tt; matrix Units3;",
        'matrix Sources3=lift(Original,Targets3,Units3,"std");',
        'if(nrows(Sources3)!=2 || ncols(Sources3)!=3){print("@@FAIL three-source-shape");quit;}',
        'if(nrows(Units3)!=3 || ncols(Units3)!=3){print("@@FAIL three-unit-shape");quit;}',
        "int j; matrix Diff3=matrix(Original)*Sources3-matrix(Targets3);",
        "for(i=1;i<=3;i++){",
        'if(Diff3[1,i]!=0){print("@@FAIL three-original-product");quit;}',
        'for(j=1;j<=3;j++){if(Units3[i,j]!=(i==j)){print("@@FAIL three-unit-entry");quit;}}}',
    ]
    for k in range(3):
        for i in range(2):
            tail+=["write("+ut.ss(out/("selftest-three-%d-%d.txt"%(k,i)),":w ")+",Sources3[%d,%d]);"%(i+1,k+1)]
    tail+=['print("@@THREE-TARGET-SELFTEST-COMPLETE");quit;']
    return base.replace(last,"\n".join(tail))
def discovery_script(fd,ut,model,out):
    gp=out/"whole-original17-discovery-basis.ssi"
    lines=ring(fd,model)+[
        'print("@@STD17-START 9");',"degBound=9; ideal G=std(Original);",
        'print("@@STD17-RETURN "+string(size(G)));',
        "write("+ut.ss(gp,"ssi:w ")+",G);",
        "def Copy=read("+ut.ss(gp,"ssi:r ")+");",
        'if(size(Copy)!=size(G)){print("@@FAIL original17-basis-copy-shape");quit;}',
        "int i; for(i=1;i<=size(G);i++){",
        'if(Copy[i]!=G[i]){print("@@FAIL original17-basis-copy-product");quit;}}',
        'print("@@STD17-SSI-ROUNDTRIP");',
        "degBound=0; int nonzero=0;",
    ]
    for k in range(3):
        lines+=["poly residual%d=reduce(Targets[%d],G);"%(k,k+1),
            "write("+ut.ss(out/("discovery-target-residual-%d.txt"%k),":w ")+",residual%d);"%k,
            "if(residual%d!=0){nonzero++;}"%k,
            'print("@@TARGET-REDUCTION '+str(k)+' "+string(size(residual%d)));'%k]
    lines+=['print("@@STD17-END "+string(size(G))+" "+string(nonzero));',"quit;"]
    return "\n".join(lines)+"\n"
def lift_script(fd,ut,model,out):
    sp=out/"whole-original17-three-target-sources.ssi"
    return "\n".join(ring(fd,model)+[
        "degBound=0; matrix Units;",
        'print("@@THREE-ORIGINAL-LIFT-START");',
        'matrix Sources=lift(Original,Targets,Units,"std");',
        'print("@@THREE-ORIGINAL-LIFT-RETURN");',
        'if(nrows(Sources)!=17 || ncols(Sources)!=3){print("@@FAIL full17-by3-source-shape");quit;}',
        'if(nrows(Units)!=3 || ncols(Units)!=3){print("@@FAIL full3-unit-shape");quit;}',
        "int i; int j; for(i=1;i<=3;i++){for(j=1;j<=3;j++){",
        'if(Units[i,j]!=(i==j)){print("@@FAIL full3-unit-entry");quit;}}}',
        "write("+ut.ss(sp,"ssi:w ")+",Sources);",
        "def Copy=read("+ut.ss(sp,"ssi:r ")+");",
        'if(nrows(Copy)!=17 || ncols(Copy)!=3){print("@@FAIL source-copy-shape");quit;}',
        "for(i=1;i<=17;i++){for(j=1;j<=3;j++){",
        'if(Copy[i,j]!=Sources[i,j]){print("@@FAIL whole51-source-copy-product");quit;}}}',
        'print("@@THREE-ORIGINAL-LIFT-CANDIDATE-END");',"quit;"])+"\n"
def verify_script(fd,ut,model,out,first,product_paid):
    lines=ring(fd,model)+[
        "degBound=0;",
        "def Sources=read("+ut.ss(out/"whole-original17-three-target-sources.ssi","ssi:r ")+");",
        'if(nrows(Sources)!=17 || ncols(Sources)!=3){print("@@FAIL verify17-by3-shape");quit;}']
    if not product_paid:
        lines+=["matrix Difference=matrix(Original)*Sources-matrix(Targets);","int i;",
            "for(i=1;i<=3;i++){",
            'if(Difference[1,i]!=0){print("@@FAIL three-full-original-products");quit;}}',
            'print("@@ALL-THREE-ORIGINAL-PRODUCTS-VERIFIED");']
    for index in range(first,51):
        k,i=divmod(index,17)
        lines+=["write("+ut.ss(out/("source-%02d.txt"%index),":w ")+",Sources[%d,%d]);"%(i+1,k+1),
            'print("@@SOURCE-TEXT '+str(index)+' "+string(size(Sources[%d,%d])));'%(i+1,k+1)]
    lines+=['print("@@ALL-51-SOURCE-TEXTS-END");',"quit;"]
    return "\n".join(lines)+"\n"
def main():
    ap=argparse.ArgumentParser()
    for name in ("model-driver","helper","utility-driver","out"):
        ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--singular",default="Singular")
    ap.add_argument("--seconds",type=float,default=600)
    ap.add_argument("--memory-mib",type=int,default=4096)
    a=ap.parse_args()
    need(0<a.seconds<=3600 and 512<=a.memory_mib<=8192,"bounded field resources")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    pins={}
    for name,p,size,digest in [
        ("model",a.model_driver,MODEL_BYTES,MODEL_SHA),("helper",a.helper,HELPER_BYTES,HELPER_SHA),
        ("utility",a.utility_driver,UTILITY_BYTES,UTILITY_SHA)]:
        pins[name]=raw_identity(p)
        need(pins[name]["bytes"]==size and pins[name]["sha256"]==digest,"exact frozen "+name)
    fd=module(a.model_driver,"r150_three_q_model")
    ut=module(a.utility_driver,"r150_three_q_literal_parser")
    need(ut.FORMAT==UTILITY_FORMAT,"frozen utility identity")
    own=raw_identity(Path(__file__));sem=semantic(own["sha256"]);binding=fd.digest(fd.canonical(sem))
    a.out.mkdir(parents=True,exist_ok=True)
    start=time.monotonic();deadline=start+a.seconds;child=None
    receipt=a.out/"original-bell-cube-three-rational-targets-receipt.json"
    manifest=a.out/"manifest.json"
    state={"format":FORMAT+"-manifest","binding":binding,"semantic":sem,
        "generation":0,"sourceTexts":[],"verifiedFieldComponents":[]}
    rec={"format":FORMAT,"binding":binding,"source":own,"status":"running","parameters":{
        "seconds":a.seconds,"memoryMiB":a.memory_mib,"pinnedSources":pins,
        "allOriginal17VariablesAnd17GradientsRetained":True,"targetCount":3,"targetWeight":9,
        "weightNineCompleteSourceColumns":16442,"weightNineCompleteOutputRows":49368,
        "completeWeightNineMatrixRankComputed":False,"boundedStandardBasisCompletenessClaimed":False,
        "characteristicZeroConclusion":False,"stages":[]}}
    def save():
        rec["elapsedSeconds"]=time.monotonic()-start
        rec["parameters"]["peakParentRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rec["parameters"]["peakChildRssKiB"]=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        rec["parameters"]["wholePhaseState"]=state
        fd.json_save(receipt,rec)
    def checkpoint():
        fd.json_save(manifest,state);rec["parameters"]["manifest"]=fd.identity(manifest);save()
    def tick():
        if time.monotonic()>=deadline-8:raise Budget("three-target whole-phase budget")
    def stop(signum,frame):raise Budget("signal "+str(signum))
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    def checked(desc):
        p=a.out/desc["path"];need(fd.identity(p)==desc,"whole temporary file SHA");return p
    def run_stage(name,script):
        nonlocal child
        tick();state["generation"]+=1;checkpoint();g=state["generation"]
        sp=a.out/("%04d-%s.sing"%(g,name));lp=a.out/("%04d-%s.log"%(g,name))
        fd.atomic(sp,script.encode("ascii"));stage={"name":name,"script":fd.identity(sp),"status":"running"}
        rec["parameters"]["stages"].append(stage);save();begin=time.monotonic();budget=False
        try:
            with lp.open("wb") as f:
                child=subprocess.Popen([str(engine),"-q",str(sp)],stdout=f,stderr=subprocess.STDOUT)
                report=time.monotonic()
                while child.poll() is None:
                    tick()
                    if time.monotonic()-report>=30:
                        print(json.dumps({"phase":name,"elapsedSeconds":time.monotonic()-begin,
                            "wholeDiscoverySaved":"discovery" in state,
                            "wholeThreeSourcesSaved":"threeSources" in state},separators=(",",":")),flush=True)
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
        markers,bad=ut.read_markers(lp)
        with lp.open("rb") as f:
            f.seek(max(0,lp.stat().st_size-4096));tail=f.read().decode("utf-8",errors="replace")
        stage.update(status="budget" if budget else "returned",exitCode=rc,
            elapsedSeconds=time.monotonic()-begin,log=fd.identity(lp),actualMarkers=markers,diagnosticTail=tail)
        save();need(not bad,"explicit Singular failure: "+repr(bad[:3]))
        if not budget:need(rc==0,"successful exact Singular process")
        return lp,markers,budget
    code=1
    try:
        if manifest.exists():
            state=json.loads(manifest.read_bytes())
            need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding and
                 state["semantic"]==sem,"same exact three-target checkpoint")
        engine=shutil.which(a.singular) if not Path(a.singular).is_file() else str(a.singular)
        need(engine is not None,"actual installed Singular");engine=Path(engine).resolve()
        version=subprocess.run([str(engine),"--version"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=15)
        need(version.returncode==0,"actual Singular version")
        actual={"binary":fd.identity(engine),"versionFirstLine":version.stdout.splitlines()[0]}
        if "engine" in state:need(state["engine"]==actual,"same engine for SSI checkpoints")
        else:state["engine"]=actual;checkpoint()
        rec["parameters"]["engine"]=actual
        if "model" not in state:
            tick();m=fd.module(a.helper);model=prepare(fd,m)
            state["model"]=fd.gz_save(a.out/"complete-original-three-rational-target-model.json.gz",
                {"format":FORMAT+"-model","binding":binding,"data":model})
            state["modelDataSHA256"]=fd.digest(fd.canonical(model));checkpoint()
        packed=fd.gz_load(a.out,state["model"])
        need(packed["format"]==FORMAT+"-model" and packed["binding"]==binding and
             fd.digest(fd.canonical(packed["data"]))==state["modelDataSHA256"],"all original model bytes")
        model=packed["data"];names=tuple(model["variableNames"][:-1])
        need(len(names)==17 and model["allThreeTargetsWeightNineVerified"] and
             model["allThreeFieldComponentsRecombineToOriginalCube"],"all rational cube target gates")
        rec["parameters"].update(originalGradientTermCounts=[len(p) for p in model["originalSeventeenGradients"]],
            rationalCubeComponentTermCounts=[len(p) for p in model["naturalCubeRationalComponents"]],
            integralTargetCoefficientCount=model["rationalTargetIntegralCoefficientCount"],
            originalCoefficientField=model["matchedCubic"])
        if "selftest" not in state:
            lp,markers,budget=run_stage("std-ssi-and-three-target-lift-selftest",selftest_script(ut,a.out))
            complete=ut.marker_once(markers,"@@THREE-TARGET-SELFTEST-COMPLETE",False)
            if complete:
                need(ut.marker_once(markers,"@@SELFTEST-COMPLETE") and
                     ut.marker_once(markers,"@@SELFTEST-DEGREE2 ") and
                     ut.marker_once(markers,"@@SELFTEST-DEGREE3 "),"all independent two-degree gates")
                ctx=nmod_mpoly_ctx.get(("x","tt"),127,"lex")
                orig=[ctx.from_dict({(2,0):1,(0,2):126}),ctx.from_dict({(1,1):1})]
                expected=[ctx.from_dict({(0,3):1}),ctx.from_dict({(1,2):1}),ctx.from_dict({(2,1):1})]
                for k in range(3):
                    total=ctx.from_dict({})
                    for i in range(2):
                        total+=orig[i]*ctx.from_dict(ut.parse_fast_polynomial(
                            a.out/("selftest-three-%d-%d.txt"%(k,i)),("x","tt")))
                    need(total==expected[k],"independent full original three-target fixture "+str(k))
                need(ut.parse_fast_polynomial(a.out/"selftest-parser.txt",("x","tt"))==
                     {(4,0):122,(1,3):3,(0,0):7},"same safe literal expanded polynomial parser")
                state["selftest"]={"log":fd.identity(lp),"degree2NoPureParameter":True,
                    "actualDegree2PrefixContinuesTo3":True,"wholeSSIRoundtrip":True,
                    "liftDegBoundZero":True,"threeByThreeUnitsIdentity":True,
                    "allThreeNativeOriginalProducts":True,"allThreeIndependentFlintProducts":True}
                checkpoint()
            if budget:raise Budget("only complete actual selftest marker is reusable")
            need(complete is not None,"actual complete three-target selftest")
        else:
            markers,bad=ut.read_markers(checked(state["selftest"]["log"]))
            need(not bad and ut.marker_once(markers,"@@THREE-TARGET-SELFTEST-COMPLETE") and
                 all(v is True for k,v in state["selftest"].items() if k!="log"),"whole paid selftest")
        if "discovery" not in state:
            lp,markers,budget=run_stage("original17-std-weight9-and-three-reductions",discovery_script(fd,ut,model,a.out))
            end=ut.marker_once(markers,"@@STD17-END ",False)
            if end:
                n,count=map(int,end.split()[1:])
                need(n>0 and 0<=count<=3 and ut.marker_once(markers,"@@STD17-SSI-ROUNDTRIP"),
                     "whole original17 discovery metadata")
                residuals=[]
                for k in range(3):
                    marker=ut.marker_once(markers,"@@TARGET-REDUCTION "+str(k)+" ")
                    parts=marker.split();need(len(parts)==3 and int(parts[1])==k,"all three target reductions")
                    residuals.append({"component":k,"terms":int(parts[2]),
                        "file":fd.identity(a.out/("discovery-target-residual-%d.txt"%k))})
                need(sum(z["terms"]>0 for z in residuals)==count,"literal number of nonzero reduced targets")
                state["discovery"]={"log":fd.identity(lp),"basis":fd.identity(a.out/"whole-original17-discovery-basis.ssi"),
                    "basisColumns":n,"nonzeroReducedTargetCount":count,"residuals":residuals,
                    "wholeSSIRoundtripVerified":True,"standardBasisCompletenessClaimed":False}
                checkpoint()
            if budget:raise Budget("std phase is retained only after actual whole end marker")
            need(end is not None,"actual whole original17 discovery")
        discovery=state["discovery"]
        markers,bad=ut.read_markers(checked(discovery["log"]));checked(discovery["basis"])
        need(not bad and ut.marker_once(markers,"@@STD17-SSI-ROUNDTRIP"),"paid complete discovery transcript")
        need(list(map(int,ut.marker_once(markers,"@@STD17-END ").split()[1:]))==
             [discovery["basisColumns"],discovery["nonzeroReducedTargetCount"]],"same actual discovery metadata")
        for k,z in enumerate(discovery["residuals"]):
            need(z["component"]==k and len(ut.parse_fast_polynomial(checked(z["file"]),names))==z["terms"],
                 "complete actual reduced polynomial file")
        if discovery["nonzeroReducedTargetCount"]:
            rec["status"]="completed-discovery";rec["parameters"].update(
                outcome="at-least-one-rational-target-has-nonzero-discovery-remainder",
                noNonmembershipConclusion=True,noExactOriginalSourceYet=True)
            checkpoint();return 0
        if "threeSources" not in state:
            lp,markers,budget=run_stage("lift-only-three-original-targets",lift_script(fd,ut,model,a.out))
            end=ut.marker_once(markers,"@@THREE-ORIGINAL-LIFT-CANDIDATE-END",False)
            if end:
                state["threeSources"]={"log":fd.identity(lp),
                    "sourceSSI":fd.identity(a.out/"whole-original17-three-target-sources.ssi"),
                    "rows":17,"columns":3,"unitsIdentityVerified":True,
                    "wholeSSIRoundtripVerified":True,"allOriginalProductsVerified":False,"degBound":0}
                checkpoint()
            if budget:raise Budget("three whole source columns saved only after exact SSI marker")
            need(end is not None,"complete original17-by3 source candidate")
        checked(state["threeSources"]["sourceSSI"])
        markers,bad=ut.read_markers(checked(state["threeSources"]["log"]))
        need(not bad and ut.marker_once(markers,"@@THREE-ORIGINAL-LIFT-CANDIDATE-END"),"actual source candidate transcript")
        if "nativeProducts" in state:
            markers,bad=ut.read_markers(checked(state["nativeProducts"]))
            need(not bad and ut.marker_once(markers,"@@ALL-THREE-ORIGINAL-PRODUCTS-VERIFIED"),
                 "actual full original native products")
        for i,z in enumerate(state["sourceTexts"]):
            need(z["index"]==i,"consecutive complete source text prefix");checked(z["file"])
        if len(state["sourceTexts"])<51:
            lp,markers,budget=run_stage("verify-three-sources-and-dump51",
                verify_script(fd,ut,model,a.out,len(state["sourceTexts"]),"nativeProducts" in state))
            mark=ut.marker_once(markers,"@@ALL-THREE-ORIGINAL-PRODUCTS-VERIFIED",False)
            if mark:state["nativeProducts"]=fd.identity(lp)
            for line in markers:
                if line.startswith("@@SOURCE-TEXT "):
                    i,n=map(int,line.split()[1:])
                    need(i==len(state["sourceTexts"]) and 0<=i<51 and n>=0,"next whole source text")
                    state["sourceTexts"].append({"index":i,"termsBeforeHomogeneousExtraction":n,
                        "file":fd.identity(a.out/("source-%02d.txt"%i))})
            checkpoint()
            if budget:raise Budget("whole native products and consecutive text files retained")
            need(ut.marker_once(markers,"@@ALL-51-SOURCE-TEXTS-END") and
                 len(state["sourceTexts"])==51 and "nativeProducts" in state,"all original source texts")
        ctx=nmod_mpoly_ctx.get(names,127,"lex")
        sources=[[None for _ in range(17)] for _ in range(3)];discarded=0
        for index,z in enumerate(state["sourceTexts"]):
            tick();k,i=divmod(index,17);raw=ut.parse_fast_polynomial(checked(z["file"]),names)
            need(len(raw)==z["termsBeforeHomogeneousExtraction"],"complete source term count")
            pp={e:c for e,c in raw.items() if sum(x*w for x,w in zip(e,WEIGHTS))==9-SOURCE_WEIGHTS[i]}
            discarded+=len(raw)-len(pp);sources[k][i]=fd.poly_record(pp)
        need(state["verifiedFieldComponents"]==list(range(len(state["verifiedFieldComponents"]))) and
             len(state["verifiedFieldComponents"])<=3,"whole original component verification cursor")
        for k in range(3):
            if k in state["verifiedFieldComponents"]:continue
            tick();total=ctx.from_dict({})
            for i in range(17):
                total+=ctx.from_dict(fd.record_dict(model["fieldOriginalSeventeenGenerators"][i],17))*\
                       ctx.from_dict(fd.record_dict(sources[k][i],17))
                tick()
            need(total==ctx.from_dict(fd.record_dict(model["fieldNaturalCubeRationalComponents"][k],17)),
                 "independent full original17-variable target product "+str(k))
            state["verifiedFieldComponents"].append(k);checkpoint()
            print(json.dumps({"phase":"complete-original-field-rational-component","component":k,
                "allOriginalPolynomialCoordinatesVerified":True},separators=(",",":")),flush=True)
        slots=set()
        for component in sources:
            for i,p in enumerate(component):
                for e,c in p:slots.add((i,tuple(e)))
        positive={"format":FORMAT+"-positive","binding":binding,"prime":127,
            "targetWeight":9,"originalGradientCount":17,"rationalTargetCount":3,
            "coefficientBasis":["1","d","d^2"],"matchedCubic":model["matchedCubic"],
            "allOriginalSourcePolynomialsByTarget":sources,"sourceTermCountsByTarget":[
                sum(len(p) for p in component) for component in sources],
            "unionOriginalSourceSupportSize":len(slots),"nonWeightNineSourceTermsDiscarded":discarded,
            "allThreeFullOriginalFieldPolynomialProductsVerified":True,
            "allOriginal17VariablesRetained":True,"characteristicZeroIdentityVerified":False,
            "completeWeightNineRankOrNegativeConclusion":False}
        state["positiveCandidate"]=fd.gz_save(a.out/"complete-original-three-target-field-sources.json.gz",positive)
        state["positiveDataSHA256"]=fd.digest(fd.canonical(positive))
        rec["parameters"].update(outcome="three-verified-original-field-sources-for-rational-cube-components",
            positiveCandidate=state["positiveCandidate"],unionSourceSupportSize=len(slots),
            sourceTermCountsByTarget=positive["sourceTermCountsByTarget"],
            allThreeFullOriginalFieldPolynomialProductsVerified=True)
        rec["status"]="completed";checkpoint();code=0
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
        print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
    return code
if __name__=="__main__":raise SystemExit(main())
