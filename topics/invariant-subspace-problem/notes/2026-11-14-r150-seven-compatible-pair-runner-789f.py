#!/usr/bin/env python3
"""Continue only actual compatible targets6/9, reusing all seven completed sources and quotients."""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,shutil,struct,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
CONTRACT="2026-11-14-r150-seven-compatible-pair-contract-789f.json"
OLD_HELPER="2026-11-14-r150-four-second-bockstein-runner-789f.py"
GLOBAL="2026-11-14-r150-seven-compatible-pair-analysis-789f.py"
PROGRAMS={
 "image":("2026-11-14-r150-seven-saturation-image-789f.cpp",[]),
 "source2":("2026-11-14-r150-seven-compatible-pair-source-789f.cpp",[]),
 "transport":("2026-11-14-r150-second-bockstein-all198-global-original-transport-789f.cpp",[]),
 "original":("2026-11-14-r150-seven-compatible-pair-original-789f.cpp",[])}
LABEL7=list(range(7001,7008));LABEL9=list(range(2,11));LABEL16=LABEL7+LABEL9
PAIR=[6,9];BETA_LABELS=list(range(2275,2279));FOUR_LABELS=list(range(4001,4005))
P=31;P2=961;P3=29791;P4=923521;BOUND=88
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
 for name in ("notes-root","t96-recovery","all198-recovery","seven-recovery","out"):parser.add_argument("--"+name,type=Path,required=True)
 parser.add_argument("--math-seconds",type=int,default=120);parser.add_argument("--memory-mib",type=int,default=512)
 parser.add_argument("--compile-seconds",type=int,default=30);parser.add_argument("--resume-recovery",type=Path);parser.add_argument("--prepare-only",action="store_true")
 a=parser.parse_args()
 if min(a.math_seconds,a.memory_mib,a.compile_seconds)<1:raise ValueError("explicit positive bounds")
 root=Path(__file__).resolve().parent;notes=a.notes_root.resolve();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 recovery=out/"recovery"
 if a.resume_recovery and a.resume_recovery.resolve()!=recovery:shutil.copytree(a.resume_recovery,recovery,dirs_exist_ok=True)
 results=out/"results";bins=out/"bin";inputs=recovery/"inputs";cache=recovery/"stage-cache"
 for d in (results,recovery,bins,inputs,cache):d.mkdir(parents=True,exist_ok=True)
 receipt_path=results/"seven-compatible-pair-pipeline-receipt.json"
 receipt={"format":"r150-seven-compatible-pair-full-original-continuation-v1","status":"preparing",
  "prime":31,"integerModulus":P4,"targetMultiplier":"31*h0","sourceRun":43630666145,"actualTargetLabels":PAIR,
  "wholeNineTargetIdentityClaimed":False,"otherSevenOriginalTargetsNotRecomputed":True,
  "fullOriginalPairMod923521IdentityVerified":False,"finite_budget_verified":False,"characteristicZeroIdentityAsserted":False,
  "originalSevenRelationStagesRecomputed":False,"old198OrSelectedSourcesRecomputed":False,
  "sharedMathematicalSecondsLimit":a.math_seconds,"perChildAddressSpaceMiBLimit":a.memory_mib,"perCompilationSecondsLimit":a.compile_seconds,
  "deadlineRule":"Four individually bounded compilations and fixed input SHA checks precede one shared120second mathematical clock; saved-matrix analysis plus new2 image/VQ/transport/fulloriginal share it. Actual VQ and original-product arrays checkpoint; other stages retain completed caches only. Compression follows.",
  "inputs":{},"sources":{},"compilations":{},"stages":{}}
 math_start=None
 def save():receipt_path.write_text(json.dumps(receipt,indent=2)+"\n")
 try:
  contract=json.loads((root/CONTRACT).read_text());receipt["inputContractSHA256"]=sha(root/CONTRACT)
  scopes={"notes":notes,"t96":a.t96_recovery.resolve(),"all198":a.all198_recovery.resolve(),"seven":a.seven_recovery.resolve()};found={}
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
  helper=load_module(root/OLD_HELPER if (root/OLD_HELPER).is_file() else notes/OLD_HELPER,"r150_pair_old_recipe")
  previous=json.loads(found["globalReceipt"].read_text())
  if previous.get("status")!="completed" or previous.get("newAugmentedFirstImageComplete") is not True or previous.get("individualTargetCompatible")!=[False,False,False,False,True,False,False,True,False]:raise ValueError("actual complete individual source-run flags")
  F=[[row[4],row[7]] for row in previous["newRelationSolutionPolynomialsAscending"]]
  C=constants([[row[4],row[7]] for row in previous["oldSevenCorrectionCoefficients"]])
  if F!=[zero(1,2)[0],zero(1,2)[0],[[30],[18]],zero(1,2)[0],zero(1,2)[0],zero(1,2)[0],zero(1,2)[0]]:raise ValueError("actual complete pair solution")
  select=[[([1] if j+2==target else []) for target in PAIR] for j in range(9)]
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
  executables["global"]=[sys.executable,str(root/GLOBAL)]
  if a.prepare_only:receipt["status"]="prepared-no-native-mathematical-stage-executed";save();return
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

  analysis=recovery/"saved-matrix-analysis";analysis.mkdir(exist_ok=True)
  run_stage("saved-matrix-analysis","global",["--notes-root",notes,"--receipt",found["globalReceipt"],"--system",found["globalSystem"],"--out",analysis],
   "completed",{"allNineRawNonzeroModuloU":True,"newImageEigenvalue":2},
   [found["globalReceipt"],found["globalSystem"],notes/"2026-11-14-r150-torsion-state.bin-789f.gz"],
   [analysis/"eighth-and-raw-annihilators-receipt.json",analysis/"eighth-and-raw-annihilators.bin.gz"],
   {"sourceRun":43630666145,"all315":True})
  receipt["eighthAndRawAnalysis"]=json.loads((analysis/"eighth-and-raw-annihilators-receipt.json").read_text());save()
  cbeta=C[:2]+zero(2,2);cfour=C[2:6];cselected=[C[6]]+zero(8,2)
  families=[
   {"nf":found["newNF"],"q":found["newQ"],"rem":found["newRem"],"trace":found["newTrace"],"labels":LABEL16,"polys":negate(F)+select},
   nf_family("beta",BETA_LABELS,negate(cbeta)),nf_family("four",FOUR_LABELS,negate(cfour)),nf_family("selected",LABEL9,negate(cselected))]
  mix=inputs/"compatible-pair.mix";helper.write_mix(mix,PAIR,BOUND,families)
  im=image_stage("compatible-pair-image",mix,families,BOUND,PAIR,True)
  source=source_stage("compatible-pair-source",im,"source2",BOUND,2)
  transport=transport_stage("compatible-pair-original-source",source,mix,families,BOUND)
  tm=json.loads(suffix(transport,"-original-transport.json").read_text())
  paid=max([BOUND]+tm["sourceCosts"])
  if paid>BOUND+96:raise ValueError("actual pair source cost exceeds original graph bound")
  original_families=[
   {"file":found["newOriginal"],"labels":LABEL16,"polys":F+select},
   {"file":found["kernels"],"labels":BETA_LABELS,"polys":scale(cbeta,961)},
   {"file":found["fourK2"],"labels":FOUR_LABELS,"polys":scale(cfour,31)},
   {"file":found["selectedK2"],"labels":LABEL9,"polys":scale(cselected,31)},
   {"file":suffix(transport,"-primitive-source-mod31.bin"),"labels":PAIR,"polys":identity(2,29791)}]
  original=original_stage("compatible-pair-original",PAIR,paid,P4,original_families)
  conclusion=json.loads(suffix(original,"-original-product.json").read_text())
  if conclusion.get("targetCount")!=2 or not all(conclusion.get(k) is True for k in ("fullOriginalSeventeenEquationIdentityMod923521","fullOriginalMacaulayIdentityMod923521","originalRowScaleTransportVerified","allWeightedBoundsVerified")):raise ValueError("complete actual original17 pair identity")
  receipt.update(status="completed",outcome="targets6-and9-full-original31h0-mod923521-certificate",
   fullOriginalPairMod923521IdentityVerified=True,finite_budget_verified=True,actualFinalSourceCosts=conclusion["actualSourceCosts"],
   originalSeventeenConclusion=conclusion,mathematicalElapsedSeconds=time.monotonic()-math_start);save()
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
  (results/"certificate-manifest.json").write_text(json.dumps({"format":"r150-seven-compatible-pair-lossless-certificates-v1","pipelineStatus":receipt["status"],"partialCheckpointIsNotIdentity":True,"files":files},indent=2)+"\n")
  (results/"text-recovery-manifest.json").write_text(json.dumps({"format":"r150-seven-compatible-pair-exact-text-recovery-v1","completeStageCachesIncluded":True,"files":texts},indent=2)+"\n")
  saved=[{"file":str(p.relative_to(recovery)),"bytes":p.stat().st_size,"sha256":sha(p)} for p in sorted(recovery.rglob("*")) if p.is_file()]
  (results/"recovery-manifest.json").write_text(json.dumps({"format":"r150-seven-compatible-pair-complete-recovery-v1","pipelineStatus":receipt["status"],"files":saved},indent=2)+"\n")
  receipt.update(recoveryFiles=len(saved),recoveryBytes=sum(p["bytes"] for p in saved),losslessGeneratedBinaryFiles=len(files));save()
  print(json.dumps({k:receipt.get(k) for k in ("status","outcome","mathematicalElapsedSeconds","actualTargetLabels","fullOriginalPairMod923521IdentityVerified","actualFinalSourceCosts","recoveryBytes")}),flush=True)
 if receipt["status"] not in ("completed","prepared-no-native-mathematical-stage-executed"):raise SystemExit(1)
if __name__=="__main__":main()
