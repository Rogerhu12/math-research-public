#!/usr/bin/env python3
"""Seven genuine augmented second directions; every positive target continues to original17."""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,shutil,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
CONTRACT="2026-11-14-r150-augmented-seven-second-contract-789f.json"
OLD_HELPER="2026-11-14-r150-four-second-bockstein-runner-789f.py"
PYPROGRAMS={"model":"2026-11-14-r150-augmented-seven-second-integer-model-789f.py",
 "matrix":"2026-11-14-r150-augmented-seven-second-matrices-789f.py"}
PROGRAMS={
 "image":("2026-11-14-r150-augmented-seven-second-image-789f.cpp",[]),
 "source7":("2026-11-14-r150-seven-saturation-source-789f.cpp",[]),
 "target7":("2026-11-14-r150-augmented-seven-second-target-source-789f.cpp",[]),
 "transport":("2026-11-14-r150-augmented-seven-second-transport-789f.cpp",[]),
 "normal":("2026-11-14-r150-augmented-seven-second-normal-789f.cpp",[]),
 "original":("2026-11-14-r150-augmented-seven-second-original-789f.cpp",[])}
LABEL7=list(range(7001,7008));LABEL9=list(range(2,11));LABEL16=LABEL7+LABEL9
TARGETS=[2,3,4,5,7,8,10];PAIR=[6,9]
BETA_LABELS=list(range(2275,2279));FOUR_LABELS=list(range(4001,4005))
P=31;P2=961;P3=29791;P4=923521;P5=28629151;BOUND=88
def sha(path):
 h=hashlib.sha256()
 with Path(path).open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return h.hexdigest()
def digest(value):return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def suffix(path,ending):return Path(str(path)+ending)
def negate(polys):return [[[-x for x in p] for p in row] for row in polys]
def scale(polys,c):return [[[c*x for x in p] for p in row] for row in polys]
def zero(rows,cols):return [[[] for _ in range(cols)] for _ in range(rows)]
def identity(n,c=1):return [[[c] if i==j else [] for j in range(n)] for i in range(n)]
def embed(polys,columns,offset):
 return [[[] for _ in range(offset)]+[list(p) for p in row]+[[] for _ in range(columns-offset-len(row))] for row in polys]
def constants(rows):return [[[x] if x else [] for x in row] for row in rows]
def load_module(path,name):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def write_original5(path,labels,bound,divisor,target_mode,active,families):
 if len(active)!=len(labels) or any(x not in (0,1,False,True) for x in active):raise ValueError("actual original target mask")
 lines=["R150_ORIGINAL_SECOND_COMBINATION_V1",f"{len(labels)} {bound} {divisor} {target_mode} {len(families)}",
        " ".join(map(str,labels))," ".join(str(int(x)) for x in active)]
 for f in families:
  if len(f["polys"])!=len(f["labels"]):raise ValueError("actual original source family rows")
  lines.append(str(f["file"])+" "+str(len(f["labels"])));lines.append(" ".join(map(str,f["labels"])))
  for row in f["polys"]:
   if len(row)!=len(labels):raise ValueError("complete original polynomial multiplier columns")
   for poly in row:
    poly=[x%P5 for x in poly]
    while poly and not poly[-1]:poly.pop()
    if len(poly)>701:raise ValueError("paid original polynomial degree")
    lines.append(" ".join(map(str,[len(poly)]+poly)))
 path.write_text("\n".join(lines)+"\n")

