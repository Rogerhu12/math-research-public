#!/usr/bin/env python3
"""Complete original202 transports and their same-Jc higher quotient.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Only temporary arrays; immutable source/input identities; exact field products at every layer.
"""
import argparse,hashlib,importlib.util,json,math,os,pathlib,resource,shutil,signal,struct,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):os.environ[k]="1"
P=31
PIN={
 "mapper_source":(22703,"a2e8fa4aa6d26c74b2f8000fb33fcda4b558021ab674582eecbd2c86edb9847e"),
 "source_native":(23360,"d0748649a3cd280fb620c85c61b82cb9d6c6fabeef8e9db81afaf9b9b01a4b2c"),
 "outside_native":(12826,"92e534d74d465f99043ec293bdd5a82a67c661309767e42e476bf765e1244262"),
 "native_model":(128145,"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"),
 "paid_projection_summary":(20819,"28b2605d03746fb5d1a4398c36d22650239d7989f5b68463ed9d6c9f99c5f830")}
HEADERS={
 "2026-11-15-r150-saturated-global-common-789f.hpp":(11284,"f19a9c64b7f57175b757d445594fb5521d1a7a9c5b0b0fe57391a407323c41e1"),
 "2026-11-14-r150-f31-bitplane-789f.hpp":(3030,"73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec")}
