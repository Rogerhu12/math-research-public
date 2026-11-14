#!/usr/bin/env python3
"""One shared300-second all200 original Bockstein pipeline.

Compilation is separately bounded before the mathematical deadline. All three
native stages and the final infinite-quotient test share one deadline. Every
child has the stated address-space cap. Large original recovery files remain
in recovery/ for the single Actions artifact; results/ contains publishable
small receipts, identities and the complete necessary-test matrices.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,shutil,subprocess,time
from pathlib import Path

INPUTS={
 "graph":(["reweighted-basis.bin"],"bb2b36e3b083bf3b66e692f3fdef603941ef3c9c0a1b8fa7a74fad6722fb56ce"),
 "model":(["normal-form-input.txt","native-normal-form-input.txt"],"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"),
 "originalNF":(["nf-normal-forms.bin"],"eeba714c9a9675a8fdac31bf3cd105f50bc5b26de7940301549d903d964d3840"),
 "normalTrace":(["nf-reduction.bin"],"e977b75f618f30d00fd4edca3bdcadba1e5553a956bf4d781ee45df0d15c1e8b"),
 "forward":(["nf-forward.bin"],"66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e"),
 "backward":(["nf-backward.bin"],"cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f"),
}
INTEGER_MODEL="71630a822927659a58a7b9df4cdcdb5385b9ea71be9f246097bbbfd1fdc9a5f8"
STATE="06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf"
FIRST="f3efdaf748571cd830decf3e67b87d9821f1508cc794a6eecd93b5a6a1260e45"
CPP_NAMES={
 "original":"2026-11-14-r150-high-kernel-bockstein-original-789f.cpp",
 "normal":"2026-11-14-r150-high-kernel-bockstein-normal-form-789f.cpp",
 "image":"2026-11-14-r150-high-kernel-bockstein-image-789f.cpp",
}

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        while b:=f.read(1048576):h.update(b)
    return h.hexdigest()

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--recovery-root",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--seconds",type=int,default=300)
    p.add_argument("--memory-mib",type=int,default=512)
    p.add_argument("--compile-seconds",type=int,default=30)
    p.add_argument("--prepare-only",action="store_true",help="validate inputs and compile; no mathematical phase")
    a=p.parse_args()
    if min(a.seconds,a.memory_mib,a.compile_seconds)<1:raise ValueError("positive explicit bounds required")
    root=Path(__file__).resolve().parent
    a.out=a.out.resolve();a.out.mkdir(parents=True,exist_ok=True)
    results=a.out/"results";recovery=a.out/"recovery";binary_dir=a.out/"bin"
    for folder in (results,recovery,binary_dir):folder.mkdir(exist_ok=True)
    rp=results/"bockstein-pipeline-receipt.json"
    receipt={"format":"r150-all200-original-bockstein-pipeline-v1","status":"preparing","field":31,
      "finite_budget_verified":False,"infiniteQuotientNecessaryTestOnly":True,
      "sharedMathematicalSecondsLimit":a.seconds,"perChildAddressSpaceMiBLimit":a.memory_mib,
      "perCompilationSecondsLimit":a.compile_seconds,"deadlineRule":"The mathematical deadline starts after input validation and compilation; all3 native stages and the final Python necessary test share it. Each child receives timeout equal to the actual remaining deadline, with10-second forced-kill grace. Input hashes/output hashes between mathematical stages count against the shared deadline. Final artifact bookkeeping is outside it.",
      "inputArtifact":{"run":43597823809,"artifact":14114364261,"oldNFOrGraphRebuilt":False},
      "inputs":{},"sources":{},"compilations":{},"stages":{},"outputs":{}}
    def save():rp.write_text(json.dumps(receipt,indent=2)+"\n")
    save()
    found={}
    try:
        for name,(names,expected) in INPUTS.items():
            candidates=sorted({f for short in names for f in a.recovery_root.rglob(short) if f.is_file()})
            good=[f for f in candidates if sha(f)==expected]
            if not good:raise ValueError("missing exact artifact input: "+name)
            found[name]=good[0].resolve();receipt["inputs"][name]={"file":str(found[name]),"bytes":found[name].stat().st_size,"sha256":expected}
        integer=root/"r150-first-padic-residual-789f/original-integer-mod961.txt"
        integer_receipt=root/"r150-first-padic-residual-789f/integer-model-receipt.json"
        state=root/"2026-11-14-r150-torsion-state.bin-789f.gz"
        state_receipt=root/"2026-11-14-r150-native-torsion-state-receipt-789f.json"
        first=root/"r150-first-residual-image-obstruction-789f/image-certificate/image-remainders.bin.gz"
        if sha(integer)!=INTEGER_MODEL:raise ValueError("original primitive integer model checksum")
        ir=json.loads(integer_receipt.read_text())
        if ir.get("status")!="exact-integer-model-generated" or ir.get("modulus")!=961 or ir["model"]["sha256"]!=INTEGER_MODEL:raise ValueError("original integer model provenance")
        if hashlib.sha256(gzip.decompress(state.read_bytes())).hexdigest()!=STATE:raise ValueError("complete original state checksum")
        if hashlib.sha256(gzip.decompress(first.read_bytes())).hexdigest()!=FIRST:raise ValueError("actual first-residual quotient checksum")
        for name,f,uncompressed in (("integerModel",integer,INTEGER_MODEL),("integerModelReceipt",integer_receipt,None),("wholeState",state,STATE),("wholeStateReceipt",state_receipt,None),("firstResidualQuotient",first,FIRST)):
            receipt["inputs"][name]={"file":str(f),"bytes":f.stat().st_size,"sha256":sha(f),"uncompressedSHA256":uncompressed}
        extra=["2026-11-14-r150-f31-bitplane-789f.hpp","2026-11-14-r150-high-kernel-bockstein-torsion-789f.py","2026-11-14-r150-torsion-characteristic-789f.py",Path(__file__).name]
        for name in list(CPP_NAMES.values())+extra:receipt["sources"][name]=sha(root/name)
        save()
        binaries={}
        for name,filename in CPP_NAMES.items():
            binary=binary_dir/name
            command=["timeout","--kill-after=10s",f"{a.compile_seconds}s","prlimit",f"--as={a.memory_mib*1048576}","--core=0","--","g++","-O2","-std=c++17",str(root/filename),"-o",str(binary)]
            started=time.monotonic();r=subprocess.run(command,capture_output=True,text=True)
            (results/("compile-"+name+".log")).write_text(r.stdout+r.stderr)
            receipt["compilations"][name]={"command":command,"exitCode":r.returncode,"elapsedSeconds":time.monotonic()-started}
            if r.returncode:raise RuntimeError("bounded compilation failed: "+name)
            receipt["compilations"][name]["binarySHA256"]=sha(binary);binaries[name]=binary;save()
        if a.prepare_only:
            receipt["status"]="prepared-no-mathematics-executed";save();print(json.dumps({"status":receipt["status"],"finite_budget_verified":False}));return
        receipt["status"]="running";math_start=time.monotonic();deadline=math_start+a.seconds;save()
        def run_stage(name,command,marker,required):
            remaining=deadline-time.monotonic()
            if remaining<=0:raise TimeoutError("shared mathematical deadline before "+name)
            bounded=["timeout","--kill-after=10s",f"{remaining:.3f}s","prlimit",f"--as={a.memory_mib*1048576}","--core=0","--"]+[str(x) for x in command]
            record={"status":"running","command":bounded,"remainingSecondsAtStart":remaining};receipt["stages"][name]=record;save();started=time.monotonic()
            child=subprocess.Popen(bounded,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
            events=[]
            with (results/(name+".log")).open("w") as log:
                for line in child.stdout:
                    log.write(line);log.flush();print(line,end="",flush=True)
                    try:event=json.loads(line);events.append(event);record["lastProgress"]=event;save()
                    except ValueError:pass
            code=child.wait();last=events[-1] if events else {};complete=code==0 and last.get("status")==marker and all(last.get(k)==v for k,v in required.items())
            record.update(status="completed" if complete else "failed-or-incomplete",exitCode=code,elapsedSeconds=time.monotonic()-started,nativeStatistics=last)
            receipt["mathematicalElapsedSeconds"]=time.monotonic()-math_start;save()
            if not complete:raise RuntimeError("actual mathematical stage incomplete: "+name)
        def record_file(name,path):
            receipt["outputs"][name]={"file":str(path),"bytes":path.stat().st_size,"sha256":sha(path)};save()
        s1=recovery/"original";s1.mkdir(exist_ok=True);pre1=s1/"kernel"
        run_stage("original",[binaries["original"],found["graph"],found["model"],found["normalTrace"],found["forward"],found["backward"],integer,pre1],"all200-original-kernel-bockstein-complete",{"highKernelColumns":200,"allOriginalKernelIdentitiesMod31":True,"fullOriginalBocksteinDivisionIdentity":True,"allIndividualWeightedBoundsVerified":True})
        original_meta=Path(str(pre1)+"-original-bockstein.json");raw_rhs=Path(str(pre1)+"-bockstein-original-rhs.bin")
        for name,path in (("originalKernels",Path(str(pre1)+"-original-kernels.bin")),("originalBocksteinRHS",raw_rhs),("originalMetadata",original_meta)):record_file(name,path)
        shutil.copyfile(original_meta,results/"original-bockstein-metadata.json")
        s2=recovery/"normal";s2.mkdir(exist_ok=True);pre2=s2/"beta"
        run_stage("normal",[binaries["normal"],found["model"],raw_rhs,pre2],"all200-original-bockstein-normal-forms-complete",{"sources":0,"targets":200,"components":1034})
        for name,expected in (("forward",INPUTS["forward"][1]),("backward",INPUTS["backward"][1])):
            path=Path(str(pre2)+"-"+name+".bin")
            if sha(path)!=expected:raise ValueError("original constant-prebasis provenance changed in all200 normal forms")
            record_file("new"+name.title(),path)
        nf=Path(str(pre2)+"-normal-forms.bin")
        record_file("bocksteinNormalForms",nf);record_file("bocksteinNormalTrace",Path(str(pre2)+"-reduction.bin"))
        s3=recovery/"image";s3.mkdir(exist_ok=True);pre3=s3/"image"
        run_stage("image",[binaries["image"],found["graph"],nf,pre3],"all200-bockstein-image-certificate-complete",{"fullImageQuotientIdentity":True,"everyRemainderIsIrreducible":True,"finite_budget_verified":False})
        imeta=Path(str(pre3)+"-image-certificate.json");iquot=Path(str(pre3)+"-image-quotients.bin");irem=Path(str(pre3)+"-image-remainders.bin")
        for name,path in (("imageMetadata",imeta),("imageQuotients",iquot),("imageRemainders",irem)):record_file(name,path)
        shutil.copyfile(imeta,results/"image-bockstein-metadata.json")
        run_stage("infinite-test",["python3",root/"2026-11-14-r150-high-kernel-bockstein-torsion-789f.py","--state",state,"--state-receipt",state_receipt,"--original-metadata",original_meta,"--image-metadata",imeta,"--image-quotients",iquot,"--image-remainders",irem,"--first-remainders",first,"--out",results],"all200-original-bockstein-infinite-test-complete",{"all200BocksteinsInTorsion":True,"allowedB85ShiftColumns":1152,"finite_budget_verified":False})
        receipt.update(status="completed",mathematicalElapsedSeconds=time.monotonic()-math_start,finite_budget_verified=False)
        final=json.loads((results/"high-kernel-infinite-quotient-result.json").read_text())
        receipt["infiniteQuotientNecessaryTest"]={k:final[k] for k in ("infiniteImageRank","augmentedRank","targetCompatibility","allNineTargetsPassInfiniteNecessaryTest")}
        save()
    except Exception as exc:
        receipt.update(status="failed-or-incomplete",errorType=type(exc).__name__,error=str(exc),finite_budget_verified=False)
        save()
    finally:
        # Preserve all large originals in the recovery artifact even on timeout.
        extra_state=results/"state-input.bin"
        if extra_state.exists():shutil.move(str(extra_state),str(recovery/"state-input.bin"))
        manifest=[]
        for f in sorted(recovery.rglob("*")):
            if f.is_file():manifest.append({"file":str(f.relative_to(a.out)),"bytes":f.stat().st_size,"sha256":sha(f)})
        (results/"recovery-manifest.json").write_text(json.dumps({"format":"r150-all200-original-bockstein-recovery-v1","pipelineStatus":receipt["status"],"completeMathematicalRun":receipt["status"]=="completed","files":manifest},indent=2)+"\n")
        receipt["recoveryFiles"]=len(manifest);receipt["recoveryBytes"]=sum(x["bytes"] for x in manifest);save()
    print(json.dumps({"status":receipt["status"],"mathematicalElapsedSeconds":receipt.get("mathematicalElapsedSeconds"),"infiniteQuotientNecessaryTest":receipt.get("infiniteQuotientNecessaryTest"),"finite_budget_verified":False,"recoveryFiles":receipt["recoveryFiles"],"recoveryBytes":receipt["recoveryBytes"]}))
    if receipt["status"]!="completed":raise SystemExit(1)

if __name__=="__main__":main()
