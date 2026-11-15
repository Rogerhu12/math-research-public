#!/usr/bin/env python3
"""Bounded complete second page of the original S2 source envelope.
All204 true integer second sources and the complete next source kernel are saved.
The next third/global continuation is explicit, never confused with this page.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,shutil,struct,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
CONTRACT="2026-11-15-r150-saturated-second-page-contract-789f.json"
NATIVE={
 "vq":"2026-11-15-r150-saturated-local-vq-789f.cpp",
 "transport":"2026-11-15-r150-saturated-local-original-transport-789f.cpp",
 "integer":"2026-11-15-r150-saturated-integer-jets-789f.cpp",
 "normal":"2026-11-15-r150-saturated-local-normal-789f.cpp"}
PYTHON={
 "matrix":"2026-11-15-r150-saturated-second-page-matrices-789f.py",
 "solve":"2026-11-15-r150-saturated-local-unit-solve-789f.py"}
P=31;P2=961;P3=29791;P4=923521;P5=28629151;P6=887503681
TARGETS=list(range(2,11));LABEL7=list(range(7001,7008));LABEL16=LABEL7+TARGETS
NEW198=list(range(15001,15199));OLD6=[7001,7002,7005,7006,7007,7004];ALL204=OLD6+NEW198
def sha(path):
 h=hashlib.sha256()
 with Path(path).open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return h.hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def suffix(path,s):return Path(str(path)+s)
def atomic_json(path,x):
 tmp=path.with_name(path.name+".tmp");tmp.write_text(json.dumps(x,separators=(",",":"))+"\n");os.replace(tmp,path)
def write_mix(path,labels,L,exponents,families):
 lines=["R150_S2_INTEGER_JET_MIX_V1",f"{len(labels)} {L} {len(families)}"," ".join(map(str,exponents))]
 for f in families:
  lines.append(str(f["file"])+" "+str(len(f["labels"]))+" "+str(len(f["edges"])))
  lines.append(" ".join(map(str,f["labels"])))
  for source,target,poly in f["edges"]:
   p=[int(x)%P6 for x in poly]
   while p and not p[-1]:p.pop()
   if not p:raise ValueError("zero sparse source edge should be omitted")
   lines.append(" ".join(map(str,[source,target,len(p)]+p)))
 path.write_text("\n".join(lines)+"\n")
 return [{"inputSHA256":sha(f["file"]),"labels":f["labels"],"edges":f["edges"]} for f in families]
def identity_edges(n,offset=0,scale=1):return [[j,j+offset,[scale]] for j in range(n)]
def main():
 p=argparse.ArgumentParser()
 for k in ("notes-root","t96-recovery","all198-recovery","seven-recovery","current-recovery","ninth-recovery","old200-recovery","third197-recovery","selector-receipt","out"):p.add_argument("--"+k,type=Path,required=True)
 p.add_argument("--five-recovery",type=Path,default=None)
 p.add_argument("--math-seconds",type=float,default=300);p.add_argument("--memory-mib",type=int,default=512);p.add_argument("--compile-seconds",type=int,default=30)
 p.add_argument("--resume-recovery",type=Path);p.add_argument("--prepare-only",action="store_true")
 a=p.parse_args()
 if min(a.math_seconds,a.memory_mib,a.compile_seconds)<=0:raise ValueError("positive explicit bounded execution")
 root=Path(__file__).resolve().parent;notes=a.notes_root.resolve();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 results=out/"results";recovery=out/"recovery";bins=out/"bin"
 if a.resume_recovery and a.resume_recovery.resolve()!=recovery:shutil.copytree(a.resume_recovery,recovery,dirs_exist_ok=True)
 for d in (results,recovery,bins,recovery/"inputs",recovery/"stage-cache"):d.mkdir(parents=True,exist_ok=True)
 cache=recovery/"stage-cache";inputs=recovery/"inputs"
 receipt_path=results/"saturated-second-page-pipeline-receipt.json"
 receipt={"format":"r150-saturated-second-page-continuous-source-v1","status":"preparing","prime":31,
  "nativeModulus":P6,"targetMultiplier":"31^2*h0","targetLabels":TARGETS,
  "originalS2EnvelopeComplete":True,"old197ThirdRunRecomputed":False,"oldSelectorRecomputed":False,
  "all204TrueOriginalSecondSourcesComputed":False,"completeRelevantSaturatedSecondImageComputed":False,
  "completeNextPolynomialSourceKernelSaved":False,"completeRelevantSaturatedThirdImageComputed":False,
  "globalAllOriginalSourceMod31SixDecisionComputed":False,"characteristicZeroIdentityAsserted":False,
  "allCompatibleTargetsOriginalIdentityVerified":False,"fullOriginalAllNineMod887503681IdentityVerified":False,
  "finitePositiveSourceBudgetsVerified":False,"finite_budget_verified":False,
  "individualTargetCompatible":[False]*9,"compatibleTargetLabels":[],"completedOriginalTargetLabels":[],
  "secondPageInsufficientTargetLabels":[],"actualFinalSourceCostsBySlot":[-1]*9,
  "sharedMathematicalSecondsLimit":a.math_seconds,"perChildAddressSpaceMiBLimit":a.memory_mib,
  "perCompilationSecondsLimit":a.compile_seconds,"nativeCompilations":4,
  "localRoot":2,"precisionChain":[20,15,10,5],
  "deadlineRule":"Four native compilations precede a single shared mathematical deadline. Actual source arrays and original-product row prefixes checkpoint. All204 second sources and their effective ten jets are retained for the next third page. Artifact compression follows the mathematical clock.",
  "inputs":{},"sources":{},"compilations":{},"stages":{}}
 started=None
 def save():atomic_json(receipt_path,receipt)
 try:
  contract=json.loads((root/CONTRACT).read_text());receipt["inputContractSHA256"]=sha(root/CONTRACT)
  scopes={"notes":notes,"t96":a.t96_recovery.resolve(),"all198":a.all198_recovery.resolve(),
   "seven":a.seven_recovery.resolve(),"current":a.current_recovery.resolve(),"ninth":a.ninth_recovery.resolve(),
   "old200":a.old200_recovery.resolve(),"third197":a.third197_recovery.resolve()}
  found={}
  for name,item in contract["inputs"].items():
   scope=scopes[item["scope"]]
   candidates=[a.selector_receipt.resolve()] if name=="selectorReceipt" else ([scope/item["relative"]] if "relative" in item else sorted({q for n in item["names"] for q in scope.rglob(n)}))
   q=next((x.resolve() for x in candidates if x.is_file() and ("bytes" not in item or x.stat().st_size==item["bytes"]) and sha(x)==item["sha256"]),None)
   if q is None:raise ValueError("exact saved input missing "+name)
   found[name]=q;receipt["inputs"][name]={"file":str(q),"bytes":q.stat().st_size,"sha256":item["sha256"]}
  for name,expected in contract["dependencies"].items():
   q=root/name if (root/name).is_file() else notes/name
   if sha(q)!=expected:raise ValueError("frozen source dependency "+name)
   receipt["sources"][name]=expected
  receipt["sources"][Path(__file__).name]=sha(Path(__file__));receipt["sources"][CONTRACT]=sha(root/CONTRACT)
  for key in ("currentK4OriginalReceipt","ninthIntegerModelReceipt"):
   if json.loads(found[key].read_text()).get("status")!="completed":raise ValueError("actual paid source receipt "+key)
  model_receipt=json.loads(found["ninthIntegerModelReceipt"].read_text())
  if model_receipt.get("modulus")!=P6 or model_receipt.get("modelSHA256")!=sha(found["ninthIntegerModel"]) or not all(model_receipt.get(k) for k in ("all4433OriginalEquationResiduesVerified","all18OriginalRowScaleResiduesVerified")):raise ValueError("same original integer model")
  with found["oldK"].open("rb") as f:data=f.read(24+200*16)
  if data[:8]!=b"R150KK31" or struct.unpack_from("<4I",data,8)!=(31,6188,200,85):raise ValueError("same original K200 source family")
  oldlabels=[struct.unpack_from("<IHHII",data,24+16*j)[1] for j in range(200)];labels197=oldlabels[1:198]
  rem=found["oldRem"].read_bytes();offset=20
  if rem[:8]!=b"R150NF31" or struct.unpack_from("<3I",rem,8)!=(0,200,1034):raise ValueError("complete old global K200 image remainders")
  for j in range(200):
   raw,label,count=struct.unpack_from("<IHI",rem,offset);offset+=10
   if raw or label!=oldlabels[j] or (j<198 and count):raise ValueError("paid first198 global first-image zero")
   for _ in range(count):_,length=struct.unpack_from("<HB",rem,offset);offset+=3+length
  if offset!=len(rem):raise ValueError("whole old200 image remainder")
  receipt["first198SavedGlobalFirstRemaindersExactlyZero"]=True
  programs={}
  for key,filename in NATIVE.items():
   q=root/filename;exe=bins/key;command=["timeout","--kill-after=10s",str(a.compile_seconds)+"s","prlimit","--as="+str(a.memory_mib*1048576),"--core=0","--","g++","-O3","-std=c++17","-I",str(root),"-I",str(notes),str(q),"-o",str(exe)]
   began=time.monotonic();r=subprocess.run(command,capture_output=True,text=True);(results/("compile-"+key+".log")).write_text(r.stdout+r.stderr)
   receipt["compilations"][key]={"command":command,"exitCode":r.returncode,"elapsedSeconds":time.monotonic()-began};save()
   if r.returncode:raise RuntimeError("bounded compilation failed "+key)
   programs[key]=[str(exe)]
  for key,filename in PYTHON.items():programs[key]=[sys.executable,str(root/filename)]
  if a.prepare_only:receipt["status"]="prepared-no-mathematical-stage-executed";save();return
  started=time.monotonic();deadline=started+a.math_seconds
  mathematical_sources={k:v for k,v in receipt["sources"].items() if k.endswith((".hpp",".cpp")) or k in PYTHON.values()}
  binding=digest({"version":"r150-saturated-second-source-chain-v1","inputs":{k:v["sha256"] for k,v in receipt["inputs"].items()},"mathematicalSources":mathematical_sources,"labels197":labels197,"root":2,"precision":[20,15,10,5]})
  receipt.update(status="running",localInputBindingSHA256=binding);save()
  def prefix(name):
   d=recovery/name;d.mkdir(exist_ok=True);return d/name
  def run(name,program,args,marker,required,infiles,outfiles,logical):
   filename=NATIVE[program] if program in NATIVE else PYTHON[program]
   key=digest({"inputs":[sha(x) for x in infiles],"logical":logical,"source":receipt["sources"][filename],"headers":{k:v for k,v in receipt["sources"].items() if k.endswith(".hpp")}})
   cp=cache/(name+".json")
   if cp.exists():
    old=json.loads(cp.read_text())
    if old.get("inputBindingSHA256")==key and all(x.is_file() and sha(x)==old.get("outputs",{}).get(str(x.relative_to(recovery))) for x in outfiles):
     receipt["stages"][name]={"status":"completed","reusedCompletedActualStage":True,"inputBindingSHA256":key,"nativeStatistics":old["nativeStatistics"],"elapsedSeconds":0};save();return
   remaining=deadline-time.monotonic()
   if remaining<=0:raise TimeoutError("shared mathematical deadline before "+name)
   actual=[max(0.001,remaining-0.2) if x=="__REMAINING__" else x for x in args]
   command=["timeout","--kill-after=10s",f"{remaining:.3f}s","prlimit","--as="+str(a.memory_mib*1048576),"--core=0","--"]+programs[program]+list(map(str,actual))
   stage={"status":"running","inputBindingSHA256":key,"command":command,"remainingSecondsAtStart":remaining};receipt["stages"][name]=stage;save();begin=time.monotonic();events=[]
   proc=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
   with (results/(name+".log")).open("w") as log:
    for line in proc.stdout:
     log.write(line);log.flush();print(line,end="",flush=True)
     try:event=json.loads(line);events.append(event);stage["lastProgress"]=event;save()
     except (ValueError,TypeError):pass
   code=proc.wait();last=events[-1] if events else {}
   ok=code==0 and last.get("status")==marker and all(last.get(k)==v for k,v in required.items()) and all(x.is_file() for x in outfiles)
   stage.update(status="completed" if ok else "failed-or-incomplete",exitCode=code,elapsedSeconds=time.monotonic()-begin,nativeStatistics=last)
   receipt["mathematicalElapsedSeconds"]=time.monotonic()-started;save()
   if not ok:raise RuntimeError("actual stage incomplete "+name)
   atomic_json(cp,{"inputBindingSHA256":key,"nativeStatistics":last,"outputs":{str(x.relative_to(recovery)):sha(x) for x in outfiles}})
  prepdir=recovery/"prepared-second";prepdir.mkdir(exist_ok=True);prep=prepdir/"prepared-saturated-second-receipt.json";prepsys=prepdir/"prepared-saturated-second.bin.gz"
  prepkeys=["prepared197Receipt","prepared197System","complete197Receipt","complete197System","selectorReceipt"]
  prepflags=["prepared197-receipt","prepared197-system","complete197-receipt","complete197-system","selector-receipt"]
  args=["--mode","prepare","--notes-root",notes,"--out",prepdir]
  for key,flag in zip(prepkeys,prepflags):args+=["--"+flag,found[key]]
  specs=[prepdir/(x+".spec") for x in ("q1-q2-root2-20","q3-root2-15","all204-root2-15","all204-state-crt8")]
  run("saved-saturated-source-preparation","matrix",args,"completed",{"complete204SourceKernelGenerationProved":True,"all198TrueSevenCorrectionsVerified":True},[found[k] for k in prepkeys]+[found["state"]],[prep,prepsys]+specs,{"savedDataOnly":True,"sourceCount":204})
  prepared=json.loads(prep.read_text());receipt["savedSourcePreparation"]=prepared;save()
  spec20,spec15,spec204,spec8=specs
  def vq(name,mode,specfile,Q,V,comparison):
   q=prefix(name);run(name,"vq",[found["model"],V,Q,found["oldK"],comparison,q,binding,mode,specfile],
    "saturated-runtime-jet-VQ-complete",{"mode":mode},
    [found["model"],V,Q,found["oldK"],specfile]+([] if str(comparison)=="-" else [comparison]),
    [suffix(q,x) for x in ("-original2195-source-jets.bin","-vq.json")]+([suffix(q,"-actual-G-root2.bin"),suffix(q,"-actual-V-root2.bin")] if mode=="q1" else []),
    {"pipelineBinding":binding,"mode":mode})
   return q
  def transport(name,mode,specfile,C,trace,comparison):
   q=prefix(name);args=[found["model"],found["oldK"],suffix(C,"-original2195-source-jets.bin"),found["normalTrace"],trace,found["forward"],found["backward"],q,binding,mode,comparison,specfile,q.parent/"checkpoints","__REMAINING__"]
   run(name,"transport",args,"runtime-local-original-source-transport-complete",{"mode":mode},
    [found[k] for k in ("model","oldK","normalTrace","forward","backward")]+[suffix(C,"-original2195-source-jets.bin"),trace,specfile]+([] if str(comparison)=="-" else [comparison]),
    [suffix(q,"-original6188-q-jets.bin"),suffix(q,"-transport.json")],{"pipelineBinding":binding,"mode":mode})
   return q
  def integer(name,specfile,L,labels,exponents,retained,families,comparison="-"):
   q=prefix(name);recipe=inputs/(name+".recipe");semantic=write_mix(recipe,labels,L,exponents,families)
   run(name,"integer",[found["model"],found["ninthIntegerModel"],specfile,recipe,q,binding,comparison,retained,"__REMAINING__"],
    "saturated-original-integer-jets-complete",{"allOriginal17CoefficientsDivisible":True,"targetCount":len(labels),"computedTaylorPrecision":L,"retainedFormalPrecision":retained},
    [found["model"],found["ninthIntegerModel"],specfile]+[f["file"] for f in families]+([] if str(comparison)=="-" else [comparison]),
    [suffix(q,x) for x in ("-original6188-integer-jets.bin","-divided-original-jets.bin","-field-root2-jets.bin","-field-projected-crt8-jets.bin","-integer-product.json")],
    {"pipelineBinding":binding,"divisors":exponents,"retained":retained,"families":semantic})
   return q
  def normal(name,specfile,field,crt=False):
   q=prefix(name);run(name,"normal",[found["model"],field,found["graph"],specfile,q,binding],
    "saturated-runtime-two-ring-state-complete" if crt else "saturated-runtime-root2-normal-form-complete",{},
    [found["model"],field,found["graph"],specfile],
    [suffix(q,"-standard-state.bin" if crt else "-original1034-root2.bin"),suffix(q,"-local-prebasis-source-jets.bin"),suffix(q,"-local-normal.json")],
    {"pipelineBinding":binding,"CRT8":crt})
   return q
  def solve(name,G,NF,fixed=None):
   q=recovery/name;q.mkdir(exist_ok=True);args=["--G",G,"--rhs",suffix(NF,"-original1034-root2.bin"),"--binding",binding,"--notes-root",notes,"--out",q,"--remaining-seconds","__REMAINING__"]
   if fixed:args+=["--fixed-prefix-q",fixed]
   run(name,"solve",args,"saturated-local-unit-solve-complete",{"fullOriginalGIdentityVerified":True,"all13FreeConditionsRetained":True},
    [G,suffix(NF,"-original1034-root2.bin")]+([fixed] if fixed else []),
    [q/"complete-G-q-root2.bin",q/"local-unit-solve-receipt.json"],{"pipelineBinding":binding,"fixedOldFive":bool(fixed)})
   return q/"complete-G-q-root2.bin"
  def fam(file,labels,edges):return {"file":file,"labels":labels,"edges":[e for e in edges if any(int(x)%P6 for x in e[2])]}
  def seven_families(C,exponent):
   n=len(C[0]);families=[]
   for key,labels,indices in [("kernels",[2275,2276,2277,2278],[(0,0),(1,1)]),
      ("fourK2",[4001,4002,4003,4004],[(0,2),(1,3),(2,4),(3,5)]),
      ("selectedK2",TARGETS,[(0,6)])]:
    edges=[]
    for source,i in indices:
     ei=1 if i<2 else 2
     for j in range(n):
      if C[i][j]:edges.append([source,j,[-(31**(exponent-ei))*C[i][j]]])
    families.append(fam(found[key],labels,edges))
   return families
  q1=vq("q1-twenty-vq","q1",spec20,found["oldQ"],found["graph"],found["paidQ1Ten2195"])
  q1raw=transport("q1-twenty-original","q1",spec20,q1,found["oldTrace"],found["paidQ1Ten6188"])
  G=suffix(q1,"-actual-G-root2.bin");V=suffix(q1,"-actual-V-root2.bin")
  C7=prepared["trueSevenCancellation197"]
  fs=[fam(found["oldK"],oldlabels,[[j,j-1,[1]] for j in range(1,198)]),
      fam(suffix(q1raw,"-original6188-q-jets.bin"),labels197,identity_edges(197,scale=-P))]+seven_families(C7,2)
  L2=integer("true-L2-twenty",spec20,20,labels197,[2]*197,20,fs,found["paidTten"])
  NF2=normal("L2-normal-twenty",spec20,suffix(L2,"-field-root2-jets.bin"))
  Q2=solve("q2-complete-twenty",G,NF2,found["paidQ2Ten"])
  q2=vq("q2-twenty-vq","q2",spec20,Q2,V,"-")
  q2raw=transport("q2-twenty-original","q2",spec20,q2,suffix(NF2,"-local-prebasis-source-jets.bin"),"-")
  L3=integer("true-L3-twenty",spec20,20,labels197,[3]*197,15,
   [fam(suffix(L2,"-original6188-integer-jets.bin"),labels197,identity_edges(197)),
    fam(suffix(q2raw,"-original6188-q-jets.bin"),labels197,identity_edges(197,scale=-P2))],found["paidD3five"])
  alpha=prepared["omegaAlphaB8"];beta=prepared["omegaBetaD2"];edgesL3=[];edges8=[]
  for k in range(196):
   edgesL3.append([k+1,k,[1]])
   if beta[k]:edgesL3.append([0,k,[-beta[k]]])
   if alpha[k]:edges8.append([2,k,[-alpha[k]]])
  edges8.append([2,196,[0,1]]);edgesL3.append([0,197,[0,1]])
  fs=[fam(suffix(L3,"-original6188-integer-jets.bin"),labels197,edgesL3),
      fam(found["newOriginal"],LABEL16,edges8)]+seven_families(prepared["trueSevenCancellation198"],3)
  M3=integer("true-198-next-relations",spec15,15,NEW198,[3]*198,15,fs)
  NF3=normal("next-relations-normal-fifteen",spec15,suffix(M3,"-field-root2-jets.bin"))
  Q3=solve("q3-complete-fifteen",G,NF3)
  q3=vq("q3-fifteen-vq","q3",spec15,Q3,V,"-")
  q3raw=transport("q3-fifteen-original","q3",spec15,q3,suffix(NF3,"-local-prebasis-source-jets.bin"),"-")
  fs=[fam(suffix(M3,"-original6188-integer-jets.bin"),NEW198,identity_edges(198,offset=6)),
      fam(suffix(q3raw,"-original6188-q-jets.bin"),NEW198,identity_edges(198,offset=6,scale=-P3)),
      fam(found["currentK4Original"],LABEL7,[[source,j,[1]] for j,source in enumerate([0,1,4,5,6,3])])]
  L4=integer("all204-genuine-second-sources",spec204,15,ALL204,[4]*204,10,fs)
  NF4=normal("all204-second-local-state",spec8,suffix(L4,"-field-projected-crt8-jets.bin"),True)
  comp=recovery/"complete-second";comp.mkdir(exist_ok=True)
  args=["--mode","complete","--notes-root",notes,"--out",comp,"--prepared-receipt",prep,"--prepared-system",prepsys,
   "--original-metadata",suffix(L4,"-integer-product.json"),"--normal-metadata",suffix(NF4,"-local-normal.json"),
   "--map",found["jetMap"],"--map-receipt",found["jetMapReceipt"],"--standard-state",suffix(NF4,"-standard-state.bin")]
  run("complete-saturated-second-page","matrix",args,"completed",
   {"all204TrueOriginalSecondSourcesComputed":True,"completeRelevantSaturatedSecondImageComputed":True,"completeNextPolynomialSourceKernelSaved":True},
   [prep,prepsys,suffix(L4,"-integer-product.json"),suffix(NF4,"-local-normal.json"),found["jetMap"],found["jetMapReceipt"],suffix(NF4,"-standard-state.bin")],
   [comp/"complete-saturated-second-page-receipt.json",comp/"complete-saturated-second.bin.gz",comp/"complete-next-source-kernel.json"],
   {"all204":True,"fullSourceKernelNotOnlyImage":True})
  final=json.loads((comp/"complete-saturated-second-page-receipt.json").read_text())
  receipt["completeSecondConclusion"]=final
  for k in ("all204TrueOriginalSecondSourcesComputed","completeRelevantSaturatedSecondImageComputed","completeNextPolynomialSourceKernelSaved",
   "individualTargetCompatible","compatibleTargetLabels","secondPageInsufficientTargetLabels","secondImageRank","sourceKernelGeneratorCount","outcome"):receipt[k]=final[k]
  receipt.update(status="completed",mathematicalElapsedSeconds=time.monotonic()-started)
  receipt["continuationRequired"]="Restore selected global positive sources if any; otherwise and for unresolved targets compute the complete third page from the saved204 actual sources and complete next kernel. Neither branch stops the overall research."
  save()
 except Exception as e:
  receipt.update(status="failed-or-incomplete",errorType=type(e).__name__,error=str(e))
  if started is not None:receipt["mathematicalElapsedSeconds"]=time.monotonic()-started
  save()
 finally:
  certificates=results/"certificates";certificates.mkdir(exist_ok=True);files=[];texts=[]
  for q in sorted(recovery.rglob("*")):
   if not q.is_file():continue
   relative=q.relative_to(recovery);flat=str(relative).replace("/","__")
   if q.suffix in (".json",".mix",".recipe",".txt",".spec") and q.stat().st_size<=1_000_000:
    dest=results/flat;shutil.copyfile(q,dest);texts.append({"originalFile":str(relative),"file":dest.name,"bytes":q.stat().st_size,"sha256":sha(q)});continue
   temporary=results/(flat+".gz.tmp")
   with q.open("rb") as src,temporary.open("wb") as dst:
    with gzip.GzipFile(filename="",mode="wb",fileobj=dst,mtime=0) as gz:shutil.copyfileobj(src,gz)
   item={"originalFile":str(relative),"uncompressedBytes":q.stat().st_size,"uncompressedSHA256":sha(q),
    "compressedBytes":temporary.stat().st_size,"compressedSHA256":sha(temporary),"parts":[]}
   with temporary.open("rb") as src:
    part=1
    while data:=src.read(4_500_000):
     dest=certificates/(flat+".gz" if item["compressedBytes"]<=4_500_000 else flat+f".gz.part{part:03d}")
     dest.write_bytes(data);item["parts"].append({"file":str(dest.relative_to(results)),"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()});part+=1
   temporary.unlink();files.append(item)
  atomic_json(results/"certificate-manifest.json",{"format":"r150-saturated-second-lossless-certificates-v1","pipelineStatus":receipt["status"],"partialCheckpointIsNotIdentity":True,"files":files})
  atomic_json(results/"text-recovery-manifest.json",{"format":"r150-saturated-second-exact-text-recovery-v1","completeStageCachesIncluded":True,"files":texts})
  saved=[{"file":str(q.relative_to(recovery)),"bytes":q.stat().st_size,"sha256":sha(q)} for q in sorted(recovery.rglob("*")) if q.is_file()]
  atomic_json(results/"recovery-manifest.json",{"format":"r150-saturated-second-complete-recovery-v1","pipelineStatus":receipt["status"],"files":saved})
  receipt.update(recoveryFiles=len(saved),recoveryBytes=sum(x["bytes"] for x in saved),losslessGeneratedBinaryFiles=len(files));save()
  print(json.dumps({k:receipt.get(k) for k in ("status","outcome","mathematicalElapsedSeconds","secondImageRank","individualTargetCompatible","completeRelevantSaturatedSecondImageComputed","completeNextPolynomialSourceKernelSaved","completeRelevantSaturatedThirdImageComputed","recoveryBytes")}),flush=True)
 if receipt["status"] not in ("completed","prepared-no-mathematical-stage-executed"):raise SystemExit(1)
if __name__=="__main__":main()
