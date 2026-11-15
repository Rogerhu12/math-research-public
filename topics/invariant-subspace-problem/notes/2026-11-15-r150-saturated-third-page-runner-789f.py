#!/usr/bin/env python3
"""Complete third continuation from paid all204 integer second sources.
No prior q1/q2/q3 or second image is rerun. Full source carry is retained.
Local positive targets still require global original-source restoration.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,shutil,struct,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
CONTRACT="2026-11-15-r150-saturated-third-page-contract-789f.json"
NATIVE={
 "vq":"2026-11-15-r150-saturated-local-vq-789f.cpp",
 "transport":"2026-11-15-r150-saturated-local-original-transport-789f.cpp",
 "integer":"2026-11-15-r150-saturated-integer-jets-789f.cpp",
 "normal":"2026-11-15-r150-saturated-local-normal-789f.cpp"}
PYTHON={
 "matrix":"2026-11-15-r150-saturated-third-page-matrices-789f.py",
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
 for k in ("notes-root","t96-recovery","all198-recovery","seven-recovery","ninth-recovery","old200-recovery","second-recovery","out"):p.add_argument("--"+k,type=Path,required=True)
 p.add_argument("--math-seconds",type=float,default=300);p.add_argument("--memory-mib",type=int,default=512);p.add_argument("--compile-seconds",type=int,default=30)
 p.add_argument("--resume-recovery",type=Path);p.add_argument("--prepare-only",action="store_true")
 a=p.parse_args()
 if min(a.math_seconds,a.memory_mib,a.compile_seconds)<=0:raise ValueError("positive explicit bounded execution")
 root=Path(__file__).resolve().parent;notes=a.notes_root.resolve();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 results=out/"results";recovery=out/"recovery";bins=out/"bin"
 if a.resume_recovery and a.resume_recovery.resolve()!=recovery:shutil.copytree(a.resume_recovery,recovery,dirs_exist_ok=True)
 for d in (results,recovery,bins,recovery/"inputs",recovery/"stage-cache"):d.mkdir(parents=True,exist_ok=True)
 cache=recovery/"stage-cache";inputs=recovery/"inputs"
 receipt_path=results/"saturated-third-page-pipeline-receipt.json"
 receipt={"format":"r150-saturated-third-page-continuous-source-v1","status":"preparing","prime":31,
  "nativeModulus":P6,"targetMultiplier":"31^2*h0","targetLabels":TARGETS,
  "originalS2EnvelopeComplete":True,"oldSecondPageRecomputed":False,"oldQ1Q2Q3Recomputed":False,
  "allTrueOriginalThirdSourcesComputed":False,"completeRelevantSaturatedSecondImageReused":False,
  "completeRelevantSaturatedThirdImageComputed":False,"completeOriginalS2SourceCoverageRetained":False,
  "globalAllOriginalSourceMod31SixObstructionVerified":False,"globalAllOriginalSourceMod31SixDecisionComputed":False,
  "characteristicZeroIdentityAsserted":False,"allCompatibleTargetsOriginalIdentityVerified":False,
  "fullOriginalAllNineMod887503681IdentityVerified":False,"finitePositiveSourceBudgetsVerified":False,"finite_budget_verified":False,
  "individualTargetCompatible":[False]*9,"compatibleTargetLabels":[],"originalMod31SixObstructedTargetLabels":[],
  "completedOriginalTargetLabels":[],"actualFinalSourceCostsBySlot":[-1]*9,
  "sharedMathematicalSecondsLimit":a.math_seconds,"perChildAddressSpaceMiBLimit":a.memory_mib,
  "perCompilationSecondsLimit":a.compile_seconds,"nativeCompilations":4,"localRoot":2,"precisionChain":[10,5],
  "deadlineRule":"Four unchanged native compilations precede one shared mathematical deadline. Reuse the actual completed second sources; compute only their complete next kernel, q4, and original p5 products. Save real source arrays, original product prefixes and every stage cache. Lossless compression level1 follows the mathematical clock.",
  "gzipCompressionLevel":1,"inputs":{},"sources":{},"compilations":{},"stages":{}}
 started=None
 def save():atomic_json(receipt_path,receipt)
 try:
  contract=json.loads((root/CONTRACT).read_text());receipt["inputContractSHA256"]=sha(root/CONTRACT)
  scopes={"notes":notes,"t96":a.t96_recovery.resolve(),"all198":a.all198_recovery.resolve(),
   "seven":a.seven_recovery.resolve(),"ninth":a.ninth_recovery.resolve(),
   "old200":a.old200_recovery.resolve(),"second":a.second_recovery.resolve()}
  found={}
  for name,item in contract["inputs"].items():
   scope=scopes[item["scope"]]
   candidates=[scope/item["relative"]] if "relative" in item else sorted({q for n in item["names"] for q in scope.rglob(n)})
   q=next((x.resolve() for x in candidates if x.is_file() and ("bytes" not in item or x.stat().st_size==item["bytes"]) and sha(x)==item["sha256"]),None)
   if q is None:raise ValueError("exact saved input missing "+name)
   found[name]=q;receipt["inputs"][name]={"file":str(q),"bytes":q.stat().st_size,"sha256":item["sha256"]}
  for name,expected in contract["dependencies"].items():
   q=root/name if (root/name).is_file() else notes/name
   if sha(q)!=expected:raise ValueError("frozen source dependency "+name)
   receipt["sources"][name]=expected
  receipt["sources"][Path(__file__).name]=sha(Path(__file__));receipt["sources"][CONTRACT]=sha(root/CONTRACT)
  model_receipt=json.loads(found["ninthIntegerModelReceipt"].read_text())
  if model_receipt.get("status")!="completed" or model_receipt.get("modulus")!=P6 or model_receipt.get("modelSHA256")!=sha(found["ninthIntegerModel"]) or not all(model_receipt.get(k) for k in ("all4433OriginalEquationResiduesVerified","all18OriginalRowScaleResiduesVerified")):raise ValueError("same original integer model")
  with found["Gcache"].open("rb") as f:ghead=f.read(88)
  with found["Vcache"].open("rb") as f:vhead=f.read(92)
  if ghead[:8]!=b"R150SG31" or struct.unpack_from("<4I",ghead,8)!=(31,1034,1021,20):raise ValueError("actual completed twenty-term G cache")
  if vhead[:8]!=b"R150SV31" or struct.unpack_from("<5I",vhead,8)!=(31,1034,1021,2195,20):raise ValueError("actual completed twenty-term V cache")
  binding=ghead[24:88].decode("ascii")
  if len(binding)!=64 or any(c not in "0123456789abcdef" for c in binding) or vhead[28:92].decode("ascii")!=binding:raise ValueError("same saved G/V data-lineage binding")
  secprep=json.loads(found["secondPreparedReceipt"].read_text());labels197=secprep["sourceLabels197"]
  if len(labels197)!=197:raise ValueError("actual original K2..K198 label dictionary")
  for key,labels,exp,prec,ret in [("secondL4ProductReceipt",ALL204,4,15,10),("secondL3ProductReceipt",labels197,3,20,15)]:
   old=json.loads(found[key].read_text())
   if old.get("status")!="completed" or old.get("targetLabels")!=labels or old.get("divisorExponents")!=[exp]*len(labels) or old.get("computedTaylorPrecision")!=prec or old.get("retainedFormalPrecision")!=ret or old.get("bindingSHA256")!=binding or not all(old.get(k) for k in ("allOriginal17CoefficientsDivisible","originalRowScaleTransportVerified","allOriginalIntegerSourceJetsSaved","allDividedIntegerJetsSaved")):raise ValueError("actual completed second-chain original product "+key)
  receipt["nativeDataLineageBindingSHA256"]=binding
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
  continuationBinding=digest({"version":"r150-saturated-third-source-chain-v1","inputs":{k:v["sha256"] for k,v in receipt["inputs"].items()},"mathematicalSources":mathematical_sources,"dataLineage":binding,"root":2,"precision":[10,5]})
  receipt.update(status="running",localInputBindingSHA256=continuationBinding);save()
  def prefix(name):
   d=recovery/name;d.mkdir(exist_ok=True);return d/name
  def run(name,program,args,marker,required,infiles,outfiles,logical):
   filename=NATIVE[program] if program in NATIVE else PYTHON[program]
   key=digest({"inputs":[sha(x) for x in infiles],"logical":logical,"source":receipt["sources"][filename],"headers":{k:v for k,v in receipt["sources"].items() if k.endswith(".hpp")}})
   cp=cache/(name+".json");context=cache/(name+".context.json")
   if context.exists():
    prior=json.loads(context.read_text())
    if prior.get("inputBindingSHA256")!=key:raise ValueError("saved partial stage belongs to different actual inputs: "+name)
   else:atomic_json(context,{"inputBindingSHA256":key,"nativeDataLineageBindingSHA256":binding,"portable":True})
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
  prepdir=recovery/"prepared-third";prepdir.mkdir(exist_ok=True);prep=prepdir/"prepared-saturated-third-receipt.json";prepsys=prepdir/"prepared-saturated-third.bin.gz"
  prepkeys=["secondPreparedReceipt","secondPreparedSystem","secondCompleteReceipt","secondCompleteSystem","secondKernel"]
  prepflags=["second-prepared-receipt","second-prepared-system","second-complete-receipt","second-complete-system","second-kernel"]
  args=["--mode","prepare","--notes-root",notes,"--out",prepdir]
  for key,flag in zip(prepkeys,prepflags):args+=["--"+flag,found[key]]
  specs=[prepdir/(x+".spec") for x in ("third-q4-root2-ten","third-state-crt8")]
  run("saved-entire-third-source-preparation","matrix",args,"completed",
   {"completeSecondPolynomialSourceKernelRetained":True,"allNextSourceImagesPaidByTrueFirstBasis":True,"integerTaylorLiftIncludesAllCarry":True},
   [found[key] for key in prepkeys],[prep,prepsys]+specs,{"wholeNextSourceKernel":True,"integerSToTaylorLift":True})
  prepared=json.loads(prep.read_text());labels=prepared["thirdSourceLabels"];n=len(labels);spec10,spec8=specs
  receipt["thirdSourceCount"]=n;receipt["thirdSourceLabels"]=labels;receipt["incomingSecondRank"]=prepared["secondImageRank"];receipt["completeRelevantSaturatedSecondImageReused"]=True;save()
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
  F=prepared["generatorIntegerTaylorCoefficientsMod31Six"];C=prepared["trueU7B8D2Correction"]
  edges=[[i,j,F[i][j]] for i in range(204) for j in range(n) if any(F[i][j])]
  families=[fam(found["secondL4Source"],ALL204,edges)]
  families+=seven_families(C[:7],4)
  families+=[fam(found["newOriginal"],LABEL16,[[2,j,[-P*C[7][j]]] for j in range(n) if C[7][j]]),
             fam(found["secondL3Source"],labels197,[[0,j,[-P*C[8][j]]] for j in range(n) if C[8][j]])]
  M4=integer("true-third-M4-corrected-ten",spec10,10,labels,[4]*n,10,families)
  NF4=normal("third-q4-normal-ten",spec10,suffix(M4,"-field-root2-jets.bin"))
  Q4=solve("third-q4-complete-ten",found["Gcache"],NF4)
  q4=vq("third-q4-ten-vq","q4",spec10,Q4,found["Vcache"],"-")
  q4raw=transport("third-q4-ten-original","q4",spec10,q4,suffix(NF4,"-local-prebasis-source-jets.bin"),"-")
  families=[fam(suffix(M4,"-original6188-integer-jets.bin"),labels,identity_edges(n)),
            fam(suffix(q4raw,"-original6188-q-jets.bin"),labels,identity_edges(n,scale=-P4))]
  L5=integer("all-genuine-third-sources",spec10,10,labels,[5]*n,5,families)
  NF5=normal("all-third-local-state",spec8,suffix(L5,"-field-projected-crt8-jets.bin"),True)
  comp=recovery/"complete-third";comp.mkdir(exist_ok=True)
  args=["--mode","complete","--notes-root",notes,"--out",comp,"--prepared-receipt",prep,"--prepared-system",prepsys,
   "--original-metadata",suffix(L5,"-integer-product.json"),"--normal-metadata",suffix(NF5,"-local-normal.json"),
   "--map",found["jetMap"],"--map-receipt",found["jetMapReceipt"],"--standard-state",suffix(NF5,"-standard-state.bin")]
  run("complete-saturated-third-page","matrix",args,"completed",
   {"allTrueOriginalThirdSourcesComputed":True,"completeRelevantSaturatedThirdImageComputed":True,"completeOriginalS2SourceCoverageRetained":True},
   [prep,prepsys,suffix(L5,"-integer-product.json"),suffix(NF5,"-local-normal.json"),found["jetMap"],found["jetMapReceipt"],suffix(NF5,"-standard-state.bin")],
   [comp/"complete-saturated-third-page-receipt.json",comp/"complete-saturated-third.bin.gz"],
   {"fullOriginalS2Coverage":True,"entireSecondKernelNotOnlyImage":True})
  final=json.loads((comp/"complete-saturated-third-page-receipt.json").read_text())
  receipt["completeThirdConclusion"]=final
  for k in ("allTrueOriginalThirdSourcesComputed","completeRelevantSaturatedThirdImageComputed","completeOriginalS2SourceCoverageRetained",
   "globalAllOriginalSourceMod31SixObstructionVerified","globalAllOriginalSourceMod31SixDecisionComputed",
   "individualTargetCompatible","compatibleTargetLabels","originalMod31SixObstructedTargetLabels","thirdImageRank","outcome"):receipt[k]=final[k]
  receipt.update(status="completed",mathematicalElapsedSeconds=time.monotonic()-started)
  receipt["continuationRequired"]="For every locally compatible target restore the selected global original sources and complete all17 identities. A complete negative concerns this original p2h0 modulo p6; the characteristic-zero R150 goal remains open."
  save()
 except Exception as e:
  receipt.update(status="failed-or-incomplete",errorType=type(e).__name__,error=str(e))
  if started is not None:receipt["mathematicalElapsedSeconds"]=time.monotonic()-started
  save()
 finally:
  packagingStarted=time.monotonic();receipt["packagingStatus"]="running";save()
  certificates=results/"certificates";certificates.mkdir(exist_ok=True);files=[];texts=[];packagedFiles=0;packagedBytes=0
  for q in sorted(recovery.rglob("*")):
   if not q.is_file():continue
   relative=q.relative_to(recovery);flat=str(relative).replace("/","__")
   if q.suffix in (".json",".mix",".recipe",".txt",".spec") and q.stat().st_size<=1_000_000:
    dest=results/flat;shutil.copyfile(q,dest);texts.append({"originalFile":str(relative),"file":dest.name,"bytes":q.stat().st_size,"sha256":sha(q)});continue
   temporary=results/(flat+".gz.tmp")
   with q.open("rb") as src,temporary.open("wb") as dst:
    with gzip.GzipFile(filename="",mode="wb",fileobj=dst,mtime=0,compresslevel=1) as gz:shutil.copyfileobj(src,gz)
   item={"originalFile":str(relative),"uncompressedBytes":q.stat().st_size,"uncompressedSHA256":sha(q),
    "compressedBytes":temporary.stat().st_size,"compressedSHA256":sha(temporary),"parts":[]}
   with temporary.open("rb") as src:
    part=1
    while data:=src.read(4_500_000):
     dest=certificates/(flat+".gz" if item["compressedBytes"]<=4_500_000 else flat+f".gz.part{part:03d}")
     dest.write_bytes(data);item["parts"].append({"file":str(dest.relative_to(results)),"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()});part+=1
   temporary.unlink();files.append(item);packagedFiles+=1;packagedBytes+=item["uncompressedBytes"]
   receipt.update(packagingBinaryFiles=packagedFiles,packagingUncompressedBytes=packagedBytes,packagingElapsedSeconds=time.monotonic()-packagingStarted);save()
   print(json.dumps({"phase":"lossless-finalization-level1","completeBinaryFiles":packagedFiles,"uncompressedBytes":packagedBytes,"elapsedSeconds":time.monotonic()-packagingStarted}),flush=True)
  atomic_json(results/"certificate-manifest.json",{"format":"r150-saturated-third-lossless-certificates-v1","pipelineStatus":receipt["status"],"partialCheckpointIsNotIdentity":True,"files":files})
  atomic_json(results/"text-recovery-manifest.json",{"format":"r150-saturated-third-exact-text-recovery-v1","completeStageCachesIncluded":True,"files":texts})
  saved=[{"file":str(q.relative_to(recovery)),"bytes":q.stat().st_size,"sha256":sha(q)} for q in sorted(recovery.rglob("*")) if q.is_file()]
  atomic_json(results/"recovery-manifest.json",{"format":"r150-saturated-third-complete-recovery-v1","pipelineStatus":receipt["status"],"files":saved})
  receipt.update(recoveryFiles=len(saved),recoveryBytes=sum(x["bytes"] for x in saved),losslessGeneratedBinaryFiles=len(files),packagingStatus="completed",packagingElapsedSeconds=time.monotonic()-packagingStarted);save()
  print(json.dumps({k:receipt.get(k) for k in ("status","outcome","mathematicalElapsedSeconds","thirdImageRank","individualTargetCompatible","completeRelevantSaturatedThirdImageComputed","completeOriginalS2SourceCoverageRetained","globalAllOriginalSourceMod31SixObstructionVerified","recoveryBytes")}),flush=True)
 if receipt["status"] not in ("completed","prepared-no-mathematical-stage-executed"):raise SystemExit(1)
if __name__=="__main__":main()
