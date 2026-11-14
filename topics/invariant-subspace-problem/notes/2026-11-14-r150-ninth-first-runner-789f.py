#!/usr/bin/env python3
"""One genuinely new F9 relation plus nine current p5 residuals; every positive target reaches original17."""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,shutil,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
CONTRACT="2026-11-14-r150-ninth-first-contract-789f.json"
OLD_HELPER="2026-11-14-r150-four-second-bockstein-runner-789f.py"
PYPROGRAMS={"model":"2026-11-14-r150-ninth-first-integer-model-789f.py",
 "matrix":"2026-11-14-r150-ninth-first-matrices-789f.py",
 "selector":"2026-11-14-r150-ninth-source-action-and-kernel-789f.py"}
PROGRAMS={
 "image":("2026-11-14-r150-ninth-first-image-789f.cpp",[]),
 "source1":("2026-11-14-r150-ninth-first-source-one-789f.cpp",[]),
 "target9":("2026-11-14-r150-ninth-first-target-source-789f.cpp",[]),
 "transport":("2026-11-14-r150-ninth-first-transport-789f.cpp",[]),
 "normal":("2026-11-14-r150-ninth-first-normal-789f.cpp",[]),
 "original":("2026-11-14-r150-ninth-first-original-789f.cpp",[])}
