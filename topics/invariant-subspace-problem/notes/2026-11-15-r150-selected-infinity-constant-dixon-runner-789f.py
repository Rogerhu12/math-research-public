#!/usr/bin/env python3
"""Same selected infinity minor: bounded Dixon36 plus exact rational attempts.
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
}
DAGS={"forward":(2378937,"66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e"),"backward":(3052119,"cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f")}
HEADERS={
 "2026-11-15-r150-saturated-global-common-789f.hpp":("source",11284,"f19a9c64b7f57175b757d445594fb5521d1a7a9c5b0b0fe57391a407323c41e1"),
 "2026-11-14-r150-f31-bitplane-789f.hpp":("repo",3030,"73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec")}
NATIVE_NAME="2026-11-15-r150-selected-infinity-constant-dixon-kernels-789f.cpp"
NATIVE_SHA="36d5d7a6f2e693311b43ae491bd0a176456a06f794ecd4434e35201cd9b92e08"
NATIVE_BYTES=15475
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
 if b[:8]!=b"R150DK31" or struct.unpack_from("<IIIIQ",b,8)!=(31,exponent,6188,36,31**exponent) or b[32:96].decode()!=binding:
  raise ValueError("actual Dixon source header")
 a=array.array("Q");a.frombytes(b[96:])
 if sys.byteorder!="little":a.byteswap()
 if len(a)!=6188*36 or any(x>=31**exponent for x in a):raise ValueError("actual Dixon source coefficients")
 return a

def main():
 ap=argparse.ArgumentParser()
 for n in ("repo-notes","paid-dir","bockstein-dir","out"):ap.add_argument("--"+n,required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=60);ap.add_argument("--memory-mib",type=int,default=512)
 ap.add_argument("--compile-seconds",type=float,default=30);ap.add_argument("--maximum-exponent",type=int,default=4)
 args=ap.parse_args()
 if not(0<args.seconds<=60 and 0<args.memory_mib<=512 and 0<args.compile_seconds<=30 and 2<=args.maximum_exponent<=4):raise ValueError("explicit authorized bounds")
 resource.setrlimit(resource.RLIMIT_AS,(args.memory_mib*1024*1024,)*2)
 out=args.out.resolve()
 if out.exists() and any(out.iterdir()):raise ValueError("new result directory only")
 out.mkdir(parents=True,exist_ok=True);build=out/"build";build.mkdir()
 src=pathlib.Path(__file__).resolve().parent
 roots={"repo":args.repo_notes,"paid":args.paid_dir,"bockstein":args.bockstein_dir,"source":src}
 receipt={"format":"isp-selected-infinity-normalized-dixon36-v1","status":"running","sharedMathematicalSeconds":args.seconds,
   "nativeMemoryMiB":args.memory_mib,"compileSecondsLimit":args.compile_seconds,"maximumRequestedExponent":args.maximum_exponent,
   "oldFullInfinityNormalFormRecomputed":False,"sameSelectedMinor":True,"inputs":{},"sources":{},"rationalAttempts":[]}
 rp=out/"selected-infinity-dixon-kernel36-pipeline-receipt.json";start=None
 try:
  cpp=checked(src/NATIVE_NAME,NATIVE_BYTES,NATIVE_SHA);(build/NATIVE_NAME).write_bytes(cpp)
  receipt["sources"][NATIVE_NAME]={"bytes":len(cpp),"sha256":sha(cpp)}
  for name,(root,n,h) in HEADERS.items():
   raw=checked(roots[root]/name,n,h);(build/name).write_bytes(raw);receipt["sources"][name]={"bytes":n,"sha256":h}
  own=pathlib.Path(__file__).read_bytes();receipt["sources"][pathlib.Path(__file__).name]={"bytes":len(own),"sha256":sha(own)}
  binary=build/"selected-infinity-dixon36"
  receipt["compile"]=bounded(["g++","-std=c++17","-O3","-DNDEBUG","-I",str(build),str(build/NATIVE_NAME),"-o",str(binary)],args.compile_seconds,out/"compile.log",args.memory_mib)
  if receipt["compile"]["exitCode"]:raise RuntimeError("compile failed or incomplete")
  receipt["compile"]["binarySHA256"]=sha(binary.read_bytes())
  start=time.monotonic()
  def left():
   r=args.seconds-(time.monotonic()-start)
   if r<=0:raise TimeoutError("shared mathematical deadline")
   return r
  data={}
  for key,(root,name,n,h) in INPUTS.items():
   data[key]=checked(roots[root]/name,n,h);receipt["inputs"][key]={"file":name,"bytes":n,"sha256":h}
  old=json.loads(data["previous"])
  if old.get("status")!="completed" or old.get("bocksteinRank")!=0 or not old.get("fullOriginalIntegerProductVerified"):raise ValueError("paid first Bockstein")
  selected=json.loads(data["selected"]);pointmodel=json.loads(data["point"])
  sources=selected["selectedSourceRows"];outputs=pointmodel["selectedOutputIndicesZeroBased"]
  independent=selected["independentSelectedSourceIndicesZeroBased"];free=selected["selectedConstantKernelFreeSourceIndicesZeroBased"]
  if len(free)!=36 or set(free)!=set(range(1021))-set(independent):raise ValueError("exact36 free coordinates")
  point=[list(map(int,row)) for row in pointmodel["primitivePointCoefficients"]]
  if len(point)!=17 or any(len(row)!=77 for row in point) or not pointmodel["characteristicZeroSameOriginal17Verified"]:raise ValueError("same exact original point model")
  semantic={"inputs":receipt["inputs"],"sources":receipt["sources"],"maximumExponent":args.maximum_exponent,"field":31,"scope":"selected4354/all4367-distinguished"}
  binding=sha(json.dumps(semantic,sort_keys=True,separators=(",",":")).encode());receipt["semanticBinding"]=binding
  m=31**args.maximum_exponent
  lines=["R150_SELECTED_INFINITY_DIXON_V1",binding,str(args.maximum_exponent)+" "+str(m)]
  lines+=[" ".join(str(x%m) for x in row) for row in point]
  for count,values in [(1021,sources),(1021,outputs),(985,independent),(36,free)]:lines.extend([str(count)," ".join(map(str,values))])
  prepared=out/"prepared-dixon-constant-model.txt";prepared.write_text("\n".join(lines)+"\n")
  model=build/"native-model.txt";model.write_bytes(data["model"])
  kernel=build/"original-kernel36.bin";kernel.write_bytes(data["kernel"])
  dags={}
  for key,(n,h) in DAGS.items():
   raw=gzip.decompress(data[key])
   if len(raw)!=n or sha(raw)!=h:raise ValueError("decompressed DAG "+key)
   dags[key]=build/(key+".bin");dags[key].write_bytes(raw)
  prefix=out/"actual";remaining=left()
  native=bounded([str(binary),str(model),str(prepared),str(dags["forward"]),str(dags["backward"]),str(kernel),str(prefix),str(remaining)],remaining,out/"execution.log",args.memory_mib)
  receipt["nativeExecution"]=native
  if native["exitCode"]:raise RuntimeError("Dixon native incomplete")
  nr=json.loads((out/"actual-receipt.json").read_bytes())
  for key,val in {"status":"completed","nativeStatus":"selected-original-kernel36-dixon-complete","inputBinding":binding,
     "all36FreeSourceCoordinatesIdentity":True,"sameSelected4354Retained":True,"allSelectedOriginalProductsVerified":True,
     "allFullOriginalProductsSaved":True}.items():
   if nr.get(key)!=val:raise ValueError("native gate "+key)
  receipt["nativeStatistics"]=nr
  chosen=set(nr["all4354SelectedOutputIndicesZeroBased"]);free_raw=nr["normalizedFreeOriginalSourceRows"]
  if len(chosen)!=4354 or len(free_raw)!=36:raise ValueError("actual selected output/free dictionaries")
  var=[8**i for i in range(11)]
  allkeys=[sum(var[i] for i in ix) for d in range(5,0,-1) for ix in itertools.combinations_with_replacement(range(11),d)]
  index={key:i for i,key in enumerate(allkeys)}
  multipliers=[sum(var[i] for i in ix) for d in range(4) for ix in itertools.combinations_with_replacement(range(11),d)]
  termkeys=var+[var[i]+var[j] for i in range(11) for j in range(i,11)]
  rowterms=[[(index[mul+termkeys[j]],v) for j,v in enumerate(point[e]) if v] for mul in multipliers for e in range(17)]
  if len(rowterms)!=6188:raise ValueError("all original integer6188 rows")
  certified={};certificates=[]
  for exponent in range(2,nr["completedExponent"]+1):
   left();vals=read_lift(out/("actual-p"+str(exponent)+"-original-kernel36.bin"),binding,exponent);modulus=31**exponent
   for k in range(36):
    left()
    if k in certified:
     cert=certified[k];den=int(cert["commonDenominator"])
     for r,numer in enumerate(cert["originalIntegerSourceNumerators"]):
      if (int(numer)-int(vals[r*36+k])*den)%modulus:raise ValueError("previous exact kernel inconsistent with actual later Dixon digit")
     receipt["rationalAttempts"].append({"exponent":exponent,"slot":k,"status":"previous-exact-kernel-residue-verified"});continue
    rats=[];den=1;first_fail=None
    for r in range(6188):
     a=rational_reconstruct(int(vals[r*36+k]),modulus)
     if a is None:first_fail=r+1;break
     rats.append(a);den=math.lcm(den,a[1])
     if den.bit_length()>8192:first_fail=r+1;break
    if first_fail is not None:
     receipt["rationalAttempts"].append({"exponent":exponent,"slot":k,"status":"balanced-rational-reconstruction-incomplete","firstOriginalSource":first_fail});continue
    nums=[a*(den//b) for a,b in rats]
    if any(nums[raw-1]!=(den if j==k else 0) for j,raw in enumerate(free_raw)):raise ValueError("rational free coordinates identity")
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
   print(json.dumps({"phase":"rational-attempts-at-p"+str(exponent),"exactKernelCount":len(certified),"elapsedSeconds":time.monotonic()-start}),flush=True)
  jsave(out/"exact-rational-kernel-certificates.json",{"format":"isp-selected-infinity-exact-rational-kernel36-v1","inputBinding":binding,
       "all4354SelectedOutputIndicesZeroBased":sorted(chosen),"normalizedFreeOriginalSourceRows":free_raw,
       "kernelCount":len(certificates),"allFreeSourceCoordinatesIdentity":True,"certificates":certificates})
  receipt["mathematicalElapsedSeconds"]=time.monotonic()-start
  if receipt["mathematicalElapsedSeconds"]>args.seconds+.25:raise ValueError("shared math deadline exceeded")
  lower=4318+nr["firstObstructionRank"];upper=min(4340,4354-len(certificates))
  if lower>upper:raise ValueError("exact rank bounds conflict")
  receipt.update({"status":"completed","completedExponent":nr["completedExponent"],"firstObstructionExponent":nr["firstObstructionExponent"],
      "firstObstructionRank":nr["firstObstructionRank"],"exactRationalKernelCount":len(certificates),
      "exactFull4367RationalKernelCount":sum(c["all4367ExactIntegerProductsZero"] for c in certificates),
      "characteristicZeroSelectedRankBounds":[lower,upper],"characteristicZeroSelectedRankProved":lower==upper,
      "allSelectedOriginalProductsVerified":True,"allFullOriginalProductsSaved":True})
 except Exception as e:
  if start is not None and "mathematicalElapsedSeconds" not in receipt:receipt["mathematicalElapsedSeconds"]=time.monotonic()-start
  receipt["status"]="failed-or-incomplete";receipt["error"]=str(e);(out/"exception.log").write_text(traceback.format_exc())
 finally:
  t=time.monotonic();files=[]
  for p in sorted(out.iterdir()):
   if not p.is_file() or p==rp:continue
   raw=p.read_bytes();entry={"file":p.name,"bytes":len(raw),"sha256":sha(raw)}
   if len(raw)>1_000_000 and not p.name.endswith(".gz"):
    packed=gzip.compress(raw,compresslevel=1,mtime=0)
    parts=[]
    for j,pos in enumerate(range(0,len(packed),4_500_000)):
     chunk=packed[pos:pos+4_500_000];q=p.with_name(p.name+(".gz" if len(packed)<=4_500_000 else ".gz.part%03d"%j));q.write_bytes(chunk)
     parts.append({"file":q.name,"bytes":len(chunk),"sha256":sha(chunk)})
    entry.update({"gzipBytes":len(packed),"gzipSHA256":sha(packed),"parts":parts});p.unlink()
   else:
    if len(raw)>4_500_000:raise ValueError("unexpected stored file above limit")
    entry["storedFile"]=p.name
   files.append(entry)
  receipt["files"]=files;receipt["persistenceSeconds"]=time.monotonic()-t;receipt["buildIsTemporary"]=True
  jsave(rp,receipt)
 print(json.dumps({k:receipt.get(k) for k in ("status","completedExponent","firstObstructionExponent","firstObstructionRank",
    "exactRationalKernelCount","exactFull4367RationalKernelCount","characteristicZeroSelectedRankBounds","mathematicalElapsedSeconds")}),flush=True)
 return 0 if receipt["status"]=="completed" else 1
if __name__=="__main__":sys.exit(main())

