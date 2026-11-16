#!/usr/bin/env python3
"""Complete original weighted-nine F7 matrix and bounded row-stream rank.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

The input has all 16,442 original source columns and all three exact rational
Bell-cube components. Every output row is constructed. A processed-row rank
of 16,047 suffices for the paid characteristic-zero obstruction. Any smaller
prefix or completed finite-field rank is diagnostic only. All arrays remain
temporary; only source, parameters, execution identities and hashes belong
in version control.
"""
from __future__ import annotations
import argparse,array,gc,gzip,hashlib,json,os,resource,shutil,signal,struct,subprocess,sys,time
from pathlib import Path
from flint import fmpq
FORMAT="r150-original-weight9-prime7-stream-rank-v1"
AUDIT_FORMAT="r150-original-bell-cube-complete-prime7-coefficient-audit-v1"
AUDIT_BINDING="4baed1013b72717e2773607c308a3f534b029c92f35592dcb6c5ff1025587339"
AUDIT_SOURCE=(8329,"33560119cb8f19902f323b5a1f5fb5a3bb59d38aad6d55108950107bd545579e")
PAID_AUDIT=(4312,"1cee8383ede9f0a458cb37ce5a384e461fdc51f20c81747411ae650df8cf4cda")
MODEL_DESC={"path":"complete-original-weight9-prime7-model.json.gz",
 "bytes":16999356,"sha256":"fe91efd8d4739de90b831449c40020a98e3b9775ee28a7e678a7b29ff2b683bd",
 "logicalBytes":58953007,"logicalSha256":"df9fb9657926a52a4c3c1a895a0ba5aa34f2d5f537d747d7f07e00d42f81bdfa"}
NATIVE_PIN=(19143,"11b82abe88ca35e698d6860aef94de49809d8b836a34668869e263db30f67e4b")
DICTIONARY_SHA={
 "completeWeight9OutputMonomials":"905e9ae68f85198299646a2c798084218e0040b012f9d62f898db9ce1bcfcda7",
 "completeQuarticWeight5SourceMonomials":"2d91e8bf2e8a3e4561014d7fe51f6415898f3cb2a9252e151fd5d548fc6219e4",
 "completeQuinticWeight4SourceMonomials":"0416d1b3f4b3ec4f52aa75ecab710d7e56bbc04f8c067cbba728fb76f27f28b1"}
ROWS=49368
SOURCES=16442
TARGETS=3
COLS=SOURCES+TARGETS
WORDS=(COLS+63)//64
CEILING=16046
THRESHOLD=CEILING+1
WEIGHTS=(1,)*6+(2,)*11
SOURCE_WEIGHTS=(4,)*11+(5,)*6
COMPILER_FLAGS=["-std=c++17","-O3","-march=native"]
class Budget(Exception):pass
def need(ok,message):
 if not ok:raise ValueError(message)
