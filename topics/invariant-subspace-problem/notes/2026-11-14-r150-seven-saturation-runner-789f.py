#!/usr/bin/env python3
"""Actual seven-relation saturation, followed by the next original31h0 lift.

Only new relations and current nine residuals are computed. The saved original
T96 graph, old198, four old second sources and selected source are reused.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,shutil,struct,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
CONTRACT="2026-11-14-r150-seven-saturation-input-contract-789f.json"
OLD_HELPER="2026-11-14-r150-four-second-bockstein-runner-789f.py"
MODEL_HELPER="2026-11-14-r150-seven-saturation-integer-model-789f.py"
GLOBAL="2026-11-14-r150-seven-saturation-global-789f.py"
PROGRAMS={
 "image":("2026-11-14-r150-seven-saturation-image-789f.cpp",[]),
 "source7":("2026-11-14-r150-seven-saturation-source-789f.cpp",["-DR150_TARGETS=7"]),
 "source9":("2026-11-14-r150-second-bockstein-source-checkpoint-789f.cpp",["-DR150_TARGETS=9"]),
 "transport":("2026-11-14-r150-second-bockstein-all198-global-original-transport-789f.cpp",[]),
 "original":("2026-11-14-r150-seven-saturation-original-789f.cpp",[]),
 "normal":("2026-11-14-r150-seven-saturation-normal-789f.cpp",[])}
LABEL7=list(range(7001,7008));LABEL9=list(range(2,11));LABEL16=LABEL7+LABEL9
BETA_LABELS=list(range(2275,2279));FOUR_LABELS=list(range(4001,4005))
P=31;P2=961;P3=29791;P4=923521;RELATION_BOUND=88;SOURCE_BOUND=184

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
def write_original4(path,labels,bound,divisor,families):
 lines=["R150_ORIGINAL_COMBINATION_V1",f"{len(labels)} {bound} {divisor} 1 {len(families)}"," ".join(map(str,labels))]
 for f in families:
  lines.append(str(f["file"])+" "+str(len(f["labels"])));lines.append(" ".join(map(str,f["labels"])))
  for row in f["polys"]:
   if len(row)!=len(labels):raise ValueError("complete original polynomial multiplier columns")
   for poly in row:
    poly=[x%P4 for x in poly]
    while poly and not poly[-1]:poly.pop()
    lines.append(" ".join(map(str,[len(poly)]+poly)))
 path.write_text("\n".join(lines)+"\n")

def main():
 parser=argparse.ArgumentParser()
 for name in ("notes-root","t96-recovery","all198-recovery","out"):parser.add_argument("--"+name,type=Path,required=True)
 parser.add_argument("--math-seconds",type=int,default=300);parser.add_argument("--memory-mib",type=int,default=512)
 parser.add_argument("--compile-seconds",type=int,default=30);parser.add_argument("--resume-recovery",type=Path);parser.add_argument("--prepare-only",action="store_true")
 a=parser.parse_args()
 if min(a.math_seconds,a.memory_mib,a.compile_seconds)<1:raise ValueError("explicit positive bounds")
 root=Path(__file__).resolve().parent;notes=a.notes_root.resolve();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 recovery=out/"recovery"
 if a.resume_recovery and a.resume_recovery.resolve()!=recovery:shutil.copytree(a.resume_recovery,recovery,dirs_exist_ok=True)
 results=out/"results";bins=out/"bin";inputs=recovery/"inputs";cache=recovery/"stage-cache"
 for d in (results,recovery,bins,inputs,cache):d.mkdir(parents=True,exist_ok=True)
 receipt_path=results/"seven-saturation-pipeline-receipt.json"
 receipt={"format":"r150-seven-true-relations-and-original31h0-next-lift-v1","status":"preparing","prime":31,"integerModulus":P4,
  "targetMultiplier":"31*h0","originalRelationCount":7,"actualNextResidualTargets":9,
  "newAugmentedFirstImageComplete":False,"fullOriginalTarget31h0Mod923521IdentityVerified":False,"finite_budget_verified":False,
  "characteristicZeroIdentityAsserted":False,"old198OrSelectedSourcesRecomputed":False,
  "sharedMathematicalSecondsLimit":a.math_seconds,"perChildAddressSpaceMiBLimit":a.memory_mib,"perCompilationSecondsLimit":a.compile_seconds,
  "deadlineRule":"Frozen restoration, exact saved-integer residue conversion and six individually bounded compilations precede the clock. All new source, original product, normal form, quotient and matrix stages share300seconds. SIGTERM receives up to10seconds for real arrays; completed stages have content-bound caches. Lossless output compression follows outside the mathematical clock.",
  "partialRecovery":{"source7AndSource9":"actual VQ arrays, next image row and reduction phase",
                     "original":"actual original product array and complete primitive/original source prefixes",
                     "otherStages":"completed-stage cache only; no invented internal checkpoints"},
  "inputs":{},"sources":{},"compilations":{},"stages":{}}
 math_start=None
 def save():receipt_path.write_text(json.dumps(receipt,indent=2)+"\n")
 try:
  contract=json.loads((root/CONTRACT).read_text());receipt["inputContractSHA256"]=sha(root/CONTRACT)
  scopes={"notes":notes,"t96":a.t96_recovery.resolve(),"all198":a.all198_recovery.resolve()};found={}
  for name,item in contract["inputs"].items():
   scope=scopes[item["scope"]]
   if "gzipParts" in item:
    joined=inputs/(name+".source.gz")
    with joined.open("wb") as target:
     for part in item["gzipParts"]:
      path=scope/part["relative"]
      if path.stat().st_size!=part["bytes"] or sha(path)!=part["sha256"]:raise ValueError("actual frozen input part "+name)
      with path.open("rb") as src:shutil.copyfileobj(src,target)
    if sha(joined)!=item["compressedSHA256"]:raise ValueError("actual joined gzip "+name)
    decoded=inputs/(name+".bin")
    if not decoded.exists() or sha(decoded)!=item["sha256"]:
     with gzip.open(joined,"rb") as src,decoded.open("wb") as dst:shutil.copyfileobj(src,dst)
    candidates=[decoded];joined.unlink()
   elif "gzipRelative" in item:
    compressed=scope/item["gzipRelative"]
    if sha(compressed)!=item["compressedSHA256"]:raise ValueError("actual frozen gzip "+name)
    decoded=inputs/(name+".bin")
    if not decoded.exists() or sha(decoded)!=item["sha256"]:
     with gzip.open(compressed,"rb") as src,decoded.open("wb") as dst:shutil.copyfileobj(src,dst)
    candidates=[decoded]
   else:
    candidates=[scope/item["relative"]] if "relative" in item else sorted({p for n in item["names"] for p in scope.rglob(n)})
   actual=next((p.resolve() for p in candidates if p.is_file() and sha(p)==item["sha256"]),None)
   if actual is None:raise ValueError("exact saved input missing "+name)
   found[name]=actual;receipt["inputs"][name]={"file":str(actual),"bytes":actual.stat().st_size,"sha256":item["sha256"]}
  for name,expected in contract["dependencies"].items():
   path=root/name if (root/name).is_file() else notes/name
   if sha(path)!=expected:raise ValueError("frozen dependency "+name)
   receipt["sources"][name]=expected
  receipt["sources"][Path(__file__).name]=sha(Path(__file__));receipt["sources"][CONTRACT]=sha(root/CONTRACT)
  helper=load_module(root/OLD_HELPER if (root/OLD_HELPER).is_file() else notes/OLD_HELPER,"r150_seven_old_recipe")
  model_module=load_module(root/MODEL_HELPER,"r150_seven_exact_model")
  found["integerModel"]=inputs/"original-integer-31h0-mod923521.txt"
  receipt["exactMod31FourModel"]=model_module.generate(found["exactInteger"],found["integerLower"],found["integerModel"])
  selector=found["selector"].read_bytes()
  if selector[:8]!=b"R150PHS1" or struct.unpack_from("<5I",selector,8)!=(31,315,15,7,9) or len(selector)!=10040:
   raise ValueError("same complete seven-source action")
  J7=[list(selector[9991+7*i:9991+7*(i+1)]) for i in range(7)]
  relation=[]
  for i in range(7):
   row=[]
   for j in range(7):
    poly=[-J7[i][j],int(i==j)]
    while poly and not poly[-1]:poly.pop()
    row.append(poly)
   relation.append(row)
  beta=relation[:2]+zero(2,7);four=relation[2:6];selected=[relation[6]]+zero(8,7)
  receipt["sevenRelationDefinition"]={"integerJ7":J7,"integerPolynomialsAscending":relation,
   "sourceOrder":["beta199","beta200","old4001","old4002","old4003","old4004","selected2"],
   "integerRelationFormula":"K3=31*kappa_beta*P+S2*P-961*z","P":"sI7-J7 using signed minus canonical J7",
   "rightHandSideCostBound":RELATION_BOUND,"provedTemporarySourceCostBound":SOURCE_BOUND}
  (results/"seven-integer-relations.json").write_text(json.dumps(receipt["sevenRelationDefinition"],indent=2)+"\n")
  def nf_family(prefix,labels,polys):
   return {"nf":found[prefix+"NF"],"q":found[prefix+"Q"],"rem":found[prefix+"Rem"],"trace":found[prefix+"Trace"],"labels":labels,"polys":polys}
  relation_families=[nf_family("beta",BETA_LABELS,beta),nf_family("four",FOUR_LABELS,four),nf_family("selected",LABEL9,selected)]
  relation_mix=inputs/"seven-relations.mix";helper.write_mix(relation_mix,LABEL7,RELATION_BOUND,relation_families)
  executables={}
  for name,(filename,flags) in PROGRAMS.items():
   source=root/filename if (root/filename).is_file() else notes/filename;executable=bins/name
   command=["timeout","--kill-after=10s",str(a.compile_seconds)+"s","prlimit","--as="+str(a.memory_mib*1048576),"--core=0","--","g++","-O3","-std=c++17","-I",str(root),"-I",str(notes)]+flags+[str(source),"-o",str(executable)]
   started=time.monotonic();proc=subprocess.run(command,capture_output=True,text=True)
   (results/("compile-"+name+".log")).write_text(proc.stdout+proc.stderr)
   receipt["compilations"][name]={"command":command,"exitCode":proc.returncode,"elapsedSeconds":time.monotonic()-started};save()
   if proc.returncode:raise RuntimeError("bounded compilation failed "+name)
   executables[name]=[str(executable)]
  executables["global"]=[sys.executable,str(root/GLOBAL)]
  if a.prepare_only:
   receipt["status"]="prepared-no-native-mathematical-stage-executed";save();return
  math_start=time.monotonic();deadline=math_start+a.math_seconds;receipt["status"]="running";save()
  def prefix(name):
   d=recovery/name;d.mkdir(exist_ok=True);return d/name
  def binding(infiles,logical,program):
   source=GLOBAL if program=="global" else PROGRAMS[program][0]
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
  def original_stage(name,labels,bound,divisor,families):
   recipe=inputs/(name+".recipe");write_original4(recipe,labels,bound,divisor,families)
   output=prefix(name);data=[found["model"],found["integerModel"]]+[f["file"] for f in families]
   logical={"bound":bound,"divisor":divisor,"targetMode":1,"labels":labels,"polynomials":[f["polys"] for f in families]}
   key=binding(data,logical,"original")
   required={"divisor":divisor,"allOriginalProductCoefficientsDivisible":True}
   if divisor==P4:required["fullOriginalSeventeenEquationIdentityMod923521"]=True
   files=[suffix(output,x) for x in ("-primitive-source-mod923521.bin","-original-seventeen-source-mod923521.bin","-original-product.json")]
   if divisor==P3:files.append(suffix(output,"-third-divided-original-rhs.bin"))
   run_stage(name,"original",[found["model"],found["integerModel"],recipe,output,key],
    "full-original-seven-saturation-product-complete",required,data,files,{**logical,"checkpointBinding":key})
   return output

  image7=image_stage("seven-relation-image",relation_mix,relation_families,RELATION_BOUND,LABEL7,True)
  source7=source_stage("seven-relation-source",image7,"source7",RELATION_BOUND,7)
  transport7=transport_stage("seven-relation-original-source",source7,relation_mix,relation_families,RELATION_BOUND)
  transport_meta=json.loads(suffix(transport7,"-original-transport.json").read_text())
  raw_bound=max([RELATION_BOUND]+transport_meta["sourceCosts"])
  if raw_bound>SOURCE_BOUND:raise ValueError("actual seven source exceeds paid184 bound")
  joint_families=[
   {"file":found["kernels"],"labels":BETA_LABELS,"polys":embed(scale(beta,31),16,0)},
   {"file":found["fourK2"],"labels":FOUR_LABELS,"polys":embed(four,16,0)},
   {"file":found["selectedK2"],"labels":LABEL9,"polys":embed(selected,16,0)},
   {"file":suffix(transport7,"-primitive-source-mod31.bin"),"labels":LABEL7,"polys":embed(identity(7,-961),16,0)},
   {"file":found["currentZ"],"labels":LABEL9,"polys":embed(identity(9),16,7)}]
  original16=original_stage("seven-and-current-original",LABEL16,raw_bound,P3,joint_families)
  original_meta=json.loads(suffix(original16,"-original-product.json").read_text())
  if not all(original_meta.get(k) is True for k in ("allOriginalProductCoefficientsDivisible","originalRowScaleTransportVerified","allWeightedBoundsVerified")):
   raise ValueError("all16 actual original identities and source scales")
  receipt["allSixteenOriginalDivisibilitiesVerified"]=True
  receipt["actualSevenRelationSourceCosts"]=original_meta["actualSourceCosts"][:7]
  receipt["actualCurrentSourceCosts"]=original_meta["actualSourceCosts"][7:]
  receipt["actualRawRightHandSideCostBound"]=raw_bound;save()
  normal16=prefix("new-sixteen-normal")
  run_stage("normal16","normal",[found["model"],suffix(original16,"-third-divided-original-rhs.bin"),normal16],
   "sixteen-augmented-first-normal-forms-complete",{"targets":16,"components":1034},
   [found["model"],suffix(original16,"-third-divided-original-rhs.bin")],
   [suffix(normal16,x) for x in ("-normal-forms.bin","-reduction.bin","-forward.bin","-backward.bin")],
   {"bound":raw_bound,"labels":LABEL16})
  if sha(suffix(normal16,"-forward.bin"))!=contract["inputs"]["forward"]["sha256"] or sha(suffix(normal16,"-backward.bin"))!=contract["inputs"]["backward"]["sha256"]:
   raise ValueError("actual original3333 prebasis DAG changed")
  receipt["sameOriginalPrebasisDAGHashesVerified"]=True
  fresh=[{"nf":suffix(normal16,"-normal-forms.bin"),"q":"-","rem":"-","trace":suffix(normal16,"-reduction.bin"),"labels":LABEL16,"polys":identity(16)}]
  fresh_mix=inputs/"new-sixteen-image.mix";helper.write_mix(fresh_mix,LABEL16,raw_bound,fresh)
  image16=image_stage("new-sixteen-image",fresh_mix,fresh,raw_bound,LABEL16,False)
  global_dir=recovery/"complete-global";global_dir.mkdir(exist_ok=True)
  global_data=[found["selector"],found["state"],suffix(original16,"-original-product.json"),suffix(image16,"-image-certificate.json"),suffix(image16,"-image-remainders.bin")]
  run_stage("complete-global","global",["--notes-root",notes,"--selector",found["selector"],
   "--image-remainders",suffix(image16,"-image-remainders.bin"),"--image-metadata",suffix(image16,"-image-certificate.json"),
   "--original-metadata",suffix(original16,"-original-product.json"),"--out",global_dir],
   "completed",{"newAugmentedFirstImageComplete":True},global_data,
   [global_dir/"complete-augmented-first-image-receipt.json",global_dir/"complete-augmented-first-image.bin.gz"],
   {"wholeOldKernel":1834,"newRelations":7,"quotientTorsion":308})
  solution=json.loads((global_dir/"complete-augmented-first-image-receipt.json").read_text())
  receipt.update(newAugmentedFirstImageComplete=True,newGlobalFirstImageRank=solution["newGlobalFirstImageRank"],
   individualTargetCompatible=solution["individualTargetCompatible"],numberOfCompatibleTargets=solution["numberOfCompatibleTargets"],
   nextTargetScope=solution["targetScope"],completeGlobalConclusion=solution);save()
  if not solution["allNineCompatible"]:
   receipt.update(status="completed",outcome="complete-augmented-first-image-fixed-fiber-obstruction",
    numberOfObstructedTargets=9-solution["numberOfCompatibleTargets"],mathematicalElapsedSeconds=time.monotonic()-math_start)
   save();return
  F=solution["newRelationSolutionPolynomialsAscending"];C=constants(solution["oldSevenCorrectionCoefficients"])
  cbeta=C[:2]+zero(2,9);cfour=C[2:6];cselected=[C[6]]+zero(8,9)
  higher_bound=raw_bound+max(0,solution["maximumSolutionDegree"])
  if higher_bound>700:raise ValueError("actual solution exceeds supported finite image degree budget")
  higher_polys=negate(F)+identity(9)
  final_families=[
   {"nf":suffix(normal16,"-normal-forms.bin"),"q":suffix(image16,"-image-quotients.bin"),"rem":suffix(image16,"-image-remainders.bin"),
    "trace":suffix(normal16,"-reduction.bin"),"labels":LABEL16,"polys":higher_polys},
   nf_family("beta",BETA_LABELS,negate(cbeta)),nf_family("four",FOUR_LABELS,negate(cfour)),nf_family("selected",LABEL9,negate(cselected))]
  final_mix=inputs/"final-nine-image.mix";helper.write_mix(final_mix,LABEL9,higher_bound,final_families)
  final_image=image_stage("final-nine-image",final_mix,final_families,higher_bound,LABEL9,True)
  final_source=source_stage("final-nine-source",final_image,"source9",higher_bound,9)
  final_transport=transport_stage("final-nine-original-source",final_source,final_mix,final_families,higher_bound)
  final_transport_meta=json.loads(suffix(final_transport,"-original-transport.json").read_text())
  paid_bound=max([higher_bound]+final_transport_meta["sourceCosts"])
  if paid_bound>higher_bound+96:raise ValueError("actual original final source exceeds paid graph bound")
  final_original_families=[
   {"file":suffix(original16,"-primitive-source-mod923521.bin"),"labels":LABEL16,"polys":F+identity(9)},
   {"file":found["kernels"],"labels":BETA_LABELS,"polys":scale(cbeta,961)},
   {"file":found["fourK2"],"labels":FOUR_LABELS,"polys":scale(cfour,31)},
   {"file":found["selectedK2"],"labels":LABEL9,"polys":scale(cselected,31)},
   {"file":suffix(final_transport,"-primitive-source-mod31.bin"),"labels":LABEL9,"polys":identity(9,29791)}]
  final_original=original_stage("final-nine-original",LABEL9,paid_bound,P4,final_original_families)
  conclusion=json.loads(suffix(final_original,"-original-product.json").read_text())
  if not all(conclusion.get(k) is True for k in ("fullOriginalSeventeenEquationIdentityMod923521","fullOriginalMacaulayIdentityMod923521","originalRowScaleTransportVerified","allWeightedBoundsVerified")):
   raise ValueError("complete actual original17 final identity")
  receipt.update(status="completed",outcome="full-original31h0-mod923521-certificate",
   fullOriginalTarget31h0Mod923521IdentityVerified=True,finite_budget_verified=True,
   actualFinalSourceCosts=conclusion["actualSourceCosts"],originalSeventeenConclusion=conclusion,
   actualFinalRightHandSideCostBound=higher_bound,mathematicalElapsedSeconds=time.monotonic()-math_start)
  save()
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
  (results/"certificate-manifest.json").write_text(json.dumps({"format":"r150-seven-saturation-lossless-certificates-v1","pipelineStatus":receipt["status"],"partialCheckpointIsNotIdentity":True,"files":files},indent=2)+"\n")
  (results/"text-recovery-manifest.json").write_text(json.dumps({"format":"r150-seven-saturation-exact-text-recovery-v1","completeStageCachesIncluded":True,"files":texts},indent=2)+"\n")
  saved=[{"file":str(p.relative_to(recovery)),"bytes":p.stat().st_size,"sha256":sha(p)} for p in sorted(recovery.rglob("*")) if p.is_file()]
  (results/"recovery-manifest.json").write_text(json.dumps({"format":"r150-seven-saturation-complete-recovery-v1","pipelineStatus":receipt["status"],"files":saved},indent=2)+"\n")
  receipt.update(recoveryFiles=len(saved),recoveryBytes=sum(p["bytes"] for p in saved),losslessGeneratedBinaryFiles=len(files));save()
  print(json.dumps({k:receipt.get(k) for k in ("status","outcome","mathematicalElapsedSeconds","newAugmentedFirstImageComplete","newGlobalFirstImageRank",
   "individualTargetCompatible","fullOriginalTarget31h0Mod923521IdentityVerified","actualFinalSourceCosts","recoveryBytes")}),flush=True)
 if receipt["status"] not in ("completed","prepared-no-native-mathematical-stage-executed"):raise SystemExit(1)
if __name__=="__main__":main()
