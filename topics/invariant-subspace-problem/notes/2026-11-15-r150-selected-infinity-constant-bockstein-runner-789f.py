#!/usr/bin/env python3
"""One bounded original selected-infinity constant Bockstein calculation.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Compilation is separate. All input preparation and native mathematics share
the explicit <=60 second deadline; no earlier infinity normal form is rerun.
"""
import argparse, fractions, gzip, hashlib, itertools, json, os, pathlib
import shutil, signal, struct, subprocess, sys, time, traceback
sys.dont_write_bytecode = True

EXPECTED = {
 "native-model": ("r150-module-actions-789f/43588728414-1/char31/native-normal-form-input.txt",128145,"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"),
 "primitive-equations": ("r150-first-padic-residual-789f/original-primitive-integer-equations.json.gz",65159,"44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe"),
 "known-infinity": ("2026-11-14-rank-one-zero-infinity-centered-systems.json",80392,"06039281494f3f30912f055cb86f995e6bdbf73b3060a6226dc350829a411506"),
 "forward": ("r150-module-actions-789f/43588728414-1/char31/nf-forward.bin.gz",1660293,"445ec1d9acfa14932d8c3122fe98b471d869b3a8df0fa09a9ce14027e67c96ca"),
 "backward": ("r150-module-actions-789f/43588728414-1/char31/nf-backward.bin.gz",2031817,"b6a40b3bb5b54053ac71dd8eb0a2b3555ffc88bb958229ef23c756b705fb5a28"),
}
PAID = {
 "selected-receipt": ("selected-infinity-minor-dag-receipt.json",75700,"5cd9543de68bdb562bbe21189d5b0712248e6943c5572fe38ff27ec4fc1f5f68"),
 "selected-kernel": ("selected-constant-source-kernel.bin",36776,"aff9aad0db90b744e05068018b9007ffb743e3078f34cc6e2dffc0fb8327c9a9"),
}
HEADERS = {
 "common": ("2026-11-15-r150-saturated-global-common-789f.hpp",11284,"f19a9c64b7f57175b757d445594fb5521d1a7a9c5b0b0fe57391a407323c41e1"),
 "bitplane": ("2026-11-14-r150-f31-bitplane-789f.hpp",3030,"73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec"),
}
NATIVE_NAME="2026-11-15-r150-selected-infinity-constant-bockstein-789f.cpp"
NATIVE_SHA="bfc5376e0c259c94288804e25b3d20c534eecdfc56dd190aeec6f4b7e443fad4"
RAW_DAG = {
 "forward": (2378937,"66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e"),
 "backward": (3052119,"cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f"),
}
def sha(b): return hashlib.sha256(b).hexdigest()
def save_json(p,x):
 p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def checked(p,n,h):
 b=p.read_bytes()
 if len(b)!=n or sha(b)!=h: raise ValueError("input bytes/hash mismatch: "+str(p))
 return b
