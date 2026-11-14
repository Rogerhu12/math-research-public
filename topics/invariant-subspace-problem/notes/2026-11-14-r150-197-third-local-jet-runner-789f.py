#!/usr/bin/env python3
"""Complete197 true local third directions; every positive continues through whole315 and original17."""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,shutil,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
CONTRACT="2026-11-14-r150-197-third-local-jet-contract-789f.json"
OLD_HELPER="2026-11-14-r150-four-second-bockstein-runner-789f.py"
PYPROGRAMS={"matrix":"2026-11-14-r150-197-third-local-matrices-789f.py"}
PROGRAMS={
 "local-vq":("2026-11-14-r150-197-third-local-vq-789f.cpp",[]),
 "local-transport":("2026-11-14-r150-197-third-local-transport-789f.cpp",[]),
 "local-product":("2026-11-14-r150-197-third-local-product-789f.cpp",[]),
 "local-normal-ten":("2026-11-14-r150-197-third-local-normal-789f.cpp",["-DJ3_LENGTH=10"]),
 "local-state-eight":("2026-11-14-r150-197-third-local-normal-789f.cpp",["-DJ3_LENGTH=8"]),
 "image":("2026-11-14-r150-ninth-first-image-789f.cpp",[]),
 "target9":("2026-11-14-r150-ninth-first-target-source-789f.cpp",[]),
 "transport":("2026-11-14-r150-original-wide-transport-checkpoint-789f.cpp",[]),
 "normal":("2026-11-14-r150-197-third-global-normal-789f.cpp",[]),
 "original":("2026-11-14-r150-197-third-global-original-789f.cpp",[])}
LABEL7=list(range(7001,7008));LABEL9=list(range(2,11));LABEL16=LABEL7+LABEL9
TARGETS=LABEL9;SAVED7=[2,3,4,5,7,8,10];PAIR=[6,9];LABEL5=[9301,9302,9305,9306,9307];LABEL10=[9001]+LABEL9
BETA_LABELS=list(range(2275,2279));FOUR_LABELS=list(range(4001,4005))
P=31;P2=961;P3=29791;P4=923521;P5=28629151;P6=887503681;BOUND=88
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
def write_original6(path,labels,bound,divisor,target_mode,active,families):
 if len(active)!=len(labels) or any(x not in (0,1,False,True) for x in active):raise ValueError("actual original target mask")
 lines=["R150_ORIGINAL_197_THIRD_COMBINATION_V1",f"{len(labels)} {bound} {divisor} {target_mode} {len(families)}",
        " ".join(map(str,labels))," ".join(str(int(x)) for x in active)]
 for f in families:
  if len(f["polys"])!=len(f["labels"]):raise ValueError("actual original source family rows")
  lines.append(str(f["file"])+" "+str(len(f["labels"])));lines.append(" ".join(map(str,f["labels"])))
  for row in f["polys"]:
   if len(row)!=len(labels):raise ValueError("complete original polynomial multiplier columns")
   for poly in row:
    poly=[x%P6 for x in poly]
    while poly and not poly[-1]:poly.pop()
    if len(poly)>701:raise ValueError("paid original polynomial degree")
    lines.append(" ".join(map(str,[len(poly)]+poly)))
 path.write_text("\n".join(lines)+"\n")