def main():
 parser=argparse.ArgumentParser()
 for name in ("notes-root","t96-recovery","all198-recovery","seven-recovery","pair-recovery","out"):parser.add_argument("--"+name,type=Path,required=True)
 parser.add_argument("--math-seconds",type=int,default=300);parser.add_argument("--memory-mib",type=int,default=512)
 parser.add_argument("--compile-seconds",type=int,default=30);parser.add_argument("--resume-recovery",type=Path);parser.add_argument("--prepare-only",action="store_true")
 a=parser.parse_args()
 if min(a.math_seconds,a.memory_mib,a.compile_seconds)<1:raise ValueError("explicit positive bounds")
 root=Path(__file__).resolve().parent;notes=a.notes_root.resolve();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 recovery=out/"recovery"
 if a.resume_recovery and a.resume_recovery.resolve()!=recovery:shutil.copytree(a.resume_recovery,recovery,dirs_exist_ok=True)
 results=out/"results";bins=out/"bin";inputs=recovery/"inputs";cache=recovery/"stage-cache"
 for d in (results,recovery,bins,inputs,cache):d.mkdir(parents=True,exist_ok=True)
 receipt_path=results/"augmented-seven-second-pipeline-receipt.json"
 receipt={"format":"r150-genuine-seven-augmented-second-complete-continuation-v1","status":"preparing",
  "prime":31,"integerModulus":P5,"targetMultiplier":"31^2*h0","sourceSevenRun":43630666145,"sourcePairRun":43632271378,
  "newDirectionLabels":LABEL7,"newTargetSlots":TARGETS,"reusedPositiveTargets":PAIR,
  "original1834KernelAndOldSevenFirstImagesRecomputed":False,"allSevenNewDirectionsComputed":False,
  "relevantPrimaryImageComplete":False,"completeOtherPrimarySecondImageAsserted":False,
  "fullOriginalAllNineMod28629151IdentityVerified":False,"allCompletedCompatibleTargetsOriginalIdentityVerified":False,
  "finite_budget_verified":False,"characteristicZeroIdentityAsserted":False,
  "sharedMathematicalSecondsLimit":a.math_seconds,"perChildAddressSpaceMiBLimit":a.memory_mib,"perCompilationSecondsLimit":a.compile_seconds,
  "deadlineRule":"Six bounded native compilations and saved input SHA checks precede one shared300second mathematical clock. Exact model reduction, matrix preparation, pair multiplication, new7 image/VQ/transport/K4/normal/global and every positive original17 continuation share it. VQ and original-product partial arrays checkpoint; completed stages have source-bound caches. Compression follows.",
  "inputs":{},"sources":{},"compilations":{},"stages":{}}
 math_start=None
 def save():receipt_path.write_text(json.dumps(receipt,separators=(",",":"))+"\n")
 try:
  contract=json.loads((root/CONTRACT).read_text());receipt["inputContractSHA256"]=sha(root/CONTRACT)
  scopes={"notes":notes,"t96":a.t96_recovery.resolve(),"all198":a.all198_recovery.resolve(),
          "seven":a.seven_recovery.resolve(),"pair":a.pair_recovery.resolve()};found={}
  for name,item in contract["inputs"].items():
   scope=scopes[item["scope"]]
   candidates=[scope/item["relative"]] if "relative" in item else sorted({p for n in item["names"] for p in scope.rglob(n)})
   actual=next((p.resolve() for p in candidates if p.is_file() and sha(p)==item["sha256"]),None)
   if actual is None:raise ValueError("exact saved input missing "+name)
   found[name]=actual;receipt["inputs"][name]={"file":str(actual),"bytes":actual.stat().st_size,"sha256":item["sha256"]}
  for name,expected in contract["dependencies"].items():
   path=root/name if (root/name).is_file() else notes/name
   if sha(path)!=expected:raise ValueError("frozen dependency "+name)
   receipt["sources"][name]=expected
  receipt["sources"][Path(__file__).name]=sha(Path(__file__));receipt["sources"][CONTRACT]=sha(root/CONTRACT)
  helper=load_module(root/OLD_HELPER if (root/OLD_HELPER).is_file() else notes/OLD_HELPER,"r150_second_actual_recipe")
  previous=json.loads(found["globalReceipt"].read_text())
  if previous.get("status")!="completed" or previous.get("newAugmentedFirstImageComplete") is not True or previous.get("individualTargetCompatible")!=[False,False,False,False,True,False,False,True,False]:raise ValueError("actual complete old individual flags")
  pair_meta=json.loads(found["pairOriginalReceipt"].read_text())
  if pair_meta.get("status")!="completed" or pair_meta.get("targetCount")!=2 or pair_meta.get("modulus")!=P4 or pair_meta.get("actualSourceCosts")!=[87,87] or not pair_meta.get("fullOriginalSeventeenEquationIdentityMod923521"):raise ValueError("actual completed original targets6/9")
  def nf_family(prefix,labels,polys):
   return {"nf":found[prefix+"NF"],"q":found[prefix+"Q"],"rem":found[prefix+"Rem"],"trace":found[prefix+"Trace"],"labels":labels,"polys":polys}
  executables={}
  for name,(filename,flags) in PROGRAMS.items():
   source=root/filename if (root/filename).is_file() else notes/filename;executable=bins/name
   command=["timeout","--kill-after=10s",str(a.compile_seconds)+"s","prlimit","--as="+str(a.memory_mib*1048576),"--core=0","--","g++","-O3","-std=c++17","-I",str(root),"-I",str(notes)]+flags+[str(source),"-o",str(executable)]
   started=time.monotonic();proc=subprocess.run(command,capture_output=True,text=True)
   (results/("compile-"+name+".log")).write_text(proc.stdout+proc.stderr)
   receipt["compilations"][name]={"command":command,"exitCode":proc.returncode,"elapsedSeconds":time.monotonic()-started};save()
   if proc.returncode:raise RuntimeError("bounded compilation failed "+name)
   executables[name]=[str(executable)]
  for name,filename in PYPROGRAMS.items():executables[name]=[sys.executable,str(root/filename)]
  if a.prepare_only:receipt["status"]="prepared-no-mathematical-stage-executed";save();return
  math_start=time.monotonic();deadline=math_start+a.math_seconds;receipt["status"]="running";save()
  def prefix(name):
   d=recovery/name;d.mkdir(exist_ok=True);return d/name
  def binding(infiles,logical,program):
   source=PYPROGRAMS[program] if program in PYPROGRAMS else PROGRAMS[program][0]
   return digest({"inputs":[sha(p) for p in infiles],"logical":logical,"program":receipt["sources"][source],
                  "headers":{k:v for k,v in receipt["sources"].items() if k.endswith(".hpp")}})
  def run_stage(name,program,args,marker,required,infiles,outfiles,logical):
   key=binding(infiles,logical,program);cachefile=cache/(name+".json")
   if cachefile.exists():
    saved=json.loads(cachefile.read_text())
    if saved.get("inputBindingSHA256")==key and all(p.exists() and sha(p)==saved.get("outputs",{}).get(str(p.relative_to(recovery))) for p in outfiles):
     receipt["stages"][name]={"status":"completed","reusedCompletedActualStage":True,"inputBindingSHA256":key,"nativeStatistics":saved["nativeStatistics"],"elapsedSeconds":0};save();return
   remaining=deadline-time.monotonic()
   if remaining<=0:raise TimeoutError("shared mathematical deadline before "+name)
   command=["timeout","--kill-after=10s",f"{remaining:.3f}s","prlimit","--as="+str(a.memory_mib*1048576),"--core=0","--"]+executables[program]+list(map(str,args))
   stage={"status":"running","inputBindingSHA256":key,"command":command,"remainingSecondsAtStart":remaining}
   receipt["stages"][name]=stage;save();started=time.monotonic();events=[]
   process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
   with (results/(name+".log")).open("w") as log:
    for line in process.stdout:
     log.write(line);log.flush();print(line,end="",flush=True)
     try:
      event=json.loads(line);events.append(event);stage["lastProgress"]=event;save()
     except (ValueError,TypeError):pass
   code=process.wait();last=events[-1] if events else {}
   complete=code==0 and last.get("status")==marker and all(last.get(k)==v for k,v in required.items()) and all(p.exists() for p in outfiles)
   stage.update(status="completed" if complete else "failed-or-incomplete",exitCode=code,elapsedSeconds=time.monotonic()-started,nativeStatistics=last)
   receipt["mathematicalElapsedSeconds"]=time.monotonic()-math_start;save()
   if not complete:raise RuntimeError("actual stage failed or incomplete "+name)
   cachefile.write_text(json.dumps({"inputBindingSHA256":key,"outputs":{str(p.relative_to(recovery)):sha(p) for p in outfiles},"nativeStatistics":last},indent=2)+"\n")
  def image_stage(name,mix,families,bound,labels,require_zero):
   output=prefix(name);infiles=[found["graph"]]
   for f in families:
    infiles.append(f["nf"])
    if str(f["q"])!="-":infiles.extend([f["q"],f["rem"]])
   required={"fullImageQuotientIdentity":True}
   if require_zero:required["completeRHSInImage"]=True
   run_stage(name,"image",[found["graph"],mix,output],"saved-quotient-mixture-complete",required,infiles,
    [suffix(output,x) for x in ("-normal-forms.bin","-image-quotients.bin","-image-remainders.bin","-image-certificate.json")],
    {"bound":bound,"labels":labels,"polynomials":[f["polys"] for f in families]})
   return output
  def source_stage(name,image,program,bound,count):
   output=prefix(name);data=[found["graph"],found["originalNF"],suffix(image,"-normal-forms.bin"),suffix(image,"-image-quotients.bin"),suffix(image,"-image-remainders.bin")]
   key=binding(data,{"bound":bound,"targets":count},program)
   run_stage(name,program,data+[output,key],"packed-image-source-convolution-complete",
    {"fullNormalFormDecompositionIdentity":True,"standardKernelNormalForm":True,"completeRHSInImage":True},data,
    [suffix(output,x) for x in ("-standard-coefficients.bin","-source-certificate.json","-vq-checkpoint.bin")],
    {"bound":bound,"checkpointBinding":key})
   return output
  def transport_stage(name,source,mix,families,bound):
   output=prefix(name);data=[suffix(source,"-standard-coefficients.bin"),found["model"],found["normalTrace"],found["forward"],found["backward"]]
   run_stage(name,"transport",data+[mix,output],"original-source-transport-complete",{},data+[f["trace"] for f in families],
    [suffix(output,"-primitive-source-mod31.bin"),suffix(output,"-original-transport.json")],
    {"bound":bound,"polynomials":[f["polys"] for f in families]})
   return output
  def original_stage(name,labels,bound,divisor,target_mode,active,families):
   recipe=inputs/(name+".recipe");write_original5(recipe,labels,bound,divisor,target_mode,active,families)
   output=prefix(name);data=[found["model"],integer_model]+[f["file"] for f in families]
   logical={"bound":bound,"divisor":divisor,"targetMode":target_mode,"labels":labels,"active":[int(x) for x in active],
            "polynomials":[f["polys"] for f in families]}
   key=binding(data,logical,"original");required={"divisor":divisor,"allOriginalProductCoefficientsDivisible":True}
   if divisor==P5:required["fullOriginalSeventeenEquationIdentityMod28629151"]=True
   files=[suffix(output,x) for x in ("-primitive-source-mod28629151.bin","-original-seventeen-source-mod28629151.bin","-original-product.json")]
   if divisor==P4:files.append(suffix(output,"-fourth-divided-original-rhs.bin"))
   run_stage(name,"original",[found["model"],integer_model,recipe,output,key],
    "full-original-augmented-second-product-complete",required,data,files,{**logical,"checkpointBinding":key})
   metadata=json.loads(suffix(output,"-original-product.json").read_text())
   if metadata.get("targetLabels")!=labels or metadata.get("activeTargetLabels")!=[j for j,f in zip(labels,active) if f] or not metadata.get("inactiveSourceColumnsExactlyZero"):raise ValueError("exact actual original target-mask scope")
   return output
  integer_model=inputs/"original-integer-31squaredh0-mod28629151.txt"
  run_stage("same-exact-integer-model","model",["--exact-gzip",found["exactInteger"],"--lower-model",found["integerModel"],"--out",integer_model],
   "completed",{"lowerMod31FourEquationModelAndDividedTargetVerified":True,"modulus":P5,"target":"31^2*h0"},
   [found["exactInteger"],found["integerModel"]],[integer_model,suffix(integer_model,".json")],
   {"sameOriginal17":True,"modulus":P5,"targetMultiplier":P2})
  prep_dir=recovery/"prepared-seven";prep_dir.mkdir(exist_ok=True)
  prepared_receipt=prep_dir/"prepared-seven-second-receipt.json";prepared_system=prep_dir/"prepared-seven-second.bin.gz"
  run_stage("prepared-seven","matrix",["--mode","prepare","--notes-root",notes,"--seven-receipt",found["globalReceipt"],
   "--seven-system",found["globalSystem"],"--pair-receipt",found["pairAnalysisReceipt"],"--pair-system",found["pairAnalysisSystem"],"--out",prep_dir],
   "completed",{"allSevenCancelledFirstClassesInU":True,"allNineRawSupportedAt1And2":True},
   [found["globalReceipt"],found["globalSystem"],found["pairAnalysisReceipt"],found["pairAnalysisSystem"],found["state"]],
   [prepared_receipt,prepared_system],{"actualSevenKernel":True,"sourcePairRun":43632271378})
  preparation=json.loads(prepared_receipt.read_text());L=preparation["sevenGenuineKernelPolynomialsAscending"]
  C=constants(preparation["oldSevenConstantCorrection"])
  if len(L)!=7 or any(len(r)!=7 for r in L) or len(C)!=7 or any(len(r)!=7 for r in C):raise ValueError("complete seven genuine direction coefficients")
  cbeta=C[:2]+zero(2,7);cfour=C[2:6];cselected=[C[6]]+zero(8,7)
  pair5=original_stage("reused-pair-original",PAIR,87,P5,1,[1,1],
   [{"file":found["pairOriginal"],"labels":PAIR,"polys":identity(2,P)}])
  pair5meta=json.loads(suffix(pair5,"-original-product.json").read_text())
  if not all(pair5meta.get(k) is True for k in ("fullOriginalSeventeenEquationIdentityMod28629151","fullOriginalMacaulayIdentityMod28629151","originalRowScaleTransportVerified","allWeightedBoundsVerified")):raise ValueError("pair31 multiplication full original17 identity")
  receipt.update(reusedPairOriginalMod28629151IdentityVerified=True,reusedPairActualSourceCosts=pair5meta["actualSourceCosts"],
   alreadyCompletedOriginalTargetLabels=PAIR,pairOriginalConclusion=pair5meta);save()
  first_families=[
   {"nf":found["newNF"],"q":found["newQ"],"rem":found["newRem"],"trace":found["newTrace"],"labels":LABEL16,"polys":L+zero(9,7)},
   nf_family("beta",BETA_LABELS,negate(cbeta)),nf_family("four",FOUR_LABELS,negate(cfour)),
   nf_family("selected",LABEL9,negate(cselected))]
  first_mix=inputs/"genuine-seven-q.mix";helper.write_mix(first_mix,LABEL7,BOUND,first_families)
  first_image=image_stage("genuine-seven-q-image",first_mix,first_families,BOUND,LABEL7,True)
  first_source=source_stage("genuine-seven-q-source",first_image,"source7",BOUND,7)
  first_transport=transport_stage("genuine-seven-q-original",first_source,first_mix,first_families,BOUND)
  qm=json.loads(suffix(first_transport,"-original-transport.json").read_text());k4_bound=max([BOUND]+qm["sourceCosts"])
  if k4_bound>184:raise ValueError("true original q exceeds paid88plus96 graph bound")
  k4_families=[
   {"file":found["newOriginal"],"labels":LABEL16,"polys":L+zero(9,7)},
   {"file":suffix(first_transport,"-primitive-source-mod31.bin"),"labels":LABEL7,"polys":identity(7,-P3)},
   {"file":found["kernels"],"labels":BETA_LABELS,"polys":scale(cbeta,-P2)},
   {"file":found["fourK2"],"labels":FOUR_LABELS,"polys":scale(cfour,-P)},
   {"file":found["selectedK2"],"labels":LABEL9,"polys":scale(cselected,-P)}]
  k4=original_stage("genuine-seven-k4-original",LABEL7,k4_bound,P4,0,[1]*7,k4_families)
  k4_meta=json.loads(suffix(k4,"-original-product.json").read_text())
  if not all(k4_meta.get(k) is True for k in ("allOriginalProductCoefficientsDivisible","originalRowScaleTransportVerified","allWeightedBoundsVerified")):raise ValueError("all7 actual original K4 identities")
  receipt.update(allSevenNewDirectionsComputed=True,actualOriginalQSourceCosts=qm["sourceCosts"],actualK4SourceCosts=k4_meta["actualSourceCosts"],
   actualK4OriginalProduct=k4_meta,actualNewDirectionPaidCost=k4_bound);save()
  normal7=prefix("genuine-seven-normal")
  run_stage("genuine-seven-normal","normal",[found["model"],suffix(k4,"-fourth-divided-original-rhs.bin"),normal7],
   "seven-augmented-second-normal-forms-complete",{"targets":7,"components":1034},
   [found["model"],suffix(k4,"-fourth-divided-original-rhs.bin")],
   [suffix(normal7,x) for x in ("-normal-forms.bin","-reduction.bin","-forward.bin","-backward.bin")],
   {"bound":k4_bound,"labels":LABEL7})
  if sha(suffix(normal7,"-forward.bin"))!=contract["inputs"]["forward"]["sha256"] or sha(suffix(normal7,"-backward.bin"))!=contract["inputs"]["backward"]["sha256"]:raise ValueError("same actual original3333 DAG hashes")
  receipt["sameOriginalPrebasisDAGHashesVerified"]=True;save()
  d_bound=max([40]+k4_meta["actualSourceCosts"])
  if d_bound>k4_bound:raise ValueError("actual source cost must satisfy recorded paid bound")
  fresh=[{"nf":suffix(normal7,"-normal-forms.bin"),"q":"-","rem":"-","trace":suffix(normal7,"-reduction.bin"),"labels":LABEL7,"polys":identity(7)}]
  fresh_mix=inputs/"genuine-seven-second-image.mix";helper.write_mix(fresh_mix,LABEL7,d_bound,fresh)
  second_image=image_stage("genuine-seven-second-image",fresh_mix,fresh,d_bound,LABEL7,False)
  global_dir=recovery/"complete-related-second";global_dir.mkdir(exist_ok=True)
  global_receipt=global_dir/"complete-augmented-second-image-receipt.json";global_system=global_dir/"complete-augmented-second-image.bin.gz"
  run_stage("complete-related-second","matrix",["--mode","complete","--notes-root",notes,"--prepared-receipt",prepared_receipt,"--prepared-system",prepared_system,
   "--image-remainders",suffix(second_image,"-image-remainders.bin"),"--image-metadata",suffix(second_image,"-image-certificate.json"),
   "--original-metadata",suffix(k4,"-original-product.json"),"--out",global_dir],
   "completed",{"relevantPrimaryImageComplete":True,"allCompatibleWhole315IdentitiesVerified":True},
   [prepared_receipt,prepared_system,suffix(second_image,"-image-remainders.bin"),suffix(second_image,"-image-certificate.json"),suffix(k4,"-original-product.json"),found["state"]],
   [global_receipt,global_system],{"oldKernelPaid":1834,"sevenActualSecondDirections":7,"relatedPrimaryDimension":39,"quotientByActualU8":True})
  solution=json.loads(global_receipt.read_text());flags=solution["individualTargetCompatible"]
  if len(flags)!=7 or solution["targetLabels"]!=TARGETS:raise ValueError("actual individual remaining-seven flags")
  compatible=[j for j,f in zip(TARGETS,flags) if f];obstructed=[j for j,f in zip(TARGETS,flags) if not f]
  receipt.update(relevantPrimaryImageComplete=True,old198RelevantCoverageUsed=True,old4ExactAugmentedCoverageUsed=True,
   old1632ExactSyzygyCoverageUsed=True,relatedSecondImageRank=solution["relatedSecondImageRank"],
   individualRemainingTargetCompatible=flags,compatibleRemainingTargetLabels=compatible,obstructedTargetLabels=obstructed,
   exactNegativeScope=solution["negativeScope"],completeRelatedSecondConclusion=solution);save()
  final_meta=None
  if compatible:
   F=solution["newSecondSolutionPolynomialsAscending"];C8=constants(solution["oldEightConstantCorrection"])
   if len(F)!=7 or any(len(row)!=7 for row in F) or len(C8)!=8 or any(len(row)!=7 for row in C8):raise ValueError("complete actual second solution matrices")
   if any(F[i][j] or C8[i][j] for j,f in enumerate(flags) if not f for i in range(7)) or any(C8[7][j] for j,f in enumerate(flags) if not f):raise ValueError("inactive target matrix columns must vanish")
   C=C8[:7];g=C8[7];cbeta=C[:2]+zero(2,7);cfour=C[2:6];cselected=[C[6]]+zero(8,7)
   select=[[([1] if label==target and flags[j] else []) for j,target in enumerate(TARGETS)] for label in LABEL9]
   old_first=zero(7,7);old_first[2]=[list(poly) for poly in g]
   final_bound=max(BOUND,d_bound+max(0,solution["maximumSolutionDegree"]))
   if final_bound>528:raise ValueError("actual projection source exceeds proved184plus344 bound")
   final_families=[
    {"nf":found["newNF"],"q":found["newQ"],"rem":found["newRem"],"trace":found["newTrace"],"labels":LABEL16,"polys":negate(old_first)+select},
    {"nf":suffix(normal7,"-normal-forms.bin"),"q":suffix(second_image,"-image-quotients.bin"),"rem":suffix(second_image,"-image-remainders.bin"),
     "trace":suffix(normal7,"-reduction.bin"),"labels":LABEL7,"polys":negate(F)},
    nf_family("beta",BETA_LABELS,negate(cbeta)),nf_family("four",FOUR_LABELS,negate(cfour)),nf_family("selected",LABEL9,negate(cselected))]
   final_mix=inputs/"compatible-remaining-seven.mix";helper.write_mix(final_mix,TARGETS,final_bound,final_families)
   fim=image_stage("compatible-remaining-image",final_mix,final_families,final_bound,TARGETS,True)
   fs=source_stage("compatible-remaining-source",fim,"target7",final_bound,7)
   ft=transport_stage("compatible-remaining-original-source",fs,final_mix,final_families,final_bound)
   tm=json.loads(suffix(ft,"-original-transport.json").read_text());paid=max([final_bound]+tm["sourceCosts"])
   if paid>final_bound+96 or any(tm["sourceCosts"][j]!=-1 for j,f in enumerate(flags) if not f):raise ValueError("actual selected original source budget/mask")
   active_identity=identity(7,P4)
   for j,f in enumerate(flags):
    if not f:active_identity[j][j]=[]
   final_original_families=[
    {"file":found["newOriginal"],"labels":LABEL16,"polys":scale(old_first,P)+scale(select,P)},
    {"file":suffix(k4,"-primitive-source-mod28629151.bin"),"labels":LABEL7,"polys":F},
    {"file":found["kernels"],"labels":BETA_LABELS,"polys":scale(cbeta,P3)},
    {"file":found["fourK2"],"labels":FOUR_LABELS,"polys":scale(cfour,P2)},
    {"file":found["selectedK2"],"labels":LABEL9,"polys":scale(cselected,P2)},
    {"file":suffix(ft,"-primitive-source-mod31.bin"),"labels":TARGETS,"polys":active_identity}]
   final_original=original_stage("compatible-remaining-original",TARGETS,paid,P5,1,flags,final_original_families)
   final_meta=json.loads(suffix(final_original,"-original-product.json").read_text())
   if not all(final_meta.get(k) is True for k in ("fullOriginalSeventeenEquationIdentityMod28629151","fullOriginalMacaulayIdentityMod28629151",
      "originalRowScaleTransportVerified","allWeightedBoundsVerified","inactiveSourceColumnsExactlyZero")) or final_meta["activeTargetLabels"]!=compatible:raise ValueError("every compatible target full original17 product")
   receipt["remainingOriginalConclusion"]=final_meta
   receipt["actualRemainingSourceCostsBySlot"]=final_meta["actualSourceCosts"];save()
  completed=sorted(PAIR+compatible)
  if all(flags):outcome="all-nine-full-original31squaredh0-mod28629151-certificates"
  elif compatible:outcome="complete-related-second-obstruction-with-all-positive-original-certificates"
  else:outcome="complete-related-second-obstruction-with-reused-pair-certificates"
  receipt.update(status="completed",outcome=outcome,completedOriginalTargetLabels=completed,
   allCompletedCompatibleTargetsOriginalIdentityVerified=True,fullOriginalAllNineMod28629151IdentityVerified=all(flags),
   allSevenNewDirectionOriginalDivisibilitiesVerified=True,finitePositiveSourceBudgetsVerified=True,finite_budget_verified=all(flags),
   totalPositiveOriginalTargets=len(completed),numberOfCompletelyObstructedAugmentedTargets=len(obstructed),
   mathematicalElapsedSeconds=time.monotonic()-math_start);save()
 except Exception as error:
  receipt.update(status="failed-or-incomplete",errorType=type(error).__name__,error=str(error))
  if math_start is not None:receipt["mathematicalElapsedSeconds"]=time.monotonic()-math_start
  save()
 finally:
  certificates=results/"certificates";certificates.mkdir(exist_ok=True)
  files=[];texts=[]
  for path in sorted(recovery.rglob("*")):
   if not path.is_file():continue
   relative=path.relative_to(recovery);flat=str(relative).replace("/","__")
   if path.suffix in (".json",".mix",".recipe",".txt"):
    destination=results/flat;shutil.copyfile(path,destination)
    texts.append({"originalFile":str(relative),"file":destination.name,"bytes":path.stat().st_size,"sha256":sha(path)})
    continue
   temporary=recovery/(flat+".gz.tmp")
   with path.open("rb") as src,temporary.open("wb") as dst:
    with gzip.GzipFile(filename="",mode="wb",fileobj=dst,mtime=0) as gz:shutil.copyfileobj(src,gz)
   item={"originalFile":str(relative),"uncompressedBytes":path.stat().st_size,"uncompressedSHA256":sha(path),
         "compressedBytes":temporary.stat().st_size,"compressedSHA256":sha(temporary),"parts":[]}
   with temporary.open("rb") as src:
    part=1
    while data:=src.read(4_500_000):
     target=certificates/(flat+".gz" if item["compressedBytes"]<=4_500_000 else flat+f".gz.part{part:03d}")
     target.write_bytes(data);item["parts"].append({"file":str(target.relative_to(results)),"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()});part+=1
   temporary.unlink();files.append(item)
  (results/"certificate-manifest.json").write_text(json.dumps({"format":"r150-augmented-seven-second-lossless-certificates-v1","pipelineStatus":receipt["status"],"partialCheckpointIsNotIdentity":True,"files":files},indent=2)+"\n")
  (results/"text-recovery-manifest.json").write_text(json.dumps({"format":"r150-augmented-seven-second-exact-text-recovery-v1","completeStageCachesIncluded":True,"files":texts},indent=2)+"\n")
  saved=[{"file":str(p.relative_to(recovery)),"bytes":p.stat().st_size,"sha256":sha(p)} for p in sorted(recovery.rglob("*")) if p.is_file()]
  (results/"recovery-manifest.json").write_text(json.dumps({"format":"r150-augmented-seven-second-complete-recovery-v1","pipelineStatus":receipt["status"],"files":saved},indent=2)+"\n")
  receipt.update(recoveryFiles=len(saved),recoveryBytes=sum(p["bytes"] for p in saved),losslessGeneratedBinaryFiles=len(files));save()
  print(json.dumps({k:receipt.get(k) for k in ("status","outcome","mathematicalElapsedSeconds","completedOriginalTargetLabels","relevantPrimaryImageComplete","fullOriginalAllNineMod28629151IdentityVerified","obstructedTargetLabels","recoveryBytes")}),flush=True)
 if receipt["status"] not in ("completed","prepared-no-mathematical-stage-executed"):raise SystemExit(1)
if __name__=="__main__":main()
