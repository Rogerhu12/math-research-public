#!/usr/bin/env python3
"""Global original17 continuation of the actual saturated third all-positive run.
Seven raw first sources, six auxiliary slots, four whole-source projections.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,shutil,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
CONTRACT="2026-11-15-r150-saturated-third-global-contract-789f.json"
NATIVE={k:"2026-11-15-r150-saturated-global-"+k+"-789f.cpp" for k in ("image","source","transport","normal","original")}
PYTHON={"matrix":"2026-11-15-r150-saturated-third-global-matrices-789f.py",
 "carry":"2026-11-15-r150-global-raw-q1-canonical-carry-789f.py"}
P=31;P2=961;P3=29791;P4=923521;P5=28629151;P6=887503681
TARGETS=list(range(2,11));LABEL7=list(range(7001,7008));LABEL16=LABEL7+TARGETS;LABEL10=[9001]+TARGETS
BETA=[2275,2276,2277,2278];FOUR=[4001,4002,4003,4004]
_sha_cache={}
def sha(path):
 path=Path(path);st=path.stat();key=(str(path.resolve()),st.st_size,st.st_mtime_ns)
 if key in _sha_cache:return _sha_cache[key]
 h=hashlib.sha256()
 with path.open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 _sha_cache[key]=h.hexdigest();return h.hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def suffix(p,s):return Path(str(p)+s)
def atomic_json(p,x):
 t=p.with_name(p.name+".tmp");t.write_text(json.dumps(x,separators=(",",":"))+"\n");os.replace(t,p)
def zero(n,m=9):return [[[] for _ in range(m)] for _ in range(n)]
def constants(a):return [[[int(x)] if int(x) else [] for x in r] for r in a]
def scale(a,c):return [[[int(x)*c for x in p] for p in r] for r in a]
def identity(active=range(9),c=1):
 s=set(active);return [[[c] if i==j and i in s else [] for j in range(9)] for i in range(9)]
def polynomial_diag(poly,active=range(9)):
 s=set(active);return [[list(poly) if i==j and i in s else [] for j in range(9)] for i in range(9)]
def select_row(n,i,coefs):
 a=zero(n);a[i]=[[int(x)] if int(x) else [] for x in coefs];return a
def whole_project(a,P):return [[[int(p[0])*x for x in P] if p else [] for p in r] for r in a]
def write_mix(path,labels,bound,families):
 lines=["R150_RHS_MIX_V1",f"{len(labels)} {bound} {len(families)}"," ".join(map(str,labels))]
 for f in families:
  lines.append(" ".join(str(f[k]) for k in ("nf","q","rem","trace"))+" "+str(len(f["labels"])))
  lines.append(" ".join(map(str,f["labels"])))
  for row in f["polys"]:
   if len(row)!=len(labels):raise ValueError("all mixture slots")
   for p in row:
    p=[int(x)%31 for x in p]
    while p and not p[-1]:p.pop()
    lines.append(" ".join(map(str,[len(p)]+p)))
 path.write_text("\n".join(lines)+"\n")
def write_original(path,labels,bound,divisor,target_mode,active,families):
 lines=["R150_ORIGINAL_SATURATED_POSITIVE_COMBINATION_V1",f"{len(labels)} {bound} {divisor} {target_mode} {len(families)}",
  " ".join(map(str,labels))," ".join(str(int(x)) for x in active)]
 for f in families:
  if len(f["polys"])!=len(f["labels"]):raise ValueError("actual original source family")
  lines.append(str(f["file"])+" "+str(len(f["labels"])));lines.append(" ".join(map(str,f["labels"])))
  for row in f["polys"]:
   if len(row)!=len(labels):raise ValueError("all original source slots")
   for p in row:
    p=[int(x)%P6 for x in p]
    while p and not p[-1]:p.pop()
    if len(p)>1250:raise ValueError("proved actual source polynomial degree")
    lines.append(" ".join(map(str,[len(p)]+p)))
 path.write_text("\n".join(lines)+"\n")
def main():
 p=argparse.ArgumentParser()
 scopes_list=("t96","all198","seven","current","ninth","old200","second","third")
 for k in ("notes-root",)+tuple(x+"-recovery" for x in scopes_list)+("out",):p.add_argument("--"+k,type=Path,required=True)
 p.add_argument("--math-seconds",type=float,default=300);p.add_argument("--memory-mib",type=int,default=1024);p.add_argument("--compile-seconds",type=int,default=30)
 p.add_argument("--resume-recovery",type=Path);p.add_argument("--resume-results",type=Path);p.add_argument("--prepare-only",action="store_true")
 a=p.parse_args()
 if min(a.math_seconds,a.memory_mib,a.compile_seconds)<=0:raise ValueError("explicit positive execution limits")
 root=Path(__file__).resolve().parent;notes=a.notes_root.resolve();out=a.out.resolve()
 results=out/"results";recovery=out/"recovery";bins=out/"bin";out.mkdir(parents=True,exist_ok=True)
 if a.resume_recovery and a.resume_recovery.resolve()!=recovery:shutil.copytree(a.resume_recovery,recovery,dirs_exist_ok=True)
 if a.resume_results and a.resume_results.resolve()!=results:shutil.copytree(a.resume_results,results,dirs_exist_ok=True)
 for d in (results,recovery,bins,recovery/"inputs",recovery/"stage-cache"):d.mkdir(parents=True,exist_ok=True)
 inputs=recovery/"inputs";cache=recovery/"stage-cache";receipt_path=results/"saturated-third-global-pipeline-receipt.json"
 receipt={"format":"r150-saturated-third-global-six-slot-original17-v1","status":"preparing",
  "prime":31,"nativeModulus":P6,"targetMultiplier":"31^2*h0","targetLabels":TARGETS,
  "sourceThirdRun":43664532571,"sourceSecondRun":43662590949,"oldLocalPagesRecomputed":False,
  "characteristicZeroIdentityAsserted":False,"fullOriginalAllNineMod887503681IdentityVerified":False,
  "allNineOriginalSeventeenIdentitiesVerified":False,"allSixAuxiliaryOriginalIdentitiesVerified":False,
  "full315FinalReconciliationVerified":False,"finitePositiveSourceBudgetsVerified":False,"finite_budget_verified":False,
  "individualTargetCompatible":[True]*9,"compatibleTargetLabels":TARGETS,"completedOriginalTargetLabels":[],
  "actualFinalSourceCostsBySlot":[-1]*9,"provedFinalSourceCostBound":1345,
  "sharedMathematicalSecondsLimit":a.math_seconds,"perChildAddressSpaceMiBLimit":a.memory_mib,
  "perCompilationSecondsLimit":a.compile_seconds,"nativeCompilations":5,
  "deadlineRule":"Five bounded compilations and exact input recovery precede one shared mathematical clock. Only the actual selected seven global raw q1 sources are computed; no local source/page is redone. Every division, free test and full315 correction precedes continued original17 restoration. Completed stages and actual partial source/product arrays are retained. Lossless level1 sealing follows the clock.",
  "inputs":{},"sources":{},"compilations":{},"stages":{}}
 started=None;old_cert={}
 if (results/"certificate-manifest.json").is_file():
  old_cert={x["originalFile"]:x for x in json.loads((results/"certificate-manifest.json").read_text()).get("files",[])}
 def save():atomic_json(receipt_path,receipt)
 try:
  contract=json.loads((root/CONTRACT).read_text());receipt["inputContractSHA256"]=sha(root/CONTRACT)
  scopes={x:getattr(a,x+"_recovery").resolve() for x in scopes_list};scopes["notes"]=notes;found={}
  for key,item in contract["inputs"].items():
   retained=list(inputs.glob(key+".*"));base=scopes[item["scope"]]
   options=retained+([base/item["relative"]] if "relative" in item else [q for n in item["names"] for q in base.rglob(n)])
   actual=next((q for q in options if q.is_file() and ("bytes" not in item or q.stat().st_size==item["bytes"]) and sha(q)==item["sha256"]),None)
   if actual is None:raise ValueError("missing exact saved input "+key)
   dst=inputs/(key+"".join(actual.suffixes))
   if actual.resolve()!=dst.resolve():shutil.copyfile(actual,dst)
   if sha(dst)!=item["sha256"]:raise ValueError("lossless actual input copy "+key)
   found[key]=dst;receipt["inputs"][key]={"file":str(dst.relative_to(recovery)),"bytes":dst.stat().st_size,"sha256":item["sha256"]}
  for name,wanted in contract["dependencies"].items():
   path=root/name if (root/name).is_file() else notes/name
   if sha(path)!=wanted:raise ValueError("frozen exact dependency "+name)
   receipt["sources"][name]=wanted
  receipt["sources"][Path(__file__).name]=sha(Path(__file__));receipt["sources"][CONTRACT]=sha(root/CONTRACT);save()
  for key,filename in NATIVE.items():
   code=root/filename;exe=bins/key
   command=["timeout","--kill-after=10s",str(a.compile_seconds)+"s","prlimit","--as="+str(a.memory_mib*1048576),"--core=0","--","g++","-O3","-std=c++17","-I",str(root),"-I",str(notes),str(code),"-o",str(exe)]
   t=time.monotonic();r=subprocess.run(command,capture_output=True,text=True)
   (results/("compile-"+key+".log")).write_text(r.stdout+r.stderr)
   receipt["compilations"][key]={"exitCode":r.returncode,"elapsedSeconds":time.monotonic()-t,"command":command};save()
   if r.returncode:raise RuntimeError("bounded compile failed "+key)
  if a.prepare_only:receipt["status"]="prepared-no-mathematical-stage-executed";save();return
  started=time.monotonic();deadline=started+a.math_seconds;receipt["status"]="running";save()
  def prefix(name):
   q=recovery/name;q.mkdir(exist_ok=True);return q/name
  def binding(infiles,logical,program):
   filename=PYTHON.get(program,NATIVE.get(program))
   return digest({"inputs":[sha(x) for x in infiles],"logical":logical,"program":receipt["sources"][filename],
    "headers":{k:v for k,v in receipt["sources"].items() if k.endswith(".hpp")}})
  def run(name,program,args,marker,required,infiles,outfiles,logical):
   key=binding(infiles,logical,program);cp=cache/(name+".json")
   if cp.exists():
    c=json.loads(cp.read_text())
    if c.get("inputBindingSHA256")==key and all(q.is_file() and sha(q)==c.get("outputs",{}).get(str(q.relative_to(recovery))) for q in outfiles):
     receipt["stages"][name]={"status":"completed","reusedCompletedActualStage":True,"elapsedSeconds":0,"inputBindingSHA256":key,"nativeStatistics":c["nativeStatistics"]};save();return
   remaining=deadline-time.monotonic()
   if remaining<=0:raise TimeoutError("shared clock before "+name)
   args=[f"{max(0.001,remaining-0.25):.6f}" if str(x)=="__REMAINING__" else str(x) for x in args]
   executable=[sys.executable,str(root/PYTHON[program])] if program in PYTHON else [str(bins/program)]
   cmd=["timeout","--kill-after=10s",f"{remaining:.6f}s","prlimit","--as="+str(a.memory_mib*1048576),"--core=0","--"]+executable+args
   stage={"status":"running","inputBindingSHA256":key,"remainingSecondsAtStart":remaining,"command":cmd};receipt["stages"][name]=stage;save()
   process=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1);last={};t=time.monotonic()
   with (results/(name+".log")).open("w") as log:
    for line in process.stdout:
     log.write(line);log.flush();print(line,end="",flush=True)
     try:
      ev=json.loads(line)
      if isinstance(ev,dict):last=ev;stage["lastProgress"]=ev;save()
     except ValueError:pass
   code=process.wait();ok=code==0 and last.get("status")==marker and all(last.get(k)==v for k,v in required.items()) and all(q.is_file() for q in outfiles)
   stage.update(status="completed" if ok else "failed-or-incomplete",exitCode=code,elapsedSeconds=time.monotonic()-t,nativeStatistics=last)
   receipt["mathematicalElapsedSeconds"]=time.monotonic()-started;save()
   if not ok:raise RuntimeError("actual stage failed or incomplete "+name)
   atomic_json(cp,{"inputBindingSHA256":key,"nativeStatistics":last,"outputs":{str(q.relative_to(recovery)):sha(q) for q in outfiles}})
  basekeys=["thirdPreparedReceipt","thirdPreparedSystem","thirdCompleteReceipt","thirdCompleteSystem"]
  baseargs=[]
  for k,flag in zip(basekeys,["third-prepared-receipt","third-prepared-system","third-complete-receipt","third-complete-system"]):baseargs+=["--"+flag,found[k]]
  prepdir=recovery/"prepared-global";prepdir.mkdir(exist_ok=True);prep=prepdir/"global-source-preparation.json"
  run("prepare-actual-six-global-sources","matrix",["--mode","prepare","--notes-root",notes,"--second-prepared-receipt",found["secondPreparedReceipt"],
   "--old-kernel",found["oldK"],"--out",prepdir]+baseargs,"completed",
   {"allNineSaved315PositiveIdentitiesVerified":True,"allSelectedParentsActuallyConstant":True},
   [found[k] for k in basekeys]+[found["secondPreparedReceipt"],found["oldK"]],[prep],{"savedConstantPositiveSourcesOnly":True})
  prepared=json.loads(prep.read_text());receipt["actualSourcePreparation"]=prepared;save()
  oldlabels=prepared["oldKernelLabels"];projector=prepared["projectorPolynomialAscending"];lam=prepared["lambda"]
  def nf_family(key,labels,polys):return {"nf":found[key+"NF"],"q":found[key+"Q"],"rem":found[key+"Rem"],"trace":found[key+"Trace"],"labels":labels,"polys":polys}
  def own_nf(normal,image,labels,polys):
   return {"nf":suffix(normal,"-normal-forms.bin"),"q":suffix(image,"-image-quotients.bin") if image else "-",
    "rem":suffix(image,"-image-remainders.bin") if image else "-","trace":suffix(normal,"-reduction.bin"),"labels":labels,"polys":polys}
  def image(name,families,bound,labels=TARGETS,zero_required=True):
   output=prefix(name);mix=inputs/(name+".mix");write_mix(mix,labels,bound,families)
   infiles=[found["graph"]]
   for f in families:
    infiles.append(f["nf"])
    if str(f["q"])!="-":infiles.extend([f["q"],f["rem"]])
   req={"fullImageQuotientIdentity":True}
   if zero_required:req["completeRHSInImage"]=True
   run(name,"image",[found["graph"],mix,output],"saved-quotient-mixture-complete",req,infiles,
    [suffix(output,s) for s in ("-normal-forms.bin","-image-quotients.bin","-image-remainders.bin","-image-certificate.json")],
    {"bound":bound,"labels":labels,"polynomials":[f["polys"] for f in families]})
   return output,mix
  def source(name,I,mix,families,bound,mode="raw"):
   output=prefix(name+"-VQ");data=[found["graph"],found["originalNF"],suffix(I,"-normal-forms.bin"),suffix(I,"-image-quotients.bin"),suffix(I,"-image-remainders.bin")]
   key=binding(data,{"bound":bound,"targets":9,"sourceMode":mode},"source")
   run(name+"-VQ","source",data+[output,key,mode],"packed-image-source-convolution-complete",
    {"fullNormalFormDecompositionIdentity":True,"standardKernelNormalForm":mode=="standard","completeRHSInImage":True},data,
    [suffix(output,s) for s in ("-standard-coefficients.bin","-source-certificate.json","-vq-checkpoint.bin")],{"bound":bound,"sourceMode":mode,"checkpointBinding":key})
   q=prefix(name+"-original");data=[suffix(output,"-standard-coefficients.bin"),found["model"],found["normalTrace"],found["forward"],found["backward"]]
   logical={"bound":bound,"polynomials":[f["polys"] for f in families],"sourceMode":mode}
   key=binding(data+[f["trace"] for f in families],logical,"transport")
   run(name+"-original","transport",data+[mix,q,q.parent/"actual-checkpoints",key,"__REMAINING__"],
    "original-source-transport-complete",{},data+[f["trace"] for f in families],
    [suffix(q,"-primitive-source-mod31.bin"),suffix(q,"-original-transport.json")],logical)
   meta=json.loads(suffix(q,"-original-transport.json").read_text())
   if max(meta["sourceCosts"])>bound+96:raise ValueError("actual original source bound")
   return q
  def original(name,labels,B,divisor,active,families,final=False):
   q=prefix(name);recipe=inputs/(name+".recipe");write_original(recipe,labels,B,divisor,int(final),active,families)
   data=[found["model"],found["ninthIntegerModel"]]+[f["file"] for f in families]
   logical={"bound":B,"divisor":divisor,"labels":labels,"active":active,"final":final,"polynomials":[f["polys"] for f in families]}
   key=binding(data,logical,"original")
   req={"divisor":divisor,"allOriginalProductCoefficientsDivisible":True}
   if final:req["fullOriginalSeventeenEquationIdentityMod887503681"]=True
   outputs=[suffix(q,s) for s in ("-primitive-source-mod887503681.bin","-original-seventeen-source-mod887503681.bin","-original-product.json")]
   if not final:outputs.append(suffix(q,"-divided-original-rhs.bin"))
   run(name,"original",[found["model"],found["ninthIntegerModel"],recipe,q,key],"full-original-saturated-positive-product-complete",
    req,data,outputs,{**logical,"checkpointBinding":key})
   meta=json.loads(suffix(q,"-original-product.json").read_text())
   if meta["targetLabels"]!=labels or meta["activeTargetLabels"]!=[x for x,v in zip(labels,active) if v] or not meta["inactiveSourceColumnsExactlyZero"]:raise ValueError("actual source-mask original identity")
   return q
  def normal_image(name,O,labels,bound):
   q=prefix(name+"-normal");data=[found["model"],suffix(O,"-divided-original-rhs.bin")];key=binding(data,{"originalRHSCost":bound},"normal")
   run(name+"-normal","normal",data+[q,key],"197-third-global-normal-forms-complete",{},data,
    [suffix(q,s) for s in ("-normal-forms.bin","-reduction.bin","-forward.bin","-backward.bin","-normal-checkpoint.bin")],{"originalRHSCost":bound,"checkpointBinding":key})
   if sha(suffix(q,"-forward.bin"))!=sha(found["forward"]) or sha(suffix(q,"-backward.bin"))!=sha(found["backward"]):raise ValueError("same3333 true original provenance DAG")
   I,_=image(name+"-whole-image",[own_nf(q,None,labels,identity())],bound,labels,False)
   return q,I
  def reconcile(name,mode,O,I,D=None,W=None):
   d=recovery/name;d.mkdir(exist_ok=True)
   args=["--mode",mode,"--notes-root",notes,"--out",d,"--original-metadata",suffix(O,"-original-product.json"),
    "--image-metadata",suffix(I,"-image-certificate.json"),"--image-remainders",suffix(I,"-image-remainders.bin")]+baseargs
   ins=[found[k] for k in basekeys]+[suffix(O,"-original-product.json"),suffix(I,"-image-certificate.json"),suffix(I,"-image-remainders.bin"),found["state"]]
   for x,flag in [(D,"d"),(W,"w")]:
    if x:
     args+=["--"+flag+"-receipt",x/"global-reconciliation.json","--"+flag+"-system",x/"global-reconciliation.bin.gz"]
     ins += [x/"global-reconciliation.json",x/"global-reconciliation.bin.gz"]
   req={"all505FreeObservationsVerified":True,"allWhole315ReconciliationIdentitiesVerified":True}
   if mode=="final":req["full315FinalReconciliationVerified"]=True
   run(name,"matrix",args,"completed",req,ins,[d/"global-reconciliation.json",d/"global-reconciliation.bin.gz"],{"whole315Mode":mode})
   return d,json.loads((d/"global-reconciliation.json").read_text())
  def rawfam(file,labels,polys):return {"file":file,"labels":labels,"polys":polys}
  def primitive(q):return suffix(q,"-primitive-source-mod887503681.bin")
  def fieldsource(q):return suffix(q,"-primitive-source-mod31.bin")
  def seven_original(C,exponent,sign=-1):
   E=[1,1,2,2,2,2,2];weights=[[sign*(31**(exponent-E[i]))*int(x) for x in C[i]] for i in range(7)]
   return seven_direct(weights)
  def seven_direct(C):
   return [rawfam(found["kernels"],BETA,constants(C[:2]+[[0]*9,[0]*9])),
    rawfam(found["fourK2"],FOUR,constants(C[2:6])),
    rawfam(found["selectedK2"],TARGETS,constants([C[6]]+[[0]*9 for _ in range(8)]))]
  def seven_field(C,sign=-1):
   C=[[sign*int(x) for x in r] for r in C]
   return [nf_family("beta",BETA,constants(C[:2]+[[0]*9,[0]*9])),
    nf_family("four",FOUR,constants(C[2:6])),nf_family("selected",TARGETS,constants([C[6]]+[[0]*9 for _ in range(8)]))]
  # One actual global raw section for K2..K8. The last two packed slots are zero.
  Kselect=zero(200)
  for j in range(7):Kselect[j+1][j]=[1]
  fs=[nf_family("old",oldlabels,Kselect)];IQ1,MQ1=image("seven-q1-image",fs,81)
  Q1=source("seven-q1",IQ1,MQ1,fs,81,"raw")
  carrydir=recovery/"same-q1-integer-carry";carrydir.mkdir(exist_ok=True)
  run("same-q1-integer-carry","carry",["--global-source",fieldsource(Q1),"--paid-jets",found["paidQ1Twenty"],"--old-kernel",found["oldK"],"--out",carrydir,"--remaining-seconds","__REMAINING__"],
   "completed",{"allOriginalRowsVerified":True,"allFieldJetsMatch":True,"integerCarryIdentityVerified":True},
   [fieldsource(Q1),found["paidQ1Twenty"],found["oldK"]],
   [carrydir/"q1-s-to-t-carry-receipt.json",carrydir/"q1-s-to-t-carry.bin"],{"sameRawSection":True,"TaylorPrecision":20})
  receipt["sameQ1IntegerCarryVerified"]=True;save()
  H=prepared["initialKernelCoefficients"];oldH=zero(200)
  for i in range(7):oldH[i+1]=constants([H[i]])[0]
  qH=constants(H+[[0]*9,[0]*9])
  fs=[rawfam(found["oldK"],oldlabels,oldH),rawfam(fieldsource(Q1),TARGETS,scale(qH,-P))]
  fs+=seven_direct(prepared["initialSevenOriginalCoefficients"])
  fs+=[rawfam(found["newOriginal"],LABEL16,select_row(16,2,prepared["initialKappa8OriginalCoefficients"]))]
  fs=[{**f,"polys":whole_project(f["polys"],projector)} for f in fs]
  a6=[1]*6+[0]*3;a5=[1]*5+[0]*4;am=[0]*9;am[4]=1
  l2=list(range(9602,9611));l3=list(range(9702,9711));l4=list(range(9802,9811));l5=list(range(9902,9911))
  PF0=original("projected-six-initial-p2",l2,373,P2,a6,fs)
  NF0,IF0=normal_image("projected-six-initial",PF0,l2,373)
  fs=[own_nf(NF0,IF0,l2,identity(range(6)))];IQ2,MQ2=image("six-q2-image",fs,373);Q2=source("six-q2",IQ2,MQ2,fs,373)
  L3=original("six-L3-p3",l3,469,P3,a6,[rawfam(primitive(PF0),l2,identity(range(6))),rawfam(fieldsource(Q2),TARGETS,identity(range(6),-P2))])
  PL3=original("projected-six-L3-p3",l3,665,P3,a6,[rawfam(primitive(L3),l3,polynomial_diag(projector,range(6)))])
  N3,I3=normal_image("projected-six-L3",PL3,l3,665);DR,Drec=reconcile("global-D2-and-seven-correction","L3",PL3,I3)
  C7=Drec["actualSevenCorrections"]
  fs=[own_nf(N3,I3,l3,identity(range(5)))]+seven_field(C7)
  IQ3,MQ3=image("five-q3-image",fs,665);Q3=source("five-q3",IQ3,MQ3,fs,665)
  fs=[rawfam(primitive(PL3),l3,identity(range(5)))]+seven_original(C7,3)+[rawfam(fieldsource(Q3),TARGETS,identity(range(5),-P3))]
  L4=original("five-L4-p4",l4,761,P4,a5,fs)
  PL4=original("projected-five-L4-p4",l4,957,P4,a5,[rawfam(primitive(L4),l4,polynomial_diag(projector,range(5)))])
  N4,I4=normal_image("projected-five-L4",PL4,l4,957);WR,Wrec=reconcile("global-four-W2-and-first-correction","L4",PL4,I4,D=DR)
  Cfirst=Wrec["actualFirstCorrections"];C7=Cfirst[:7];C8=Cfirst[7];CD=Cfirst[8]
  fs=[own_nf(N4,I4,l4,identity([4]))]+seven_field(C7)
  fs += [nf_family("new",LABEL16,select_row(16,2,[-x for x in C8])),own_nf(N3,I3,l3,select_row(9,5,[-x for x in CD]))]
  IQ4,MQ4=image("main-q4-image",fs,957);Q4=source("main-q4",IQ4,MQ4,fs,957)
  fs=[rawfam(primitive(PL4),l4,identity([4]))]+seven_original(C7,4)
  fs += [rawfam(found["newOriginal"],LABEL16,select_row(16,2,[-P*x for x in C8])),
   rawfam(primitive(PL3),l3,select_row(9,5,[-P*x for x in CD])),
   rawfam(fieldsource(Q4),TARGETS,identity([4],-P4))]
  L5=original("main-L5-p5",l5,1053,P5,am,fs)
  PL5=original("projected-main-L5-p5",l5,1249,P5,am,[rawfam(primitive(L5),l5,polynomial_diag(projector,[4]))])
  N5,I5=normal_image("projected-main-L5",PL5,l5,1249);FR,Frec=reconcile("final-full315-nine-reconciliation","final",PL5,I5,W=WR)
  C9=Frec["actualNineCorrections"];CW=Frec["actualFourW2Corrections"]
  current=zero(10)
  for j in range(9):current[j+1][j]=[1]
  wpolys=constants(CW+[[0]*9 for _ in range(5)])
  fs=[nf_family("ninth",LABEL10,current),own_nf(N5,I5,l5,select_row(9,4,[-x for x in lam])),
   own_nf(N4,I4,l4,scale(wpolys,-1))]+seven_field(C9[:7])
  fs += [nf_family("new",LABEL16,select_row(16,2,[-x for x in C9[7]])),
   nf_family("currentK4",LABEL7,select_row(7,3,[-x for x in C9[8]]))]
  IQF,MQF=image("final-nine-image",fs,1249);QF=source("final-nine",IQF,MQF,fs,1249)
  fs=[rawfam(found["ninthOriginal"],LABEL10,current),rawfam(primitive(PL5),l5,select_row(9,4,lam)),
   rawfam(primitive(PL4),l4,scale(wpolys,P))]+seven_original(C9[:7],5,1)
  fs += [rawfam(found["newOriginal"],LABEL16,select_row(16,2,[P2*x for x in C9[7]])),
   rawfam(found["currentK4Original"],LABEL7,select_row(7,3,[P*x for x in C9[8]])),
   rawfam(fieldsource(QF),TARGETS,identity(c=P5))]
  final=original("final-nine-original17-p6",TARGETS,1345,P6,[1]*9,fs,True)
  fm=json.loads(suffix(final,"-original-product.json").read_text())
  for k in ("fullOriginalSeventeenEquationIdentityMod887503681","fullOriginalMacaulayIdentityMod887503681","originalRowScaleTransportVerified","allWeightedBoundsVerified"):
   if fm.get(k) is not True:raise ValueError("full final identity field "+k)
  if fm["activeTargetLabels"]!=TARGETS or max(fm["actualSourceCosts"])>1345:raise ValueError("all original nine weighted bounds")
  receipt.update(status="completed",outcome="all-nine-original-p6-complete",finalOriginalConclusion=fm,
   fullOriginalAllNineMod887503681IdentityVerified=True,allNineOriginalSeventeenIdentitiesVerified=True,
   allSixAuxiliaryOriginalIdentitiesVerified=True,full315FinalReconciliationVerified=True,
   finitePositiveSourceBudgetsVerified=True,finite_budget_verified=True,completedOriginalTargetLabels=TARGETS,
   actualFinalSourceCostsBySlot=fm["actualSourceCosts"],mathematicalElapsedSeconds=time.monotonic()-started);save()
 except Exception as e:
  receipt.update(status="failed-or-incomplete",errorType=type(e).__name__,error=str(e))
  if started is not None:receipt["mathematicalElapsedSeconds"]=time.monotonic()-started
  save()
 finally:
  t=time.monotonic();receipt["packagingStatus"]="running";save();cert=results/"certificates";cert.mkdir(exist_ok=True)
  files=[];texts=[];count=0
  for q in sorted(recovery.rglob("*")):
   if not q.is_file():continue
   relative=str(q.relative_to(recovery));flat=relative.replace("/","__");size=q.stat().st_size;rawhash=sha(q)
   if q.suffix in (".json",".mix",".recipe",".txt",".spec") and size<=1_000_000:
    dest=results/flat;shutil.copyfile(q,dest);texts.append({"originalFile":relative,"file":dest.name,"bytes":size,"sha256":rawhash});continue
   old=old_cert.get(relative)
   if old and old.get("uncompressedBytes")==size and old.get("uncompressedSHA256")==rawhash and all((results/x["file"]).is_file() and (results/x["file"]).stat().st_size==x["bytes"] and sha(results/x["file"])==x["sha256"] for x in old.get("parts",[])) and old.get("parts"):
    files.append(old);continue
   tmp=results/(flat+".gz.tmp")
   with q.open("rb") as src,tmp.open("wb") as dst:
    with gzip.GzipFile(filename="",mode="wb",fileobj=dst,mtime=0,compresslevel=1) as gz:shutil.copyfileobj(src,gz)
   item={"originalFile":relative,"uncompressedBytes":size,"uncompressedSHA256":rawhash,"compressedBytes":tmp.stat().st_size,"compressedSHA256":sha(tmp),"parts":[]}
   with tmp.open("rb") as src:
    part=1
    while data:=src.read(4_500_000):
     dest=cert/(flat+".gz" if item["compressedBytes"]<=4_500_000 else flat+f".gz.part{part:03d}")
     dest.write_bytes(data);item["parts"].append({"file":str(dest.relative_to(results)),"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()});part+=1
   tmp.unlink();files.append(item);count+=1
   print(json.dumps({"phase":"lossless-global-sealing-level1","completeBinaryFiles":count,"elapsedSeconds":time.monotonic()-t}),flush=True)
  atomic_json(results/"certificate-manifest.json",{"format":"r150-third-global-lossless-v1","pipelineStatus":receipt["status"],"partialCheckpointIsNotIdentity":True,"files":files})
  atomic_json(results/"text-recovery-manifest.json",{"format":"r150-third-global-text-v1","completeStageCachesIncluded":True,"files":texts})
  saved=[{"file":str(q.relative_to(recovery)),"bytes":q.stat().st_size,"sha256":sha(q)} for q in sorted(recovery.rglob("*")) if q.is_file()]
  atomic_json(results/"recovery-manifest.json",{"format":"r150-third-global-complete-recovery-v1","pipelineStatus":receipt["status"],"files":saved})
  receipt.update(recoveryFiles=len(saved),recoveryBytes=sum(x["bytes"] for x in saved),packagingStatus="completed",packagingElapsedSeconds=time.monotonic()-t);save()
  print(json.dumps({k:receipt.get(k) for k in ("status","outcome","mathematicalElapsedSeconds","fullOriginalAllNineMod887503681IdentityVerified","completedOriginalTargetLabels","actualFinalSourceCostsBySlot","recoveryBytes")}),flush=True)
 if receipt["status"] not in ("completed","prepared-no-mathematical-stage-executed"):raise SystemExit(1)
if __name__=="__main__":main()