def main():
 parser=argparse.ArgumentParser()
 for name in ("notes-root","t96-recovery","all198-recovery","seven-recovery","current-recovery","ninth-recovery","old200-recovery","five-recovery","out"):parser.add_argument("--"+name,type=Path,required=True)
 parser.add_argument("--math-seconds",type=int,default=300);parser.add_argument("--memory-mib",type=int,default=512)
 parser.add_argument("--compile-seconds",type=int,default=30);parser.add_argument("--resume-recovery",type=Path);parser.add_argument("--prepare-only",action="store_true")
 a=parser.parse_args()
 if min(a.math_seconds,a.memory_mib,a.compile_seconds)<1:raise ValueError("explicit positive bounds")
 root=Path(__file__).resolve().parent;notes=a.notes_root.resolve();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 recovery=out/"recovery"
 if a.resume_recovery and a.resume_recovery.resolve()!=recovery:shutil.copytree(a.resume_recovery,recovery,dirs_exist_ok=True)
 results=out/"results";bins=out/"bin";inputs=recovery/"inputs";cache=recovery/"stage-cache"
 for d in (results,recovery,bins,inputs,cache):d.mkdir(parents=True,exist_ok=True)
 receipt_path=results/"197-third-local-jet-pipeline-receipt.json"
 receipt={"format":"r150-complete197-low-initial-third-local-continuous-lift-v1","status":"preparing",
  "prime":31,"integerModulus":P6,"targetMultiplier":"31^2*h0","sourceCurrentRun":43638830039,"sourceFiveRun":43646683083,
  "targetLabels":LABEL9,"oldNineRawAndSourcesRecomputed":False,"oldFiveThirdDirectionsRecomputed":False,
  "all197ThirdDirectionsComputed":False,"completeRelevantLowInitialThirdImageComputed":False,
  "completeGlobalThirdImageComputed":False,"originalWholeIntegerLatticeClaimed":False,"characteristicZeroIdentityAsserted":False,
  "oldFiveThirdDirectionsReused":True,"exactK1Covered":True,"low1632ExactDirectionsCovered":True,
  "oldFourHighExactDirectionsCovered":True,"higherDigitImagesPaid":True,
  "fullOriginalAllNineMod887503681IdentityVerified":False,"allCompatibleTargetsOriginalIdentityVerified":False,
  "finitePositiveSourceBudgetsVerified":False,"finite_budget_verified":False,
  "individualTargetCompatible":[False]*9,"compatibleTargetLabels":[],"completedOriginalTargetLabels":[],
  "insufficientTargetLabels":[],"actualFinalSourceCostsBySlot":[-1]*9,
  "sharedMathematicalSecondsLimit":a.math_seconds,"perChildAddressSpaceMiBLimit":a.memory_mib,"perCompilationSecondsLimit":a.compile_seconds,
  "deadlineRule":"Ten bounded native compilations and exact saved-input decoding precede one shared mathematical deadline. The same q1 canonical t-lift is extended from five to ten root2 coefficients and its old five coefficients are compared. Actual q2 uses full original1034 ten-jet identities and original4367 ten-jet multiplyback. Every positive proceeds to whole315 reconciliation, both paid projections and all original17 equations. True stage/array/row-prefix checkpoints are retained; only compression follows the clock.",
  "inputs":{},"sources":{},"compilations":{},"stages":{}}
 math_start=None
 def save():receipt_path.write_text(json.dumps(receipt,separators=(",",":"))+"\n")
 try:
  contract=json.loads((root/CONTRACT).read_text());receipt["inputContractSHA256"]=sha(root/CONTRACT)
  scopes={"notes":notes,"t96":a.t96_recovery.resolve(),"all198":a.all198_recovery.resolve(),
          "seven":a.seven_recovery.resolve(),"current":a.current_recovery.resolve(),"ninth":a.ninth_recovery.resolve(),"old200":a.old200_recovery.resolve(),"five":a.five_recovery.resolve()};found={}
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
  oldfirst=json.loads(found["ninthFirstReceipt"].read_text())
  oldproduct=json.loads(found["ninthOriginalReceipt"].read_text())
  oldmodel=json.loads(found["ninthIntegerModelReceipt"].read_text())
  oldk4=json.loads(found["currentK4OriginalReceipt"].read_text())
  if oldfirst.get("status")!="completed" or not oldfirst.get("fullF9FirstImageComplete") or oldfirst.get("newFirstImageRank")!=0 or oldfirst.get("individualTargetCompatible")!=[False]*9:raise ValueError("same completed entire F9 first image")
  if oldproduct.get("status")!="completed" or oldproduct.get("modulus")!=P6 or oldproduct.get("divisor")!=P5 or oldproduct.get("targetLabels")!=LABEL10 or not oldproduct.get("allOriginalProductCoefficientsDivisible") or oldproduct.get("actualSourceCosts",[])[1:]!=[87]*9:raise ValueError("same actual ten old sources and nine original residuals")
  if oldmodel.get("status")!="completed" or oldmodel.get("modulus")!=P6 or oldmodel.get("target")!="31^2*h0" or oldmodel.get("modelSHA256")!=sha(found["ninthIntegerModel"]) or not oldmodel.get("all4433OriginalEquationResiduesVerified") or not oldmodel.get("all18OriginalRowScaleResiduesVerified"):raise ValueError("same exact primitive integer model already constructed")
  if oldk4.get("status")!="completed" or oldk4.get("modulus")!=P5 or oldk4.get("divisor")!=P4 or oldk4.get("targetLabels")!=LABEL7 or not oldk4.get("allOriginalProductCoefficientsDivisible"):raise ValueError("same actual seven K4 sources")
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
   logical={"bound":bound,"polynomials":[f["polys"] for f in families]}
   key=binding(data+[f["trace"] for f in families],logical,"transport")
   remaining=max(0.001,deadline-time.monotonic()-0.25)
   run_stage(name,"transport",data+[mix,output,output.parent/"actual-checkpoints",key,remaining],
    "original-source-transport-complete",{},data+[f["trace"] for f in families],
    [suffix(output,"-primitive-source-mod31.bin"),suffix(output,"-original-transport.json")],logical)
   return output
  def original_stage(name,labels,bound,divisor,target_mode,active,families):
   recipe=inputs/(name+".recipe");write_original6(recipe,labels,bound,divisor,target_mode,active,families)
   output=prefix(name);data=[found["model"],integer_model]+[f["file"] for f in families]
   logical={"bound":bound,"divisor":divisor,"targetMode":target_mode,"labels":labels,"active":[int(x) for x in active],
            "polynomials":[f["polys"] for f in families]}
   key=binding(data,logical,"original");required={"divisor":divisor,"allOriginalProductCoefficientsDivisible":True}
   if divisor==P6:required["fullOriginalSeventeenEquationIdentityMod887503681"]=True
   files=[suffix(output,x) for x in ("-primitive-source-mod887503681.bin","-original-seventeen-source-mod887503681.bin","-original-product.json")]
   if divisor<P6:files.append(suffix(output,"-divided-original-rhs.bin"))
   run_stage(name,"original",[found["model"],integer_model,recipe,output,key],
    "full-original197-third-product-complete",required,data,files,{**logical,"checkpointBinding":key})
   metadata=json.loads(suffix(output,"-original-product.json").read_text())
   if metadata.get("targetLabels")!=labels or metadata.get("activeTargetLabels")!=[j for j,f in zip(labels,active) if f] or not metadata.get("inactiveSourceColumnsExactlyZero"):raise ValueError("exact actual original target-mask scope")
   return output
  integer_model=found["ninthIntegerModel"]
  receipt["exactIntegerMod31SixModelReusedWithoutReconstruction"]=True
  # Validate the original200 quotient's zero first-image remainder, without recomputing it.
  import struct
  with found["oldK"].open("rb") as f:head=f.read(24+200*16)
  if head[:8]!=b"R150KK31" or struct.unpack_from("<4I",head,8)!=(31,6188,200,85):raise ValueError("same original200 kernel input")
  oldlabels=[struct.unpack_from("<IHHII",head,24+16*j)[1] for j in range(200)]
  rem=found["oldRem"].read_bytes();offset=20
  if rem[:8]!=b"R150NF31" or struct.unpack_from("<3I",rem,8)!=(0,200,1034):raise ValueError("same original200 remainder file")
  for j in range(200):
   raw,label,n=struct.unpack_from("<IHI",rem,offset);offset+=10
   if raw or label!=oldlabels[j] or (j<198 and n):raise ValueError("old first198 full remainders are not zero")
   for _ in range(n):component,length=struct.unpack_from("<HB",rem,offset);offset+=3+length
  if offset!=len(rem):raise ValueError("same complete old200 remainder tail")
  receipt["first198SavedGlobalRemaindersExactlyZero"]=True
  local_binding=digest({"inputs":{k:v["sha256"] for k,v in receipt["inputs"].items()},
   "sources":receipt["sources"],"directionIndices":"K2..K198","TaylorRoot":2,"precision":10,
   "integerLift":"same canonical0..30 t-coefficients as old all198; original K is canonical s coefficient lift"})
  receipt["localInputBindingSHA256"]=local_binding;save()
  prep_dir=recovery/"prepared-197";prep_dir.mkdir(exist_ok=True)
  prep_receipt=prep_dir/"prepared-197-third-receipt.json";prep_system=prep_dir/"prepared-197-third.bin.gz"
  prepkeys=["fiveReceipt","fiveSystem","oldPrimaryReceipt","oldPrimarySystem","jetMap","jetMapReceipt","ninthRem","oldK","k1Recipe"]
  prepflags=["five-receipt","five-system","old-primary-receipt","old-primary-system","map","map-receipt","ninth-remainders","kernels","k1-recipe"]
  args=["--mode","prepare","--notes-root",notes,"--out",prep_dir]
  for flag,key in zip(prepflags,prepkeys):args+=["--"+flag,found[key]]
  run_stage("saved-197-preparation","matrix",args,"completed",
   {"trueV10InvariantVerified":True,"trueSevenCancellationVerifiedOnComplete39":True,"relevantQuotientDimension":24},
   [found[k] for k in prepkeys]+[found["state"]],[prep_receipt,prep_system,prep_dir/"true-seven-cancellation.bin"],
   {"onlySavedData":True,"exactK1Deleted":True,"trueB10":9305})
  prep=json.loads(prep_receipt.read_text());receipt["savedPreparationConclusion"]=prep;save()
  q1vq=prefix("q1-ten-vq")
  run_stage("q1-ten-vq","local-vq",[found["model"],found["graph"],found["oldQ"],found["oldK"],found["oldQ1Jet2195"],q1vq,local_binding,"q1"],
   "197-ten-jet-VQ-complete",{"mode":"q1"},
   [found[k] for k in ("model","graph","oldQ","oldK","oldQ1Jet2195")],
   [suffix(q1vq,x) for x in ("-original2195-source-jets.bin","-vq-checkpoint.bin","-vq.json","-actual-G-root2-ten.bin","-actual-V-root2-ten.bin")],
   {"localBinding":local_binding,"sameOldCanonicalTSource":True})
  q1raw=prefix("q1-ten-original")
  run_stage("q1-ten-original","local-transport",[found["model"],found["oldK"],suffix(q1vq,"-original2195-source-jets.bin"),
   found["normalTrace"],found["oldTrace"],found["forward"],found["backward"],q1raw,local_binding,"q1",found["oldQ1Jet6188"]],
   "197-ten-jet-original-source-transport-complete",{"mode":"q1"},
   [found[k] for k in ("model","oldK","normalTrace","oldTrace","forward","backward","oldQ1Jet6188")]+[suffix(q1vq,"-original2195-source-jets.bin")],
   [suffix(q1raw,x) for x in ("-original6188-q-jets.bin","-transport-checkpoint.bin","-transport.json")],
   {"localBinding":local_binding,"completeOriginalDAG":True})
  first=prefix("true-R2-ten")
  run_stage("true-R2-ten","local-product",["first",found["model"],integer_model,found["oldK"],suffix(q1raw,"-original6188-q-jets.bin"),found["oldR2Jets"],first,local_binding],
   "197-original17-local-integer-product-complete",{"mode":"first"},
   [found[k] for k in ("model","ninthIntegerModel","oldK","oldR2Jets")]+[suffix(q1raw,"-original6188-q-jets.bin")],
   [suffix(first,x) for x in ("-R2-mod961-root2-ten.bin","-original-product.json")],
   {"localBinding":local_binding,"modulus":P4,"sameCanonicalTLiftComparedOnOriginal4367FiveJets":True})
  bases_recipe=inputs/"true-seven-source-jets.recipe"
  bases_recipe.write_text("R150_197_TRUE_SEVEN_SOURCE_JETS_V1\n3\n"+"\n".join(str(found[k]) for k in ("kernels","fourK2","selectedK2"))+"\n")
  bases=prefix("true-seven-b-ten")
  run_stage("true-seven-b-ten","local-product",["bases",found["model"],integer_model,found["oldK"],bases_recipe,"-",bases,local_binding],
   "197-original17-local-integer-product-complete",{"mode":"bases"},
   [found[k] for k in ("model","ninthIntegerModel","oldK","kernels","fourK2","selectedK2")],
   [suffix(bases,x) for x in ("-true-seven-b-mod961-root2-ten.bin","-original-product.json")],
   {"localBinding":local_binding,"trueSourceDivisors":[31,31,961,961,961,961,961]})
  subtraction_recipe=inputs/"actual-integer-T.recipe"
  subtraction_recipe.write_text(str(suffix(first,"-R2-mod961-root2-ten.bin"))+"\n"+str(prep_dir/"true-seven-cancellation.bin")+"\n")
  subtract=prefix("actual-T-ten")
  run_stage("actual-T-ten","local-product",["subtract",found["model"],integer_model,found["oldK"],suffix(bases,"-true-seven-b-mod961-root2-ten.bin"),subtraction_recipe,subtract,local_binding],
   "197-integer-ten-jet-subtraction-complete",{},
   [found[k] for k in ("model","ninthIntegerModel","oldK")]+[suffix(first,"-R2-mod961-root2-ten.bin"),suffix(bases,"-true-seven-b-mod961-root2-ten.bin"),prep_dir/"true-seven-cancellation.bin"],
   [suffix(subtract,x) for x in ("-T-mod961-root2-ten.bin","-T-field-root2-ten.bin","-subtraction.json")],
   {"localBinding":local_binding,"sameIntegerCarry":True})
  nf10=prefix("actual-T-normal-ten")
  run_stage("actual-T-normal-ten","local-normal-ten",[found["model"],suffix(subtract,"-T-field-root2-ten.bin"),found["graph"],found["oldK"],nf10,local_binding],
   "197-original-ten-jet-normal-form-complete",{},
   [found[k] for k in ("model","graph","oldK")]+[suffix(subtract,"-T-field-root2-ten.bin")],
   [suffix(nf10,x) for x in ("-original1034-root2-ten.bin","-local-prebasis-source-jets.bin","-local-normal.json","-forward.bin","-backward.bin","-normal-checkpoint.bin")],
   {"localBinding":local_binding,"original4367PrebasisIdentity":True})
  if sha(suffix(nf10,"-forward.bin"))!=sha(found["forward"]) or sha(suffix(nf10,"-backward.bin"))!=sha(found["backward"]):raise ValueError("same exact original3333 DAG in local normal form")
  solve_dir=recovery/"complete-local-unit-solve";solve_dir.mkdir(exist_ok=True)
  qG=solve_dir/"complete-G-q2-root2-ten.bin";qGreceipt=solve_dir/"local-unit-solve-receipt.json"
  run_stage("complete-local-unit-solve","matrix",["--mode","local-solve","--notes-root",notes,"--G",suffix(q1vq,"-actual-G-root2-ten.bin"),
   "--rhs",suffix(nf10,"-original1034-root2-ten.bin"),"--binding",local_binding,"--remaining-seconds",max(0.001,deadline-time.monotonic()-0.25),"--out",solve_dir],
   "completed",{"fullOriginalG1034TenJetIdentityVerified":True,"all13FreeConditionsRetained":True},
   [suffix(q1vq,"-actual-G-root2-ten.bin"),suffix(nf10,"-original1034-root2-ten.bin")],[qG,qGreceipt],
   {"localBinding":local_binding,"constantUnits":573,"remainingShape":[461,448],"precision":10,"smithBound":5})
  q2vq=prefix("q2-ten-vq")
  run_stage("q2-ten-vq","local-vq",[found["model"],suffix(q1vq,"-actual-V-root2-ten.bin"),qG,found["oldK"],"-",q2vq,local_binding,"q2"],
   "197-ten-jet-VQ-complete",{"mode":"q2"},
   [found["model"],found["oldK"],suffix(q1vq,"-actual-V-root2-ten.bin"),qG],
   [suffix(q2vq,x) for x in ("-original2195-source-jets.bin","-vq-checkpoint.bin","-vq.json")],
   {"localBinding":local_binding,"localSolutionSourceTransport":True})
  q2raw=prefix("q2-ten-original")
  run_stage("q2-ten-original","local-transport",[found["model"],found["oldK"],suffix(q2vq,"-original2195-source-jets.bin"),
   found["normalTrace"],suffix(nf10,"-local-prebasis-source-jets.bin"),found["forward"],found["backward"],q2raw,local_binding,"q2","-"],
   "197-ten-jet-original-source-transport-complete",{"mode":"q2"},
   [found[k] for k in ("model","oldK","normalTrace","forward","backward")]+[suffix(q2vq,"-original2195-source-jets.bin"),suffix(nf10,"-local-prebasis-source-jets.bin")],
   [suffix(q2raw,x) for x in ("-original6188-q-jets.bin","-transport-checkpoint.bin","-transport.json")],
   {"localBinding":local_binding,"trueLocalCochainTransport":True})
  third=prefix("true-third-original-five")
  run_stage("true-third-original-five","local-product",["third",found["model"],integer_model,found["oldK"],suffix(q2raw,"-original6188-q-jets.bin"),suffix(subtract,"-T-mod961-root2-ten.bin"),third,local_binding],
   "197-original17-local-integer-product-complete",{"mode":"third"},
   [found[k] for k in ("model","ninthIntegerModel","oldK")]+[suffix(q2raw,"-original6188-q-jets.bin"),suffix(subtract,"-T-mod961-root2-ten.bin")],
   [suffix(third,x) for x in ("-third-projected-original-delta-jets.bin","-original-product.json")],
   {"localBinding":local_binding,"originalTenJetIdentityThenFiveJetDivision":True,"root1ExplicitZeroProjection":True})
  state8=prefix("third-projected-standard-state")
  run_stage("third-projected-standard-state","local-state-eight",[found["model"],suffix(third,"-third-projected-original-delta-jets.bin"),found["graph"],found["oldK"],state8,local_binding],
   "197-projected-two-ring-standard-state-complete",{},
   [found[k] for k in ("model","graph","oldK")]+[suffix(third,"-third-projected-original-delta-jets.bin")],
   [suffix(state8,x) for x in ("-all197-standard-state.bin","-local-G-quotient-jets.bin","-local-prebasis-source-jets.bin","-local-normal.json","-forward.bin","-backward.bin","-normal-checkpoint.bin")],
   {"localBinding":local_binding,"complete143MapInput":True})
  complete_dir=recovery/"complete-197-third";complete_dir.mkdir(exist_ok=True)
  complete_receipt=complete_dir/"complete-197-third-image-receipt.json";complete_system=complete_dir/"complete-197-third-image.bin.gz"
  run_stage("complete-197-third","matrix",["--mode","complete","--notes-root",notes,
   "--prepared-receipt",prep_receipt,"--prepared-system",prep_system,"--map",found["jetMap"],"--map-receipt",found["jetMapReceipt"],
   "--standard-state",suffix(state8,"-all197-standard-state.bin"),"--original-metadata",suffix(third,"-original-product.json"),"--normal-metadata",suffix(state8,"-local-normal.json"),"--out",complete_dir],
   "completed",{"all197ThirdDirectionsComputed":True,"completeRelevantLowInitialThirdImageComputed":True},
   [prep_receipt,prep_system,found["jetMap"],found["jetMapReceipt"],found["state"],suffix(state8,"-all197-standard-state.bin"),suffix(third,"-original-product.json"),suffix(state8,"-local-normal.json")],
   [complete_receipt,complete_system],{"all197AndPaidFive":True,"full104FreeChecks":True,"coefficientDegree":4,"negativeNaturalGraphScopeOnly":True})
  solution=json.loads(complete_receipt.read_text());flags=solution["individualTargetCompatible"]
  if len(flags)!=9 or solution["targetLabels"]!=LABEL9:raise ValueError("actual nine compatibility flags")
  compatible=[j for j,f in zip(LABEL9,flags) if f];insufficient=[j for j,f in zip(LABEL9,flags) if not f]
  receipt.update(all197ThirdDirectionsComputed=True,completeRelevantLowInitialThirdImageComputed=True,
   individualTargetCompatible=flags,compatibleTargetLabels=compatible,insufficientTargetLabels=insufficient,
   completeRelevantThirdConclusion=solution,newRelatedThirdImageRank=solution["newRelatedThirdImageRank"]);save()
  def normal_stage(name,original):
   output=prefix(name);data=[found["model"],suffix(original,"-divided-original-rhs.bin")]
   key=binding(data,{"actualFullOriginalRHS":True},"normal")
   run_stage(name,"normal",data+[output,key],"197-third-global-normal-forms-complete",{},data,
    [suffix(output,x) for x in ("-normal-forms.bin","-reduction.bin","-forward.bin","-backward.bin","-normal-checkpoint.bin")],
    {"actualFullOriginalRHS":True,"checkpointBinding":key})
   if sha(suffix(output,"-forward.bin"))!=sha(found["forward"]) or sha(suffix(output,"-backward.bin"))!=sha(found["backward"]):raise ValueError("same complete original3333 provenance")
   return output
  def own_nf_family(normal,image,labels,polys):
   return {"nf":suffix(normal,"-normal-forms.bin"),"q":suffix(image,"-image-quotients.bin") if image else "-",
    "rem":suffix(image,"-image-remainders.bin") if image else "-","trace":suffix(normal,"-reduction.bin"),"labels":labels,"polys":polys}
  def classify_global(name,mode,normal,actual,labels,bound):
   plain=own_nf_family(normal,None,labels,identity(9))
   mix=inputs/(name+"-plain.mix");helper.write_mix(mix,labels,bound,[plain])
   image=image_stage(name+"-image",mix,[plain],bound,labels,False)
   directory=recovery/name;directory.mkdir(exist_ok=True);rec=directory/("global-second-reconciliation.json" if mode=="global-second" else "global-third-reconciliation.json")
   system=directory/("global-second-reconciliation.bin.gz" if mode=="global-second" else "global-third-reconciliation.bin.gz")
   run_stage(name,"matrix",["--mode",mode,"--notes-root",notes,"--prepared-receipt",prep_receipt,"--prepared-system",prep_system,
    "--complete-receipt",complete_receipt,"--original-metadata",suffix(actual,"-original-product.json"),
    "--image-metadata",suffix(image,"-image-certificate.json"),"--image-remainders",suffix(image,"-image-remainders.bin"),"--out",directory],
    "completed",{"all505FreeObservationsVerified":True,"allCompatibleWhole315IdentitiesVerified":True},
    [prep_receipt,prep_system,complete_receipt,found["state"],suffix(actual,"-original-product.json"),suffix(image,"-image-certificate.json"),suffix(image,"-image-remainders.bin")],
    [rec,system],{"entire315PositiveReconciliation":True,"mode":mode})
   return image,json.loads(rec.read_text())
  if compatible:
   F=solution["solutionPolynomialsAscending"];projector=solution["projectorPolynomialAscending"]
   if len(F)!=197 or any(len(row)!=9 for row in F) or max([len(p) for row in F for p in row]+[0])>5 or len(projector)>197:raise ValueError("paid197 source/projector degrees")
   select=identity(9)
   for j,ok in enumerate(flags):
    if not ok:select[j][j]=[]
   projected=[[projector if i==j and flags[j] else [] for j in range(9)] for i in range(9)]
   oldF=zero(1,9)+F+zero(2,9)
   first_families=[{"nf":found["oldNF"],"q":found["oldQ"],"rem":found["oldRem"],"trace":found["oldTrace"],"labels":oldlabels,"polys":oldF}]
   first_mix=inputs/"positive-first-q.mix";helper.write_mix(first_mix,LABEL9,85,first_families)
   im1=image_stage("positive-first-q-image",first_mix,first_families,85,LABEL9,True)
   so1=source_stage("positive-first-q-source",im1,"target9",85,9)
   tr1=transport_stage("positive-first-q-original",so1,first_mix,first_families,85)
   tr1m=json.loads(suffix(tr1,"-original-transport.json").read_text());B1=max([85]+tr1m["sourceCosts"])
   if B1>181:raise ValueError("paid first global source181")
   H2families=[{"file":found["oldK"],"labels":oldlabels,"polys":oldF},
    {"file":suffix(tr1,"-primitive-source-mod31.bin"),"labels":LABEL9,"polys":scale(select,-P)}]
   H2=original_stage("positive-H2-original",list(range(9402,9411)),B1,P2,0,flags,H2families)
   N2=normal_stage("positive-H2-normal",H2)
   I2,C2rec=classify_global("positive-second-whole315","global-second",N2,H2,list(range(9402,9411)),B1)
   C2=constants(C2rec["actualConstantCorrections"]);cbeta=C2[:2]+zero(2,9);cfour=C2[2:6];cselected=[C2[6]]+zero(8,9)
   B2=max(40,B1+len(projector)-1)
   if B2>377:raise ValueError("paid first projector RHS377")
   q2families=[own_nf_family(N2,I2,list(range(9402,9411)),projected),
    nf_family("beta",BETA_LABELS,negate(cbeta)),nf_family("four",FOUR_LABELS,negate(cfour)),nf_family("selected",LABEL9,negate(cselected))]
   q2mix=inputs/"positive-second-q.mix";helper.write_mix(q2mix,LABEL9,B2,q2families)
   im2=image_stage("positive-second-q-image",q2mix,q2families,B2,LABEL9,True)
   so2=source_stage("positive-second-q-source",im2,"target9",B2,9)
   tr2=transport_stage("positive-second-q-original",so2,q2mix,q2families,B2)
   tr2m=json.loads(suffix(tr2,"-original-transport.json").read_text());B5=max([B2]+tr2m["sourceCosts"])
   if B5>473:raise ValueError("paid second global source473")
   H5families=[{"file":suffix(H2,"-primitive-source-mod887503681.bin"),"labels":list(range(9402,9411)),"polys":scale(projected,P2)},
    {"file":found["kernels"],"labels":BETA_LABELS,"polys":scale(cbeta,-P3)},
    {"file":found["fourK2"],"labels":FOUR_LABELS,"polys":scale(cfour,-P2)},
    {"file":found["selectedK2"],"labels":LABEL9,"polys":scale(cselected,-P2)},
    {"file":suffix(tr2,"-primitive-source-mod31.bin"),"labels":LABEL9,"polys":scale(select,-P4)}]
   H5=original_stage("positive-H5-original",list(range(9502,9511)),B5,P5,0,flags,H5families)
   N5=normal_stage("positive-H5-normal",H5)
   I5,C5rec=classify_global("positive-third-whole315","global-third",N5,H5,list(range(9502,9511)),B5)
   C10=constants(C5rec["actualConstantCorrections"])
   if len(C10)!=10:raise ValueError("true ten-source correction")
   cbeta=C10[:2]+zero(2,9);cfour=C10[2:6];cselected=[C10[6]]+zero(8,9)
   old8=zero(16,9);old8[2]=C10[7]
   old9=zero(7,9);old9[3]=C10[8]
   old10=zero(5,9);old10[2]=C10[9]
   current_select=zero(1,9)+select;B3=max(40,B5+len(projector)-1)
   if B3>669:raise ValueError("paid outer projector RHS669")
   wfamilies=[nf_family("ninth",LABEL10,current_select),
    own_nf_family(N5,I5,list(range(9502,9511)),negate(projected)),
    nf_family("beta",BETA_LABELS,negate(cbeta)),nf_family("four",FOUR_LABELS,negate(cfour)),
    nf_family("selected",LABEL9,negate(cselected)),nf_family("new",LABEL16,negate(old8)),
    nf_family("currentK4",LABEL7,negate(old9)),nf_family("five",LABEL5,negate(old10))]
   wmix=inputs/"positive-final-q.mix";helper.write_mix(wmix,LABEL9,B3,wfamilies)
   iw=image_stage("positive-final-q-image",wmix,wfamilies,B3,LABEL9,True)
   sw=source_stage("positive-final-q-source",iw,"target9",B3,9)
   tw=transport_stage("positive-final-q-original",sw,wmix,wfamilies,B3)
   twm=json.loads(suffix(tw,"-original-transport.json").read_text());paid=max([B3]+twm["sourceCosts"])
   if paid>765 or any(twm["sourceCosts"][j]!=-1 for j,ok in enumerate(flags) if not ok):raise ValueError("actual final765/inactive source bound")
   finalfamilies=[{"file":found["ninthOriginal"],"labels":LABEL10,"polys":current_select},
    {"file":suffix(H5,"-primitive-source-mod887503681.bin"),"labels":list(range(9502,9511)),"polys":projected},
    {"file":found["kernels"],"labels":BETA_LABELS,"polys":scale(cbeta,P4)},
    {"file":found["fourK2"],"labels":FOUR_LABELS,"polys":scale(cfour,P3)},
    {"file":found["selectedK2"],"labels":LABEL9,"polys":scale(cselected,P3)},
    {"file":found["newOriginal"],"labels":LABEL16,"polys":scale(old8,P2)},
    {"file":found["currentK4Original"],"labels":LABEL7,"polys":scale(old9,P)},
    {"file":found["fiveOriginal"],"labels":LABEL5,"polys":old10},
    {"file":suffix(tw,"-primitive-source-mod31.bin"),"labels":LABEL9,"polys":scale(select,P5)}]
   final=original_stage("positive-final-original17",LABEL9,paid,P6,1,flags,finalfamilies)
   fm=json.loads(suffix(final,"-original-product.json").read_text())
   if not all(fm.get(k) is True for k in ("fullOriginalSeventeenEquationIdentityMod887503681","fullOriginalMacaulayIdentityMod887503681","originalRowScaleTransportVerified","allWeightedBoundsVerified","inactiveSourceColumnsExactlyZero")) or fm["activeTargetLabels"]!=compatible:raise ValueError("all compatible original17 full identities")
   receipt.update(finalOriginalConclusion=fm,actualFinalSourceCostsBySlot=fm["actualSourceCosts"],completedOriginalTargetLabels=compatible,
    allCompatibleTargetsOriginalIdentityVerified=True,finitePositiveSourceBudgetsVerified=True);save()
  outcome="all-nine-original-p6-complete" if all(flags) else "partial-original-p6-complete" if compatible else "complete-relevant-low-initial-third-obstruction"
  receipt.update(status="completed",outcome=outcome,fullOriginalAllNineMod887503681IdentityVerified=all(flags),
   finite_budget_verified=all(flags),numberOfCompatibleTargets=len(compatible),mathematicalElapsedSeconds=time.monotonic()-math_start);save()
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
  (results/"certificate-manifest.json").write_text(json.dumps({"format":"r150-197-third-lossless-certificates-v1","pipelineStatus":receipt["status"],"partialCheckpointIsNotIdentity":True,"files":files},indent=2)+"\n")
  (results/"text-recovery-manifest.json").write_text(json.dumps({"format":"r150-197-third-exact-text-recovery-v1","completeStageCachesIncluded":True,"files":texts},indent=2)+"\n")
  saved=[{"file":str(p.relative_to(recovery)),"bytes":p.stat().st_size,"sha256":sha(p)} for p in sorted(recovery.rglob("*")) if p.is_file()]
  (results/"recovery-manifest.json").write_text(json.dumps({"format":"r150-197-third-complete-recovery-v1","pipelineStatus":receipt["status"],"files":saved},indent=2)+"\n")
  receipt.update(recoveryFiles=len(saved),recoveryBytes=sum(p["bytes"] for p in saved),losslessGeneratedBinaryFiles=len(files));save()
  print(json.dumps({k:receipt.get(k) for k in ("status","outcome","mathematicalElapsedSeconds","completedOriginalTargetLabels","completeRelevantLowInitialThirdImageComputed","fullOriginalAllNineMod887503681IdentityVerified","insufficientTargetLabels","recoveryBytes")}),flush=True)
 if receipt["status"] not in ("completed","prepared-no-mathematical-stage-executed"):raise SystemExit(1)
if __name__=="__main__":main()