FULL_BINDING="9e86556a7a82c1c2306b395c87a49a7059d0945f12db7d4962c789717bd35dc6"
OUTSIDE_BINDING="f07acb3347e775dc41658f95e015c2e169b4df34c6c1e829a2737fe83acb2781"
class BudgetExpired(Exception):pass
def need(ok,msg):
 if not ok:raise ValueError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def digest(b):return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def identity(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   n+=len(b);h.update(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def read(p):return json.loads(pathlib.Path(p).read_text())
def save(p,x):
 q=p.with_name(p.name+".partial");q.write_bytes(canonical(x)+b"\n");os.replace(q,p)
 return {"file":p.name,**identity(p),"temporaryOnly":True}
def checked(p,pin):
 b=p.read_bytes();need(digest(b)=={"bytes":pin[0],"sha256":pin[1]},"complete pinned input: "+str(p));return b
def field_read(p,magic,k,nr,nc,binding,sha):
 b=p.read_bytes()
 need(hashlib.sha256(b).hexdigest()==sha,"every complete actual field SHA")
 need(b[:8]==magic and struct.unpack_from("<IIII",b,8)==(P,k,nr,nc)
      and b[24:88].decode()==binding and len(b)==88+nr*nc and all(v<P for v in b[88:]),"complete original bound field coordinates")
 return b[88:]
def field_write(p,magic,k,M,binding):
 nr,nc=M.nrows(),M.ncols()
 b=magic+struct.pack("<IIII",P,k,nr,nc)+binding.encode()+bytes(int(x) for x in M.entries())
 need(len(magic)==8 and len(b)==88+nr*nc,"complete higher field array extent")
 q=p.with_name(p.name+".partial");q.write_bytes(b);os.replace(q,p)
 return {"file":p.name,**digest(b),"temporaryOnly":True}
def small_square_smith(series,c,check):
 mats=series;labels=list(range(mats[0].ncols()));rlabels=labels[:];paid=[];height=0;steps=[]
 while labels:
  check();n=len(labels);precision=len(mats)-1;pc=c.pivots(mats[0]);rank=len(pc)
  pr=c.pivots(c.sub(mats[0],list(range(n)),pc).transpose()) if rank else []
  need(len(pr)==rank,"actual higher square unit profile")
  ps,cs=set(pr),set(pc);ri=pr+[i for i in range(n) if i not in ps];ci=pc+[i for i in range(n) if i not in cs]
  steps.append({"exponent":height,"active":n,"availableDegree":precision,"constantRank":rank,
    "originalRows":[rlabels[i] for i in pr],"originalColumns":[labels[i] for i in pc]})
  paid.extend([height]*rank)
  if rank==n:
   need(all(1<=e<=21 for e in paid),"all positive higher indices within proved original cutoff")
   return {"complete":True,"paidExponents":paid,"torsionLength":sum(paid),
      "maximumPositiveExponent":max(paid),"steps":steps}
  if rank:
   U=[c.sub(M,ri[:rank],ci[:rank]) for M in mats]
   V=[c.sub(M,ri[:rank],ci[rank:]) for M in mats]
   W=[c.sub(M,ri[rank:],ci[:rank]) for M in mats]
   Z=[c.sub(M,ri[rank:],ci[rank:]) for M in mats]
   IV=c.mul(c.inverse_series(U,check),V,len(mats),check);WIV=c.mul(W,IV,len(mats),check)
   reduced=[Z[k]-WIV[k] for k in range(len(mats))]
  else:reduced=mats
  need(c.zero(reduced[0]),"whole higher Schur constant zero before exact u division")
  labels=[labels[i] for i in ci[rank:]];rlabels=[rlabels[i] for i in ri[rank:]];height+=1
  if precision==0:
   return {"complete":False,"paidExponents":paid,"unresolvedCount":len(labels),
    "unresolvedExponentAtLeast":height,"torsionLengthLowerBound":sum(paid)+height*len(labels),"steps":steps}
  mats=reduced[1:]
 raise ValueError("empty higher positive block unexpectedly bypassed its paid order")
def main(argv=None):
 ap=argparse.ArgumentParser(description=__doc__)
 for key in PIN:ap.add_argument("--"+key.replace("_","-"),type=pathlib.Path,required=True)
 for key in ("prepared_out","full_out","outside_out","out"):ap.add_argument("--"+key.replace("_","-"),type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=600);ap.add_argument("--compile-seconds",type=float,default=30)
 ap.add_argument("--memory-mib",type=int,default=1024);ap.add_argument("--through",choices=("transports","final"),default="final")
 a=ap.parse_args(argv)
 need(math.isfinite(a.seconds) and 30<=a.seconds<=1200 and 1<=a.compile_seconds<=30 and 512<=a.memory_mib<=4096,"explicit bounded complete original high quotient")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 prep=a.prepared_out.resolve();full=a.full_out.resolve();outside=a.outside_out.resolve()
 start=time.monotonic();compile_time=[0.0];stopped=[False];active=[None];files={};binding=None;rc=1
 rp=out/"higher-original-two-mapper-quotient-receipt.json"
 rec={"format":"isp-complete-original202-two-mapper-higher-quotient-v1","status":"running","phase":"inputs","field":31,
  "characteristicZeroHighSmithComputed":False,"characteristicZeroFullSmithComputed":False,
  "selectedLeadingCoefficientUnitProved":False,"largeDataUploadedOrCommitted":False,"newLargeGaussianEliminations":0,
  "parameters":{"mathematicalSecondsLimit":a.seconds,"compileSecondsPerProgram":a.compile_seconds,
    "nativePrograms":2,"memoryMiB":a.memory_mib,"through":a.through},"events":[]}
 def elapsed():return time.monotonic()-start-compile_time[0]
 def remaining():return a.seconds-elapsed()
 def sig(signum,frame):
  stopped[0]=True
  if active[0] is not None and active[0].poll() is None:active[0].terminate()
 signal.signal(signal.SIGTERM,sig);signal.signal(signal.SIGINT,sig)
 def check():
  if stopped[0] or remaining()<=4:raise BudgetExpired("shared mathematical deadline; complete original stages retained")
 def keep(p):
  p=pathlib.Path(p);name=str(p.relative_to(out));files[name]={"file":name,**identity(p),"temporaryOnly":True};return files[name]
 def checkpoint():
  rec["mathematicalElapsedSeconds"]=elapsed();rec["compileElapsedSeconds"]=compile_time[0]
  rec["wallElapsedSeconds"]=time.monotonic()-start;rec["parameters"]["temporaryFiles"]=list(files.values());save(rp,rec)
 def beat(phase):
  rec["phase"]=phase;checkpoint();print(json.dumps({"phase":phase,"elapsedSeconds":elapsed()}),flush=True);check()
 try:
  blobs={k:checked(getattr(a,k),v) for k,v in PIN.items()};ids={k:digest(v) for k,v in blobs.items()}
  spec=importlib.util.spec_from_file_location("r150_regular_mapper_core",a.mapper_source)
  c=importlib.util.module_from_spec(spec);sys.modules[spec.name]=c;spec.loader.exec_module(c)
  pr=read(prep/"higher-two-regular202-mappers-receipt.json")
  need(pr["status"]=="completed" and pr["outcome"]=="complete-two-original-regular202-mapper-heads"
       and pr["maximumVerifiedMapperDegree"]==21 and pr["sourcePrecisionLoss"]==11 and pr["outsidePrecisionLoss"]==14
       and pr["all119988OriginalHighSmallProductsVerified"] and pr["all128876OriginalOutsideSmallProductsVerified"]
       and pr["all202HighFreeCoordinatesVerified"] and pr["all202OutsideFreeCoordinatesVerified"]
       and pr["independentPrecisionLossesVerified"],"both actual regular202 mappers complete")
  hb=pr["parameters"]["binding"]
  need(hashlib.sha256(canonical(pr["parameters"]["inputIdentity"])).hexdigest()==hb
       and pr["parameters"]["inputIdentity"]["source"]==ids["mapper_source"],"complete mapper source and semantic binding")
  pm=read(prep/"complete-mapper-stage-manifest.json")
  need(pm["binding"]==hb and set(pm["stages"])=={"high-small-kernel","outside-small-kernel","native-heads"},
       "all complete mapper stages")
  for stage in pm["stages"].values():
   for it in stage:need(identity(prep/it["file"])=={"bytes":it["bytes"],"sha256":it["sha256"]},"every complete mapper file")
  md=read(prep/"prepared-two-original-mapper-transports.json")
  need(md["binding"]==hb and md["maximumDegree"]==21 and md["field"]==31
       and md["allOriginalSmallKernelProductsVerified"] and md["bothOriginalFree202BlocksVerified"]
       and md["sourceParentBinding"]==FULL_BINDING and md["outsideParentBinding"]==OUTSIDE_BINDING
       and md["sourceNative"]==ids["source_native"] and md["outsideNative"]==ids["outside_native"],
       "whole prepared original transport protocol and source pins")
  hpaths={}
  for role,key in (("source","sourceHeads"),("outside","outsideHeads")):
   it=md[key];p=prep/it["file"]
   need(identity(p)=={"bytes":it["bytes"],"sha256":it["sha256"]},"whole prepared original transport head")
   hpaths[role]=p
  headers={}
  for name,pin in HEADERS.items():
   for parent in (a.source_native.parent,a.outside_native.parent):checked(parent/name,pin)
   headers[name]={"bytes":pin[0],"sha256":pin[1]}
  need(md["headers"]==headers,"same native original headers")
  fr=read(full/"full-infinity-natural-dual-schur-receipt.json");orc=read(outside/"koszul-outside-minimal-field-smith-receipt.json")
  need(fr["status"]=="completed" and fr["parameters"]["binding"]==FULL_BINDING
       and orc["status"]=="completed" and orc["parameters"]["binding"]==OUTSIDE_BINDING,"same actual parents")
  ff={x["file"]:x for x in fr["parameters"]["temporaryFiles"]};of={x["file"]:x for x in orc["parameters"]["temporaryFiles"]}
  parent_inputs={}
  def pfile(role,directory,entries,name):
   p=directory/name;it=entries[name]
   need(identity(p)=={"bytes":it["bytes"],"sha256":it["sha256"]},"complete parent original transport input")
   parent_inputs[role]=identity(p);return p
  fp=pfile("fullProfile",full,ff,"prepared/full-original-constant-profile.txt")
  fw=pfile("forward",full,ff,"prepared/forward.bin");bw=pfile("backward",full,ff,"prepared/backward.bin")
  fops=pfile("fullOperations",full,ff,"prepared/full_operations.bin")
  oc=pfile("outsideCoefficients",outside,of,"outside-original-natural-coefficients.bin")
  oi=pfile("outsideInverse",outside,of,"outside-constant-unit-inverse-field31.bin")
  need(parent_inputs["fullProfile"]=={k:md["fullParentNativeProfile"][k] for k in ("bytes","sha256")}
       and parent_inputs["outsideCoefficients"]=={k:md["outsideOriginalCoefficients"][k] for k in ("bytes","sha256")}
       and parent_inputs["outsideInverse"]=={k:md["outsideConstantInverse"][k] for k in ("bytes","sha256")},
       "all whole original unit inputs match prepared transport")
  decomp_outer=json.loads(blobs["paid_projection_summary"]);decomp=decomp_outer["result"]
  expected={"selectedMinor":243,"fullOriginalTorsion":66,"deletedOutputProjection":2,
    "outsideKoszulTorsion":149,"remainingHigherKernelQuotient":26}
  need(str(decomp_outer["runId"])=="43731615668" and decomp_outer["exitCode"]==0
       and decomp["status"]=="completed" and decomp["parameters"]["exactFieldLengthDecomposition"]==expected,
       "paid exact same-original field length decomposition")
  need(decomp["parameters"]["inputIdentity"]["inputs"]["native_model"]==ids["native_model"]
       and decomp["parameters"]["inputIdentity"]["inputs"]["selected_receipt"]==
        pr["parameters"]["inputIdentity"]["inputs"]["selected_receipt"],"same J and original native model in paid length decomposition")
  material={"version":"complete-original202-two-mapper-high-quotient-v1","source":identity(__file__),
    "inputs":ids,"headers":headers,"preparedMetadata":identity(prep/"prepared-two-original-mapper-transports.json"),
    "preparedBinding":hb,"parentUnitInputs":parent_inputs,"maximumDegree":21,
    "knownFieldLengthDecomposition":expected,"field":31}
  binding=hashlib.sha256(canonical(material)).hexdigest()
  rec["parameters"].update({"binding":binding,"preparedMapperBinding":hb,"inputIdentity":material,
    "exactFieldLengthDecomposition":expected,"parentFullBinding":FULL_BINDING,"parentOutsideBinding":OUTSIDE_BINDING})
  plan=out/"complete-original-transport-plan.json"
  if plan.exists():need(read(plan)==material,"same complete wrapper semantic plan")
  else:save(plan,material)
  keep(plan)
  from flint import nmod_mat
  import flint
  rec["pythonFlintVersion"]=flint.__version__
  def compile_native(role,source):
   check();build=out/("build-"+role);build.mkdir(exist_ok=True)
   target=build/source.name
   if not target.exists():shutil.copyfile(source,target)
   else:need(identity(target)==identity(source),"same actual native source in build")
   for name in HEADERS:
    dest=build/name;src=source.parent/name
    if not dest.exists():shutil.copyfile(src,dest)
    else:need(identity(dest)==headers[name],"same complete build header")
   cb=hashlib.sha256(canonical({"source":identity(source),"headers":headers,"flags":["g++","-std=c++17","-O2"]})).hexdigest()
   exe=build/"program";cachep=build/"compile-cache.json";old=read(cachep) if cachep.exists() else {}
   if exe.exists() and old.get("binding")==cb and old.get("binary")==identity(exe):
    rec["events"].append({"reusedActualNativeCompilation":role});keep(cachep);return exe
   log=build/"compile.log";t=time.monotonic()
   try:
    with log.open("wb") as stream:
     done=subprocess.run(["g++","-std=c++17","-O2",str(target),"-o",str(exe)],cwd=build,
       stdout=stream,stderr=subprocess.STDOUT,timeout=a.compile_seconds)
   finally:compile_time[0]+=time.monotonic()-t
   keep(log)
   if done.returncode:
    rec["compileLogTail"]=log.read_text(errors="replace")[-5000:];raise ValueError("actual "+role+" native compilation failed")
   save(cachep,{"binding":cb,"binary":identity(exe),"source":identity(source),"headers":headers});keep(cachep);return exe
  def inspect_native(role,prefix):
   rp0=pathlib.Path(str(prefix)+"-receipt.json")
   if not rp0.exists():return None
   nr=read(rp0);need(nr["inputBinding"]==hb and nr["field"]==31 and nr["requestedMaximumDegree"]==21,
      "same complete native transport input binding")
   k=int(nr["completedDegree"]);need(-1<=k<=21,"actual completed original native degree")
   if role=="source":
    need(nr["format"]=="isp-full-original-high202-source-transport-v1" and nr["parentFullBinding"]==FULL_BINDING
       and nr["inputHeadsSHA256"]==md["sourceHeads"]["sha256"],"actual high original source native provenance")
    need(nr["highHeadOriginalSourceRowsOneBased"]==md["highHeadOriginalSourceRowsOneBased"]
      and nr["freeOriginalSourceRowsOneBased"]==[md["highHeadOriginalSourceRowsOneBased"][i] for i in md["highFreeHeadPositionsZeroBased"]],
      "all actual high source/free coordinate labels")
    need(nr["actualConstantUnitRank"]==4340 and nr["originalSourceRows"]==6188 and nr["originalOutputRows"]==4367,
      "whole actual original source dimensions and unit rank")
    marks=("all3333OriginalPrebasisTriangularUnitProductsVerified","all1007OriginalFullPivotProductsVerified",
      "all202OriginalFreeSourceCoordinatesVerified","all1848OriginalTailMapperCoordinatesVerified",
      "all4340OriginalUnitSourceSolveProductsVerified","all4367OriginalHigherKernelProductsVerifiedThroughCompletedDegree")
    header=["R15HKLEDGER1",hb,md["sourceHeads"]["sha256"],FULL_BINDING];rowcount=6188;prodrows=4367
    magic=b"R15HKX31";pmagic=b"R15HKR31";suffix="source"
    free=[x-1 for x in nr["freeOriginalSourceRowsOneBased"]]
   else:
    need(nr["format"]=="isp-original-outside202-left-transport-v1" and nr["parentOutsideBinding"]==OUTSIDE_BINDING
       and nr["inputHeadsSHA256"]==md["outsideHeads"]["sha256"]
       and nr["inputCoefficientsSHA256"]==parent_inputs["outsideCoefficients"]["sha256"]
       and nr["inputInverseSHA256"]==parent_inputs["outsideInverse"]["sha256"],"actual original outside-left provenance")
    need(nr["actualConstantUnitRank"]==1603 and nr["originalOutsideRows"]==1834 and nr["originalKoszulColumns"]==1632,
      "whole actual original outside dimensions and unit rank")
    marks=("all202OriginalFreeCoordinatesVerified","all1834OriginalOutsideCoordinatesRetained",
      "all1632OriginalKoszulProductsZeroThroughCompletedDegree")
    header=["R15OLLEDGER1",hb,md["outsideHeads"]["sha256"],parent_inputs["outsideCoefficients"]["sha256"],
      parent_inputs["outsideInverse"]["sha256"],OUTSIDE_BINDING];rowcount=1834;prodrows=1632
    magic=b"R15OLX31";pmagic=b"R15OLR31";suffix="left"
    free=[md["outsideTailRows"][i] for i in md["outsideFreeTailPositionsZeroBased"]]
    need(nr["freeOriginalOutsideRowPositionsZeroBased"]==free,"all original outside free coordinate labels")
   records=[]
   if k>=0:
    for mark in marks:need(nr[mark] is True,"all original native products: "+mark)
    need(nr["originalProductCoordinatesVerified"]==(k+1)*prodrows*202,"complete original native product count")
    ledger=pathlib.Path(str(prefix)+"-ledger.txt");words=ledger.read_text().split();n=len(header)
    need(words[:n]==header and int(words[n])==k and len(words)==n+1+2*(k+1),"complete bound original native ledger")
    for degree in range(k+1):
     pp=pathlib.Path(str(prefix)+"-"+suffix+"-"+str(degree)+".bin")
     qp=pathlib.Path(str(prefix)+"-product-"+str(degree)+".bin")
     sha=words[n+1+2*degree];qsha=words[n+2+2*degree]
     body=field_read(pp,magic,degree,rowcount,202,hb,sha)
     product=field_read(qp,pmagic,degree,prodrows,202,hb,qsha)
     need(not any(product),"all original native product coordinates actually zero")
     for j,i in enumerate(free):
      need(body[i*202:(i+1)*202]==bytes(int(degree==0 and j==v) for v in range(202)),
        "whole original native free202 block")
     records.append({"degree":degree,"sourceFile":str(pp.relative_to(out)),"sourceSHA256":sha,
       "productFile":str(qp.relative_to(out)),"productSHA256":qsha});keep(pp);keep(qp)
    keep(ledger)
   keep(rp0)
   rec["parameters"].setdefault("nativeSummaries",{})[role]={k:v for k,v in nr.items() if k not in
     ("highHeadOriginalSourceRowsOneBased","freeOriginalSourceRowsOneBased","freeOriginalOutsideRowPositionsZeroBased")}
   return nr,records
  def run_native(role,source,prefix,inputargs):
   prefix.parent.mkdir(exist_ok=True)
   previous=inspect_native(role,prefix)
   if previous and previous[0]["status"]=="completed" and previous[0]["completedDegree"]==21:
    rec["events"].append({"reusedCompleteOriginalNativeTransport":role});return previous
   exe=compile_native(role,source);check();log=prefix.parent/"native.log";t=time.monotonic()
   args=[str(exe)]+[str(x) for x in inputargs]+[str(prefix),"21",str(max(.1,remaining()-5))]
   with log.open("ab") as f:
    proc=subprocess.Popen(args,stdout=f,stderr=subprocess.STDOUT);active[0]=proc
    try:ret=proc.wait(timeout=max(.1,remaining()-1))
    except subprocess.TimeoutExpired:
     proc.terminate()
     try:ret=proc.wait(timeout=12)
     except subprocess.TimeoutExpired:proc.kill();ret=proc.wait()
     active[0]=None;keep(log);inspect_native(role,prefix)
     raise BudgetExpired("original native retained its last complete coefficient")
   active[0]=None;keep(log)
   rec["parameters"].setdefault("nativeRuns",{})[role]={"seconds":time.monotonic()-t,"exitCode":ret}
   if ret not in (0,75):
    rec["nativeLogTail"]=log.read_text(errors="replace")[-5000:]
    raise ValueError("actual original "+role+" native failed")
   current=inspect_native(role,prefix);need(current is not None,"actual native receipt retained")
   if ret==75:raise BudgetExpired("original "+role+" transport checkpointed")
   need(current[0]["status"]=="completed" and current[0]["completedDegree"]==21,"all original native transport degrees completed")
   return current
  beat("complete-original202-source-transport")
  sp=out/"source"/"high202"
  sr,srecords=run_native("source",a.source_native,sp,[a.native_model.resolve(),fp,fw,bw,fops,hpaths["source"]])
  rec.update(completeOriginal202SourceTransport=True,all19406948OriginalSourceProductCoordinatesVerified=True,
    all202OriginalSourceFreeCoordinatesVerified=True)
  beat("complete-original202-outside-left-transport")
  lp=out/"outside"/"outside202"
  lr,lrecords=run_native("outside",a.outside_native,lp,[oc,oi,hpaths["outside"]])
  rec.update(completeOriginal202OutsideLeftTransport=True,all7252608OriginalOutsideProductCoordinatesVerified=True,
    all202OriginalOutsideFreeCoordinatesVerified=True)
  if a.through=="transports":
   rec.update(status="completed",outcome="complete-original-two-mapper-transports",higherQuotientActuallyComputed=False);rc=0
  else:
   beat("load-same-original-outside-source-pairing")
   outside_rows=list(map(int,md["originalOutsideSourceRowsOneBased"]))
   need(len(outside_rows)==len(set(outside_rows))==1834 and outside_rows==sorted(outside_rows)
       and hashlib.sha256(canonical(outside_rows)).hexdigest()==pr["parameters"]["inputIdentity"]["originalOutsideRowsSHA256"],
       "same ordered original J-complement for both mappers")
   K=[];LT=[]
   for degree in range(22):
    check();ss=srecords[degree];ls=lrecords[degree]
    kb=field_read(out/ss["sourceFile"],b"R15HKX31",degree,6188,202,hb,ss["sourceSHA256"])
    ob=field_read(out/ls["sourceFile"],b"R15OLX31",degree,1834,202,hb,ls["sourceSHA256"])
    selected=b"".join(kb[(i-1)*202:i*202] for i in outside_rows)
    K.append(nmod_mat(1834,202,list(selected),P));LT.append(nmod_mat(1834,202,list(ob),P).transpose())
   qdir=out/"quotient";qdir.mkdir(exist_ok=True);ql=qdir/"complete-quotient-layer-ledger.json"
   old=read(ql) if ql.exists() else {"binding":binding,"layers":[]}
   need(old["binding"]==binding,"same actual higher quotient layer binding")
   records=list(old["layers"]);need([x["degree"] for x in records]==list(range(len(records))),"all complete quotient degrees contiguous")
   D=[];Y=[];S=[];R=[];uinfo=None;Uinv=None
   for item in records:
    degree=item["degree"]
    for key,magic in (("matrix",b"R15HDQ31"),("graph",b"R15HDG31"),("residual",b"R15HDR31")):
     it=item[key];p=qdir/it["file"];nc=202 if key=="matrix" else int(item["smallDimension"])
     need(identity(p)=={"bytes":it["bytes"],"sha256":it["sha256"]},"every complete higher quotient stage")
     body=field_read(p,magic,degree,202,nc,binding,it["sha256"])
     M=nmod_mat(202,nc,list(body),P);keep(p)
     if key=="matrix":D.append(M)
     elif key=="graph":Y.append(M)
     else:R.append(M)
   if records:keep(ql)
   profile=qdir/"constant-higher-quotient-unit-profile.json"
   if profile.exists():
    uinfo=read(profile);need(uinfo["binding"]==binding,"same original higher constant unit profile")
    it=uinfo["inverse"];p=qdir/it["file"];rank=uinfo["constantRank"]
    body=field_read(p,b"R15HDI31",0,rank,rank,binding,it["sha256"]);Uinv=nmod_mat(rank,rank,list(body),P)
    need(identity(p)=={"bytes":it["bytes"],"sha256":it["sha256"]},"whole higher constant inverse")
    keep(p);keep(profile)
   else:need(not records,"no committed quotient graph without its actual unit")
   if records:
    rows=uinfo["unitRows"];cols=uinfo["unitColumns"];tails=uinfo["tailRows"];frees=uinfo["freeColumns"];small=uinfo["smallDimension"]
    need(identity(qdir/records[0]["matrix"]["file"])==uinfo["constantMatrix"],"same actual higher constant matrix")
    for rr in R:
     need(c.zero(c.sub(rr,rows,list(range(small)))),"all restored higher unit products zero")
     S.append(c.sub(rr,tails,list(range(small))))
   smith=small_square_smith(S,c,check) if S else None
   for degree in range(len(D),22):
    if smith is not None and smith["complete"]:break
    beat("actual-original-higher-pairing-degree-"+str(degree))
    Q=c.zmat(202,202)
    for j in range(degree+1):check();Q+=LT[j]*K[degree-j]
    D.append(Q)
    if degree==0:
     cols=c.pivots(Q);rank=len(cols);small=202-rank
     need(1<=small<=26,"actual constant higher corank obeys paid positive length26")
     rows=c.pivots(c.sub(Q,list(range(202)),cols).transpose());need(len(rows)==rank,"actual higher constant unit rank")
     tails=[i for i in range(202) if i not in set(rows)];frees=[j for j in range(202) if j not in set(cols)]
     U=c.sub(Q,rows,cols);Uinv=U.inv();need(U*Uinv==c.eye(rank),"whole actual higher constant inverse identity")
    rhs=c.sub(Q,rows,frees)
    for j in range(1,degree+1):rhs+=c.sub(D[j],rows,cols)*c.sub(Y[degree-j],cols,list(range(small)))
    top=-(Uinv*rhs);graph=c.zmat(202,small)
    for i,row in enumerate(cols):
     for j in range(small):graph[row,j]=top[i,j]
    if degree==0:
     for j,row in enumerate(frees):graph[row,j]=1
    Y.append(graph);residual=c.zmat(202,small)
    for j in range(degree+1):residual+=D[j]*Y[degree-j]
    need(c.zero(c.sub(residual,rows,list(range(small)))),"all original202 higher constant-unit row cancellations")
    need(c.sub(graph,frees,list(range(small)))==(c.eye(small) if degree==0 else c.zmat(small,small)),
         "all actual higher small free coordinates")
    R.append(residual);S.append(c.sub(residual,tails,list(range(small))))
    item={"degree":degree,"smallDimension":small}
    for key,magic,M in (("matrix",b"R15HDQ31",Q),("graph",b"R15HDG31",graph),("residual",b"R15HDR31",residual)):
     p=qdir/("higher-"+key+"-"+str(degree)+".bin");item[key]=field_write(p,magic,degree,M,binding);keep(p)
    if degree==0:
     invp=qdir/"constant-higher-quotient-inverse.bin";invitem=field_write(invp,b"R15HDI31",0,Uinv,binding);keep(invp)
     uinfo={"binding":binding,"constantRank":rank,"smallDimension":small,"unitRows":rows,"unitColumns":cols,
       "tailRows":tails,"freeColumns":frees,"constantMatrix":{"bytes":item["matrix"]["bytes"],"sha256":item["matrix"]["sha256"]},
       "inverse":invitem,"allOriginalConstantInverseProductsVerified":True}
     save(profile,uinfo);keep(profile)
    records.append(item);save(ql,{"binding":binding,"layers":records});keep(ql)
    smith=small_square_smith(S,c,check)
    rec["parameters"]["currentHigherSmallSmith"]=smith
    rec["highestActuallyPairedDegree"]=degree;rec["actualHigherConstantRank"]=rank
    rec["actualHigherPositiveFactorCount"]=small
    if not smith["complete"]:need(smith["torsionLengthLowerBound"]<=26,"actual partial higher order consistent with paid exact decomposition")
    checkpoint()
   need(smith is not None and smith["complete"],"proved original21 cutoff resolves the complete higher quotient")
   need(smith["torsionLength"]==26 and len(smith["paidExponents"])==small,"actual higher quotient equals complete paid residual length26")
   sm=qdir/"complete-original-higher-small-smith.json";save(sm,{"binding":binding,"constantProfile":uinfo,
      "smallSmith":smith,"highestActuallyPairedDegree":len(D)-1,"bothOriginalMapperDegrees":21,
      "exactFieldLengthDecomposition":expected});keep(sm)
   rec.update(status="completed",outcome="complete-original-higher-kernel-field-smith",
    higherQuotientActuallyComputed=True,completeHigherKernelSmithComputedModulo31=True,
    higherKernelUnitFactorCount=uinfo["constantRank"],higherKernelPositiveFactorCount=small,
    higherKernelPositiveExponents=smith["paidExponents"],higherKernelTorsionLengthModulo31=26,
    higherKernelMaximumPositiveExponentModulo31=smith["maximumPositiveExponent"],
    highestActuallyPairedDegree=len(D)-1,allOriginalHigherPairingsRetained=True,
    allOriginalHigherUnitRowsVerified=True,completeOriginalHigherKernelModuleJustifiedModulo31=True)
   rec["parameters"].update({"higherConstantUnitRows":rows,"higherConstantUnitColumns":cols,
     "higherSmallTargetRows":tails,"higherSmallSourceColumns":frees,"completeHigherSmallSmith":smith,
     "completeHigherSmallSmithFile":identity(sm),"formalSourceProof":"ker A = Phi direct-sum j(E216 ker(SE216)); both original202 mappers have unit free coordinates",
     "quotientProof":"L_O^T is onto and has kernel Sat(im O); pair the whole original j(E N_H) on the same J-complement"})
   rc=0
 except (BudgetExpired,subprocess.TimeoutExpired) as ex:
  rec.update(status="budget-exhausted",outcome="checkpointed-original-higher-kernel",error=str(ex));rc=75
 except Exception as ex:
  rec.update(status="failed",error=str(ex),exceptionType=type(ex).__name__)
  p=out/"exception.log";p.write_text(traceback.format_exc());keep(p);rc=1
 finally:checkpoint()
 need(rp.stat().st_size<100000,"only small execution summaries may be published")
 print(json.dumps(rec,separators=(",",":")),flush=True);return rc
if __name__=="__main__":sys.exit(main())