LABEL7=list(range(7001,7008));LABEL9=list(range(2,11));LABEL16=LABEL7+LABEL9
TARGETS=LABEL9;SAVED7=[2,3,4,5,7,8,10];PAIR=[6,9];LABEL1=[9001];LABEL10=LABEL1+LABEL9
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
 lines=["R150_ORIGINAL_NINTH_COMBINATION_V1",f"{len(labels)} {bound} {divisor} {target_mode} {len(families)}",
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
 for name in ("notes-root","t96-recovery","all198-recovery","seven-recovery","current-recovery","out"):parser.add_argument("--"+name,type=Path,required=True)
 parser.add_argument("--math-seconds",type=int,default=300);parser.add_argument("--memory-mib",type=int,default=512)
 parser.add_argument("--compile-seconds",type=int,default=30);parser.add_argument("--resume-recovery",type=Path);parser.add_argument("--prepare-only",action="store_true")
 a=parser.parse_args()
 if min(a.math_seconds,a.memory_mib,a.compile_seconds)<1:raise ValueError("explicit positive bounds")
 root=Path(__file__).resolve().parent;notes=a.notes_root.resolve();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 recovery=out/"recovery"
 if a.resume_recovery and a.resume_recovery.resolve()!=recovery:shutil.copytree(a.resume_recovery,recovery,dirs_exist_ok=True)
 results=out/"results";bins=out/"bin";inputs=recovery/"inputs";cache=recovery/"stage-cache"
 for d in (results,recovery,bins,inputs,cache):d.mkdir(parents=True,exist_ok=True)
 receipt_path=results/"ninth-first-pipeline-receipt.json"
 receipt={"format":"r150-ninth-complete-first-and-current-nine-continuous-lift-v1","status":"preparing",
  "prime":31,"integerModulus":P6,"targetMultiplier":"31^2*h0","sourceCurrentRun":43634830833,
  "newDirectionLabels":LABEL1,"actualNewRHSLabels":LABEL10,"targetLabels":LABEL9,
  "old1834AndOldSevenDirectionsRecomputed":False,"newNinthDirectionComputed":False,
  "fullF9FirstImageComplete":False,"completeHigherInitialFreedomComputed":False,
  "fullOriginalAllNineMod887503681IdentityVerified":False,"allCompatibleTargetsOriginalIdentityVerified":False,
  "finite_budget_verified":False,"characteristicZeroIdentityAsserted":False,
  "sharedMathematicalSecondsLimit":a.math_seconds,"perChildAddressSpaceMiBLimit":a.memory_mib,"perCompilationSecondsLimit":a.compile_seconds,
  "deadlineRule":"Six bounded native compilations and saved input SHA checks precede one shared mathematical clock. Same exact p6 model, saved U9/J9 selector, one new q/image/VQ/transport, joint original10 product, normal10, full306 first image and every positive original17 continuation share it. VQ and original-product partial arrays checkpoint; all completed stages have source-bound caches. Compression follows.",
  "inputs":{},"sources":{},"compilations":{},"stages":{}}
 math_start=None
 def save():receipt_path.write_text(json.dumps(receipt,separators=(",",":"))+"\n")
 try:
  contract=json.loads((root/CONTRACT).read_text());receipt["inputContractSHA256"]=sha(root/CONTRACT)
  scopes={"notes":notes,"t96":a.t96_recovery.resolve(),"all198":a.all198_recovery.resolve(),
          "seven":a.seven_recovery.resolve(),"current":a.current_recovery.resolve()};found={}
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
  for key,labels in (("currentSevenReceipt",SAVED7),("currentPairReceipt",PAIR)):
   meta=json.loads(found[key].read_text())
   if meta.get("status")!="completed" or meta.get("modulus")!=P5 or meta.get("targetLabels")!=labels or meta.get("actualSourceCosts")!=[87]*len(labels) or not meta.get("fullOriginalSeventeenEquationIdentityMod28629151"):raise ValueError("same actual current original nine source certificates")
  previous=json.loads(found["currentGlobalReceipt"].read_text())
  if previous.get("status")!="completed" or not previous.get("allSevenCompatible") or previous.get("KrylovBasisColumnIndicesZeroBased")!=[3] or previous.get("maximumSolutionDegree")!=0:raise ValueError("same actual ninth independent source")
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
   recipe=inputs/(name+".recipe");write_original6(recipe,labels,bound,divisor,target_mode,active,families)
   output=prefix(name);data=[found["model"],integer_model]+[f["file"] for f in families]
   logical={"bound":bound,"divisor":divisor,"targetMode":target_mode,"labels":labels,"active":[int(x) for x in active],
            "polynomials":[f["polys"] for f in families]}
   key=binding(data,logical,"original");required={"divisor":divisor,"allOriginalProductCoefficientsDivisible":True}
   if divisor==P6:required["fullOriginalSeventeenEquationIdentityMod887503681"]=True
   files=[suffix(output,x) for x in ("-primitive-source-mod887503681.bin","-original-seventeen-source-mod887503681.bin","-original-product.json")]
   if divisor==P5:files.append(suffix(output,"-fifth-divided-original-rhs.bin"))
   run_stage(name,"original",[found["model"],integer_model,recipe,output,key],
    "full-original-ninth-first-product-complete",required,data,files,{**logical,"checkpointBinding":key})
   metadata=json.loads(suffix(output,"-original-product.json").read_text())
   if metadata.get("targetLabels")!=labels or metadata.get("activeTargetLabels")!=[j for j,f in zip(labels,active) if f] or not metadata.get("inactiveSourceColumnsExactlyZero"):raise ValueError("exact actual original target-mask scope")
   return output
  integer_model=inputs/"original-integer-31squaredh0-mod887503681.txt"
  run_stage("same-exact-integer-model","model",["--exact-gzip",found["exactInteger"],"--lower-model",found["integerModel"],"--out",integer_model],
   "completed",{"lowerMod31FiveModelIncludingTargetVerified":True,"modulus":P6,"target":"31^2*h0"},
   [found["exactInteger"],found["integerModel"]],[integer_model,suffix(integer_model,".json")],
   {"sameOriginal17":True,"modulus":P6,"unchangedTargetMultiplier":P2})
  prep_dir=recovery/"saved-ninth-action";prep_dir.mkdir(exist_ok=True)
  prepared_receipt=prep_dir/"ninth-source-action-receipt.json";prepared_system=prep_dir/"ninth-source-action.bin.gz"
  selector_names=["currentGlobalReceipt","currentGlobalSystem","currentPreparedReceipt","currentPreparedSystem","currentK4Original","currentSevenOriginal","currentPairOriginal"]
  selector_flags=["receipt","system","prepared-receipt","prepared-system","k4-source","current-seven-source","current-pair-source"]
  selector_args=["--notes-root",notes,"--out",prep_dir]
  for flag,key in zip(selector_flags,selector_names):selector_args+=["--"+flag,found[key]]
  run_stage("saved-ninth-action","selector",selector_args,"completed",{"fullF9FirstImageRequiresOnlyNinthRelation":True,"U9Dimension":9},
   [found[k] for k in selector_names]+[found["state"]],[prepared_receipt,prepared_system],
   {"onlySavedData":True,"sameOriginalSourceRun":43634830833})
  preparation=json.loads(prepared_receipt.read_text());a9=preparation["ninthRelationOldEightCorrection"]
  if len(a9)!=8 or preparation.get("ninthQuotientEigenvalue")!=2:raise ValueError("actual ninth relation coefficients")
  receipt["savedNinthActionConclusion"]=preparation;save()
  C8=constants([[x] for x in a9]);C=C8[:7];g=C8[7]
  cbeta=C[:2]+zero(2,1);cfour=C[2:6];cselected=[C[6]]+zero(8,1)
  L=zero(7,1);L[3][0]=[-2,1]
  oldfirst=zero(16,1);oldfirst[2]=negate([g])[0]
  first_families=[
   nf_family("currentK4",LABEL7,L),nf_family("new",LABEL16,oldfirst),
   nf_family("beta",BETA_LABELS,negate(cbeta)),nf_family("four",FOUR_LABELS,negate(cfour)),
   nf_family("selected",LABEL9,negate(cselected))]
  first_mix=inputs/"genuine-ninth-q.mix";helper.write_mix(first_mix,LABEL1,BOUND,first_families)
  first_image=image_stage("genuine-ninth-q-image",first_mix,first_families,BOUND,LABEL1,True)
  first_source=source_stage("genuine-ninth-q-source",first_image,"source1",BOUND,1)
  first_transport=transport_stage("genuine-ninth-q-original",first_source,first_mix,first_families,BOUND)
  qm=json.loads(suffix(first_transport,"-original-transport.json").read_text())
  k5_bound=max([BOUND]+qm["sourceCosts"])
  if k5_bound>184:raise ValueError("true ninth q exceeds paid88plus96 source bound")
  def one_column(polys):
   return [row+[[] for _ in range(9)] for row in polys]
  def target_embedding(labels):
   return [[[1] if output==label else [] for output in LABEL10] for label in labels]
  original_old8=zero(16,10);original_old8[2][0]=[-P*a9[7]] if a9[7] else []
  k5_families=[
   {"file":found["currentK4Original"],"labels":LABEL7,"polys":one_column(L)},
   {"file":found["newOriginal"],"labels":LABEL16,"polys":original_old8},
   {"file":found["kernels"],"labels":BETA_LABELS,"polys":one_column(scale(cbeta,-P3))},
   {"file":found["fourK2"],"labels":FOUR_LABELS,"polys":one_column(scale(cfour,-P2))},
   {"file":found["selectedK2"],"labels":LABEL9,"polys":one_column(scale(cselected,-P2))},
   {"file":suffix(first_transport,"-primitive-source-mod31.bin"),"labels":LABEL1,"polys":one_column(identity(1,-P4))},
   {"file":found["currentSevenOriginal"],"labels":SAVED7,"polys":target_embedding(SAVED7)},
   {"file":found["currentPairOriginal"],"labels":PAIR,"polys":target_embedding(PAIR)}]
  actual=original_stage("ninth-and-current-original",LABEL10,k5_bound,P5,0,[1]*10,k5_families)
  actual_meta=json.loads(suffix(actual,"-original-product.json").read_text())
  if not all(actual_meta.get(k) is True for k in ("allOriginalProductCoefficientsDivisible","originalRowScaleTransportVerified","allWeightedBoundsVerified")):raise ValueError("one plus nine actual original identities")
  if actual_meta["actualSourceCosts"][1:]!=[87]*9:raise ValueError("current nine original sources changed before next residual")
  receipt.update(newNinthDirectionComputed=True,newDirectionOriginalDivisibilityVerified=True,
   actualNewQSourceCosts=qm["sourceCosts"],actualJointSourceCosts=actual_meta["actualSourceCosts"],
   actualJointOriginalProduct=actual_meta,actualNewDirectionPaidCost=k5_bound);save()
  normal10=prefix("ninth-and-current-normal")
  run_stage("ninth-and-current-normal","normal",[found["model"],suffix(actual,"-fifth-divided-original-rhs.bin"),normal10],
   "ninth-and-current-ten-normal-forms-complete",{"targets":10,"components":1034},
   [found["model"],suffix(actual,"-fifth-divided-original-rhs.bin")],
   [suffix(normal10,x) for x in ("-normal-forms.bin","-reduction.bin","-forward.bin","-backward.bin")],
   {"bound":k5_bound,"labels":LABEL10,"signs":[1]+[-1]*9})
  if sha(suffix(normal10,"-forward.bin"))!=contract["inputs"]["forward"]["sha256"] or sha(suffix(normal10,"-backward.bin"))!=contract["inputs"]["backward"]["sha256"]:raise ValueError("same complete original3333 DAG hashes")
  receipt["sameOriginalPrebasisDAGHashesVerified"]=True;save()
  d_bound=max([40]+actual_meta["actualSourceCosts"])
  if d_bound>k5_bound:raise ValueError("actual source cost versus paid bound")
  fresh=[{"nf":suffix(normal10,"-normal-forms.bin"),"q":"-","rem":"-","trace":suffix(normal10,"-reduction.bin"),"labels":LABEL10,"polys":identity(10)}]
  fresh_mix=inputs/"ninth-and-current-image.mix";helper.write_mix(fresh_mix,LABEL10,d_bound,fresh)
  all_image=image_stage("ninth-and-current-image",fresh_mix,fresh,d_bound,LABEL10,False)
  global_dir=recovery/"complete-ninth-first";global_dir.mkdir(exist_ok=True)
  global_receipt=global_dir/"complete-ninth-first-image-receipt.json";global_system=global_dir/"complete-ninth-first-image.bin.gz"
  run_stage("complete-ninth-first","matrix",["--notes-root",notes,"--prepared-receipt",prepared_receipt,"--prepared-system",prepared_system,
   "--image-remainders",suffix(all_image,"-image-remainders.bin"),"--image-metadata",suffix(all_image,"-image-certificate.json"),
   "--original-metadata",suffix(actual,"-original-product.json"),"--out",global_dir],
   "completed",{"fullF9FirstImageComplete":True,"allCompatibleWhole315IdentitiesVerified":True},
   [prepared_receipt,prepared_system,suffix(all_image,"-image-remainders.bin"),suffix(all_image,"-image-certificate.json"),
    suffix(actual,"-original-product.json"),found["state"]],[global_receipt,global_system],
   {"allOldKernelAndEightRelationsPaid":1842,"newGenuineFirstDirections":1,"all315":True,"quotientByActualU9":True})
  solution=json.loads(global_receipt.read_text());flags=solution["individualTargetCompatible"]
  if len(flags)!=9 or solution["targetLabels"]!=LABEL9:raise ValueError("actual individual original nine flags")
  compatible=[j for j,f in zip(LABEL9,flags) if f];obstructed=[j for j,f in zip(LABEL9,flags) if not f]
  receipt.update(fullF9FirstImageComplete=True,all1834OriginalAndEightAugmentedDirectionsCovered=True,
   individualTargetCompatible=flags,compatibleTargetLabels=compatible,obstructedTargetLabels=obstructed,
   exactNegativeScope=solution["negativeScope"],newFirstImageRank=solution["newFirstImageRank"],
   completeNinthFirstConclusion=solution);save()
  if compatible:
   F=solution["firstSolutionPolynomialsAscending"];C9=constants(solution["oldNineConstantCorrection"])
   if len(F)!=1 or len(F[0])!=9 or len(C9)!=9 or any(len(row)!=9 for row in C9):raise ValueError("complete ninth first solution matrices")
   if any(F[0][j] or any(C9[i][j] for i in range(9)) for j,f in enumerate(flags) if not f):raise ValueError("inactive target source matrices must vanish")
   C=C9[:7];cbeta=C[:2]+zero(2,9);cfour=C[2:6];cselected=[C[6]]+zero(8,9)
   old8=zero(16,9);old8[2]=[list(poly) for poly in C9[7]]
   old9=zero(7,9);old9[3]=[list(poly) for poly in C9[8]]
   select=identity(9)
   for j,f in enumerate(flags):
    if not f:select[j][j]=[]
   final_bound=max(BOUND,d_bound+max(0,solution["maximumSolutionDegree"]))
   if final_bound>489:raise ValueError("actual full cyclic source exceeds184plus305")
   final_families=[
    {"nf":suffix(normal10,"-normal-forms.bin"),"q":suffix(all_image,"-image-quotients.bin"),
     "rem":suffix(all_image,"-image-remainders.bin"),"trace":suffix(normal10,"-reduction.bin"),
     "labels":LABEL10,"polys":negate(F)+select},
    nf_family("currentK4",LABEL7,negate(old9)),nf_family("new",LABEL16,negate(old8)),
    nf_family("beta",BETA_LABELS,negate(cbeta)),nf_family("four",FOUR_LABELS,negate(cfour)),
    nf_family("selected",LABEL9,negate(cselected))]
   final_mix=inputs/"compatible-current-nine.mix";helper.write_mix(final_mix,LABEL9,final_bound,final_families)
   fim=image_stage("compatible-current-image",final_mix,final_families,final_bound,LABEL9,True)
   fs=source_stage("compatible-current-source",fim,"target9",final_bound,9)
   ft=transport_stage("compatible-current-original-source",fs,final_mix,final_families,final_bound)
   tm=json.loads(suffix(ft,"-original-transport.json").read_text());paid=max([final_bound]+tm["sourceCosts"])
   if paid>final_bound+96 or any(tm["sourceCosts"][j]!=-1 for j,f in enumerate(flags) if not f):raise ValueError("actual final original source budget and zero inactive slots")
   active_identity=scale(select,P5)
   final_original_families=[
    {"file":suffix(actual,"-primitive-source-mod887503681.bin"),"labels":LABEL10,"polys":F+select},
    {"file":found["currentK4Original"],"labels":LABEL7,"polys":scale(old9,P)},
    {"file":found["newOriginal"],"labels":LABEL16,"polys":scale(old8,P2)},
    {"file":found["kernels"],"labels":BETA_LABELS,"polys":scale(cbeta,P4)},
    {"file":found["fourK2"],"labels":FOUR_LABELS,"polys":scale(cfour,P3)},
    {"file":found["selectedK2"],"labels":LABEL9,"polys":scale(cselected,P3)},
    {"file":suffix(ft,"-primitive-source-mod31.bin"),"labels":LABEL9,"polys":active_identity}]
   final_original=original_stage("compatible-current-original",LABEL9,paid,P6,1,flags,final_original_families)
   final_meta=json.loads(suffix(final_original,"-original-product.json").read_text())
   if not all(final_meta.get(k) is True for k in ("fullOriginalSeventeenEquationIdentityMod887503681","fullOriginalMacaulayIdentityMod887503681",
     "originalRowScaleTransportVerified","allWeightedBoundsVerified","inactiveSourceColumnsExactlyZero")) or final_meta["activeTargetLabels"]!=compatible:raise ValueError("every compatible actual target full original17 identity")
   receipt["finalOriginalConclusion"]=final_meta;receipt["actualFinalSourceCostsBySlot"]=final_meta["actualSourceCosts"];save()
  if all(flags):outcome="all-nine-full-original31squaredh0-mod887503681-certificates"
  elif compatible:outcome="complete-ninth-first-obstruction-with-positive-original-certificates"
  else:outcome="complete-ninth-first-obstruction-no-compatible-current-source"
  receipt.update(status="completed",outcome=outcome,completedOriginalTargetLabels=compatible,
   allCompatibleTargetsOriginalIdentityVerified=True,fullOriginalAllNineMod887503681IdentityVerified=all(flags),
   finitePositiveSourceBudgetsVerified=True,finite_budget_verified=all(flags),numberOfCompatibleTargets=len(compatible),
   numberOfObstructedCurrentSourceLifts=len(obstructed),mathematicalElapsedSeconds=time.monotonic()-math_start);save()
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
  (results/"certificate-manifest.json").write_text(json.dumps({"format":"r150-ninth-first-lossless-certificates-v1","pipelineStatus":receipt["status"],"partialCheckpointIsNotIdentity":True,"files":files},indent=2)+"\n")
  (results/"text-recovery-manifest.json").write_text(json.dumps({"format":"r150-ninth-first-exact-text-recovery-v1","completeStageCachesIncluded":True,"files":texts},indent=2)+"\n")
  saved=[{"file":str(p.relative_to(recovery)),"bytes":p.stat().st_size,"sha256":sha(p)} for p in sorted(recovery.rglob("*")) if p.is_file()]
  (results/"recovery-manifest.json").write_text(json.dumps({"format":"r150-ninth-first-complete-recovery-v1","pipelineStatus":receipt["status"],"files":saved},indent=2)+"\n")
  receipt.update(recoveryFiles=len(saved),recoveryBytes=sum(p["bytes"] for p in saved),losslessGeneratedBinaryFiles=len(files));save()
  print(json.dumps({k:receipt.get(k) for k in ("status","outcome","mathematicalElapsedSeconds","completedOriginalTargetLabels","fullF9FirstImageComplete","fullOriginalAllNineMod887503681IdentityVerified","obstructedTargetLabels","recoveryBytes")}),flush=True)
 if receipt["status"] not in ("completed","prepared-no-mathematical-stage-executed"):raise SystemExit(1)
if __name__=="__main__":main()