def canonical(v):return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()
def digest(b):return hashlib.sha256(b).hexdigest()
def identity(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def json_save(p,v):
 raw=canonical(v)+b"\n";t=p.with_name(p.name+".tmp")
 with t.open("wb") as f:f.write(raw);f.flush();os.fsync(f.fileno())
 t.replace(p)
def pinned(p,size,sha,label):
 d=identity(p);need(d["bytes"]==size and d["sha256"]==sha,"complete frozen "+label+" identity");return d
def weight(e):return sum(a*b for a,b in zip(e,WEIGHTS))
def code(e):
 need(len(e)==17 and all(type(v) is int and v>=0 for v in e),"all17 nonnegative original exponents")
 need(all(v<16 for v in e[:6]) and all(v<8 for v in e[6:]),"no packed-exponent digit overflow")
 return sum(v<<(4*i) for i,v in enumerate(e[:6]))+sum(v<<(24+3*i) for i,v in enumerate(e[6:]))
def audit_input(a):
 rraw=a.audit_receipt.read_bytes();r=json.loads(rraw)
 need(r["format"]==AUDIT_FORMAT and r["status"]=="completed" and r["binding"]==AUDIT_BINDING,
      "actual completed coefficient audit and semantic binding")
 p=r["parameters"];sem=p["semantic"]
 need(digest(canonical(sem))==AUDIT_BINDING and
      sem["source"]["bytes"]==AUDIT_SOURCE[0] and sem["source"]["sha256"]==AUDIT_SOURCE[1],
      "actual original coefficient-audit source")
 for k in ("allOriginalCoefficients7Integral","allThreeF7CoefficientAlgebraCubeProductsVerified",
           "allCompleteOriginalRationalProductsVerified","prime7CompleteOriginalModelAdmitted",
           "cubicIrreducibleOverF7"):
  need(p[k] is True,"actual original coefficient gate "+k)
 need(p["allOriginalCoefficientCount"]==134399 and p["originalJ3DeterminantModulo7"]==1 and
      p["originalMatchedCubicModulo7"]==[6,0,6,1] and p["allSevenCubicValues"]==[6,6,3,3,5,1,4] and
      p["completeOriginalWeight9OutputRows"]==ROWS and p["completeOriginalWeight9SourceColumns"]==SOURCES,
      "same full original model and prime7 specialization")
 need(p["temporaryCompleteModel"]==MODEL_DESC,"actual complete original model descriptor")
 source=a.audit_out/MODEL_DESC["path"]
 pinned(source,MODEL_DESC["bytes"],MODEL_DESC["sha256"],"complete original model")
 return source,{"path":a.audit_receipt.name,"bytes":len(rraw),"sha256":digest(rraw),
               "exactPaidReceiptBytesReused":len(rraw)==PAID_AUDIT[0] and digest(rraw)==PAID_AUDIT[1]}
def load_model(p):
 with gzip.open(p,"rb") as f:b=f.read()
 need(len(b)==MODEL_DESC["logicalBytes"] and digest(b)==MODEL_DESC["logicalSha256"],
      "all logical original model bytes")
 v=json.loads(b);del b
 need(v["format"]==AUDIT_FORMAT+"-complete-data" and v["binding"]==AUDIT_BINDING and
      v["field7ModelAdmitted"] is True and v["rankNotComputed"] is True,
      "same admitted original coefficient model without imported rank")
 need(digest(canonical(v["semantic"]))==AUDIT_BINDING,"same original model semantic source")
 return v
def dictionaries(v):
 out=[]
 for label,n,w in (("completeWeight9OutputMonomials",ROWS,9),
                   ("completeQuarticWeight5SourceMonomials",1264,5),
                   ("completeQuinticWeight4SourceMonomials",423,4)):
  z=v[label]
  need(len(z)==n and digest(canonical(z))==DICTIONARY_SHA[label],"complete original dictionary "+label)
  codes=[code(e) for e in z]
  need(len(set(codes))==n and all(weight(e)==w for e in z),"all unique original dictionary monomials and weights")
  out.append((z,codes))
 return out
def exact_field_record(qpoly,record,w,label):
 q={}
 for e,c in qpoly:
  k=code(e);need(k not in q and weight(e)==w,"all unique weighted rational terms "+label)
  z=fmpq(c);den=int(z.denom());need(den%7!=0,"every original rational denominator is a7-unit")
  value=int(z.numer())%7*pow(den%7,-1,7)%7
  q[k]=value
 actual={}
 for e,c in record:
  k=code(e);need(type(c) is int and 1<=c<=6 and weight(e)==w and k not in actual,
                 "all unique canonical complete field terms "+label)
  actual[k]=c
 expected={k:c for k,c in q.items() if c}
 need(actual==expected,"every original rational coefficient reduces to the exact stored field coefficient "+label)
 return list(actual.items()),len(qpoly)
def build_input(a,sem,binding,check,emit):
 v=load_model(a.audit_out/MODEL_DESC["path"])
 model=v["completeOriginalRationalModel"];field=v["allField7Polynomials"]
 for k in ("all17OriginalGradientPolynomialsVerified","allWeightedEulerCoefficientsVerified",
           "allThreeTargetsWeightNineVerified","allThreeFieldComponentsRecombineToOriginalCube"):
  need(model[k] is True,"complete original polynomial source gate "+k)
 dd=dictionaries(v);output,ocodes=dd[0];five,fcodes=dd[1];four,qcodes=dd[2]
 need(len(field["gradients"])==17 and len(field["bellComponents"])==3 and len(field["cubeComponents"])==3,
      "all original gradients and all rational targets")
 counts=0;grad=[];targets=[]
 for i,(qpoly,fpoly) in enumerate(zip(model["originalSeventeenGradients"],field["gradients"])):
  terms,n=exact_field_record(qpoly,fpoly,SOURCE_WEIGHTS[i],"gradient"+str(i));grad.append(terms);counts+=n
 for i,(qpoly,fpoly) in enumerate(zip(model["BellFieldComponents"],field["bellComponents"])):
  _,n=exact_field_record(qpoly,fpoly,3,"Bell"+str(i));counts+=n
 for i,(qpoly,fpoly) in enumerate(zip(model["naturalCubeRationalComponents"],field["cubeComponents"])):
  terms,n=exact_field_record(qpoly,fpoly,9,"cube"+str(i));targets.append(terms);counts+=n
 need(counts==134399 and len(grad)==17 and len(targets)==3,"all134399 original coefficient conversions")
 need([len(z) for z in targets]==[34456,34560,34371],"all exact three rational cube components")
 columns=[[i,e] for i in range(17) for e in (five if i<11 else four)]
 need(len(columns)==SOURCES,"all16442 complete original source labels")
 column_sha=digest(canonical(columns));target_labels=[["original-Bell-cube-Q-component",i] for i in range(3)]
 expected_entries=sum(len(grad[i])*(len(fcodes) if i<11 else len(qcodes)) for i in range(17))+sum(map(len,targets))
 # Every exponent sum has weight9, hence y exponent<=9 and H exponent<=4.
 # Therefore addition of the original packed codes has no carry between digits.
 row_index={c:i for i,c in enumerate(ocodes)}
 del columns,output,model,field,v,dd
 gc.collect();check()
 need(sys.byteorder=="little" and array.array("Q").itemsize==8,"actual little-endian uint64 plane storage")
 planes=array.array("Q",[0])*(ROWS*3*WORDS)
 insertions=0
 def insert(row,col,c):
  nonlocal insertions
  at=row*3*WORDS+col//64;bit=1<<(col%64)
  need((planes[at]|planes[at+WORDS]|planes[at+2*WORDS])&bit==0,
       "each original source-target matrix coordinate inserted exactly once")
  if c&1:planes[at]|=bit
  if c&2:planes[at+WORDS]|=bit
  if c&4:planes[at+2*WORDS]|=bit
  insertions+=1
 col=0
 for i,poly in enumerate(grad):
  for multiplier in (fcodes if i<11 else qcodes):
   for exponent,c in poly:
    summed=exponent+multiplier
    need(summed in row_index,"every original product exponent is in the complete weight9 output dictionary")
    insert(row_index[summed],col,c)
   col+=1
   if col%256==0:check()
  emit("complete-original-generator-products",{"originalGenerator":i,"completeColumns":col,
                                              "coefficientProducts":insertions})
 need(col==SOURCES,"no source column omitted or duplicated")
 for j,poly in enumerate(targets):
  for exponent,c in poly:insert(row_index[exponent],SOURCES+j,c)
 need(insertions==expected_entries,"all source and target polynomial coefficient products inserted")
 check()
 p=a.out/"complete-original-m9-plus-three-targets-prime7.bin";tmp=p.with_name(p.name+".tmp")
 with tmp.open("wb") as f:
  f.write(b"R15M9071");f.write(struct.pack("<8I",1,7,ROWS,COLS,SOURCES,TARGETS,WORDS,THRESHOLD))
  f.write(binding.encode("ascii"));planes.tofile(f);f.flush();os.fsync(f.fileno())
 need(tmp.stat().st_size==104+ROWS*3*WORDS*8,"all49368 complete original rows in input transaction")
 tmp.replace(p);del planes,grad,targets,row_index,ocodes,fcodes,qcodes,five,four;gc.collect()
 d=identity(p)
 paid={"allOriginalCoefficientConversions":counts,"completeOriginalProductCoordinatesInserted":insertions,
       "completeOutputRows":ROWS,"completeOriginalSourceColumns":SOURCES,"completeOriginalTargetColumns":TARGETS,
       "completeSourceColumnDictionarySHA256":column_sha,
       "targetColumnDictionarySHA256":digest(canonical(target_labels)),
       "dictionarySHA256":DICTIONARY_SHA,"allOriginalCoefficientsAndWeightsReverified":True,
       "allOriginalSourceAndTargetProductsInsertedExactly":True,
       "allOriginalRowsConstructedBeforeAnyRankOperation":True,"input":d}
 manifest={"format":FORMAT+"-complete-input","binding":binding,"semantic":sem,"parameters":paid}
 json_save(a.out/"complete-original-input-manifest.json",manifest)
 emit("complete-original-input-saved",{"bytes":d["bytes"],"sha256":d["sha256"],"products":insertions})
 return paid
def read_input(a,sem,binding,check,emit):
 mp=a.out/"complete-original-input-manifest.json"
 if mp.exists():
  v=json.loads(mp.read_bytes())
  need(v["format"]==FORMAT+"-complete-input" and v["binding"]==binding and v["semantic"]==sem,
       "same complete input checkpoint semantic source")
  p=v["parameters"];d=p["input"]
  need(p["allOriginalCoefficientsAndWeightsReverified"] is True and
       p["allOriginalSourceAndTargetProductsInsertedExactly"] is True and
       p["allOriginalRowsConstructedBeforeAnyRankOperation"] is True and
       p["dictionarySHA256"]==DICTIONARY_SHA and p["completeOriginalSourceColumns"]==SOURCES and
       p["completeOriginalTargetColumns"]==TARGETS and p["completeOutputRows"]==ROWS,
       "actual complete input preparation gates")
  pinned(a.out/d["path"],d["bytes"],d["sha256"],"whole original matrix input")
  with (a.out/d["path"]).open("rb") as f:header=f.read(104)
  need(header==b"R15M9071"+struct.pack("<8I",1,7,ROWS,COLS,SOURCES,TARGETS,WORDS,THRESHOLD)+binding.encode(),
       "actual complete matrix input header")
  check();emit("reused-complete-original-input",d);return p
 return build_input(a,sem,binding,check,emit)
def compile_native(a,check,emit):
 version=subprocess.run(["g++","--version"],capture_output=True,text=True,timeout=10,check=True).stdout.splitlines()[0]
 spec={"source":identity(a.native),"compiler":"g++","version":version,"flags":COMPILER_FLAGS}
 bp=a.out/"original-m9-prime7-native";mp=a.out/"native-build.json";reused=False
 if mp.exists():
  prev=json.loads(mp.read_bytes())
  if prev.get("spec")==spec and bp.exists():
   d=identity(bp)
   reused=d==prev["binary"]
 if not reused:
  check();tmp=bp.with_name(bp.name+".tmp");start=time.monotonic()
  cp=subprocess.run(["g++"]+COMPILER_FLAGS+[str(a.native),"-o",str(tmp)],
                     capture_output=True,text=True,timeout=60)
  (a.out/"native-compile.stdout.log").write_text(cp.stdout)
  (a.out/"native-compile.stderr.log").write_text(cp.stderr)
  need(cp.returncode==0,"actual native compiler success: "+cp.stderr[-2000:])
  tmp.replace(bp);d=identity(bp)
  json_save(mp,{"spec":spec,"binary":d,"compileSeconds":time.monotonic()-start})
 check()
 run=subprocess.run([str(bp),"--selftest-only"],capture_output=True,text=True,timeout=20)
 need(run.returncode==0,"actual independent native arithmetic and small-matrix tests")
 test=json.loads(run.stdout.strip())
 need(test["status"]=="completed-selftest" and test["all49FieldAdds"] is True and
      test["all49FieldProducts"] is True and test["independentSmallRectangularFixtures"]==8 and
      test["allOriginalSelectedMinorDeterminantsVerified"] is True and test["SHAKnownFixtures"] is True,
      "all full independent native selftest gates")
 out={"spec":spec,"binary":identity(bp),"reusedBinary":reused,"actualSelftests":test}
 emit("native-compile-and-selftests-complete",{"binary":out["binary"],"reused":reused})
 return bp,out
def checked_state(root,binding,inputsha):
 mp=root/"native-state-manifest.json"
 if not mp.exists():return None
 v=json.loads(mp.read_bytes())
 need(v["format"]=="r150-original-m9-prime7-row-state-v1" and v["binding"]==binding and
      v["inputSHA256"]==inputsha and v["completeOriginalRowsOnly"] is True,
      "actual complete native state source and whole-row gate")
 n=v["nextRow"];rank=v["rank"];d=v["file"]
 need(type(n) is int and 0<=n<=ROWS and type(rank) is int and 0<=rank<=min(n,COLS) and
      type(v["generation"]) is int and v["generation"]>=1 and
      d["path"]=="complete-row-state-slot-"+str(v["generation"]%2)+".bin" and
      d["bytes"]==204+rank*(12+3*WORDS*8),"actual full native state dimensions")
 pinned(root/d["path"],d["bytes"],d["sha256"],"whole original row state")
 with (root/d["path"]).open("rb") as f:header=f.read(204)
 expected=(b"R15M9S71"+struct.pack("<8I",1,7,ROWS,COLS,SOURCES,TARGETS,WORDS,THRESHOLD)+
           struct.pack("<4QI",v["generation"],n,rank,v["reductionCount"],v["selectedInsertionMinorDeterminant7"])+
           binding.encode()+inputsha.encode())
 need(header==expected and 1<=v["selectedInsertionMinorDeterminant7"]<=6,
      "actual state header and selected original minor unit")
 return v
def main():
 ap=argparse.ArgumentParser()
 for k in ("audit-receipt","audit-out","native","out"):ap.add_argument("--"+k,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=600)
 ap.add_argument("--memory-mib",type=int,default=2048)
 ap.add_argument("--through",choices=("input","final"),default="final")
 a=ap.parse_args();need(30<=a.seconds<=3600 and 768<=a.memory_mib<=4096,"bounded original rank resources")
 a.out.mkdir(parents=True,exist_ok=True)
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 start=time.monotonic();deadline=start+a.seconds
 def check():
  if time.monotonic()>deadline-15:raise Budget("no remaining whole-phase budget")
 def emit(phase,p):
  print(json.dumps({"phase":phase,"elapsedSeconds":time.monotonic()-start,"parameters":p},sort_keys=True,separators=(",",":")),flush=True)
 sem={"format":FORMAT,"source":identity(Path(__file__)),"native":identity(a.native),
      "originalAuditBinding":AUDIT_BINDING,"completeOriginalModel":MODEL_DESC,
      "prime":7,"rows":ROWS,"sourceColumns":SOURCES,"targetColumns":TARGETS,
      "paidRationalSourceRankCeiling":CEILING,"strictRankThreshold":THRESHOLD,
      "coefficientBasis":["1","d","d^2"],"weight":9,"dictionarySHA256":DICTIONARY_SHA,
      "algorithm":"complete-original-three-plane-input-then-atomic-whole-original-row-echelon",
      "compilerFlags":COMPILER_FLAGS,"inputProtocol":"R15M9071","stateProtocol":"R15M9S71"}
 binding=digest(canonical(sem))
 rec={"format":FORMAT,"binding":binding,"status":"running","parameters":{
      "semantic":sem,"seconds":a.seconds,"memoryMiB":a.memory_mib,
      "through":a.through,"rationalCubeNonmembershipCertified":False}}
 rp=a.out/"original-weight9-prime7-stream-rank-receipt.json";code_exit=1;child=None
 def save():
  rec["elapsedSeconds"]=time.monotonic()-start
  rec["parameters"]["peakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  json_save(rp,rec)
 def stopped(signum,frame):
  if child is not None and child.poll() is None:child.send_signal(signal.SIGTERM)
  raise Budget("wrapper received signal "+str(signum))
 for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,stopped)
 try:
  save();pinned(a.native,*NATIVE_PIN,"prime7 rank native")
  _,auditdesc=audit_input(a);rec["parameters"]["actualAuditReceipt"]=auditdesc;save()
  bp,build=compile_native(a,check,emit);rec["parameters"]["nativeBuild"]=build;save()
  prepared=read_input(a,sem,binding,check,emit);rec["parameters"]["completeOriginalInput"]=prepared;save()
  if a.through=="input":
   rec["status"]="completed-input-only";code_exit=0
  else:
   check();native_root=a.out/"native";native_root.mkdir(exist_ok=True)
   state=checked_state(native_root,binding,prepared["input"]["sha256"])
   rec["parameters"]["previousWholeState"]=state
   budget=deadline-time.monotonic()-15;need(budget>20,"enough bounded native time for a complete row")
   argv=[str(bp),"--input",str(a.out/prepared["input"]["path"]),"--binding",binding,
         "--input-sha",prepared["input"]["sha256"],"--out",str(native_root),"--seconds",str(budget)]
   if state is not None:argv+=["--resume",str(native_root/state["file"]["path"]),"--resume-sha",state["file"]["sha256"]]
   nrp=native_root/"original-m9-prime7-native-receipt.json"
   if nrp.exists():shutil.copy2(nrp,native_root/"previous-original-m9-prime7-native-receipt.json");nrp.unlink()
   generation=state["generation"] if state is not None else 0
   logfile=native_root/("invocation-after-generation-"+str(generation)+".log")
   emit("starting-original-row-stream",{"seconds":budget,"previousNextRow":state["nextRow"] if state else 0,
                                       "previousRank":state["rank"] if state else 0})
   ns=time.monotonic()
   with logfile.open("wb") as log:
    child=subprocess.Popen(argv,stdout=log,stderr=subprocess.STDOUT)
    try:rc=child.wait(timeout=budget+10)
    except subprocess.TimeoutExpired:
     child.send_signal(signal.SIGTERM)
     try:rc=child.wait(timeout=10)
     except subprocess.TimeoutExpired:child.kill();child.wait();raise Budget("native exceeded whole-row shutdown grace")
   rec["parameters"].update(nativeArguments=argv,nativeExitCode=rc,
     nativeElapsedSeconds=time.monotonic()-ns,nativeLog=identity(logfile))
   state=checked_state(native_root,binding,prepared["input"]["sha256"])
   rec["parameters"]["lastWholeState"]=state
   need(rc in (0,75),"native failure: "+logfile.read_text(errors="replace")[-4000:])
   need(nrp.exists() and state is not None,"actual native receipt and complete whole-row state")
   n=json.loads(nrp.read_bytes())
   need(n["format"]=="r150-original-m9-prime7-native-v1" and n["binding"]==binding and
        n["inputSHA256"]==prepared["input"]["sha256"] and n["generation"]==state["generation"] and
        n["nextOriginalRow"]==state["nextRow"] and n["rankOfProcessedOriginalRows"]==state["rank"] and
        n["fullStateSHA256"]==state["file"]["sha256"],"actual native receipt binds complete original state")
   for k in ("allFieldArithmeticSelftestsVerified","allEightIndependentSmallRankAndMinorTestsVerified",
             "everyActualPivotCancellationVerified","allProcessedOriginalRowsHaveCanonicalPrime7Coefficients",
             "checkpointContainsOnlyWholeOriginalRows"):
    need(n[k] is True,"actual native verification gate "+k)
   reached=n["rankOfProcessedOriginalRows"]>=THRESHOLD
   need(n["rank16047ThresholdReached"]==reached and n["sourcePivotCount"]<=CEILING and
        n["sourcePivotCount"]+n["targetPivotCount"]==n["rankOfProcessedOriginalRows"] and
        (not reached or n["targetPivotCount"]>0),"strict actual rank threshold and original source ceiling")
   need((rc==0)==(reached or n["allOriginalRowsProcessed"]),"actual completed versus budget scope")
   rec["parameters"].update(nativeReceipt=identity(nrp),nativeResult=n,
     rationalCubeNonmembershipCertified=reached,augmentedFieldRankExceedsPaidQSourceCeiling=reached,
     rankOfProcessedOriginalRows=n["rankOfProcessedOriginalRows"],nextOriginalRow=n["nextOriginalRow"],
     allOriginalRowsProcessed=n["allOriginalRowsProcessed"],
     all16442OriginalSourcesAndThreeQTargetsRetained=True,
     smallerRankHasNoRationalNegativeConclusion=True)
   rec["status"]="completed" if rc==0 else "budget-checkpoint";code_exit=rc
  save()
 except Budget as e:
  rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code_exit=75
 except BaseException as e:
  rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code_exit=1
 finally:
  if child is not None and child.poll() is None:
   child.send_signal(signal.SIGTERM)
   try:child.wait(timeout=10)
   except subprocess.TimeoutExpired:child.kill();child.wait()
  try:
   if "completeOriginalInput" in rec["parameters"]:
    state=checked_state(a.out/"native",binding,rec["parameters"]["completeOriginalInput"]["input"]["sha256"])
    if state is not None:rec["parameters"]["lastWholeState"]=state
  except BaseException as e:
   rec["parameters"]["finalStateInspectionError"]={"type":type(e).__name__,"message":str(e)}
  save();print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
 return code_exit
if __name__=="__main__":raise SystemExit(main())
