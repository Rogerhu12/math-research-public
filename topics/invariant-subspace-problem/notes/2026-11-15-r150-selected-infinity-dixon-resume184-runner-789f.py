#!/usr/bin/env python3
"""Same selected infinity minor: resume exact GMP Dixon36 at actual p184; stop when exact kernels close.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
No rational kernel is asserted until the original integer selected matrix
has been multiplied back exactly; full4367 is recorded separately.
"""
import argparse,array,fractions,gzip,hashlib,itertools,json,math,os,pathlib
import resource,signal,struct,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
P=31
INPUTS={
 "model":("repo","r150-module-actions-789f/43588728414-1/char31/native-normal-form-input.txt",128145,"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"),
 "forward":("repo","r150-module-actions-789f/43588728414-1/char31/nf-forward.bin.gz",1660293,"445ec1d9acfa14932d8c3122fe98b471d869b3a8df0fa09a9ce14027e67c96ca"),
 "backward":("repo","r150-module-actions-789f/43588728414-1/char31/nf-backward.bin.gz",2031817,"b6a40b3bb5b54053ac71dd8eb0a2b3555ffc88bb958229ef23c756b705fb5a28"),
 "selected":("paid","selected-infinity-minor-dag-receipt.json",75700,"5cd9543de68bdb562bbe21189d5b0712248e6943c5572fe38ff27ec4fc1f5f68"),
 "point":("bockstein","actual-original-infinity-constant-model.json",87459,"97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074"),
 "kernel":("bockstein","actual-original-kernel36.bin",222788,"c008e57b7a7e80312f8ba292bb24241d53bb59d4c57b2a8d07ec1017b9de0744"),
 "previous":("bockstein","selected-infinity-constant-bockstein-pipeline-receipt.json",8877,"80ec709359d3530df19b075a7e4cdac7bfaa01a609c017258ed81fa658b90667"),
 "start-part0":("p184","stage-p256/actual-p184-exact-source36.bin.gz.part000",4500000,"943560fdc543450450a51fccbda30a02bf5396e8635ae143e98fcb47bbcf3078"),
 "start-part1":("p184","stage-p256/actual-p184-exact-source36.bin.gz.part001",4223275,"2cd61573a08d40a66f7228ce17bd23e64f90ac89e7f9e21f409c8eca5f4e0b17"),
 "paid-exact-kernels":("p184","exact-rational-kernel-certificates.json.gz",690600,"fbd6089ccf043af574e5c6c58c654e259732782c4a36d40af0ba8a7352078758"),
 "start-receipt":("p184","stage-p256/actual-p184-receipt.json",385,"c92c23695b219d9a3a4449a21fa548c79efc6147dde72b92714d7dc82a7a43a1"),
 "source-dag":("dixon","actual-selected-image-source-dag.bin.gz",957557,"c50e7bb8558a7f637d9d6951f64ae002c96cdce06dfcb7d1a4619ea6dc07337a"),
}
DAGS={"forward":(2378937,"66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e"),"backward":(3052119,"cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f")}
HEADERS={
 "2026-11-15-r150-saturated-global-common-789f.hpp":("source",11284,"f19a9c64b7f57175b757d445594fb5521d1a7a9c5b0b0fe57391a407323c41e1"),
 "2026-11-14-r150-f31-bitplane-789f.hpp":("repo",3030,"73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec")}