def run_bounded(cmd,limit,log):
 start=time.monotonic()
 with log.open("wb") as f:
  proc=subprocess.Popen(cmd,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
  try: code=proc.wait(timeout=max(.001,limit))
  except subprocess.TimeoutExpired:
   os.killpg(proc.pid,signal.SIGKILL);proc.wait();code=124
 return {"exitCode":code,"elapsedSeconds":time.monotonic()-start,"log":log.name}
def bounded_command(cmd,mem):
 return ["prlimit","--as="+str(mem*1024*1024),"--core=0","--"]+cmd

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--repo-notes",required=True,type=pathlib.Path)
 ap.add_argument("--paid-dir",required=True,type=pathlib.Path)
 ap.add_argument("--out",required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=60)
 ap.add_argument("--memory-mib",type=int,default=512)
 ap.add_argument("--compile-seconds",type=float,default=30)
 args=ap.parse_args()
 if not(0<args.seconds<=60 and 0<args.compile_seconds<=30 and 0<args.memory_mib<=512):
  raise ValueError("explicit authorized 60s / 512MiB; compile <=30s")
 out=args.out.resolve()
 if out.exists() and any(out.iterdir()): raise ValueError("new output directory required; do not overwrite a checkpoint")
 out.mkdir(parents=True,exist_ok=True)
 srcdir=pathlib.Path(__file__).resolve().parent
 receipt={"format":"isp-selected-infinity-constant-bockstein-v1","status":"running",
   "sharedMathematicalSeconds":args.seconds,"nativeMemoryMiB":args.memory_mib,
   "compileSecondsLimit":args.compile_seconds,"scope":"same original selected4354 constant infinity minor",
   "oldFullInfinityJetRecomputed":False,"otherPrimeComputed":False,
   "characteristicZeroInfinityConnectionComputed":False,
   "inputs":{},"sources":{},"stages":[]}
 rp=out/"selected-infinity-constant-bockstein-pipeline-receipt.json"
 mathstart=None
 try:
  build=out/"build";build.mkdir()
  cpp=srcdir/NATIVE_NAME;cppbytes=checked(cpp,13515,NATIVE_SHA)
  (build/NATIVE_NAME).write_bytes(cppbytes)
  receipt["sources"]["native"]={"file":cpp.name,"bytes":len(cppbytes),"sha256":sha(cppbytes)}
  for key,(name,n,h) in HEADERS.items():
   p=srcdir/name if key=="common" else args.repo_notes/name
   raw=checked(p,n,h);(build/name).write_bytes(raw)
   receipt["sources"][key]={"file":name,"bytes":n,"sha256":h}
  rb=pathlib.Path(__file__).read_bytes()
  receipt["sources"]["runner"]={"file":pathlib.Path(__file__).name,"bytes":len(rb),"sha256":sha(rb)}
  binary=build/"selected-infinity-bockstein"
  compile_cmd=bounded_command(["g++","-std=c++17","-O3","-DNDEBUG","-I",str(build),str(build/NATIVE_NAME),"-o",str(binary)],args.memory_mib)
  cr=run_bounded(compile_cmd,args.compile_seconds,out/"compile.log")
  receipt["compile"]=cr
  if cr["exitCode"]!=0: raise RuntimeError("native compilation incomplete")
  receipt["compile"]["binarySHA256"]=sha(binary.read_bytes())
  mathstart=time.monotonic()
  def remaining():
   r=args.seconds-(time.monotonic()-mathstart)
   if r<=0: raise TimeoutError("shared mathematical deadline reached")
   return r
  inputs={}
  for key,(name,n,h) in EXPECTED.items():
   p=args.repo_notes/name;inputs[key]=checked(p,n,h)
   receipt["inputs"][key]={"file":name,"bytes":n,"sha256":h}
  for key,(name,n,h) in PAID.items():
   p=args.paid_dir/name;inputs[key]=checked(p,n,h)
   receipt["inputs"][key]={"file":name,"bytes":n,"sha256":h}
  paid=json.loads(inputs["selected-receipt"])
  for key,val in [("status","completed"),("selectedConstantRank",985),("selectedFullConstantRankModulo31",4318),
     ("selectedMod31SchurSize",36),("allConstantKernelRowsVerified",True),("onlySelectedConstantImageQuotiented",True)]:
   if paid.get(key)!=val:raise ValueError("paid receipt field "+key)
  sources=paid["selectedSourceRows"]; keys=paid["selectedOutputMonomialKeys"]
  independent=paid["independentSelectedSourceIndicesZeroBased"]
  if len(set(sources))!=1021 or len(set(keys))!=1021 or len(set(independent))!=985:
   raise ValueError("paid selected dictionaries")
  var=[8**i for i in range(11)]
  fullkeys=[sum(var[i] for i in m) for d in range(5,0,-1) for m in itertools.combinations_with_replacement(range(11),d)]
  if len(fullkeys)!=4367 or len(set(fullkeys))!=4367:raise ValueError("original monomial dictionary")
  index={k:i for i,k in enumerate(fullkeys)}
  outputs=[index[int(k)] for k in keys]
  kb=inputs["selected-kernel"]
  if kb[:8]!=b"R150DM31" or struct.unpack_from("<III",kb,8)!=(31,36,1021) or len(kb)!=20+36*1021:
   raise ValueError("complete selected K36 matrix format")
  K=kb[20:]
  if any(a>=31 for a in K):raise ValueError("K36 field")
  primitive=json.loads(gzip.decompress(inputs["primitive-equations"]))
  equations=primitive["equations"]
  if len(equations)!=17 or any(len(row)!=77 for row in equations):raise ValueError("original17 primitive dimensions")
  point=[]
  for e,row in enumerate(equations):
   r=[]
   for j,pol in enumerate(row):
    vals=list(map(int,pol))
    if not vals:raise ValueError("empty integer coefficient")
    d=10 if e<11 and j<11 else 0 if e<11 else 5
    if e>=11 and j<11:
     if any(vals):raise ValueError("Gamma linear term is not zero")
     v=0
    else:
     if any(vals[d+1:]):raise ValueError("natural infinity degree exceeded")
     v=vals[d] if d<len(vals) else 0
    r.append(v)
   point.append(r)
  known=json.loads(inputs["known-infinity"])["infinity"]
  if known["quadraticMonomials"]!=[[i,j] for i in range(11) for j in range(i,11)]:
   raise ValueError("same quadratic monomial order")
  ratios=[]
  for e,(r,old) in enumerate(zip(point,known["equations"])):
   oldrow=list(map(int,old["linear"]+old["quadratic"]))
   if len(oldrow)!=77 or not any(oldrow):raise ValueError("known full infinity row")
   k=next(k for k,v in enumerate(oldrow) if v)
   rat=fractions.Fraction(r[k],oldrow[k])
   if not rat or any(a*rat.denominator!=b*rat.numerator for a,b in zip(r,oldrow)):
    raise ValueError("full characteristic-zero original row proportionality: "+str(e))
   ratios.append({"equation":e,"name":old["name"],"primitiveOverKnownNumerator":str(rat.numerator),
       "primitiveOverKnownDenominator":str(rat.denominator),"all77CoordinatesVerified":True})
  model_record={"format":"isp-same-original-infinity-primitive-integers-v1",
     "characteristicZeroSameOriginal17Verified":True,"rowProportionalities":ratios,
     "primitivePointCoefficients":[list(map(str,r)) for r in point],
     "selectedSourceRows":sources,"selectedOutputIndicesZeroBased":outputs,
     "selectedOutputMonomialKeys":keys,"independentSelectedSourceIndicesZeroBased":independent}
  save_json(out/"actual-original-infinity-constant-model.json",model_record)
  semantic={"version":receipt["format"],"inputs":receipt["inputs"],"sources":receipt["sources"],
     "field":31,"integerModulus":961,"selectedSourceRows":sources,"selectedOutputIndicesZeroBased":outputs}
  binding=sha(json.dumps(semantic,sort_keys=True,separators=(",",":")).encode())
  receipt["semanticBinding"]=binding
  prepared=out/"prepared-original-constant-mod961.txt"
  lines=["R150_SELECTED_INFINITY_CONSTANT_961_V1",binding]
  lines.extend(" ".join(str(v%961) for v in r) for r in point)
  lines.extend(["1021"," ".join(map(str,sources)),"1021"," ".join(map(str,outputs)),
    "985"," ".join(map(str,independent)),"36"])
  lines.extend(" ".join(map(str,K[i*1021:(i+1)*1021])) for i in range(36))
  prepared.write_text("\n".join(lines)+"\n")
  model=out/"native-normal-form-input.txt";model.write_bytes(inputs["native-model"])
  dags={}
  for key in ("forward","backward"):
   raw=gzip.decompress(inputs[key]);n,h=RAW_DAG[key]
   if len(raw)!=n or sha(raw)!=h:raise ValueError("complete decompressed "+key+" DAG")
   p=build/(key+".bin");p.write_bytes(raw);dags[key]=p
  receipt["stages"].append({"stage":"exact-input-preparation","elapsedSeconds":time.monotonic()-mathstart,
      "characteristicZeroSameOriginal17Verified":True,"inputBinding":binding})
  left=remaining()
  prefix=out/"actual"
  nr=run_bounded(bounded_command([str(binary),str(model),str(prepared),
      str(dags["forward"]),str(dags["backward"]),str(prefix),str(left)],args.memory_mib),
      left,out/"execution.log")
  receipt["stages"].append({"stage":"native-original-selected-bockstein",**nr})
  receipt["mathematicalElapsedSeconds"]=time.monotonic()-mathstart
  if nr["exitCode"]!=0:raise RuntimeError("native failed or reached explicit shared time budget")
  native=json.loads((out/"actual-receipt.json").read_bytes())
  required={"status":"completed","nativeStatus":"original-selected-constant-bockstein-complete",
    "inputBinding":binding,"selectedBaseRank":4318,"completeKernelDimension":36,
    "fullOriginalIntegerProductVerified":True,"allOriginalCoordinatesDivisible31":True,
    "sameSelectedSourceSupportVerified":True,"onlySelectedImageQuotiented":True,
    "all36KernelDirectionsRetained":True,"originalProductCoordinates":157212}
  for key,value in required.items():
   if native.get(key)!=value:raise ValueError("native completion gate "+key)
  if receipt["mathematicalElapsedSeconds"]>args.seconds+.25:raise ValueError("shared mathematical budget exceeded")
  receipt.update({"status":"completed","nativeStatistics":native,
     "bocksteinRank":native["bocksteinRank"],
     "characteristicZeroSelectedRankBounds":[native["characteristicZeroSelectedRankLowerBound"],4340],
     "characteristicZeroSelectedRankProved":native["characteristicZeroSelectedRankProved"],
     "characteristicZeroSameOriginal17Verified":True,
     "fullOriginalIntegerProductVerified":True,"all36KernelDirectionsRetained":True,
     "onlySelectedImageQuotiented":True,"sameSelectedSourceSupportVerified":True})
 except Exception as e:
  if mathstart is not None and "mathematicalElapsedSeconds" not in receipt:
   receipt["mathematicalElapsedSeconds"]=time.monotonic()-mathstart
  receipt["status"]="failed-or-incomplete";receipt["error"]=str(e)
  (out/"exception.log").write_text(traceback.format_exc())
 finally:
  # Lossless persistence is outside the mathematical clock, with decimal limits.
  persist=time.monotonic();files=[]
  for p in sorted(out.iterdir()):
   if not p.is_file() or p==rp:continue
   raw=p.read_bytes();entry={"file":p.name,"bytes":len(raw),"sha256":sha(raw)}
   if len(raw)>1_000_000 and not p.name.endswith(".gz"):
    compressed=gzip.compress(raw,compresslevel=1,mtime=0)
    if len(compressed)>4_500_000:raise ValueError("unexpected large small-certificate compressed output")
    q=p.with_name(p.name+".gz");q.write_bytes(compressed)
    entry["storedFile"]=q.name;entry["storedBytes"]=len(compressed);entry["storedSHA256"]=sha(compressed)
    p.unlink()
   else:
    if len(raw)>4_500_000:raise ValueError("stored file above decimal limit")
    entry["storedFile"]=p.name
   files.append(entry)
  receipt["files"]=files;receipt["persistenceSeconds"]=time.monotonic()-persist
  receipt["buildIsTemporary"]=True
  save_json(rp,receipt)
 print(json.dumps({k:receipt.get(k) for k in ("status","bocksteinRank","characteristicZeroSelectedRankBounds",
     "characteristicZeroSelectedRankProved","mathematicalElapsedSeconds","fullOriginalIntegerProductVerified",
     "sameSelectedSourceSupportVerified","onlySelectedImageQuotiented")}),flush=True)
 return 0 if receipt["status"]=="completed" else 1
if __name__=="__main__":sys.exit(main())