NATIVE_NAME="2026-11-15-r150-selected-infinity-dixon-through256-789f.cpp"
NATIVE_SHA="3c7168211c585d1198e3c730ea1823839f3479e1279975cc37eb12db4128331f"
NATIVE_BYTES=19375
def sha(b):return hashlib.sha256(b).hexdigest()
def jsave(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def checked(p,n,h):
 b=p.read_bytes()
 if len(b)!=n or sha(b)!=h:raise ValueError("bytes/hash: "+str(p))
 return b
def bounded(cmd,seconds,log,memory):
 start=time.monotonic()
 with log.open("wb") as f:
  proc=subprocess.Popen(["prlimit","--as="+str(memory*1024*1024),"--core=0","--"]+cmd,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
  try:r=proc.wait(timeout=max(.001,seconds))
  except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);proc.wait();r=124
 return {"exitCode":r,"elapsedSeconds":time.monotonic()-start,"log":log.name}
def rational_reconstruct(a,m):
 if a==0:return (0,1)
 bound=math.isqrt(m//2);r0,r1=m,a;t0,t1=0,1
 while abs(r1)>bound:
  q=r0//r1;r0,r1=r1,r0-q*r1;t0,t1=t1,t0-q*t1
 if not t1:return None
 if t1<0:r1,t1=-r1,-t1
 if t1>bound or abs(r1)>bound or math.gcd(r1,t1)!=1 or (a*t1-r1)%m:return None
 return (r1,t1)
def read_lift(p,binding,exponent):
 b=p.read_bytes()
 if b[:8]!=b"R150BK31" or struct.unpack_from("<IIII",b,8)!=(31,exponent,6188,36) or b[24:88].decode()!=binding:
  raise ValueError("actual big-integer Dixon source header")
 pos=88;values=[]
 for i in range(6188*36):
  if pos+3>len(b):raise ValueError("truncated exact coefficient")
  sign=b[pos];length=int.from_bytes(b[pos+1:pos+3],"little");pos+=3
  if sign>1 or length>4096 or pos+length>len(b) or (not length and sign) or (length and not b[pos+length-1]):
   raise ValueError("noncanonical arbitrary-precision integer")
  a=int.from_bytes(b[pos:pos+length],"little");pos+=length;values.append(-a if sign else a)
 if pos!=len(b):raise ValueError("trailing exact coefficients")
 return values


def main():
 ap=argparse.ArgumentParser()
 for n in ("repo-notes","paid-dir","bockstein-dir","dixon-dir","p184-dir","out"):ap.add_argument("--"+n,required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=120);ap.add_argument("--memory-mib",type=int,default=512)
 ap.add_argument("--compile-seconds",type=float,default=30);ap.add_argument("--maximum-exponent",type=int,choices=(192,200),default=200)
 ap.add_argument("--paid-binary",required=True,type=pathlib.Path)
 args=ap.parse_args()
 if not(0<args.seconds<=120 and 0<args.memory_mib<=512 and 0<args.compile_seconds<=30):raise ValueError("explicit authorized bounds")
 resource.setrlimit(resource.RLIMIT_AS,(args.memory_mib*1024*1024,)*2)
 out=args.out.resolve()
 if out.exists() and any(out.iterdir()):raise ValueError("new result directory only")
 out.mkdir(parents=True,exist_ok=True);build=out/"build";build.mkdir()
 src=pathlib.Path(__file__).resolve().parent
 roots={"repo":args.repo_notes,"paid":args.paid_dir,"bockstein":args.bockstein_dir,"dixon":args.dixon_dir,"p184":args.p184_dir,"source":src}
 receipt={"format":"isp-selected-infinity-gmp-dixon36-resume-p184-v1","status":"running","sharedMathematicalSeconds":args.seconds,
   "nativeMemoryMiB":args.memory_mib,"compileSecondsLimit":args.compile_seconds,"maximumRequestedExponent":args.maximum_exponent,
   "startExponent":184,"earlierDigitsRecomputed":False,"oldFullInfinityNormalFormRecomputed":False,
   "sameSelectedMinor":True,"inputs":{},"sources":{},"nativeStages":[],"rationalAttempts":[]}
 rp=out/"selected-infinity-dixon-after184-pipeline-receipt.json";start=None
 certificates=[];certified={};chosen=[];free_raw=[];basebinding=None;completed=184
 first_obstruction=0;obstruction_rank=0;outside_failure=0
 def savecert():
  if chosen:
   jsave(out/"exact-rational-kernel-certificates.json",{"format":"isp-selected-infinity-exact-rational-kernel36-v1","inputBinding":basebinding,
      "all4354SelectedOutputIndicesZeroBased":sorted(chosen),"normalizedFreeOriginalSourceRows":free_raw,
      "kernelCount":len(certificates),"allFreeSourceCoordinatesIdentity":True,"certificates":certificates})
 try:
  cpp=checked(src/NATIVE_NAME,NATIVE_BYTES,NATIVE_SHA);(build/NATIVE_NAME).write_bytes(cpp)
  receipt["sources"][NATIVE_NAME]={"bytes":len(cpp),"sha256":sha(cpp)}
  for name,(root,n,h) in HEADERS.items():
   raw=checked(roots[root]/name,n,h);(build/name).write_bytes(raw);receipt["sources"][name]={"bytes":n,"sha256":h}
  own=pathlib.Path(__file__).read_bytes();receipt["sources"][pathlib.Path(__file__).name]={"bytes":len(own),"sha256":sha(own)}
  binary=args.paid_binary.resolve()
  checked(binary,153200,"2b490e2d4663a83b0cc2eecd835b5f83409eac07c6d395750cf82f041abf68ac")
  receipt["compile"]={"reusedPaidBinary":True,"exitCode":0,"elapsedSeconds":0,
    "binarySHA256":"2b490e2d4663a83b0cc2eecd835b5f83409eac07c6d395750cf82f041abf68ac",
    "originalCompilationSourceSHA256":NATIVE_SHA}
  start=time.monotonic()
  def left():
   r=args.seconds-(time.monotonic()-start)
   if r<=0:raise TimeoutError("shared mathematical deadline")
   return r
  data={}
  for key,(root,name,n,h) in INPUTS.items():
   data[key]=checked(roots[root]/name,n,h);receipt["inputs"][key]={"file":name,"bytes":n,"sha256":h}
  selected=json.loads(data["selected"]);pointmodel=json.loads(data["point"]);sr=json.loads(data["start-receipt"])
  if sr.get("status")!="completed" or sr.get("exponent")!=184 or not sr.get("all4367FreshExactOriginalProductsVerified") or not sr.get("all4367OriginalCoordinatesDivisibleByFullModulus"):
   raise ValueError("actual p184 full original source checkpoint")
  sources=selected["selectedSourceRows"];outputs=pointmodel["selectedOutputIndicesZeroBased"]
  independent=selected["independentSelectedSourceIndicesZeroBased"];free=selected["selectedConstantKernelFreeSourceIndicesZeroBased"]
  if len(free)!=36 or set(free)!=set(range(1021))-set(independent):raise ValueError("same36 free coordinates")
  point=[list(map(int,row)) for row in pointmodel["primitivePointCoefficients"]]
  if len(point)!=17 or any(len(row)!=77 for row in point) or not pointmodel["characteristicZeroSameOriginal17Verified"]:raise ValueError("same original integer point")
  semantic={"inputs":receipt["inputs"],"sources":receipt["sources"],"startExponent":184,"requestedCheckpoints":[e for e in (192,200) if e<=args.maximum_exponent],
       "field":31,"scope":"selected4354/full4367-distinguished"}
  basebinding=sha(json.dumps(semantic,sort_keys=True,separators=(",",":")).encode());receipt["semanticBinding"]=basebinding
  model=build/"native-model.txt";model.write_bytes(data["model"])
  current_source=build/"actual-p184-exact-source36.bin"
  packed_start=data["start-part0"]+data["start-part1"]
  if len(packed_start)!=8723275 or sha(packed_start)!="fdb0390d2b59f516d75a61f66599c0dc3b60eecbb2f80f556043e9e5c6f846e7":raise ValueError("actual p184 compressed source")
  kr=gzip.decompress(packed_start)
  if len(kr)!=9234336 or sha(kr)!="9a000acba358eb042289eb1a63145f205e4049e1d2120100d27416e459030b48":raise ValueError("actual p184 raw source")
  current_source.write_bytes(kr);old_binding=sr["inputBinding"]
  paidcert_raw=gzip.decompress(data["paid-exact-kernels"])
  if len(paidcert_raw)!=2367435 or sha(paidcert_raw)!="2b2b14d844ed6fb6ef1edaea1a84509ef717e93cdd94d51fe4db1b15d911c1a0":raise ValueError("paid thirteen exact kernel certificate")
  paidcert=json.loads(paidcert_raw)
  if paidcert.get("kernelCount")!=13 or not paidcert.get("allFreeSourceCoordinatesIdentity"):raise ValueError("paid thirteen identity gate")
  chosen=set(paidcert["all4354SelectedOutputIndicesZeroBased"]);free_raw=paidcert["normalizedFreeOriginalSourceRows"]
  certificates=paidcert["certificates"]
  if len(chosen)!=4354 or len(free_raw)!=36 or len(certificates)!=13:raise ValueError("paid thirteen maps")
  certified={c["slot"]:c for c in certificates}
  if len(certified)!=13 or any(not c.get("all4354SelectedExactIntegerProductsZero") or not c.get("all4367ExactIntegerProductsZero") for c in certificates):raise ValueError("paid thirteen exact original products")
  receipt["paidExactFullOriginalKernelCount"]=13
  receipt["paidExactKernelSourceBinding"]=paidcert["inputBinding"]
  image_dag=build/"paid-selected-image-source-dag.bin";gd=gzip.decompress(data["source-dag"])
  if len(gd)!=1397793 or sha(gd)!="41097ab491dcedda36746204a92ab29fcdfe97d09ed03cd9ec66ecd90ed8684c":raise ValueError("paid985 complete source DAG")
  image_dag.write_bytes(gd)
  dags={}
  for key,(n,h) in DAGS.items():
   raw=gzip.decompress(data[key])
   if len(raw)!=n or sha(raw)!=h:raise ValueError("paid prebasis DAG "+key)
   dags[key]=build/(key+".bin");dags[key].write_bytes(raw)
  var=[8**i for i in range(11)]
  allkeys=[sum(var[i] for i in ix) for d in range(5,0,-1) for ix in itertools.combinations_with_replacement(range(11),d)]
  index={key:i for i,key in enumerate(allkeys)}
  multipliers=[sum(var[i] for i in ix) for d in range(4) for ix in itertools.combinations_with_replacement(range(11),d)]
  termkeys=var+[var[i]+var[j] for i in range(11) for j in range(i,11)]
  rowterms=[[(index[mul+termkeys[j]],v) for j,v in enumerate(point[e]) if v] for mul in multipliers for e in range(17)]
  if len(rowterms)!=6188:raise ValueError("original6188 source dictionary")
  for goal in (192,200):
   if goal>args.maximum_exponent or len(certificates)==36:break
   if left()<18:break
   stage=out/("stage-p"+str(goal));stage.mkdir()
   current_bytes=current_source.read_bytes()
   stage_semantic={"pipeline":basebinding,"startExponent":completed,"requestedExponent":goal,
        "actualStartSourceBytes":len(current_bytes),"actualStartSourceSHA256":sha(current_bytes),"actualStartSourceBinding":old_binding}
   binding=sha(json.dumps(stage_semantic,sort_keys=True,separators=(",",":")).encode())
   lines=["R150_SELECTED_INFINITY_DIXON_BIG_V1",binding,old_binding,str(completed)+" "+str(goal)]
   lines+=[" ".join(map(str,row)) for row in point]
   for count,values in [(1021,sources),(1021,outputs),(985,independent),(36,free)]:lines.extend([str(count)," ".join(map(str,values))])
   prepared=stage/"prepared-exact-model.txt";prepared.write_text("\n".join(lines)+"\n")
   prefix=stage/"actual";remaining=left()
   execution=bounded([str(binary),str(model),str(prepared),str(dags["forward"]),str(dags["backward"]),
       str(current_source),str(image_dag),str(prefix),str(remaining)],remaining,stage/"execution.log",args.memory_mib)
   execution["log"]=str((stage/"execution.log").relative_to(out))
   record={"requestedExponent":goal,"startExponent":completed,"inputBinding":binding,"inputs":stage_semantic,"execution":execution}
   receipt["nativeStages"].append(record)
   if execution["exitCode"] not in (0,75):raise RuntimeError("actual big-integer native failed/incomplete")
   nr=json.loads((stage/"actual-receipt.json").read_bytes());record["nativeStatistics"]=nr
   if nr.get("status") not in ("completed","checkpointed-time-budget"):raise ValueError("native completion state")
   for key,val in {"nativeStatus":"exact-original-dixon36-big-integer","inputBinding":binding,"startExponent":completed,
      "all36FreeSourceCoordinatesIdentity":True,"sameSelected4354Retained":True,"all4367ExactOriginalProductsVerified":True,
      "allFullOriginalResidualsRetained":True,"arbitraryPrecisionIntegerArithmetic":True}.items():
    if nr.get(key)!=val:raise ValueError("native gate "+key)
   completed=nr["completedExponent"];first_obstruction=nr["firstObstructionExponent"];obstruction_rank=nr["firstObstructionRank"];outside_failure=nr["firstOutsideFailureExponent"]
   nowchosen=set(nr["all4354SelectedOutputIndicesZeroBased"]);nowfree=nr["normalizedFreeOriginalSourceRows"]
   if len(nowchosen)!=4354 or len(nowfree)!=36:raise ValueError("complete actual coordinate maps")
   if chosen and (nowchosen!=chosen or nowfree!=free_raw):raise ValueError("source/output dictionaries changed")
   chosen=nowchosen;free_raw=nowfree
   for exponent in [e for e in nr["savedCheckpointExponents"] if e>record["startExponent"]]:
    left();source_file=stage/("actual-p"+str(exponent)+"-exact-source36.bin");vals=read_lift(source_file,binding,exponent);modulus=31**exponent
    for k in range(36):
     left()
     if k in certified:
      cert=certified[k];den=int(cert["commonDenominator"])
      for r,numer in enumerate(cert["originalIntegerSourceNumerators"]):
       if (int(numer)-int(vals[r*36+k])*den)%modulus:raise ValueError("exact kernel inconsistent with later actual source")
      receipt["rationalAttempts"].append({"exponent":exponent,"slot":k,"status":"previous-exact-kernel-residue-verified"});continue
     rats=[];den=1;first_fail=None
     for r in range(6188):
      a=rational_reconstruct(int(vals[r*36+k])%modulus,modulus)
      if a is None:first_fail=r+1;break
      rats.append(a);den=math.lcm(den,a[1])
      if den.bit_length()>8192:first_fail=r+1;break
     if first_fail is not None:
      receipt["rationalAttempts"].append({"exponent":exponent,"slot":k,"status":"balanced-rational-reconstruction-incomplete","firstOriginalSource":first_fail});continue
     nums=[a*(den//b) for a,b in rats]
     if any(nums[raw-1]!=(den if j==k else 0) for j,raw in enumerate(free_raw)):raise ValueError("rational free-coordinate identity")
     product=[0]*4367
     for r,a in enumerate(nums):
      if a:
       for c,v in rowterms[r]:product[c]+=v*a
      if r%500==0:left()
     bad=next((c for c in sorted(chosen) if product[c]),None)
     if bad is not None:
      receipt["rationalAttempts"].append({"exponent":exponent,"slot":k,"status":"candidate-not-an-exact-selected-kernel",
        "firstOriginalOutputIndexZeroBased":bad,"firstExactResidual":str(product[bad])});continue
     outside=[{"originalOutputIndexZeroBased":c,"value":str(v)} for c,v in enumerate(product) if v]
     cert={"slot":k,"firstSuccessfulExponent":exponent,"freeOriginalSource":free_raw[k],"commonDenominator":str(den),
       "originalIntegerSourceNumerators":list(map(str,nums)),"all4354SelectedExactIntegerProductsZero":True,
       "all4367ExactIntegerProductsZero":not outside,"outsideSelected13ExactProducts":outside}
     certificates.append(cert);certified[k]=cert
     receipt["rationalAttempts"].append({"exponent":exponent,"slot":k,"status":"exact-selected-rational-kernel-certified",
       "all4367ExactIntegerProductsZero":not outside,"commonDenominatorBits":den.bit_length()})
    savecert()
    print(json.dumps({"phase":"rational-attempts-at-p"+str(exponent),"exactKernelCount":len(certificates),
          "exactFull4367KernelCount":sum(c["all4367ExactIntegerProductsZero"] for c in certificates),"elapsedSeconds":time.monotonic()-start}),flush=True)
   current_source=stage/("actual-p"+str(completed)+"-exact-source36.bin");old_binding=binding
   if first_obstruction or outside_failure or nr["status"]=="checkpointed-time-budget":break
  savecert()
  elapsed=time.monotonic()-start
  if elapsed>args.seconds+.25:raise ValueError("shared mathematical deadline exceeded")
  lower=4318+obstruction_rank;upper=min(4340,4354-len(certificates))
  full_count=sum(c["all4367ExactIntegerProductsZero"] for c in certificates)
  if lower>upper:raise ValueError("actual char0 rank bounds conflict")
  if len(certificates)==36:outcome="exact-selected-characteristic-zero-rank4318";status="completed"
  elif first_obstruction:outcome="first-nonzero-selected-obstruction";status="completed"
  elif outside_failure:outcome="full-extra-row-obstruction-only";status="completed"
  elif completed==args.maximum_exponent:outcome="bounded-precision-complete-without-rational-kernel-basis";status="completed"
  else:outcome="checkpointed-time-budget";status="checkpointed-time-budget"
  receipt.update({"status":status,"outcome":outcome,"completedExponent":completed,"firstObstructionExponent":first_obstruction,
      "firstObstructionRank":obstruction_rank,"firstOutsideFailureExponent":outside_failure,
      "exactRationalKernelCount":len(certificates),"exactFull4367RationalKernelCount":full_count,
      "characteristicZeroSelectedRankBounds":[lower,upper],"characteristicZeroSelectedRankProved":lower==upper,
      "characteristicZeroSelectedColumnsFull4367RankBounds":[lower,min(4340,4354-full_count)],
      "mathematicalElapsedSeconds":elapsed,"allSelectedOriginalProductsVerified":True,
      "allFullOriginalProductsSaved":True,"arbitraryPrecisionIntegerArithmetic":True})
 except Exception as e:
  if start is not None:receipt["mathematicalElapsedSeconds"]=time.monotonic()-start
  receipt["status"]="failed-or-incomplete";receipt["error"]=str(e);(out/"exception.log").write_text(traceback.format_exc())
  savecert()
 finally:
  t=time.monotonic();files=[]
  for p in sorted(out.rglob("*")):
   if not p.is_file() or p==rp or build in p.parents:continue
   raw=p.read_bytes();rel=str(p.relative_to(out));entry={"file":rel,"bytes":len(raw),"sha256":sha(raw)}
   if len(raw)>1_000_000 and not p.name.endswith(".gz"):
    packed=gzip.compress(raw,compresslevel=1,mtime=0);parts=[]
    for j,pos in enumerate(range(0,len(packed),4_500_000)):
     chunk=packed[pos:pos+4_500_000];q=p.with_name(p.name+(".gz" if len(packed)<=4_500_000 else ".gz.part%03d"%j));q.write_bytes(chunk)
     parts.append({"file":str(q.relative_to(out)),"bytes":len(chunk),"sha256":sha(chunk)})
    entry.update({"gzipBytes":len(packed),"gzipSHA256":sha(packed),"parts":parts});p.unlink()
   else:
    if len(raw)>4_500_000:raise ValueError("stored file above decimal bound")
    entry["storedFile"]=rel
   files.append(entry)
  receipt["files"]=files;receipt["persistenceSeconds"]=time.monotonic()-t;receipt["buildIsTemporary"]=True
  jsave(rp,receipt)
 print(json.dumps({k:receipt.get(k) for k in ("status","outcome","completedExponent","firstObstructionExponent","firstObstructionRank",
      "exactRationalKernelCount","exactFull4367RationalKernelCount","characteristicZeroSelectedRankBounds","mathematicalElapsedSeconds")}),flush=True)
 return 0 if receipt["status"]=="completed" else 75 if receipt["status"]=="checkpointed-time-budget" else 1
if __name__=="__main__":sys.exit(main())
